# References and Borrowing

> Original: <https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html>  
> Finished date: _____  
> Status: [ ] Not started / [ ] Reading / [ ] Done

## One-Sentence Summary

References let code use a value without taking ownership, while Rust's borrowing rules ensure that reads, writes, and lifetimes remain safe at compile time.

## Core Points

- Borrowing means passing a reference to a value instead of transferring ownership of the value.
- `&T` creates an immutable reference, which allows reading but not modifying the value.
- `&mut T` creates a mutable reference, which allows modifying the value but requires exclusive access.
- At any given time, Rust allows either one mutable reference or any number of immutable references to the same value, but not both.
- A reference must never outlive the value it points to; Rust prevents dangling references at compile time.
- Borrowing errors can feel restrictive, but they help catch potential bugs before the program runs.

## Key Concepts

| Concept | Explanation |
| --- | --- |
| Reference | A pointer-like value that lets you access data without owning it. |
| Borrowing | Creating and using a reference to a value. |
| Immutable reference | A reference written as `&T`; it allows read-only access. |
| Mutable reference | A reference written as `&mut T`; it allows modification through exclusive access. |
| Exclusive access | The rule that only one active mutable reference may access a value at a time. |
| Data race | A bug where multiple accesses to the same data happen at the same time, at least one is a write, and there is no synchronization. |
| Dangling reference | A reference that points to data that no longer exists. |
| Non-lexical lifetime | Rust's ability to end a borrow after its last use, even before the end of the block scope. |

## Code Examples

```rust
fn calculate_length(s: &String) -> usize {
    s.len()
}

fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1);

    println!("The length of '{s1}' is {len}.");
}
```

```rust
fn change(s: &mut String) {
    s.push_str(", world");
}

fn main() {
    let mut s = String::from("hello");

    change(&mut s);

    println!("{s}");
}
```

```rust
fn main() {
    let mut s = String::from("hello");

    let r1 = &s;
    let r2 = &s;
    println!("{r1} and {r2}");

    let r3 = &mut s;
    r3.push_str(", world");
    println!("{r3}");
}
```

## My Questions and Thoughts

- Why does `&mut T` require exclusive access instead of using a runtime lock?
- How does Rust decide exactly where a reference's lifetime ends?
- What is the difference between a safe reference and a raw pointer in low-level Rust?
- Borrowing feels strict at first, but the core intuition is simple: many readers are safe, one writer is safe, but readers and writers together need control.

## Connections to Other Chapters

- This section builds on ownership, move semantics, `Copy`, `Clone`, stack memory, and heap memory from the previous section.
- It prepares for slices, because slices are references to parts of a collection.
- It connects to structs and methods, where references are often used as method parameters such as `&self` and `&mut self`.
- It connects to concurrency, because Rust's borrowing rules are one foundation for preventing data races.
- It connects to smart pointers, because types such as `Box<T>`, `Rc<T>`, `Arc<T>`, and `RefCell<T>` extend or adjust the basic ownership and borrowing model.




## 词语
- ampersand = &
- depict = show, describe, represent something, especially in a pecture, diagram 
- likewise = similarly, in the same way 
- explanatory = used for explaining sth 
- spoiler alter
- it is behind = 在xxx的后面
- mutable = modify 
- borrowed as mutable = temporarily accessed with permission to modify
-  tweaks = a small change or adjustment
-  instead = as an alternative, rather than the previous thing 
-  once = one time 
-  at a time = druing the same period, simultaneously 
-  lexical = based on written code/block structure 
-  non-lexical = based on actual usage, more precise
-  non-lexical lifetime = borrow ends after last actual use, not just at end of block 
-  allow for = make possible, permit, leave room for 
-  controlled fashion = controlled way 
-  rustacean = rust programmer, people who use rust, nick name
-  struggle = have trouble with something 
-  mutate = change, modify 
-  whenever = at any time, every time 
-  you'd like = you would like, you want 
-  restriction = a rule or limit that prevents you from doing stgh freely 
-  race = a competition to be first
-  mechanism = method, tool, system 
-  synchronize = coordinate timing, order or operations do not conflict 
-  diagnose = identify the cause of a problem
-  track them down = search carfully util you find sth 
-  as always = as usual, as we normally can 
-  curly = curved, not straight
-  bracket = a punctuation mark used to group things
-  simultaneous = happening at the same time
-  enforce = make sure a rule is followed 强制执行
-  combine = use together, put together 
-  whew = hu
-  under them = under those users, while they are relying on it
-  overlap = two things cover/share part of the same sapce, time or range
-  can tell = can detect/ can figure out 
-  frustrate = making you feel annyoed, stuck 
-  at times = sometimes/occasionally
-  erroneously = wrongly/incorrectly 
-  dangling = to hang loosely 
-  preserve = keep/maintain/not destory 
-  by contrast = in comparsion/showing a difference
-  disregard = ignore/treat it as not important 
-  recap = a short summary
