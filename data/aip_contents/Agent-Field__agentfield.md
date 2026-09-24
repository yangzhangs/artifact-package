## <mark>AI-Assisted Contributions</mark>

<mark>We welcome contributions made with AI assistance (Claude, GitHub Copilot, Cursor, etc.).</mark>

---

### Guidelines

1. **Quality matters, not method** - We evaluate PRs on code quality, test coverage, and adherence to standards. How you wrote the code doesn't affect acceptance.

2. <mark>**Commit attribution** - If using an AI assistant, you may include it as a co-author:</mark>
   ```
   Co-Authored-By: Claude <noreply@anthropic.com>
   ```
   This is optional but helps with transparency.

3. <mark>**You own the submission** - You're responsible for reviewing AI-generated code before submitting. Ensure it:</mark>
   - Follows project conventions
   - Includes appropriate tests
   - Doesn't introduce security issues
   - Makes sense in context

---

### <mark>Testing Requirements for AI-Assisted Code</mark>

<mark>AI-generated code requires the same test coverage as human-written code. When using AI:</mark>

**Before Submitting:**
1. Run `./scripts/test-all.sh` and verify all tests pass
2. For Go code: `go test ./...` in the relevant package
3. For Python code: `pytest` with coverage
4. For Web UI: `npm test` (once vitest is set up)

**Writing Tests with AI - Prompt Strategies:**

When asking AI to write tests, be explicit about what to test:

```
Write unit tests for [function/component] that cover:
1. Happy path - normal expected inputs
2. Edge cases - empty inputs, null values, boundary conditions
3. Error cases - invalid inputs, network failures, timeouts
4. Integration points - verify mocks are called correctly
```

Example prompt for better test coverage:
```
Add tests for the retry handler. Include:
- Test successful retry on transient error
- Test max retries exceeded
- Test context cancellation during retry
- Test exponential backoff timing
- Mock the underlying service to control failures
```

**Common AI Testing Pitfalls to Avoid:**
- Tests that only check "no error" without verifying behavior
- Missing edge case coverage (empty arrays, null, negative numbers)
- Mocking everything instead of testing integration
- Tests that pass but don't actually assert anything meaningful
- Copy-paste tests that don't adapt to specific scenarios

**Test Quality Checklist:**
- [ ] Tests actually fail when the code is broken
- [ ] Each test has clear assertions, not just "runs without error"
- [ ] Edge cases are covered (null, empty, boundary values)
- [ ] Error paths are tested, not just happy paths
- [ ] Tests are independent and can run in any order
- [ ] Test names clearly describe what is being tested

---

### <mark>Tips for Using AI with AgentField</mark>

- <mark>Point your AI to `CLAUDE.md` for project context</mark>
- Share relevant file paths from the issue description
- Ask the AI to run tests before considering the task complete
- Review diffs carefully - AI sometimes over-engineers or misses edge cases
- If the issue has a "Files" section, give those paths to your AI
- Ask AI to explain its test strategy before writing tests
