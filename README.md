# 📚 我的读书笔记 (mdBook 多本书)

用 [mdBook](https://rust-lang.github.io/mdBook/) 维护多本书的读书笔记，自动部署到 GitHub Pages。

## 目录结构

```
.
├── books/
│   ├── rust-book/           # 《The Rust Programming Language》笔记
│   │   ├── book.toml
│   │   └── src/
│   │       ├── SUMMARY.md   # 完整复刻 Rust Book 的目录
│   │       ├── ch01-*.md    # 每章一个 md 文件，预填了"读后总结"模板
│   │       └── ...
│   └── _template/           # 新书的空模板（不会被构建）
├── index.html               # 落地页（列出所有书）
├── scripts/
│   ├── new-book.sh          # 一键创建新书
│   └── generate_rust_book_chapters.py
└── .github/workflows/deploy.yml  # 自动构建 + 发布
```

## 本地预览

```bash
# 安装 mdBook（任选一种）
brew install mdbook              # macOS
cargo install mdbook             # 任何系统（需要 Rust）

# Windows 还可以：
# - winget install rust-lang.mdBook
# - scoop install mdbook
# - 或从 https://github.com/rust-lang/mdBook/releases 下载 .zip，解压后把 mdbook.exe 放进 PATH

# 预览 Rust Book 笔记
cd books/rust-book
mdbook serve --open
# 浏览器会自动打开 http://localhost:3000
# 编辑 md 文件会自动热重载
```

## 部署到 GitHub Pages

### 一次性配置

1. **推到 GitHub**：把整个文件夹推到一个新仓库（比如叫 `notes`）。
2. **打开 Pages**：仓库 → Settings → Pages → Source 选 **GitHub Actions**。
3. **改 book.toml 里的链接**：把 `books/rust-book/book.toml` 里的 `your-username` 和 `your-notes-repo` 改成你自己的。

### 之后

每次 `git push` 到 `main` 分支，Workflow 会：
1. 自动遍历 `books/` 下的所有文件夹（跳过 `_` 开头的）
2. 用 mdBook 把每本书构建到 `<book>/`
3. 把 `index.html` 放到根目录作为入口
4. 发布到 GitHub Pages

最终结构：

```
https://<你的用户名>.github.io/<仓库名>/             ← 落地页（列出所有书）
https://<你的用户名>.github.io/<仓库名>/rust-book/   ← Rust 书笔记
https://<你的用户名>.github.io/<仓库名>/sicp/        ← 之后加的其他书
```

## 怎么加一本新书

### 用脚本（推荐）

**macOS / Linux / Git Bash / WSL:**

```bash
./scripts/new-book.sh sicp "计算机程序的构造与解释"
```

**Windows PowerShell:**

```powershell
.\scripts\new-book.ps1 sicp "计算机程序的构造与解释"
```

> 如果 PowerShell 报"无法加载脚本，因为在此系统上禁止运行脚本"，先在 PowerShell 里跑一次：
> `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

这会从 `books/_template/` 复制一份到 `books/sicp/`，并把书名填好。

然后：
1. 编辑 `books/sicp/src/SUMMARY.md` 列出章节
2. 在 `index.html` 里加一张卡片指向 `./sicp/`
3. 提交、推送，等 Action 跑完就上线了

### 手动

复制 `books/_template/` → `books/<新书名>/`，改 `book.toml`，写 `SUMMARY.md`，同样在 `index.html` 加卡片。

## Rust Book 笔记的用法

`books/rust-book/src/` 里已经有 111 个 markdown 文件（完整复刻官方的 21 章 + 附录目录）。

每个文件长这样：

```markdown
# What is Ownership?

> 📖 原文：<https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html>
> 📅 读完时间：_____
> 状态：⬜ 未读 / 🟡 在读 / ✅ 已读

## 一句话总结
## 核心要点
## 关键概念
## 代码示例
## 我的疑问与思考
## 与其他章节的联系
```

每读完一节就填一下对应的文件 → `git push` → 网站自动更新。

## SUMMARY.md 速查

mdBook 的目录是手写的，格式很严格：

- `[文字](file.md)` 不带前导 `-` → **不编号**的章节（前言、附录）
- `- [文字](file.md)` 带前导 `-` → **编号**的章节
- 缩进 4 空格 → 子章节

```markdown
# Summary

[前言](preface.md)                    ← 不编号

- [第一章](ch01.md)                    ← 编号 1
    - [小节 1.1](ch01-01.md)           ← 编号 1.1

- [第二章](ch02.md)                    ← 编号 2

[附录](appendix.md)                   ← 不编号
```

详见 <https://rust-lang.github.io/mdBook/format/summary.html>。
