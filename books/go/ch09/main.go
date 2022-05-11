package main

import (
	"./formatter"
	"./math"
	"fmt"
)

func main() {
	num := math.Double(2)
	output := print.Format(num)
	fmt.Println(output)
}
