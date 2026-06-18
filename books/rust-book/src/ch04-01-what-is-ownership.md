# What is Ownership?

> 📖 原文：<https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html>
> 📅 读完时间：_____
> 状态：⬜ 未读 / 🟡 在读 / ✅ 已读

## 一句话总结

<!-- 用一句话概括这一节讲了什么 -->

## 核心要点

-
-
-

## 关键概念

<!-- 本节出现的术语、概念、API -->

| 概念 | 解释 |
| --- | --- |
|      |      |

## 代码示例

```rust
// 在阅读时想动手试的例子写在这里
```

## 我的疑问与思考

<!-- 没读懂的地方、想深入研究的方向、和已知知识的联系 -->
### stack
fixed-size

### heap 
unknown-sized
less organized = 
allocating on the heap 



## 与其他章节的联系

<!-- 这一节用到了哪些前面学过的概念？它会被后面的哪些章节用到？ -->


## 词语
- govern = control, guide
- regulary = again and again, repeatly, at normal intervals
- explicitly = directly, clearly, not automatically or hidden
- violated = broken rules, laws, or agreements
- None of = not any of 
- it does take some time = it really takes some time, emphasized sentence
- get used to = become familiar with something after some time
- work through = study or resolve sth step by step from beginning to end
- whether = 
- parts of = sections, 
- later = 
- refer to = known as 
- plate = flat dish
- pile = a group of things stacked together, a pile of books
- take one off =  remove
- not as well = 不那么好 
- push onto = adding data
- pop off = removing data
- instead = 
- abbreviate = make a word or phrase shorter
- state = to say clearly, to tell someone clearly
- seated = placed at a seat/table
- comparatively = compared with the ting just mentioned
- bookkeeping = keeping financial records
- contemporary = modern, current
- jump around less = move from place to place, not in order
- continuing the analogy = continuing to use the same example
- analogy = a comparsion used to explain sth
- by the same token = for the same reason, in the same way 
- usually = in most cases, but not always 
- potentially = possibly, maybe 
- including = 
- keep track of = watch, record, 
- address = handle, solve, deal with 
- run out of space = 
- now that = because sth is now true
- following along = read/watch and to the same steps yourself 跟着做
- a bit more = a little more
- concise =  short but clear
- boilerplate = standard repeated code/text that is necessary but not interesting
- literal = a value written directly in the source code, fixed value written directly in code 
- hardcode into = written directly and fixed inside the code 
- declare = introduce, create by a declaration in code 
- annotate = add notes or explanations
- trivially = very easily, simply, without much work or complexity
- as such = because of, therefore, for that reason 
- colon = :: operator 
- namespace = to push a name inside a specific named area, group, verb
- some sort of = some kine of 
- assumed = ascepted as 
- in terms of = when considering, from the perspective of 
- reverse = opposite, reverse relationship
- vis = through, by means of, using 
- as well = also, too
- entirety = the whole thing, the complete thing
- wrinkle = small line, fold on skin or cloth, small complication, extra detail
- not yet = not 
- contradict = go against sth, 
- prevent from = stop sb from doing sth 
- usual = normal, ordinary, typical, default
- leave it out = omit, not include it 
- subtle = not obvious, requiring careful thinging
- special annotation = a mark or note added to given extra info
- as integers are = in the same way that integers are stored on the stack
- as integers are stored on the stack 
- scalar value = represent one thing, not a collection of many things
- tuple = triple, an ordered group of values 
- afterward = after that, later 
- backing memory = the actual memory storage behind a value or data structure 
- backing memory = heap memory 
- tedious = boring, repetitive, and annoying because it takes too much effort 
- annoying = a little angry, bothered
- in addition to = as well as, besides 除了 ... 之外，还要加上
- resulting from = caused by , produced by, coming from 
- ceremony = extral formal steps, extra code, template code
- too much ceremony = too many unnecessary formal step
- two much ceremony = too much boilerplate-like code 
- 
- 

# ---------------------------------------------------------------------------------------------------------------------------------------------

## 句子
The stack stores values in the order it gets them
and remove the values in the opposite order.

in this paragraph, heap bookkeeping means the allocator must remember thing like: 
```text
Whick heap blocks are used?
Whick heap locks are frees?
How Large is each free block?
Where can the next allocation go?
```

Ownership helps solve three problems: knowing which code is using which heap data, avoiding unnecessary duplicate heap data, and cleaning up heap data that is no longer used.




This chapter is really about one question:

> **Who is responsible for cleaning up memory?**

