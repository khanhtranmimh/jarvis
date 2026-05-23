# Hướng Dẫn Đóng Góp / Contributing Guide

Cảm ơn bạn muốn đóng góp cho Jarvis! / Thanks for contributing to Jarvis!

## Cách đóng góp

### 1. Thêm prompt mới

Tạo file `.md` trong thư mục `prompts/<category>/`:

```markdown
# Tên Prompt

**Biến / Variables:** `{{VAR1}}`, `{{VAR2}}`

---

Nội dung prompt với {{VAR1}} và {{VAR2}}...
```

**Tiêu chí prompt tốt:**
- Có biến rõ ràng dùng `{{VARIABLE_NAME}}`
- Mô tả output mong muốn cụ thể
- Test trước khi submit

### 2. Thêm Python tool

Tạo file trong `tools/` với cấu trúc:
- Function rõ ràng, có type hints
- Docstring ngắn gọn
- Ví dụ trong `examples/`

### 3. Quy trình submit

```bash
# Fork repo, tạo branch
git checkout -b feature/ten-tinh-nang

# Thêm code / prompt
# ...

# Commit
git add <files>
git commit -m "feat: mô tả ngắn gọn"

# Push và tạo Pull Request
git push origin feature/ten-tinh-nang
```

### Commit message format

```
feat: thêm tính năng mới
fix: sửa lỗi
docs: cập nhật tài liệu
prompt: thêm/cải thiện prompt
```

## Code style

```bash
# Format code
uv run ruff format .

# Lint
uv run ruff check .

# Type check
uv run mypy tools/
```
