# Using Box<T> to Point to Data on the Heap

> 📖 原文：<https://doc.rust-lang.org/book/ch15-01-box.html>
> 📅 读完时间：_____
> 状态：⬜ 未读 / 🟡 在读 / ✅ 已读

## 一句话总结

<!-- 用一句话概括这一节讲了什么 -->
What is Box and how to use Box?

Box<T> gives Rust a fixed-size pointer on the stack to data on the heap.

This is especially usefull when direct storage would make the type to large, recursively infinite, or impossible to size at compile time.

## 核心要点

- Where does Box come From?
- What is Box?
- How to use Box?
- Box<BigData> = own a large concrete value through a small pointer
- Box<dyn Draw> = own any vlaue that implements Draw through a small dynamic interface

## 关键概念

<!-- 本节出现的术语、概念、API -->

| 概念 | 解释 |
| --- | --- |
|      |      |
- smart pointer
- transfer value from stack to heap
- value on heap, pointer on tack and point to heap
- allocated by Box::new() on heap, deallocated automically Rust when going out of scope
- use cases
  > 1. You have a type whose size cannot be known at compile time.
  > 2. You have a large value and want to move ownership cheaply by moving only a pointer
  > 3. You want to own a value through a trait object, such as Box<dyn Trait>


## 代码示例

### allocate vs deallocate
```rust
fn main() {
     // puts the integer 5 on the heap
     // stores a pointer to it in b on stack
    let b = Box::new(5);// allocate on the heap 
    println!("b = {b}");
}// deallocate both the box value and the heap data it points to.
```

### recursive types
```rust
enum Expr {
    Number(i32), 
    Add(Expr, Expr), // type has infinite size
}

enum Expr {
    Number(i32), 
    Add(Box<Expr>, Box<Expr>),// now Add contains two fixed-size pointers, not null Expr values directly
}
```

### store large type 

```rust
struct BigData {
    bytes: [u8; 1_000_000],
}

fn process_bid_data(data: Box<BigData>) {
    println!("first byte ={}", data.bytes[0]);
}
```
without Box, BigData is a huge value, about 1MB
```text
stack:
[data: pointer] ──────▶️ heap:
                       [ BigData: 1,000,000 bytes ]
```
When you pass data to process, you move only the Box, which is basically a pointer

```text
move Box<BigData> = move pointer-sized owner
```

The deep meaning
> Box<T> separates ownership from physical storage. You still own the BigData, but the stack only carries a small fixed-size handle to it.

### trait ojbect Box<dyn Trait>

> Box<dyn Trait> lets you own values of different concrete types through one shared behavior interface.
```rust
trait Draw {
    fn draw(&self);
}

struct Button;
struct Image;

impl Draw for Button {
    fn draw(&self) {
        printl!("drawing a button");
    }
}

impl draw for Image {
    fn draw(&self) {
        println!("drawing an image");
    }
}

fn main() {
    let widgets: Vec<Box<dyn Draw>> = vec![
        Box::new(Button),
        Box::new(Image),
    ];

    for widget in widgets {
        widget.draw();
    }
}

```





## 我的疑问与思考

<!-- 没读懂的地方、想深入研究的方向、和已知知识的联系 -->

## 与其他章节的联系

<!-- 这一节用到了哪些前面学过的概念？它会被后面的哪些章节用到？ -->
