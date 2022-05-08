package main

func doPanic(msg string) {
	panic(msg)
}

func main() {
	doPanic("ERR")
}
