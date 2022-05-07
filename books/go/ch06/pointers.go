package main

import "fmt"

func failedUpdate(px *int) {
	x2 := 20
	px = &x2
}

func update(px *int) {
	*px = 20
}

func main() {
	y := "hello"
	fmt.Println(y, &y, *&y)

	x := 10
	failedUpdate(&x)
	fmt.Println(x)
	update(&x)
	fmt.Println(x)
}
