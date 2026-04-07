# Bản đồ Đông Á Chí Chính (1351) — AI Agent Instructions

> Powered by Antigravity Kit + OMC patterns.
> This file provides project-level context, specialist agent routing, and operating principles for AI agents.

<specialist_agents>
## 🤖 Specialist Agents (20)
Agent definitions are in `.agents/agents/*.md`. See `ARCHITECTURE.md` for full skill mappings.

| Agent | Domain | Use When |
|-------|--------|----------|
| `orchestrator` | Coordination | Multi-agent tasks |
| `project-planner` | Planning | Discovery, task breakdown |
| `frontend-specialist` | Web UI/UX | React, Next.js, Tailwind |
| `backend-specialist` | Backend/API | Node.js, Express, FastAPI |
| `database-architect` | Database | Schema, Prisma, SQL |
| `mobile-developer` | Mobile | React Native, Flutter |
| `game-developer` | Games | Game logic, mechanics |
| `devops-engineer` | DevOps | CI/CD, Docker |
| `security-auditor` | Security | Auth, OWASP vuln scan |
| `penetration-tester` | Red Team | Offensive security |
| `test-engineer` | Testing | Unit, E2E, coverage |
| `debugger` | Debugging | Root cause analysis |
| `performance-optimizer` | Performance | Web Vitals, profiling |
| `seo-specialist` | SEO | Ranking, visibility |
| `documentation-writer` | Docs | Only when explicitly requested |
| `product-manager` | PM | Requirements, user stories |
| `product-owner` | PO | Strategy, backlog, MVP |
| `qa-automation-engineer` | QA | E2E pipelines |
| `code-archaeologist` | Legacy | Refactoring old code |
| `explorer-agent` | Discovery | Read-only codebase analysis |

**Routing:** See `GEMINI.md` rules → Intelligent Routing → Auto-select agent by domain.
</specialist_agents>

<operating_principles>
- Prefer evidence over assumptions: verify outcomes before final claims.
- Choose the lightest-weight path that preserves quality (direct action vs subagent).
- Consult `.agents/state/project-memory.json` at session start for project context.
- Write critical discoveries to `.agents/state/notepad.md` before ending a session.
- Keep diffs small, reversible, and easy to review.
- Reuse existing utilities and patterns before introducing new ones.
- Do not add new dependencies without explicit user approval.
</operating_principles>

<project_context>
**Project:** Bản đồ Đông Á Chí Chính (1351) — Bản đồ lịch sử tương tác thời mạt Nguyên
**Tech Stack:** HTML5, CSS3, Vanilla JS, ECharts
**Key Modules:**
- `china_1351.js` / `china_1351_full.js`: Dữ liệu bản đồ GeoJSON
- `lore_1351.js`: Dữ liệu bối cảnh lịch sử và thông tin phe phái
- `test.html` / `final_test.html`: Giao diện web hiển thị bản đồ với ECharts
</project_context>

<delegation_rules>
**Delegate to subagents when:**
- Multi-file changes spanning 3+ files
- Debugging requires codebase-wide investigation
- Refactoring with test verification needed
- Independent tasks that can run in parallel

**Work directly when:**
- Single file edits < 50 lines
- Quick lookups, explanations, config changes
- Running commands, checking status
</delegation_rules>

<verification_protocol>
Before claiming any work is complete:
1. **BUILD** — Build passes without errors
2. **LINT** — No console errors or warnings in relevant files
3. **FUNCTIONALITY** — Feature works as described
4. **REGRESSION** — Existing features still work
5. **EVIDENCE** — Include actual command output, not assumptions

Evidence must be fresh (run in current session). Never say "should work" — run it and prove it.
</verification_protocol>

<commit_protocol>
Use conventional commits with structured trailers:

```
<type>(<scope>): <description>

[Optional body explaining WHY, not WHAT]

Constraint: <active constraint that shaped this decision>
Rejected: <alternative considered> | <reason for rejection>
Confidence: high | medium | low
Scope-risk: narrow | moderate | broad
```

Types: feat, fix, refactor, docs, style, test, chore, perf
</commit_protocol>

<keyword_triggers>
When user message contains these keywords, activate the corresponding skill:

| Keyword (EN) | Keyword (VN) | Skill |
|-------------|-------------|-------|
| "autopilot", "build me" | "tự động", "tự làm" | autopilot-mode |
| "ralph", "don't stop" | "đừng dừng", "làm cho xong" | ralph-mode |
| "deep interview" | "phỏng vấn", "hỏi kỹ" | deep-interview |
| "verify", "check it" | "kiểm tra", "xác minh" | omc-verify |
| "smart commit" | "commit chuẩn" | smart-commit |
</keyword_triggers>

<session_lifecycle>
**Session Start:**
1. Check `.agents/state/project-memory.json` for project context
2. Check `.agents/state/notepad.md` for pending notes from previous sessions
3. Use `nmem_recall("<project> current context")` if Neural Memory available

**Session End:**
1. Save critical findings to `.agents/state/notepad.md`
2. Update `.agents/state/project-memory.json` if decisions were made
3. Use `nmem_remember` to persist important learnings to Neural Memory
</session_lifecycle>
