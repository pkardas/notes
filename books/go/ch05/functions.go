package main

import (
	"errors"
	"fmt"
)

func main() {
	result := Div(5, 2)
	fmt.Println(result)

	MyFunc(MyFuncOpts{
		LastName: "Smith",
		Age:      10,
	})

	fmt.Println(addTo(10, 1, 2, 3, 4, 5))
	fmt.Println(addTo(10, []int{1, 2, 3, 4, 5}...))

	result, remainder, err := divAndRemainder(5, 2)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(result, remainder)
}

func Div(numerator int, denominator int) int {
	if denominator == 0 {
		return 0
	}
	return numerator / denominator
}

type MyFuncOpts struct {
	FirstName string
	LastName  string
	Age       int
}

func MyFunc(opts MyFuncOpts) int {
	return opts.Age
}

func addTo(base int, vals ...int) []int {
	out := make([]int, 0, len(vals))
	for _, v := range vals {
		out = append(out, base+v)
	}
	return out
}

func divAndRemainder(numerator int, denominator int) (result int, remainder int, err error) {
	if denominator == 0 {
		err = errors.New("cannot divide by zero")
		return result, remainder, err
	}
	result, remainder, err = numerator/denominator, numerator%denominator, nil
	return result, remainder, err
}
