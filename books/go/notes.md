[go back](https://github.com/pkardas/learning)

# Learning Go: An Idiomatic Approach to Real-World Go Programming

Book by Jon Bodner

- [Chapter 1: Setting Up Your Go Environment](#chapter-1-setting-up-your-go-environment)
- [Chapter 2: Primitive Types and Declarations](#chapter-2-primitive-types-and-declarations)
- [Chapter 3: Composite Types](#chapter-3-composite-types)

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
formatting code, Go developers avoid arguments over code styling. Go developers expect code to look in a certain way and
follow certain rules, and if your code does not, it sticks out.

`go fmt` automatically reformat code to match the standard format.

Go requires a semicolon at the end of every statement. However, Go developers never put the semicolons by themselves;
the Go compiler does it for them.

`go vet` detects things like: passing the wrong number of parameters to formatting methods or assigning values to
variables that are never used.

Make `golint` and `go vet part of your development process to avoid common bugs and non-idiomatic code.

An IDE is nice to use, but it is hard to automate. Modern software development relies on repeatable, automatable builds
that can be run by anyone, anywhere, at any time. Go developers have adopted `make` as their solution.

You can use different Go versions:

```
go get golang.org/dl/go.1.15.6
go.1.15.6 download
go.1.15.6 build
```

In order to update Go version globally on your computer use regular `brew` commands.

## Chapter 2: Primitive Types and Declarations

When trying to figure out what "best" means, there is one overriding principle: write your programs in a way that makes
your intention clear.

LITERAL - in Go refers to writing out a number, character, or string.

- integer literals
    - sequences of numbers, normally base 10, but different prefixes are used to indicate other bases (`0b` binary, `0o`
      octal, `0x` hexadecimal).
    - put underscores in the middle of your literal, use them to improve readability, e.g. `120_000_000`
- floating point literals - they can also have an exponent specified with the letter `e` and a positive or negative
  number, e.g. `6.03e23`
- rune literals - characters surrounded by single quotes, in Go `"` and `'` are _not_ interchangeable.
- string literals - two different ways to create:
    - interpreted string literal (") zero or more rune literals
    - raw string literal (`) can contain any literal character except a backquote
    - strings in Go are immutable

Literals in Go are untyped - they can interact with any variable that is compatible with the literal.

BOOLEAN - `true` or `false`, variable definition defaults to `false`. Go doesn't allow truthiness - e.g. positive
integer can not be treated as `true`.

INTEGER TYPES - 12 different types, more than other languages. 3 rules to follow:

1. If you are working with a binary format or network protocol that has an integer of a specific size or sign, use
   corresponding integer type.
2. If you are writing a library function that should work with any integer type, write a pair of functions, one for
   `int64`, and the other for `uint64`. You can see this pattern in std library (ParseInt/ParseUint, ...)
3. In all other cases, just use `int`.

FLOATING POINT - `float64` is the default type, simples option is to use this type. Don't worry about memory usage,
unless you have used the profiler to determine it is a significant source of problems.

A floating point number cannot represent a decimal value exactly. Do not use them to represent money or any other value
that must have an exact decimal representation.

Go stores floats using IEEE 754 standard. 64 bits for the sign, 11 bits for the exponent, 52 bits to represent mantissa.

Go doesn't allow automatic type promotion, as a language that values clarity of intent and readability. It turns out
that the rules to properly convert one type to another can get complicated and produce unexpected results. You must use
type conversion.

Variable declaration. Go has multiple ways of declaring a variable, because each declaration style communicates
something about how the variable is used.

- `var x int = 10`
- `var x = 10`
- `var x int` - will default to 0
- `var z, y int = 10, 20`
- `var x, y = 10, "hello"`
- `var(...)` - declaration list
- `x := 10`

The most common declaration style within functions is `:=`. Outside a function, use declaration lists. Sometimes you
need to avoid `:=`:

1. When initializing a variable to its zero value, use `var x int`. This makes it clear that the zero is intended.
2. Because `:=` allows assigning to new and existing variables, it is confusing if you use new or existing variable.
   Declare all new variables with `var`, and then use assignment operator (`=`) to both new and old variables.
3. When you need to convert type during assignment, use `var x byte = 20`, not `x := byte(20)`.

Go allows Unicode characters and letters in the variable name. However, don't use this feature.

Naming:

- use `camelCase`, even for constant vars
- use single letters for e.g. loops: `k`, `v` are common names for `key`, `value`; `i` for `integer`, ...
- do not put type in the variable name
- use short names, they remove repetitive typing and force you to write smaller blocks of code (if you need a complete
  name to keep track of it, it is likely that your block of code does too much)

## Chapter 3: Composite Types

ARRAYS - rarely used in Go. All the elements in the array must be of the type that is specified.

```go
var x [3] int
var x [3] int{10, 20, 30}
var x = [12]int{1, 5: 4}  // Sparse array (most elements are set to zero value)
var x = [...]int{12, 20, 30}
```

Arrays are rarely used in go because they come with an unusual limitations:

- _size_ of the array is part of the _type_, `[3]int` has different type than `[4]int`, you can't use a variable to
  specify the size of an array
- you can't use a type conversion to convert arrays of different sizes to identical types

Don't use arrays unless you know the exact length you need ahead of time. Arrays in Go exist to provide backing stores
for SLICES.

SLICES - slices remove limitations of arrays. We can write a single function that processes slices of any size. We can
also grow slices as needed.

Slice definition:

```go
var x = []int{12, 20, 30}
```

Using `[...]` makes an array. Using `[]` makes a slice.

`nil` in Go has no type, can be assigned or compared against values of different types.

Built-in functions:

- `len` - `len(nil)`
- `append` - `x = append(x, 10, 20, 30)`, `x = append(x, y...)` (`...` used to expand the source slice)
- `cap` - `cap(v)` - returns the current capacity of a slice
- `make` - `x := make([]int, 5)` - it allows us to specify the type, length, and optionally, the capacity
- `copy` - `numberOfElementsCopied := copy(destination, source)` - if you need to create a copy that is independent of
  the original

Go is _Call by value_ - every time you pass a parameter to a function, Go makes a copy of the value that is passed in.

When a slice grows via `append`, Go increases a slice by more than a one when it runs out of capacity. Doubles the size
when the size of the capacity is less than 1024 and then grow by at least 25% afterward.

`make` and `append` is a preferred way of declaring slices.

Slicing: `[startingOffset: endingOffset]`. In Go when you take a slice from a slice, you are not making a copy of the
data, Instead you have 2 variables that are sharing two variables. Avoid modifying slices after they have been sliced or
if they were produced by slicing. Use the full slice expression to prevent `append` from sharing capacity between
slices (`x[:2:2]`, `x[2:4:4]`). The last position indicates the last position in the parent slice's capacity that is
available for the subslice. Subtract the starting offset from this number to get the subslice's capacity.

Array can be converted to Slice by using slicing expression.

Go allows us to use slicing notation to make substrings. Be very careful when doing so. Strings are immutable, they
don't have modification problem BUT a string is composed of _bytes_, a code point in UTF-8 can be anywhere from one to
four bytes long. When dealing with languages other than English or with emojis, you run into code points that are
multiple bytes long.

UTF-8 is very clever, in worst case uses 4 bytes, in best case only one. The only downside is that you cannot randomly
access a string encoded with UTF-8.

MAPS - dictionary/hash map. Declaration `map[keyType]valueType`.

- maps automatically grow as you add key-value pairs
- is you know how many key-value pairs you plan to insert into a map, you can use `make` to create a map with specific
  initial size
- passing a _map_ to the _len_ function tells you the number of key-value pairs in a _map_
- the zero value for a map is nil
- maps are not comparable

Go doesn't allow you to define your own hash algorithm.

Comma ok idiom - boolean value, if ok is true - key is present, ok is false - key is not present.

- `delete` - `delete(m, key)` (remove key-value pair from the map)

Go does not include sets, but you can use a map to simulate some of its features. Set simulation:

```go
set := map[int]bool{}
```

If you need sets that provide operations like union, intersection, and subtraction - write one yourself or use 3rd-party
library.

STRUCT - when you have related data that you want to group together.

```
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
```

Anonymous struct - without giving it a name first:

```
var person struct {
    name string
    age  int
    pet  string
}
person.name = "Bob"
```

Whether struct is comparable depends on struct's fields. Structs that are entirely composed of comparable types are
comparable, those with slice of map fields are not. Unlike Python, there are no methods that can be overridden to
redefine equality.

Go allows you to perform a type conversion from one struct to another _if the fields of both structs have the same
names, order, and types_.