Rust’s answer is:

> Every value has exactly one owner. When the owner goes out of scope, Rust automatically drops the value. ([doc.rust-lang.org](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html))

中文直觉：

> Rust 不想让你手动记 `free`，也不想用 GC 在运行时帮你找垃圾。Rust 让编译器在编译期检查：谁拥有这个值？谁负责清理它？

**1. Stack vs Heap**

English intuition:

```text
Stack = simple, fixed-size, automatic.
Heap = flexible, dynamic-size, needs ownership.
```

Stack data is easy: Rust knows its size, pushes it when a function starts, and pops it when the function ends. Heap data is harder: the allocator must find space, return a pointer, and later someone must give that memory back. Ownership mainly exists to manage heap data safely. ([doc.rust-lang.org](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html))

中文直觉：

> 栈像一摞盘子，规则简单。堆像餐厅找桌子，灵活但需要管理。Ownership 主要是在回答：堆上的东西到底谁负责？

**2. `String` Is The Key Example**

String literal:

```rust
let s = "hello";
```

English intuition:

```text
"hello" is fixed and known at compile time.
```

`String`:

```rust
let s = String::from("hello");
```

English intuition:

```text
String owns heap memory.
String can grow.
String must be cleaned up.
```

The chapter uses `String` because it stores text on the heap, so Rust must know when to free that heap memory. When a `String` goes out of scope, Rust calls `drop` automatically. ([doc.rust-lang.org](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html))

中文直觉：

> `String` 不是单纯的几个字母。它在栈上有 `pointer + length + capacity`，真正的文本在堆上。所以 `String` 有“资源责任”。

**3. Move**

This is the most important intuition:

```rust
let s1 = String::from("hello");
let s2 = s1;
```

English thinking:

```text
s1 does not get copied.
Ownership moves from s1 to s2.
After the move, s1 is invalid.
Only s2 will drop the heap memory.
```

Rust does this to prevent double free. If both `s1` and `s2` were valid and both pointed to the same heap data, they might both try to free the same memory. Rust solves this by invalidating `s1`. ([doc.rust-lang.org](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html))

中文直觉：

> move 不是“复制一份”，而是“换主人”。原主人 `s1` 失效，新主人 `s2` 负责清理。

**4. Clone**

If you really want a deep copy:

```rust
let s1 = String::from("hello");
let s2 = s1.clone();
```

English intuition:

```text
clone means: I know this may be expensive.
Please copy the heap data too.
```

The chapter emphasizes that Rust never automatically creates deep copies. If you see `.clone()`, that is a visual signal that extra work may happen. ([doc.rust-lang.org](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html))

中文直觉：

> Rust 不偷偷帮你做昂贵复制。你写 `.clone()`，就是你明确说：我要复制背后的资源。

**5. Copy**

For simple values:

```rust
let x = 5;
let y = x;

println!("{x}");
```

English intuition:

```text
i32 is small.
i32 has no heap resource.
Copying it is cheap.
So x stays valid.
```

Types like integers, booleans, floats, chars, and tuples made only of `Copy` values can implement `Copy`; types that allocate memory or own resources cannot implement `Copy`. ([doc.rust-lang.org](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html))

中文直觉：

> `Copy` 类型没有“资源责任”。复制它只是复制几个字节，不会产生 double free。

**6. Functions**

Passing values to functions follows the same rule as assignment:

```rust
fn takes_ownership(s: String) {}

let s = String::from("hello");
takes_ownership(s);
// s is no longer valid
```

English intuition:

```text
Passing a String moves ownership into the function.
When the function ends, it drops the String.
```

But for `Copy` types:

```rust
fn makes_copy(x: i32) {}

let x = 5;
makes_copy(x);
// x is still valid
```

English intuition:

```text
Passing an i32 copies it.
No ownership problem.
```

Return values can also transfer ownership back to the caller. The chapter ends by saying this take-and-return style works, but it is too much ceremony, which leads naturally to references: using a value without taking ownership. ([doc.rust-lang.org](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html))

**The English Mental Model**

Try to remember these sentences directly in English:

```text
A value has one owner.
Ownership can move.
Copy types are copied, not moved.
Clone is an explicit deep copy.
Drop runs when the owner goes out of scope.
Heap data needs an owner.
References let code use a value without owning it.
```

如果你能直接用这些英文句子思考，这章就通了。核心不是背规则，而是形成直觉：

> **Rust tracks responsibility. Whoever owns the value is responsible for cleanup.**