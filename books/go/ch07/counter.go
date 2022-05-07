package main

import (
	"fmt"
	"time"
)

type Counter struct {
	total       int
	lastUpdated time.Time
}

func (c *Counter) Increment() {
	c.total++
	c.lastUpdated = time.Now()
}

func (c Counter) String() string {
	return fmt.Sprintf("total: %d, last updated %v", c.total, c.lastUpdated)
}

func updateWrong(c Counter) {
	c.Increment()
	fmt.Println("in updateWrong:", c.String())
}

func updateRight(c *Counter) {
	c.Increment()
	fmt.Println("in updateRight:", c.String())
}

func main() {
	var c Counter
	fmt.Println(c.String())
	c.Increment()
	fmt.Println(c.String())

	updateWrong(c)
	fmt.Println("in main:", c.String())
	updateRight(&c)
	fmt.Println("in main:", c.String())
}
