package main

import (
	"fmt"
	"sort"
)

type Person struct {
	FirstName string
	LastName  string
	Age       int
}

func main() {
	people := []Person{
		{"Pat", "Patterson", 34},
		{"Tracy", "Bobbert", 23},
		{"Fred", "Fredson", 18},
	}
	sort.Slice(people, func(i int, j int) bool {
		return people[i].LastName < people[j].LastName
	})
	fmt.Println(people)
}
