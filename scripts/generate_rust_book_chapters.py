#!/usr/bin/env python3
"""Generate all chapter files for the Rust Book notes with summary templates."""

from pathlib import Path

SRC = Path(__file__).parent.parent / "books/rust-book/src"

# (filename, chinese_title, english_title_for_url, original_url_path)
# original_url_path is the path after https://doc.rust-lang.org/book/
CHAPTERS = [
    # prefix
    ("title-page.md", "The Rust Programming Language", "title-page.html", None),
    ("foreword.md", "Foreword", "foreword.html", None),
    ("ch00-00-introduction.md", "Introduction", "ch00-00-introduction.html", None),
    # ch1
    ("ch01-00-getting-started.md", "Getting Started", "ch01-00-getting-started.html", 1),
    ("ch01-01-installation.md", "Installation", "ch01-01-installation.html", 1),
    ("ch01-02-hello-world.md", "Hello, World!", "ch01-02-hello-world.html", 1),
    ("ch01-03-hello-cargo.md", "Hello, Cargo!", "ch01-03-hello-cargo.html", 1),
    # ch2
    ("ch02-00-guessing-game-tutorial.md", "Programming a Guessing Game", "ch02-00-guessing-game-tutorial.html", 2),
    # ch3
    ("ch03-00-common-programming-concepts.md", "Common Programming Concepts", "ch03-00-common-programming-concepts.html", 3),
    ("ch03-01-variables-and-mutability.md", "Variables and Mutability", "ch03-01-variables-and-mutability.html", 3),
    ("ch03-02-data-types.md", "Data Types", "ch03-02-data-types.html", 3),
    ("ch03-03-how-functions-work.md", "Functions", "ch03-03-how-functions-work.html", 3),
    ("ch03-04-comments.md", "Comments", "ch03-04-comments.html", 3),
    ("ch03-05-control-flow.md", "Control Flow", "ch03-05-control-flow.html", 3),
    # ch4
    ("ch04-00-understanding-ownership.md", "Understanding Ownership", "ch04-00-understanding-ownership.html", 4),
    ("ch04-01-what-is-ownership.md", "What is Ownership?", "ch04-01-what-is-ownership.html", 4),
    ("ch04-02-references-and-borrowing.md", "References and Borrowing", "ch04-02-references-and-borrowing.html", 4),
    ("ch04-03-slices.md", "The Slice Type", "ch04-03-slices.html", 4),
    # ch5
    ("ch05-00-structs.md", "Using Structs to Structure Related Data", "ch05-00-structs.html", 5),
    ("ch05-01-defining-structs.md", "Defining and Instantiating Structs", "ch05-01-defining-structs.html", 5),
    ("ch05-02-example-structs.md", "An Example Program Using Structs", "ch05-02-example-structs.html", 5),
    ("ch05-03-method-syntax.md", "Methods", "ch05-03-method-syntax.html", 5),
    # ch6
    ("ch06-00-enums.md", "Enums and Pattern Matching", "ch06-00-enums.html", 6),
    ("ch06-01-defining-an-enum.md", "Defining an Enum", "ch06-01-defining-an-enum.html", 6),
    ("ch06-02-match.md", "The match Control Flow Construct", "ch06-02-match.html", 6),
    ("ch06-03-if-let.md", "Concise Control Flow with if let and let...else", "ch06-03-if-let.html", 6),
    # ch7
    ("ch07-00-managing-growing-projects-with-packages-crates-and-modules.md", "Packages, Crates, and Modules", "ch07-00-managing-growing-projects-with-packages-crates-and-modules.html", 7),
    ("ch07-01-packages-and-crates.md", "Packages and Crates", "ch07-01-packages-and-crates.html", 7),
    ("ch07-02-defining-modules-to-control-scope-and-privacy.md", "Control Scope and Privacy with Modules", "ch07-02-defining-modules-to-control-scope-and-privacy.html", 7),
    ("ch07-03-paths-for-referring-to-an-item-in-the-module-tree.md", "Paths for Referring to an Item in the Module Tree", "ch07-03-paths-for-referring-to-an-item-in-the-module-tree.html", 7),
    ("ch07-04-bringing-paths-into-scope-with-the-use-keyword.md", "Bringing Paths Into Scope with the use Keyword", "ch07-04-bringing-paths-into-scope-with-the-use-keyword.html", 7),
    ("ch07-05-separating-modules-into-different-files.md", "Separating Modules into Different Files", "ch07-05-separating-modules-into-different-files.html", 7),
    # ch8
    ("ch08-00-common-collections.md", "Common Collections", "ch08-00-common-collections.html", 8),
    ("ch08-01-vectors.md", "Storing Lists of Values with Vectors", "ch08-01-vectors.html", 8),
    ("ch08-02-strings.md", "Storing UTF-8 Encoded Text with Strings", "ch08-02-strings.html", 8),
    ("ch08-03-hash-maps.md", "Storing Keys with Associated Values in Hash Maps", "ch08-03-hash-maps.html", 8),
    # ch9
    ("ch09-00-error-handling.md", "Error Handling", "ch09-00-error-handling.html", 9),
    ("ch09-01-unrecoverable-errors-with-panic.md", "Unrecoverable Errors with panic!", "ch09-01-unrecoverable-errors-with-panic.html", 9),
    ("ch09-02-recoverable-errors-with-result.md", "Recoverable Errors with Result", "ch09-02-recoverable-errors-with-result.html", 9),
    ("ch09-03-to-panic-or-not-to-panic.md", "To panic! or Not to panic!", "ch09-03-to-panic-or-not-to-panic.html", 9),
    # ch10
    ("ch10-00-generics.md", "Generic Types, Traits, and Lifetimes", "ch10-00-generics.html", 10),
    ("ch10-01-syntax.md", "Generic Data Types", "ch10-01-syntax.html", 10),
    ("ch10-02-traits.md", "Defining Shared Behavior with Traits", "ch10-02-traits.html", 10),
    ("ch10-03-lifetime-syntax.md", "Validating References with Lifetimes", "ch10-03-lifetime-syntax.html", 10),
    # ch11
    ("ch11-00-testing.md", "Writing Automated Tests", "ch11-00-testing.html", 11),
    ("ch11-01-writing-tests.md", "How to Write Tests", "ch11-01-writing-tests.html", 11),
    ("ch11-02-running-tests.md", "Controlling How Tests Are Run", "ch11-02-running-tests.html", 11),
    ("ch11-03-test-organization.md", "Test Organization", "ch11-03-test-organization.html", 11),
    # ch12
    ("ch12-00-an-io-project.md", "An I/O Project: Building a Command Line Program", "ch12-00-an-io-project.html", 12),
    ("ch12-01-accepting-command-line-arguments.md", "Accepting Command Line Arguments", "ch12-01-accepting-command-line-arguments.html", 12),
    ("ch12-02-reading-a-file.md", "Reading a File", "ch12-02-reading-a-file.html", 12),
    ("ch12-03-improving-error-handling-and-modularity.md", "Refactoring to Improve Modularity and Error Handling", "ch12-03-improving-error-handling-and-modularity.html", 12),
    ("ch12-04-testing-the-librarys-functionality.md", "Adding Functionality with Test Driven Development", "ch12-04-testing-the-librarys-functionality.html", 12),
    ("ch12-05-working-with-environment-variables.md", "Working with Environment Variables", "ch12-05-working-with-environment-variables.html", 12),
    ("ch12-06-writing-to-stderr-instead-of-stdout.md", "Redirecting Errors to Standard Error", "ch12-06-writing-to-stderr-instead-of-stdout.html", 12),
    # ch13
    ("ch13-00-functional-features.md", "Functional Language Features: Iterators and Closures", "ch13-00-functional-features.html", 13),
    ("ch13-01-closures.md", "Closures", "ch13-01-closures.html", 13),
    ("ch13-02-iterators.md", "Processing a Series of Items with Iterators", "ch13-02-iterators.html", 13),
    ("ch13-03-improving-our-io-project.md", "Improving Our I/O Project", "ch13-03-improving-our-io-project.html", 13),
    ("ch13-04-performance.md", "Performance in Loops vs. Iterators", "ch13-04-performance.html", 13),
    # ch14
    ("ch14-00-more-about-cargo.md", "More about Cargo and Crates.io", "ch14-00-more-about-cargo.html", 14),
    ("ch14-01-release-profiles.md", "Customizing Builds with Release Profiles", "ch14-01-release-profiles.html", 14),
    ("ch14-02-publishing-to-crates-io.md", "Publishing a Crate to Crates.io", "ch14-02-publishing-to-crates-io.html", 14),
    ("ch14-03-cargo-workspaces.md", "Cargo Workspaces", "ch14-03-cargo-workspaces.html", 14),
    ("ch14-04-installing-binaries.md", "Installing Binaries with cargo install", "ch14-04-installing-binaries.html", 14),
    ("ch14-05-extending-cargo.md", "Extending Cargo with Custom Commands", "ch14-05-extending-cargo.html", 14),
    # ch15
    ("ch15-00-smart-pointers.md", "Smart Pointers", "ch15-00-smart-pointers.html", 15),
    ("ch15-01-box.md", "Using Box<T> to Point to Data on the Heap", "ch15-01-box.html", 15),
    ("ch15-02-deref.md", "Treating Smart Pointers Like Regular References", "ch15-02-deref.html", 15),
    ("ch15-03-drop.md", "Running Code on Cleanup with the Drop Trait", "ch15-03-drop.html", 15),
    ("ch15-04-rc.md", "Rc<T>, the Reference Counted Smart Pointer", "ch15-04-rc.html", 15),
    ("ch15-05-interior-mutability.md", "RefCell<T> and the Interior Mutability Pattern", "ch15-05-interior-mutability.html", 15),
    ("ch15-06-reference-cycles.md", "Reference Cycles Can Leak Memory", "ch15-06-reference-cycles.html", 15),
    # ch16
    ("ch16-00-concurrency.md", "Fearless Concurrency", "ch16-00-concurrency.html", 16),
    ("ch16-01-threads.md", "Using Threads to Run Code Simultaneously", "ch16-01-threads.html", 16),
    ("ch16-02-message-passing.md", "Transfer Data Between Threads with Message Passing", "ch16-02-message-passing.html", 16),
    ("ch16-03-shared-state.md", "Shared-State Concurrency", "ch16-03-shared-state.html", 16),
    ("ch16-04-extensible-concurrency-sync-and-send.md", "Extensible Concurrency with Send and Sync", "ch16-04-extensible-concurrency-sync-and-send.html", 16),
    # ch17
    ("ch17-00-async-await.md", "Fundamentals of Asynchronous Programming: Async, Await, Futures, and Streams", "ch17-00-async-await.html", 17),
    ("ch17-01-futures-and-syntax.md", "Futures and the Async Syntax", "ch17-01-futures-and-syntax.html", 17),
    ("ch17-02-concurrency-with-async.md", "Applying Concurrency with Async", "ch17-02-concurrency-with-async.html", 17),
    ("ch17-03-more-futures.md", "Working With Any Number of Futures", "ch17-03-more-futures.html", 17),
    ("ch17-04-streams.md", "Streams: Futures in Sequence", "ch17-04-streams.html", 17),
    ("ch17-05-traits-for-async.md", "A Closer Look at the Traits for Async", "ch17-05-traits-for-async.html", 17),
    ("ch17-06-futures-tasks-threads.md", "Futures, Tasks, and Threads", "ch17-06-futures-tasks-threads.html", 17),
    # ch18
    ("ch18-00-oop.md", "Object Oriented Programming Features", "ch18-00-oop.html", 18),
    ("ch18-01-what-is-oo.md", "Characteristics of Object-Oriented Languages", "ch18-01-what-is-oo.html", 18),
    ("ch18-02-trait-objects.md", "Using Trait Objects to Abstract over Shared Behavior", "ch18-02-trait-objects.html", 18),
    ("ch18-03-oo-design-patterns.md", "Implementing an Object-Oriented Design Pattern", "ch18-03-oo-design-patterns.html", 18),
    # ch19
    ("ch19-00-patterns.md", "Patterns and Matching", "ch19-00-patterns.html", 19),
    ("ch19-01-all-the-places-for-patterns.md", "All the Places Patterns Can Be Used", "ch19-01-all-the-places-for-patterns.html", 19),
    ("ch19-02-refutability.md", "Refutability: Whether a Pattern Might Fail to Match", "ch19-02-refutability.html", 19),
    ("ch19-03-pattern-syntax.md", "Pattern Syntax", "ch19-03-pattern-syntax.html", 19),
    # ch20
    ("ch20-00-advanced-features.md", "Advanced Features", "ch20-00-advanced-features.html", 20),
    ("ch20-01-unsafe-rust.md", "Unsafe Rust", "ch20-01-unsafe-rust.html", 20),
    ("ch20-02-advanced-traits.md", "Advanced Traits", "ch20-02-advanced-traits.html", 20),
    ("ch20-03-advanced-types.md", "Advanced Types", "ch20-03-advanced-types.html", 20),
    ("ch20-04-advanced-functions-and-closures.md", "Advanced Functions and Closures", "ch20-04-advanced-functions-and-closures.html", 20),
    ("ch20-05-macros.md", "Macros", "ch20-05-macros.html", 20),
    # ch21
    ("ch21-00-final-project-a-web-server.md", "Final Project: Building a Multithreaded Web Server", "ch21-00-final-project-a-web-server.html", 21),
    ("ch21-01-single-threaded.md", "Building a Single-Threaded Web Server", "ch21-01-single-threaded.html", 21),
    ("ch21-02-multithreaded.md", "From Single-Threaded to Multithreaded Server", "ch21-02-multithreaded.html", 21),
    ("ch21-03-graceful-shutdown-and-cleanup.md", "Graceful Shutdown and Cleanup", "ch21-03-graceful-shutdown-and-cleanup.html", 21),
    # appendix
    ("appendix-00.md", "Appendix", "appendix-00.html", None),
    ("appendix-01-keywords.md", "A - Keywords", "appendix-01-keywords.html", None),
    ("appendix-02-operators.md", "B - Operators and Symbols", "appendix-02-operators.html", None),
    ("appendix-03-derivable-traits.md", "C - Derivable Traits", "appendix-03-derivable-traits.html", None),
    ("appendix-04-useful-development-tools.md", "D - Useful Development Tools", "appendix-04-useful-development-tools.html", None),
    ("appendix-05-editions.md", "E - Editions", "appendix-05-editions.html", None),
    ("appendix-06-translation.md", "F - Translations of the Book", "appendix-06-translation.html", None),
    ("appendix-07-nightly-rust.md", "G - How Rust is Made and \"Nightly Rust\"", "appendix-07-nightly-rust.html", None),
]

TEMPLATE = """# {title}

> 📖 原文：<https://doc.rust-lang.org/book/{url_path}>
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

## 与其他章节的联系

<!-- 这一节用到了哪些前面学过的概念？它会被后面的哪些章节用到？ -->
"""

def main():
    SRC.mkdir(parents=True, exist_ok=True)
    for filename, title, url_path, _ in CHAPTERS:
        path = SRC / filename
        path.write_text(TEMPLATE.format(title=title, url_path=url_path), encoding="utf-8")
    print(f"Created {len(CHAPTERS)} chapter files in {SRC}")

if __name__ == "__main__":
    main()
