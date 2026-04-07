---
description: Comprehensive code review with structured feedback and approval gates
---

# Code Review Workflow

Pipeline: **Scope → Review → Report → Fix → Re-review**

## Steps

1. **Define Scope** — What files/changes to review
   - Get list of changed files (git diff, or user specifies)
   - Understand the intent of the changes

2. **Style Review** — Code quality and conventions
   - Naming consistency
   - Code formatting
   - Comment quality
   - Import organization
   - Dead code

3. **Logic Review** — Correctness and robustness
   - Edge case handling
   - Error handling (try/catch, null checks)
   - State management correctness
   - Race conditions
   - Off-by-one errors

4. **Security Review** — Safety checks
   - Hardcoded secrets or tokens
   - SQL/XSS injection risks
   - Input validation
   - Authentication/authorization gaps
   - Sensitive data exposure

5. **Performance Review** — Efficiency
   - Unnecessary re-renders (React)
   - N+1 queries or excessive API calls
   - Memory leaks
   - Bundle size impact

6. **Generate Report** — Structured feedback

   ```markdown
   ## Code Review Report

   **Scope:** [files reviewed]
   **Reviewer:** AI Agent
   **Date:** [date]

   ### 🔴 Critical (must fix)
   - [ ] [file:line] — [issue description]

   ### 🟡 Important (should fix)
   - [ ] [file:line] — [issue description]

   ### 🟢 Suggestions (nice to have)
   - [ ] [file:line] — [suggestion]

   ### ✅ Strengths
   - [what was done well]

   **Verdict:** APPROVE / REQUEST_CHANGES / NEEDS_DISCUSSION
   ```

7. **Fix Cycle** (if REQUEST_CHANGES)
   - Author fixes critical and important issues
   - Re-review only changed portions
   - Max 2 review rounds

8. **Final Approval**
   - All critical issues resolved
   - Important issues resolved or tracked
   - `smart-commit` the fixes
