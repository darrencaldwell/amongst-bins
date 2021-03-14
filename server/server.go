/* ThreadedEchoServer
 */
 package main

 import (
	 "net"
	 "os"
	 "fmt"
	 "io"
//	 "encoding/binary"
	 "bufio"
	 "github.com/golang/protobuf/proto"
 )
 
func main() {
 
	//  service := ":3333"
	//  tcpAddr, err := net.ResolveTCPAddr("ip6", service)
	//  checkError(err)
 
	listener, err := net.Listen("tcp", ":8080")
	checkError(err)
 
	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("conn err")
			continue
		}
		// run as a goroutine
		go handleClient(conn)
	}
}
 
 func handleClient(conn net.Conn) {
	// close connection on exit
	defer conn.Close()
	rx := bufio.NewReader(conn)
        tx := bufio.NewWriter(conn)

	fmt.Println("connection made!")

	//infiniti boi to handle a client
	for {
		// 
		send_player := &ServerPositionUpdate{}
		for _, p := range game.Players {
			pp := &PlayerPosition{}
			pp.PlayerId = int64(p.Id)
			pp.X = int64(p.Pos.x)
			pp.Y = int64(p.Pos.y)
			send_player.PlayerPos = append(send_player.PlayerPos, pp)
		}
		res, err := proto.Marshal(send_player)
		if err != nil {
			fmt.Println("handleClient: error marshalling")
			return
		}
		// write protocol
		if err = tx.WriteByte(5); err != nil {
			fmt.Println("EchoJoinGame: sending protocol type")
			return
		}
		if err = tx.Flush(); err != nil {
			return
		}
		// write size
		length := proto.Size(send_player)
		err = tx.WriteByte(byte(length))
		if err != nil {
			fmt.Println("EchoJoinGame: sending length")
			return 
		}
		if err = tx.Flush(); err != nil {
			return
		}

		// write the n bytes
		_, err = tx.Write(res)
		if err != nil {
			fmt.Println("couldn't write")
			return
		}
		if err = tx.Flush(); err != nil {
			return
		}


		// read type of message
		action, err := rx.ReadByte()
		if err != nil {
			fmt.Println("handler: error reading type")
			return 
		}
		fmt.Println("action:", action)

		// read size
		size, err := rx.ReadByte()
		if err != nil {
			fmt.Println("handler: error reading size")
			return 
		}
		fmt.Println("msg size:", size)

		// read upto size bytes
		buf := make([]byte, size)
		n, err := io.ReadFull(rx, buf[:])
		if err != nil || n != int(size) {
			fmt.Println("handleClient: failed to read correct amount")
		}

		fmt.Printf("read %d bytes\n", n)

		switch action {
		case 1:
			fmt.Println("player joined")
			JoinHandler(conn, buf)
		case 3:
			fmt.Println("player moved")
			PlayerPositionHandler(conn, buf)
			
		default:
			// fmt.Println("aaaaaaaa")
		}

		// // write the n bytes read
		// _, err2 := conn.Write(buf[0:n])
		// if err2 != nil {
		// fmt.Println("couldn't write")
		// 	return
		// }
		// fmt.Println("written")
	}
}
 
func checkError(err error) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
		os.Exit(1)
	}
}
