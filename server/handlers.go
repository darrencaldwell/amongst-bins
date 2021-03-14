package main

import(
	"fmt"
	"net"
	"os"
	"bufio"
	"github.com/golang/protobuf/proto"
)

func JoinHandler(conn net.Conn, buf []byte) {
	
	// rx := bufio.NewReader(conn)
	tx := bufio.NewWriter(conn)

	var m JoinGame
	if err := proto.Unmarshal(buf, &m); err != nil {
		fmt.Fprintf(os.Stderr, "error: %s", err.Error())
		return
	}
	fmt.Println(m)
	resp := &EchoJoinGame{}
	id := Join(m.Username)
	resp.PlayerId = int32(id)

	res, err := proto.Marshal(resp)
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
	length := proto.Size(resp)
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