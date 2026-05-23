# Hướng Dẫn Viết Prompt Hiệu Quả

## Nguyên tắc cơ bản

### 1. Đặt vai trò rõ ràng
Thay vì: *"Giúp tôi review code"*  
Dùng: *"Bạn là senior Python engineer với 10 năm kinh nghiệm. Review đoạn code sau..."*

### 2. Cung cấp context đầy đủ
Thay vì: *"Viết email cho khách hàng"*  
Dùng: *"Viết email cho khách hàng doanh nghiệp (B2B, formal tone) thông báo delay 1 tuần do lý do kỹ thuật..."*

### 3. Chỉ định format output
```
Trả lời theo format:
1. Tóm tắt (1-2 câu)
2. Chi tiết (bullet points)
3. Action items
```

### 4. Dùng ví dụ (few-shot prompting)
```
Ví dụ input: "Tôi mệt"
Ví dụ output: "Bạn đang cảm thấy kiệt sức về thể chất hay tinh thần?"

Bây giờ hãy phân tích: "{{USER_INPUT}}"
```

### 5. Giới hạn độ dài output
```
Trả lời trong 3 câu. / Không quá 200 từ. / Tóm tắt trong 5 bullet points.
```

## Prompt Chaining

Chia task phức tạp thành nhiều bước:

```python
# Bước 1: Phân tích
analysis = ask("Phân tích vấn đề này: ...")

# Bước 2: Lấy kết quả bước 1 làm input
solution = ask(f"Dựa trên phân tích sau, đề xuất giải pháp:\n{analysis}")
```

## Khi nào dùng model nào?

| Task | Model đề xuất |
|------|--------------|
| Phân tích phức tạp, sáng tác | Claude Opus |
| Task hàng ngày, code | Claude Sonnet |
| Task đơn giản, nhanh | Claude Haiku |
| Code generation | GPT-4o |
| Image understanding | GPT-4o / Claude Sonnet |
