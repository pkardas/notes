package main

import (
	"fmt"
)

func main() {
	completeFor()
	conditionOnlyFor()
	infiniteFor()
	forRange()
	labelingStatements()
}

func completeFor() {
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}
}

func conditionOnlyFor() {
	i := 1
	for i < 100 {
		fmt.Println(i)
		i = i * 2
	}
}

func infiniteFor() {
	for {
		fmt.Println("Hello")
		break
	}
}

func forRange() {
	evenVals := []int{2, 4, 6, 8, 10, 12}
	for i, v := range evenVals {
		fmt.Println(i, v)
	}

	for _, v := range evenVals {
		fmt.Println(v)
	}

	for _, v := range evenVals {
		fmt.Println(v)
	}

	uniqueNames := map[string]bool{"Fred": true, "Paul": true, "Wilma": true}
	for k := range uniqueNames {
		fmt.Println(k)
	}
}

func labelingStatements() {
	samples := []string{"hello", "apple_π!"}
outer:
	for _, sample := range samples {
		for i, r := range sample {
			fmt.Println(i, r, string(r))
			if r == 'l' {
				continue outer
			}
		}
		fmt.Println()
	}
}
