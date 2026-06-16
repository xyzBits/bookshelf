# 用法: .\scripts\new-book.ps1 <book-folder-name> "<书名>"
# 示例: .\scripts\new-book.ps1 sicp "计算机程序的构造与解释"

param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$BookDir,

    [Parameter(Mandatory=$true, Position=1)]
    [string]$BookTitle
)

$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Target = Join-Path $Root "books\$BookDir"
$Template = Join-Path $Root "books\_template"

if (Test-Path $Target) {
    Write-Host "X books/$BookDir 已经存在" -ForegroundColor Red
    exit 1
}

# 复制模板
Copy-Item -Path $Template -Destination $Target -Recurse

# 替换 book.toml 里的标题（用 UTF-8 写回避免中文乱码）
$tomlPath = Join-Path $Target "book.toml"
$content = Get-Content $tomlPath -Raw -Encoding UTF8
$content = $content -replace 'title = "新书笔记"', "title = `"$BookTitle`""
[System.IO.File]::WriteAllText($tomlPath, $content, [System.Text.UTF8Encoding]::new($false))

Write-Host "OK 已创建 books/$BookDir" -ForegroundColor Green
Write-Host ""
Write-Host "下一步："
Write-Host "  1. 编辑 books\$BookDir\src\SUMMARY.md 列出章节"
Write-Host "  2. 在 index.html 里加一张卡片指向 ./$BookDir/"
Write-Host "  3. cd books\$BookDir; mdbook serve --open"
