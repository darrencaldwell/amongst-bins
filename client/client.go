/* GetHeadInfo
 */
 package main

 import (
	 "net"
	 "os"
	 "fmt"
	 "io/ioutil"
	 "bufio"
	 "github.com/golang/protobuf/proto"
 )
 
 func main() {
	 if len(os.Args) != 2 {
		 fmt.Fprintf(os.Stderr, "Usage: %s host:port ", os.Args[0])
		 os.Exit(1)
	 }
	 service := os.Args[1]
 
	 tcpAddr, err := net.ResolveTCPAddr("tcp4", service)
	 checkError(err)
 
	 conn, err := net.DialTCP("tcp", nil, tcpAddr)
	 c := bufio.NewWriter(conn)
	 checkError(err)
	 fmt.Println("connected?")
 
	g := &JoinGame{
		Username: "aaa",
	}
  	out, err := proto.Marshal(g)
  	if err != nil {
  		fmt.Println("Failed to encode address book:", err)
  	}
	// write len of message
	var size uint8 = uint8(len(out))
	err = c.WriteByte(size)
  	if err != nil {
  		fmt.Println("Failed to encode address book:", err)
  	}
	 fmt.Println("ASDASD")
	 // write message
	 _, err = c.Write(out)
  	if err != nil {
  		fmt.Println("Failed to encode address book:", err)
  	}
	 checkError(err)
 
	 //result, err := readFully(conn)
	 result, err := ioutil.ReadAll(conn)
	 checkError(err)
 
	 fmt.Println(string(result))
 
	 os.Exit(0)
 }
 
 func checkError(err error) {
	 if err != nil {
		 fmt.Fprintf(os.Stderr, "Fatal error: %s", err.Error())
		 os.Exit(1)
	 }
 }
