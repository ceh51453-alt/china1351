---
description: Systematic bug investigation and fix pipeline with evidence-based verification
---

# Bug Investigation Workflow

Pipeline: **Reproduce → Investigate → Fix → Verify → Commit**

## Steps

// turbo-all

1. **Load Context** — Read `.agents/state/project-memory.json` for relevant project info

2. **Reproduce** — Confirm the bug exists
   - Get exact steps to reproduce
   - Note actual vs expected behavior
   - Capture error messages

3. **Investigate** — Use `systematic-debugging` skill
   - Form hypotheses about root cause
   - Search codebase for related code (`grep_search`)
   - Trace the execution flow
   - Identify the specific file(s) and line(s)

4. **Plan Fix** — Before touching code
   - Describe the root cause
   - Propose a minimal fix
   - Identify regression risks

5. **Implement Fix** — Make the smallest change that fixes the bug
   - Follow existing patterns
   - Don't refactor unrelated code

6. **Verify** — Run `omc-verify` skill (Level 2: Standard)
   - Original bug is fixed
   - No new errors introduced
   - Build still passes

7. **Fix Loop** (if verify fails, max 3 iterations using `ralph-mode`)
   - Fix specific failures
   - Re-verify

8. **Commit** — Use `smart-commit` skill
   ```
   fix(<scope>): <what was fixed>

   Root cause: <explanation>
   Constraint: <why this approach>
   Confidence: high | medium | low
   Scope-risk: narrow | moderate
   ```

9. **Persist** — Update notepad.md with bug findings
