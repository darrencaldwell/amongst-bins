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
	//  "github.com/golang/protobuf/proto"
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
	// tx := bufio.NewWriter(conn)

	fmt.Println("connection made!")

	//infiniti boi to handle a client
	for {
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
		if err != nil {
			fmt.Println("couldn't read")
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
