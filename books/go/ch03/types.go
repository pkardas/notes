package main

import "fmt"

func main() {
	var x [3]int
	fmt.Println(x)

	var y = [12]int{1, 5: 4}
	fmt.Println(y)

	var z = [...]int{12, 20, 30}
	fmt.Println(z)

	var p = []int{12, 20, 30}
	fmt.Println(p)

	var v []int
	fmt.Println(v == nil)
	fmt.Println(len(v))
	v = append(v, 10, 20)
	fmt.Println(v)
	v = append(v, p...)
	fmt.Println(v)
	fmt.Println(cap(v))

	r := make([]int, 5)
	fmt.Println(r)
	r = make([]int, 0, 20)
	r = append(r, 10, 20)
	fmt.Println(r)

	s := "Hello 😇"
	fmt.Println(s[6:7])
	fmt.Println(s[6:10]) // 4 bytes for emoji

	teams := map[string][]string{
		"Orcas": {"Fred", "Ralph"},
		"Lions": {"Sarah", "Peter"},
	}
	fmt.Println(teams)
	team, ok := teams["Kittens"]
	fmt.Println(team, ok)

	set := map[int]bool{}
	vals := []int{1, 2, 3, 4, 5, 6, 7, 4, 3, 2, 3, 4, 3}
	for _, v := range vals {
		set[v] = true
	}
	fmt.Println(len(set), len(vals))
	if set[1] {
		fmt.Println("1 is in the set")
	}

	type person struct {
		name string
		age  int
		pet  string
	}
	julia := person{
		"Julia",
		30,
		"cat",
	}
	beth := person{
		name: "Beth",
	}
	fmt.Println(julia, beth)

	var bob struct {
		name string
		age  int
		pet  string
	}
	bob.name = "Bob"
	fmt.Println(bob)
}
