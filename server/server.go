/* ThreadedEchoServer
 */
 package main

 import (
	 "net"
	 "os"
	 "fmt"
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

	 fmt.Println("connection made!")
 
	 var buf [512]byte
	 //infiniti boi to handle reqs from a client
	 for {
		 // read upto 512 bytes
		 n, err := conn.Read(buf[0:])
		 if err != nil {
			fmt.Println("couldn't read")
			 return
		 }
		 fmt.Printf("readen %s", string(buf[:]))
 
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
