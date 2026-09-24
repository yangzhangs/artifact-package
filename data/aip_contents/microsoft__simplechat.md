## Tests and Validation

Before opening a pull request, run the tests that match your change.

- Add or update functional tests for bug fixes and new features when appropriate.
- Run relevant tests from `functional_tests/` and `ui_tests/` when your change affects those areas.
- If you change Flask routes, keep the existing Swagger route decorator pattern intact.

Pull requests are reviewed by the SimpleChat team and go through repository validation. Depending on the files changed, that can include Python syntax checks, release-note validation, Swagger route validation, and additional maintainer review. Maintainers may also run additional security or AI-assisted review before merge.

---

## Security and Repo Conventions

- Never commit secrets, keys, or environment-specific credentials.
- Review [SECURITY.md](./SECURITY.md) before submitting security-sensitive changes.
- Follow the repository's existing structure and conventions instead of introducing broad cleanup changes.
- If you use AI-assisted tooling while contributing, also review [CLAUDE.md](./CLAUDE.md) and [.github/copilot-instructions.md](./.github/copilot-instructions.md) for repo-specific guidance.
