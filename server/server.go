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
 
	 //infiniti boi to handle reqs from a client
	 for {
		// read type of message
		_, err := rx.ReadByte()
		if err != nil {
			fmt.Println("EchoJoinGame: error reading type")
			return 
		}
		// read size
		size, err := rx.ReadByte()
		if err != nil {
			fmt.Println("EchoJoinGame: error reading size")
			return 
		}

		 // read upto size bytes
		 buf := make([]byte, size)
		 _, err = io.ReadFull(rx, buf[:])
		 if err != nil {
			 fmt.Println("EchoJoinGame: error reading message")
			 return
		 }

		 // respond

		 m := &EchoJoinGame{}
		 m.PlayerId = 2
		 res, err := proto.Marshal(m)
		 if err != nil {
			 fmt.Println("EchoJoinGame: error marshalling")
			 return
		 }

		 // write protocol
		if err = tx.WriteByte(2); err != nil {
			 fmt.Println("EchoJoinGame: sending protocol type")
			return
		}
		err = tx.Flush()
		// write size
		length := proto.Size(m)
		err = tx.WriteByte(byte(length))
		if err != nil {
			 fmt.Println("EchoJoinGame: sending length")
			return 
		}
		err = tx.Flush()
 
		 // write the n bytes
		 _, err2 := tx.Write(res)
		err = tx.Flush()
		 if err2 != nil {
			fmt.Println("couldn't write")
			 return
		 }
	 }
 }
 
 func checkError(err error) {
	 if err != nil {
		 fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
		 os.Exit(1)
	 }
 }
