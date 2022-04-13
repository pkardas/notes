[go back](https://github.com/pkardas/learning)

# Learning Go: An Idiomatic Approach to Real-World Go Programming

Book by Jon Bodner

- [Chapter 1: Setting Up Your Go Environment](#chapter-1-setting-up-your-go-environment)

## Chapter 1: Setting Up Your Go Environment

Go is intended for building programs that last, programs that are modified by dozens of developers over dozens of years.
Using Go correctly requires an understanding of how its features are intended to fit together. You can write code that
looks like Java or Python, but you are going to be unhappy with the result.

> $ brew install go

Validate that your env is set up correctly: `go version`

There have been several changes in how Go developers organize their code and their dependencies. For modern Go
development, the rules is simple: **you are free to organize your projects as you see fit**. However, Go still expects
there to be a single workspace (default `$HOME/go`) for third-party Go tools installed via `go install`. You can use
this default or set `$GOPATH` env variable.

Add following lines to `.zshrc`:

```
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin
```

Use `go run` when you want to treat a Go program like a script and run the source code immediately. `go run` builds the
binary in a temporary directory, and the deletes the binary after your program finishes. Useful for testing out small
programs or using Go like a scripting language.

Use `go build` to create a binary that is distributed for other people to use. Most of the time, this is what you want
to do. Use the `-o` flag to give the binary a different name or location.

Go programs can be also built from source and installed into your Go work-space via `go install link@version`. Go
developers don't rely on a centrally hosted service (Maven, PyPI, NPM, ...). Instead they share projects via their
source code repositories. If you already installed a tool and want to update it to a newer version, rerun `go install`
with the newer version specified after `@`.

Developers have historically wasted extraordinary amounts of time on format wars. Go defines a standard way of
formatting code, Go developers avoid arguments over code styling.

`go fmt` automatically reformat code to match the standard format.

Go requires a semicolon at the end of every statement. However, Go developers never put the semicolons by themselves;
the Go compiler does it for them.
