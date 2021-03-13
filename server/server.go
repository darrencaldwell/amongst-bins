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
	 c := bufio.NewReader(conn)

	 fmt.Println("connection made!")
 
	 //infiniti boi to handle reqs from a client
	 for {
		// read type of message
		num, err := c.ReadByte()
		if err != nil {
			return 
		}
		// read size
		size, err := c.ReadByte()
		if err != nil {
			return 
		}

		 // read upto size bytes
		 buf := make([]byte, size)
		 n, err := io.ReadFull(c, buf[:])
		 if err != nil {
			fmt.Println("couldn't read")
			 return
		 }

		 m := &JoinGame{}
		 if err := proto.Unmarshal(buf, m); err != nil {
		 }
		 fmt.Println(m)
 
		 // write the n bytes read
		 _, err2 := conn.Write(buf[0:n])
		 if err2 != nil {
			fmt.Println("couldn't write")
			 return
		 }
		 fmt.Println("written")
	 }
 }
 
 func checkError(err error) {
	 if err != nil {
		 fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
		 os.Exit(1)
	 }
 }
