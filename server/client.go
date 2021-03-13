/* GetHeadInfo
 */
 package main

 import (
	 "net"
	 "os"
	 "fmt"
	 "io/ioutil"
	 "github.com/golang/protobuf/proto"
	 "github.com/CynicalCode21/amongst-bins/protocol"
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
	 checkError(err)
	 fmt.Println("connected?")
 
	g := &JoinGame{
		Username: "aaa",
	}
	out, err := proto.Marshal(g)
	if err != nil {
		fmt.Println("Failed to encode address book:", err)
	}
	 _, err = conn.Write([]byte(out))
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
