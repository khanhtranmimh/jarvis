# Bắt đầu với Jarvis / Getting Started

## 1. Cài đặt môi trường

### Cài uv (Python package manager)

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Clone và cài dependencies

```bash
git clone https://github.com/khanhhust200897/jarvis.git
cd jarvis
uv sync
```

Để cài thêm optional dependencies:
```bash
uv sync --extra automation   # Playwright cho web automation
uv sync --extra data         # Pandas cho xử lý dữ liệu
uv sync --extra dev          # Tools phát triển (pytest, ruff)
```

## 2. Cấu hình API Keys

```bash
cp .env.example .env
```

Mở `.env` và điền API keys:
- **Anthropic (Claude):** https://console.anthropic.com/
- **OpenAI (ChatGPT):** https://platform.openai.com/api-keys
- **Google (Gemini):** https://aistudio.google.com/app/apikey

> **Quan trọng:** `.env` đã được thêm vào `.gitignore` — không bao giờ commit file này lên GitHub.

## 3. Chạy thử

```bash
uv run python examples/hello_jarvis.py
```

## 4. Khám phá thêm

| Bạn muốn... | Xem ở... |
|-------------|----------|
| Dùng prompt có sẵn | `prompts/` |
| Gọi Claude API | `tools/llm/claude_client.py` |
| Gọi OpenAI API | `tools/llm/openai_client.py` |
| Ví dụ code | `examples/` |
| Hướng dẫn chi tiết | `docs/guides/` |
