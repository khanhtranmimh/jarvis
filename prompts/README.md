# 📝 Thư Viện Prompt / Prompt Library

Mỗi file `.md` là một prompt template có thể tái sử dụng.
Dùng `{{VARIABLE}}` để đánh dấu chỗ cần điền.

Each `.md` file is a reusable prompt template.
Use `{{VARIABLE}}` to mark placeholders.

## Cách dùng / Usage

```python
from tools.utils.file_utils import read_prompt

prompt = read_prompt("code_review", category="coding")
# Thay thế biến / Replace variables
prompt = prompt.replace("{{LANGUAGE}}", "Python")
```

## Danh mục / Categories

| Thư mục | Mô tả |
|---------|-------|
| `coding/` | Lập trình, code review, debug |
| `writing/` | Viết lách, email, báo cáo |
| `analysis/` | Phân tích dữ liệu, nghiên cứu |
| `work/` | Công việc, họp, kế hoạch |
| `life/` | Cuộc sống, học tập, sức khỏe |
