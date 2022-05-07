package main

import "fmt"

type LogicProvider struct{}

func (lp LogicProvider) Process(data string) string {
	return data
}

type Logic interface {
	Process(data string) string
}

type Client struct {
	L Logic
}

func (c Client) Program() {
	data := "whatever"
	c.L.Process(data)
}

func main() {
	c := Client{L: LogicProvider{}}
	c.Program()

	var i interface{}
	i = 1
	i = "a"
	fmt.Println(i)
}
