# Set default target, when 'make' executed, runs 'build' by default:
.DEFAULT_GOAL := build

fmt:
	go fmt ./...
# Keep 'make' from getting confused with directories, in this case with directory 'fmt' (if it is ever created):
.PHONY: fmt

# Before running 'lint', run 'fmt'
lint: fmt
	golint ./...
.PHONY: lint

vet: fmt
	go vet ./...
.PHONY: vet

build: vet
	go build hello.go
.PHONY: build
