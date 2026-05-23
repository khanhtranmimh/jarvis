# ⚡ JARVIS — Bộ Công Cụ AI Cá Nhân

> *"Just A Rather Very Intelligent System"* — lấy cảm hứng từ trợ lý AI của Iron Man

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![uv](https://img.shields.io/badge/managed%20by-uv-purple)](https://github.com/astral-sh/uv)

---

## 🇻🇳 Tiếng Việt

**Jarvis** là bộ công cụ AI cá nhân — tập hợp prompt, Python tools, và AI agents giúp tự động hóa và nâng cao hiệu quả công việc hàng ngày.

### Tính năng

- **📝 Prompt Library** — Thư viện prompt tái sử dụng cho Claude, ChatGPT, Gemini
- **🔧 Python Tools** — Scripts tích hợp LLM API, tự động hóa tác vụ
- **🤖 AI Agents** — Agents phức tạp hơn với tool use và memory
- **⚙️ Workflows** — Kịch bản end-to-end kết hợp nhiều công cụ
- **📚 Docs & Guides** — Hướng dẫn sử dụng AI hiệu quả

### Cấu trúc

```
jarvis/
├── prompts/          # Thư viện prompt (Markdown)
│   ├── coding/       # Lập trình
│   ├── writing/      # Viết lách
│   ├── analysis/     # Phân tích dữ liệu
│   ├── work/         # Công việc
│   └── life/         # Cuộc sống cá nhân
├── tools/            # Python tools
│   ├── llm/          # Tích hợp Claude/OpenAI/Gemini
│   ├── automation/   # Tự động hóa
│   └── utils/        # Tiện ích chung
├── agents/           # AI agents
├── workflows/        # Kịch bản kết hợp
├── docs/             # Tài liệu
└── examples/         # Code mẫu chạy được
```

### Bắt đầu nhanh

```bash
# 1. Clone repo
git clone https://github.com/khanhhust200897/jarvis.git
cd jarvis

# 2. Cài uv (nếu chưa có)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Tạo môi trường ảo và cài dependencies
uv sync

# 4. Cấu hình API keys
cp .env.example .env
# Mở .env và điền API key của bạn

# 5. Chạy thử
uv run python examples/hello_jarvis.py
```

---

## 🇬🇧 English

**Jarvis** is a personal AI toolkit — a collection of prompts, Python tools, and AI agents to automate and enhance daily work and life.

### Features

- **📝 Prompt Library** — Reusable prompts for Claude, ChatGPT, Gemini
- **🔧 Python Tools** — LLM API integrations and automation scripts
- **🤖 AI Agents** — Complex agents with tool use and memory
- **⚙️ Workflows** — End-to-end pipelines combining multiple tools
- **📚 Docs & Guides** — Guides for using AI effectively

### Quick Start

```bash
git clone https://github.com/khanhhust200897/jarvis.git
cd jarvis
uv sync
cp .env.example .env   # fill in your API keys
uv run python examples/hello_jarvis.py
```

---

## 🤝 Đóng góp / Contributing

Mọi đóng góp đều được chào đón! Xem [docs/guides/contributing.md](docs/guides/contributing.md).

All contributions are welcome! See [docs/guides/contributing.md](docs/guides/contributing.md).

---

*Built with ❤️ and AI — Powered by Claude, OpenAI, and the open-source community*
