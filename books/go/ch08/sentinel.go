package main

import (
	"archive/zip"
	"bytes"
	"fmt"
)

type Sentinel string

func (s Sentinel) Error() string {
	return string(s)
}

const (
	ErrFoo = Sentinel("foo err")
	ErrBar = Sentinel("bar err")
)

func main() {
	data := []byte("This is not a zip file")
	notZipFile := bytes.NewReader(data)
	_, err := zip.NewReader(notZipFile, int64(len(data)))
	if err == zip.ErrFormat {
		fmt.Println("Told you so")
	}
}
