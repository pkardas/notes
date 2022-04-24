package main

import (
	"fmt"
	"math/rand"
)

func main() {
	if n := rand.Intn(10); n == 10 {
		fmt.Println("That's too low")
	} else if n > 5 {
		fmt.Println("That's too big:", n)
	} else {
		fmt.Println("That's a good number:", n)
	}
}
