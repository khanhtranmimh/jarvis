# ⚙️ Workflows

Các kịch bản end-to-end kết hợp nhiều tools và prompts để tự động hóa tác vụ phức tạp.

## Khái niệm

Một **workflow** là chuỗi các bước tự động:
1. Input → xử lý → output
2. Có thể kết hợp nhiều LLM calls
3. Có thể đọc/ghi file, gọi API ngoài

## Roadmap

- [ ] `weekly_report.py` — Tổng hợp báo cáo tuần từ ghi chú
- [ ] `content_pipeline.py` — Input ý tưởng → outline → bài viết hoàn chỉnh
- [ ] `code_review_bot.py` — Review toàn bộ PR tự động
- [ ] `learning_tracker.py` — Theo dõi tiến độ học và tạo quiz

## Ví dụ (sắp có)

```python
from workflows.content_pipeline import ContentPipeline

pipeline = ContentPipeline()
article = pipeline.run(
    topic="Cách dùng AI để tăng năng suất làm việc",
    target_length=800,
    style="blog post thân thiện"
)
```
