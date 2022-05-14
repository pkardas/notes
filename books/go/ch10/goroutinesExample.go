package main

func process(val int) int {
	return val * 2
}

func runThingConcurrently(in <-chan int, out chan<- int) {
	go func() {
		for val := range in {
			result := process(val)
			out <- result
		}
	}()
}
