## Testing

Run tests before submitting PRs:

```bash
npm run test        # Unit tests (Vitest)
npm run test:e2e    # E2E tests (Playwright)
```

E2E tests use mocked API responses - no AI provider needed. Tests are in `tests/e2e/`.

To run a specific test file:
```bash
npx playwright test tests/e2e/diagram-generation.spec.ts
```

To run tests with UI mode:
```bash
npx playwright test --ui
```

---

## Using AI Tools

AI-assisted contributions are welcome. But please **review the output before opening a PR**:

1. **Review the code** — understand what was generated, don't just commit blindly
2. **Write a PR description** — explain what changed and why
3. **Rebase on latest `main`** — AI tools often work on stale branches, run `git rebase origin/main` before pushing
4. **Clean up artifacts** — remove IDE configs (`.idea/`, `.kiro/`), env files, scratch notes, and throwaway test scripts that AI tools leave behind

---

## Code Review

This project uses GitHub Copilot for automated code review. If you receive review comments from Copilot on your PR:
- **Valid suggestions**: Please address them in your code.
- **Invalid or irrelevant suggestions**: Feel free to click "Resolve" to dismiss them.
