---
description: Full feature development pipeline from idea to verified, committed code
---

# Feature Development Workflow

Pipeline: **Explore → Plan → Execute → Verify → Commit**

## Steps

// turbo-all

1. **Load Context** — Read `.agents/state/project-memory.json` and `.agents/state/notepad.md`

2. **Explore** — Investigate the codebase area where the feature will live
   - Identify existing patterns, related files, and conventions
   - Note dependencies and potential impact areas

3. **Plan** — Create implementation plan
   - Break into ordered tasks with file paths
   - If scope is large: use `brainstorming` skill first
   - If requirements are vague: use `deep-interview` skill first
   - Write plan to `.agents/state/plans/feature-<name>.md`

4. **Execute** — Implement each task in order
   - Follow existing code patterns
   - For independent tasks: consider `dispatching-parallel-agents`
   - For multi-file tasks: consider `subagent-driven-development`

5. **Verify** — Run `omc-verify` skill (Level 2: Standard)
   - BUILD: `npm run build`
   - LINT: Check modified files
   - FUNCTION: Test the feature manually
   - REGRESSION: Verify existing features still work

6. **Fix Loop** (if verify fails, max 3 iterations)
   - Fix specific failures
   - Re-run verification
   - Use `ralph-mode` if multiple things need fixing

7. **Commit** — Use `smart-commit` skill
   - Conventional commit + trailers
   - Update project-memory.json with decisions

8. **Persist** — Use `context-guard` skill
   - Save session notes to notepad.md
   - Record learnings in Neural Memory
