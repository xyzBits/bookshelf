#!/usr/bin/env bash
# 用法：./scripts/new-book.sh <book-folder-name> "<书名>"
# 示例：./scripts/new-book.sh sicp "计算机程序的构造与解释"

set -e

if [ -z "$1" ] || [ -z "$2" ]; then
  echo "用法: $0 <book-folder-name> \"<书名>\""
  echo "示例: $0 sicp \"计算机程序的构造与解释\""
  exit 1
fi

BOOK_DIR="$1"
BOOK_TITLE="$2"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="$ROOT/books/$BOOK_DIR"
TEMPLATE="$ROOT/books/_template"

if [ -d "$TARGET" ]; then
  echo "❌ books/$BOOK_DIR 已经存在"
  exit 1
fi

cp -r "$TEMPLATE" "$TARGET"

# 替换 book.toml 里的标题
if [ "$(uname)" = "Darwin" ]; then
  # macOS sed
  sed -i '' "s/title = \"新书笔记\"/title = \"$BOOK_TITLE\"/" "$TARGET/book.toml"
else
  # GNU sed (Linux)
  sed -i "s/title = \"新书笔记\"/title = \"$BOOK_TITLE\"/" "$TARGET/book.toml"
fi

echo "✅ 已创建 books/$BOOK_DIR"
echo ""
echo "下一步："
echo "  1. 编辑 books/$BOOK_DIR/src/SUMMARY.md 列出章节"
echo "  2. 在 index.html 里加一张卡片指向 ./$BOOK_DIR/"
echo "  3. cd books/$BOOK_DIR && mdbook serve --open  # 本地预览"
