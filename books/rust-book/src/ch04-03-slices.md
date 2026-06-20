# The Slice Type

> Original: <https://doc.rust-lang.org/book/ch04-03-slices.html>  
> Finished date: 2026-06-19 
> Status: ✅ 已读

## One-Sentence Summary

Slices let you borrow a contiguous part of a collection without taking ownership, making APIs safer because the borrowed view stays tied to the original data.

## Core Points

- A slice is a reference to a contiguous sequence of elements in a collection.
- A slice does not own the data; it borrows part of existing data.
- Returning an index like `usize` can be brittle because the index is separate from the data it was calculated from.
- Returning a string slice, `&str`, ties the result to the original string, so Rust can catch invalid usage at compile time.
- String slice syntax uses ranges: `&s[start..end]`, where `start` is included and `end` is excluded.
- You can omit range endpoints: `&s[..2]`, `&s[3..]`, and `&s[..]`.
- String slice indices are byte indices and must be valid UTF-8 character boundaries.
- String literals have type `&str`; they are immutable slices pointing into the program binary.
- Function parameters should often use `&str` instead of `&String` because `&str` is more general.
- Slices are not only for strings; arrays and other collections can also have slices such as `&[i32]`.

## Key Concepts

| Concept | Explanation |
| --- | --- |
| Slice | A borrowed view into a contiguous part of a collection. |
| String slice | A slice of string data, written as `&str`. |
| `&str` | A reference to UTF-8 string data; it can point to a whole string or part of one. |
| `&s[start..end]` | Creates a slice from `start` up to, but not including, `end`. |
| Half-open range | A range where the start is included and the end is excluded. |
| `&s[..end]` | Slice from the beginning to `end`. |
| `&s[start..]` | Slice from `start` to the end. |
| `&s[..]` | Slice of the entire string or collection. |
| UTF-8 boundary | A valid position between UTF-8 characters; string slices must start and end on these boundaries. |
| `as_bytes()` | Converts a string-like value into a byte slice so code can inspect individual bytes. |
| `iter()` | Creates an iterator over a collection. |
| `enumerate()` | Wraps an iterator so each item comes with its index. |
| Deref coercion | The feature that lets `&String` be used where `&str` is expected. |
| Array slice | A borrowed view into part of an array, such as `&[i32]`. |

## Code Examples

```rust
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[..i];
        }
    }

    &s[..]
}

fn main() {
    let my_string = String::from("hello world");

    let word = first_word(&my_string);
    println!("first word: {word}");

    let literal = "hello rust";
    let word = first_word(literal);
    println!("first word: {word}");
}
```

```rust
fn main() {
    let s = String::from("hello world");

    let hello = &s[0..5];
    let world = &s[6..11];
    let whole = &s[..];

    println!("{hello}, {world}, {whole}");
}
```

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];

    let slice = &a[1..3];

    assert_eq!(slice, &[2, 3]);
}
```

## My Questions and Thoughts

- Why is `&str` preferred over `&String` in function parameters?
- How exactly does deref coercion convert `&String` into `&str`?
- Why are string slice indices byte indices instead of character indices?
- What happens if a slice range is out of bounds or not on a UTF-8 boundary?
- The key design insight is that an index is just a number, but a slice is a reference connected to the original data.

## Connections to Other Chapters

- This section builds directly on ownership and borrowing: a slice is another form of borrowing.
- It depends on the rule that immutable references prevent simultaneous mutable access.
- It prepares for Chapter 8, where `String`, `Vec<T>`, and other collections are discussed more deeply.
- It connects to iterators and `enumerate()`, which are explained later in Chapter 13.
- It connects to pattern matching because `for (i, &item)` uses a pattern to destructure iterator items.
- It connects to smart pointers and deref coercion, which are explained later in Chapter 15.



## 词语
- contiguous = next to each other/with no gaps
- slice = contiguous elements 
- slice = cut a piece from something 
- thorough discussion = detailed, careful, complete explanation 
- wrap = cover around sth 
- pattern = a repeated form, structure, a common way 
- sync = synchronization 
- out of sync = no longer inconsistent 
- brittle = easy to break/fragile
- tedious = boring, repetitive
- error-prone = likely to case mistakes
- even more = more than before 
- float around 
- one more than the last position
- internally = inside something
- drop = omit/not write 
- two periods = .. 
- trailing = following behind/ at the end 
- signify = mean/indicate/represent/show
- mess up = make a mistake/ confused 
- sooner = eariler/ before a later time
- recall = remember/ bring back to mind 
- tuncate = to cut sth short
- deref = dereference
- dereference = follow a reference or pointer to get the value it points to 
- coercion = automatic conversion from one type to another when Rust knows it is safe and expected 

## sentence 
- using indexes to remember parts of a String.
- index: just a number, disconnected from the string 
- slice: a reference into the string, connected to the string 
- 
