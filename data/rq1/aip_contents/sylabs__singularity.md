## AI Authored / Assisted Contributions

<mark>If you use AI/LLM tools (e.g. Copilot, Claude) when contributing to</mark>
SingularityCE please ensure that:

- Commit messages and PR descriptions clearly indicate which tool(s) were used.
- You make use of settings that block or identify generated code that matches
  public code, to ensure that any public code is incorporated according to the
  license terms of the relevant project.
- You have reviewed all generated code, with reference to this guide, prior to
  requesting a review from the SingularityCE maintainers.

**Important**: Due to the nature of this project, many tests must be run with
privilege. The integration and end-to-end tests perform many actions that have
security & resource consumption implications, including but not limited to:

- Creating & destroying virtual network interfaces using CNI plugins.
- Manipulating cgroups.
- Retrieving containers from public registries including Docker Hub.
- Creating and manipulating root-owned test files.
- Running containers as the root user.

Our [AGENTS.md](AGENTS.md) describes to agents how to run tests using the
wrapper scripts `-sudo` flags or other means that provide privilege. You
should consider the security implications before allowing an agent to execute
tests. Working in an isolated VM / container based development environment is
recommended.
