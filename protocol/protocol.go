package main

import (
	"fmt"
	"github.com/golang/protobuf/proto"
)

func aaa() {
	fmt.Println("Heelo nerd")
	g := &JoinGame{
		Username: "aaa",
	}
	out, err := proto.Marshal(g)
	if err != nil {
		fmt.Println("Failed to encode address book:", err)
	}
	fmt.Println(out)
	fmt.Println(g)
}
