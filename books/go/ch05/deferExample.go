package main

import (
	"io"
	"log"
	"os"
)

func getFile(name string) (*os.File, func(), error) {
	f, err := os.Open(name)
	if err != nil {
		return nil, nil, err
	}
	return f, func() {
		f.Close()
	}, nil
}

func main() {
	if len(os.Args) < 2 {
		log.Fatal("no file specified")
	}
	f, closer, err := getFile(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	defer closer()
	data := make([]byte, 2048)
	for {
		count, err := f.Read(data)
		os.Stdout.Write(data[:count])
		if err != nil {
			if err != io.EOF {
				log.Fatal(err)
			}
			break
		}
	}
}
