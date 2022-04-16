package main

import "fmt"

const x int64 = 10

const (
	idKey   = "id"
	nameKey = "name"
)

const z = 20 * 20

func main() {
	const y = "hello"

	fmt.Println(x)
	fmt.Println(y)

	//x = x + 1 // Error
	//y = "bye" // Error

	fmt.Println(x)
	fmt.Println(y)
}
