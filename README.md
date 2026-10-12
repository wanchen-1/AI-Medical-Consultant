# AI Medical Consultant

基于 LangChain + RAG + Agent 的智能医疗问诊系统示例。

> 仅用于技术演示和健康信息辅助，不构成诊断、处方或医疗建议。出现胸痛、呼吸困难、大出血、意识异常等情况请立即联系急救服务。

## 技术栈

- Vue 3 + Vite + Pinia
- FastAPI + LangChain
- FAISS（可替换为 PostgreSQL pgvector）
- PostgreSQL + Redis
- Docker Compose

## 快速开始

```bash
cp .env.example .env
docker compose up --build
```

API: `http://localhost:8000/docs`  前端: `http://localhost:5173`

## 目录

`backend/` 提供异步问诊 API、急症识别和 RAG 检索接口；`frontend/` 提供多轮问诊界面；`knowledge/` 放置经过审核的医学资料。

## License

MIT
