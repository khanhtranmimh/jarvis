# 🤖 Agents

Module này chứa các AI agent phức tạp hơn — kết hợp tool use, memory, và multi-step reasoning.

## Khái niệm

Một **agent** khác với một **prompt** ở chỗ:
- Agent có thể gọi nhiều công cụ (tools)
- Agent lặp lại nhiều bước cho đến khi hoàn thành task
- Agent có thể có memory ngắn hạn hoặc dài hạn

## Roadmap

- [ ] `research_agent.py` — Tự động research một chủ đề và tổng hợp báo cáo
- [ ] `coding_agent.py` — Viết, test, và sửa code tự động
- [ ] `email_agent.py` — Đọc, phân loại và soạn thảo email
- [ ] `daily_planner.py` — Lên kế hoạch ngày dựa trên task list

## Ví dụ cơ bản (sắp có)

```python
from agents.research_agent import ResearchAgent

agent = ResearchAgent()
report = agent.run("Xu hướng AI trong năm 2026")
print(report)
```
