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
		fmt.Fprintf(os.Stderr, "yeet: %s\n", err.Error())
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
	if err = tx.Flush(); err != nil {
		return
	}
	// write size
	length := proto.Size(resp)
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
}

func PlayerPositionHandler(conn net.Conn, buf []byte) {
	m := &PlayerPosition{}
	if err := proto.Unmarshal(buf, m); err != nil {
		fmt.Fprintf(os.Stderr, "error: %s\n", err.Error())
		return
	}
	fmt.Println(m)
}
