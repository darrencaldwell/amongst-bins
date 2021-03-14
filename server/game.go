package main

import(
	// "fmt"
	"sync"
)

var game Game //change this to a map[id]->Game
var mutex = &sync.Mutex{}

type Game struct {
	Players []Player
	Litter []Litter
	InProgress bool
}

type Litter struct {
	Id int //tell the client how to sprite the litter
	Pos Pos
}

type Player struct {
	// conn net.Conn,
	Id int
	Name string
	Pos Pos
}

type Pos struct {
	x int
	y int
}

//
func MovePlayer(id int, x int, y int) {
	pos := Pos{x,y}
	mutex.Lock()
	game.Players[id].Pos = pos
	mutex.Unlock()
}


// func PlaceLitter() {
// }


func CreateGame() {
	game = Game{
		Players: []Player{},
		Litter: []Litter{},
		InProgress: true,
	}
	// Game.players := make()
}


//return their index into the players array
func Join(nickname string) int {
	mutex.Lock()
	ind := len(game.Players)
	p := Player{ind, nickname, Pos{0,0}}
	mutex.Unlock()
	game.Players = append(game.Players, p)
	return ind
}

// func main() {
// 	CreateGame()
// 	bob := JoinGame("bob")
// 	fmt.Printf("%+v", game.Players)
// 	steve := JoinGame("steve")
// 	fmt.Printf("%+v", game.Players)

// 	MovePlayer(bob,40,40)
// 	MovePlayer(steve,80,40)

// 	fmt.Printf("%+v", game.Players)
// }

