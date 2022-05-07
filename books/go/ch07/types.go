package main

import "fmt"

type Person struct {
	FirstName string
	LastName  string
	Age       int
}

type King Person // this is not an inheritance

func (p Person) String() string {
	return fmt.Sprintf("%s %s, age %d", p.FirstName, p.LastName, p.Age)
}

type Score int
type Converter func(string) Score
type TeamScore map[string]Score

func main() {
	p := Person{
		FirstName: "Fred",
		LastName:  "Fredson",
		Age:       52,
	}
	fmt.Println(p.String())
}
