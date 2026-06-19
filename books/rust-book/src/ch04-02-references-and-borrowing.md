# References and Borrowing

> 📖 原文：<https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html>
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
A reference is not slower just because it is safe. The checking mostly happens at compile time.

We call the action of creating a reference **borrowing**.

Mutable references have one big restriction: If you have a mutable reference to a value, you can have no other references to that value. 

You can have either:
one mutable reference
or many immutable references 
but not both at a time.

Many readers OR one writer.

&T = shared read access
&mut T = exclusive write access 

Rust allows

many shared readers 

one exclusive writer 

But never 

shared readers + writer

multiple writers 

```text 
&mut T
compile-time exclusivity, no runtime lock 
&mut T itself is still a synchronization-like guarantee in Rust's type system, but it is not a runtime synchronization mechanism.

Mutex<T>
runtime synchronization, my block/wait 

```

a reference's scope starts from where it is introduced and continues through the last time that reference is used.



<!-- 没读懂的地方、想深入研究的方向、和已知知识的联系 -->

## 与其他章节的联系

<!-- 这一节用到了哪些前面学过的概念？它会被后面的哪些章节用到？ -->


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