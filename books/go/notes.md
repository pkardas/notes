[go back](https://github.com/pkardas/learning)

# Learning Go: An Idiomatic Approach to Real-World Go Programming

Book by Jon Bodner

- [Chapter 1: Setting Up Your Go Environment](#chapter-1-setting-up-your-go-environment)
- [Chapter 2: Primitive Types and Declarations](#chapter-2-primitive-types-and-declarations)
- [Chapter 3: Composite Types](#chapter-3-composite-types)
- [Chapter 4: Blocks, Shadows, and Control Structures](#chapter-4-blocks-shadows-and-control-structures)
- [Chapter 5: Functions](#chapter-5-functions)
- [Chapter 6: Pointers](#chapter-6-pointers)
- [Chapter 7: Types, Methods, and Interfaces](#chapter-7-types-methods-and-interfaces)

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
comparable, those with slice or map fields are not. Unlike Python, there are no methods that can be overridden to
redefine equality.

Go allows you to perform a type conversion from one struct to another _if the fields of both structs have the same
names, order, and types_.

## Chapter 4: Blocks, Shadows, and Control Structures

BLOCKS - Go lets you declare variables in lots of places. You can declare them outside of functions, as the parameters
to functions, and as local variables within functions.

Each place where a declaration occurs is called a _block_. Variables, constants, types and functions declared outside
any functions are placed in the package module.

`:=` reuses variables that are declared in the current block. When using `:=` make sure that you don't have any
variables from an outer scope on the left-hand side, unless you intend to shadow them.

Sometimes avoid using `:=` because it may make it unclear what variables are being used.

There is a `shadow` linter - a tool to detect shadowing.

The Universe Block - the block that contains all other blocks. Never redefine any of the identifiers in the universe
block (`true`, `false`, `string`, `int`, ...). If you accidentally do so, you will get some very strange behavior.

IF - Go doesn't require you to put parenthesis around the condition. You can declare variables that are scoped to the
condition and to both the `if` and `else` blocks.

```go
if n := rand.Intn(10); n == 10
```

Having this special scope is very handy, it lets you create variables that are available only where they are needed.
Once the series of `if/else` statements ends, `n` is undefined.

FOR - Go has 4 formats of `for`.

- C-style `for`
- condition only `for`
- infinite `for`
- `for-range`

When iterating over `map`, some runs may be identical. This is a security feature. In older Go versions, the iteration
order was usually the same. People used to write code that the order was fixed, and this would break at weird times.
Random read, prevents _Hash DoS_ attack.

When iterating over a string with `for-range` loop, it iterates over the runes, not the bytes. Whenever a `for-range`
loop encounters a multibyte rune in a string, it converts the UTF-8 representation into a single 32-nit number and
assigns it to the value.

Every time the `for-loop` iterates over your compound type, it copies the value from the compound type to the value
variable.

SWITCH - like an `if` statement, you can declare a variable that is scoped to all the branches of the switch statement.

If you have a `switch` statement inside a `for loop`, and you want to break out of the `for loop`, put a label on
the `for` statement, and then do `break label`. If you don't use a label, Go assumes that you want to break out of the
case.

You can create a "blank switch" - this allows you to use any boolean comparison for each case. There isn't a lot of
difference between a series of `if/else` statements and a blank `switch`. Favor blank `switch` statements over `if/else`
chains when you have multiple related cases. Using a `switch` makes the comparisons more visible and reinforces that
they ate a related set of concerns.

GOTO - Traditionally `goto` was dangerous because it could jump to nearly anywhere in a program (jump into/out of a
loop, skip variable definitions, or into the middle of a set of statements in `if`). This made it difficult to
understand what a goto-using program did.

Go has a `goto` statement (most modern languages don't). You should still do what you can to avoid using it. Go forbids
jumps that skip over variable declarations and jumps that go into an inner or parallel block.

## Chapter 5: Functions

`main` - the starting point for every Go program.

Go is a typed language, so you must specify the types of parameters. If a function returns a value, you must supply a
return.

Go doesn't have named and optional input parameters. If you want to emulate named and optional parameters, define a
struct that has fields that match the desired parameters, and pass the struct to your function.

Not having named and optional parameters isn't a limitation. A function shouldn't have more than a few parameters, and
named and optional parameters are mostly useful when a function has many inputs. If you find yourself in that situation,
your function is quite possibly too complicated.

Variadic input - `func addTo(base int, vals ... int)` - must be the last parameter in the input parameter list.

Go allows for multiple return values - `def divAndRemainder(numerator int, denominator int) (int, int, error)`. You can
pre-declare variables that you use within function to hold the return
values: `def divAndRemainder(numerator int, denominator int) (result int, remainder int, err error)`. Name that is used
for a named returned value is local to the function - it doesn't enforce any name outside the function.

If you use named return values, you can use empty/blank/naked return - never use it. This returns the last values
assigned to the named return values. It can be really confusing to figure out what value is actually returned.

Use `_` whenever you don't need to read a value that is returned by a function.

Just like in many other languages, functions in Go are values. Any function that has the exact same number and types of
parameters and return values meets the type signature.

Anonymous functions - they don't have a name. You don't have to assign them to a variable. You can write them inline and
call them immediately.

Functions declared inside functions are called _closures_. This is a computer science word that means that functions
declared inside of functions are able to access and modify variables declared in the outer function.

Not only you can use a closure to pass some function state to another function, you can also return a closure from a
function.

`defer` - used to release resources. Programs often create temporary resources, like files or network connections, that
need to be cleaned up. You can `defer` multiple closures in a Go function. They run last-in-first-out order - the last
defer registered runs first.

In Go, _defer_ statements delay the execution of the function or method or an anonymous method until the nearby
functions returns. In other words, defer function or method call arguments evaluate instantly, but they don't execute
until the nearby functions returns.

A common pattern in Go is for a function that allocates a resource to also return a closure that cleans up the resource.

Empirical Software Engineering:
> Of... eleven proposed characteristics, only two markedly influence complexity growth: the nesting depth and the lack
> of structure.

Go is _Call By Value_ - it means that when you supply a variable for a parameter to a function, Go always makes a copy
of the value of the variable. Every type in Go is a value type. It is just that sometimes the value is pointer (map,
slice).

## Chapter 6: Pointers

A pointer - a variable that holds the location in memory where a value is stored. Every variable is stored in one or
more contiguous memory locations - _addresses_.

- `&` - the _address_ operator, returns the address of the memory location where the value is stored.
- `*` - the _indirection_ operator, returns pointed-to value.

Example pointer **type**: `*int`

Before de-referencing a pointer, you must make sure that the pointer is non-nil. Your program will panic if you attempt
to de-reference a _nil_ pointer.

Java, Python, JavaScript, and Ruby are pass-by-value (values passed to functions are copies) - just like Go. Every
instance of a class in these languages is implemented as a pointer. When a class instance is passed to a function or
method, the value being copied is the pointer to the instance.

> Immutable types are safer from bugs, easier to understand, and more ready for change. Mutability makes it harder to
> understand what your program is doing, and much harder ro enforce contracts.

The lack of immutable declarations in Go might seem problematic, but the ability to choose between value and pointer
parameter types addresses the issue.

Be careful when using pointers in Go. They make it hard to understand data flow anc can create extra work for the
garbage collector. Rather than populating a struct by passing a pointer to it to function, have the function instantiate
the struct. The only time you should use pointer params to modify a variable is when the function expects an interface,
You see this pattern when working with JSON.

The time to pass a pointer into a function ~ 1ns. Passing a value into a function takes longer as the data gets larger,
1ms for ~10MB data. So if data is large enough, there are performance benefits from using a pointer. On the other hand
it does not pay off to use a pointer for small data (< 1MB), e.g. 100 byte data: 30ns (pointer) vs 10ns (copy value).

Pointers indicate mutability - be careful when using this pattern.

Avoid using maps for input or return values (map is implemented as a pointer to a struct). Rather than passing map
around, use a struct. Passing a slice to a function has even more complicated behavior: any modification to the contents
is reflected, but use of _append_ is not reflected. As the only linear data structure, slices are often passed around in
Go programs - by default you should assume that a slice is not modified by a function.

Garbage - data that has no more pointers pointing to it. Once there are no more pointers pointing to some data, the
memory can be reused. If the memory isn't recovered, the program's memory usage would continue to grow until the
computer run out of RAM. The job of a garbage collector is to automatically detect unused memory and recover it.

The Stack - consecutive block of memory, allocation fast and simple, local variables along parameters passed into a
function stored on a stack. You have to know exactly how big it is at compile time. When the compiler determines that
the data can't be stored on the stack, the data the pointer points to _escapes_ the stack and the compiler stores the
data on the heap.

The Heap - memory managed by the garbage collector. Go's garbage collector favours lower latency (< 500ms, finish as
quickly as possible) over throughput (find the most garbage possible in a single scan). If your program creates a lot of
garbage, the garbage collector will not find all the garbage during a cycle, slowing down the collector and increasing
memory usage.

Go encourages you to use pointers sparingly.We reduce teh workload of the garbage collector by making sure that as much
as possible is stored on the stack.

## Chapter 7: Types, Methods, and Interfaces

Go is designed to encourage the best practices that are advocated by software engineers, avoiding inheritance while
encouraging composition.

Methods: `func (p Person) String() string`, `(p Person)` is like `self` or `this`, however it is non-idiomatic to
use `self` or `this`. This is called a _receiver_, usually should have a short name. Methods can not be overloaded. You
can't add methods to the types you don't control.

- If method modifies the receiver, you _must_ use a pointer receiver
- If method needs to handle _nil_ instances, you _must_ use a pointer receiver
- If method doesn't modify the receiver, you can _use_ a value receiver

When a type has any pointer receiver methods, a common practice is to be consistent and use pointer receivers for all
methods, even the ones that don;t modify the receiver.

Do not write getters/setters. Go encourages you to directly access a field. Reserve methods for business logic.

Defining a user-defined type based on other type, makes code clearer by providing a name for a concept and describing
the kind of data that is expected (e.g. type `Percentage` vs `int`).

Go doesn't have enumerations, instead it has `iota` - which allows you to assign an increasing value to a set of
constants. `iota` makes sense when you care about being able to differentiate between a set of values, and don't
particularly care what the value is behind the scenes. If teh actual value matters, specify it explicitly.

Embedding - promote methods on the embedded type to the containing struct. Embedding support is rare in programming
languages. Do not mislead embedding with inheritance, they are not the same. If the containing struct has fields/methods
with the same name, you need to use embedded field type to refer to the obscured fields/methods.

The real star of Go's design - implicit interfaces. `interface` literal lists all methods that must be implemented by a
concrete type to meet the interface. Interfaces are usually named with `er` endings (`io.Reader`, `io.Closer`
, `json.Marshaller`, `http.Handler`).

Go blends duck-typing and Java's interfaces. Implicit interfaces give the flexibility of changing implementation and
make it easier to understand whe the code is doing.

> Interfaces specify what callers need. The client code defines the interface to specify what functionality it requires.

**Accept interfaces, return structs.** The business logic invoked by your functions should be invoked via interfaces,
but the output of your functions should be a concrete type. Go encourages small interfaces.

Sometimes you need to say that a variable could store any value, Go uses `interface{}` to represent this. It matches
every type in Go. However, avoid this. Go was designed as a strongly typed language and attempts to work around this are
unidiomatic.

Dependency injection - code should explicitly specify the functionality it needs to perform its task. Implicit
interfaces make dependency injection an excellent way to decouple your code.

> "Dependency Injection" is a 25-dollar term for a 5-cent concept. [...] Dependency injection means giving an object its
> instance variables. [...].

> Dependency injection is basically providing the objects that an object needs (its dependencies) instead of having it
> construct them itself. It's a very useful technique for testing, since it allows dependencies to be mocked or stubbed
> out.

Use `Wire` if you think writing dependency injection code by hand is too much work.

Go is not Object-Oriented, nor functional, nor procedural. It is practical. It borrows concepts from many places with
the overriding goal of creating a language that is simple, readable, and maintainable by large teams for many years.
