---
description: Initialize a new project with Antigravity Kit agent structure. Copies template agents, workflows, scripts, and rules into the current project.
---
// turbo-all

# /init-project — Khởi tạo Antigravity cho dự án mới

## Khi nào dùng
- Bắt đầu dự án mới cần agent framework
- Dự án chưa có thư mục `.agents/`
- User nói "init project", "khởi tạo project", hoặc `/init-project`

## Các bước (AGENT TỰ LÀM HẾT — USER KHÔNG CẦN LÀM GÌ)

### 1. Copy template vào dự án
```powershell
xcopy "%USERPROFILE%\.gemini\antigravity\templates\project-template\.agents" ".agents\" /E /I /Y
```

### 2. Tự động phát hiện thông tin dự án
Agent PHẢI tự phân tích dự án để lấy thông tin:

**Phát hiện Project Name:**
- Đọc `package.json` → field `name`
- Hoặc đọc `Cargo.toml`, `pyproject.toml`, `go.mod`
- Hoặc lấy tên thư mục gốc
- Viết hoa chữ cái đầu, format đẹp

**Phát hiện Tech Stack:**
- `package.json` → dependencies (React, Vue, Express, Next.js...)
- `requirements.txt` / `pyproject.toml` → Python, Django, FastAPI...
- `Cargo.toml` → Rust
- `go.mod` → Go
- Kiểm tra các file đặc trưng: `vite.config.*`, `next.config.*`, `tailwind.config.*`, `prisma/schema.prisma`, `Dockerfile`, `.github/workflows/`

**Phát hiện Project Description:**
- `package.json` → field `description`
- `README.md` → dòng đầu tiên sau heading
- Hoặc tóm tắt từ cấu trúc thư mục

**Phát hiện Key Modules:**
- Liệt kê các thư mục chính trong `src/`, `app/`, `lib/`, `server/`, `api/`
- Mô tả ngắn gọn chức năng từng module

### 3. Cập nhật AGENTS.md tự động
Dùng tool edit file để thay thế:
- `{{PROJECT_NAME}}` → tên dự án đã phát hiện
- `{{PROJECT_DESCRIPTION}}` → mô tả đã phát hiện  
- `{{TECH_STACK}}` → tech stack đã phát hiện
- `TODO: Fill in after project setup` → danh sách key modules thực tế

### 4. Cập nhật project-memory.json
Ghi thông tin đã phát hiện vào `.agents/state/project-memory.json`:
```json
{
  "project_name": "<detected>",
  "tech_stack": ["<detected>"],
  "architecture_decisions": [],
  "current_phase": "setup",
  "last_session": "<current ISO date>",
  "notes": ["Project initialized with Antigravity Kit"]
}
```

### 5. Cập nhật .gitignore
Thêm vào `.gitignore` nếu chưa có:
```
# Agent session state (volatile)
.agents/state/notepad.md
.agents/state/plans/
```

### 6. Xác nhận
```powershell
Write-Host "Agents:" ; (Get-ChildItem ".agents\agents\*.md").Count
Write-Host "Skills:" ; (Get-ChildItem "$env:USERPROFILE\.gemini\antigravity\skills" -Directory).Count  
Write-Host "Workflows:" ; (Get-ChildItem ".agents\workflows\*.md").Count
```

### 7. Lưu Neural Memory
```
nmem_remember: "Project <name> initialized with Antigravity Kit. Tech: <stack>. Modules: <modules>"
```

### 8. Báo cáo cho user
```
✅ Dự án <name> đã được khởi tạo với Antigravity Kit:
- 20 specialist agents
- 61+ global skills  
- 15 workflows
- 4 master scripts
- Đã tự động phát hiện: tech stack, modules, mô tả
- Sẵn sàng sử dụng!
```

## LƯU Ý QUAN TRỌNG
- **Agent tự làm 100%** — user KHÔNG cần chỉnh sửa gì
- Nếu không phát hiện được thông tin → hỏi user 1 câu duy nhất
- Nếu dự án trống (chưa có code) → hỏi user: "Dự án này sẽ làm gì và dùng tech gì?"
