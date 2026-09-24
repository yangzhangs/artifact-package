## Submitting Pull Requests


1.  **Fork the repository** and create a new branch for your feature or bug fix.
2.  **Keep it Focused:**
    *   Do not include unrelated refactoring, whitespace changes, or formatting fixes in the same PR as a bug fix or feature.
    *   PRs with excessive "noise" or unrelated changes will be closed.
3.  **Write Tests:**
    *   For bug fixes, you **MUST** include a test case that reproduces the issue on the `main` branch (fails before your fix) and passes with your fix.
    *   For new features, add tests that cover the new functionality.
    *   Add your new test C file to `tests/` and register it in `tests/meson.build`.
4.  **Run Tests:** Ensure all tests pass before submitting.
    ```bash
    meson setup build/
    meson test -C build/
    ```
5.  **AI Tooling Attribution:** If you used any AI models or tooling (e.g., ChatGPT, Claude Code, GitHub Copilot, Gemini, etc.) to create your PR, please specify:
    *   The model used (e.g., "Claude Sonnet 4.6", "Gemini 3 Pro", "GPT-5.2").
    *   A brief description of how it was used (e.g., "Used to generate the initial implementation of function X", "Used to write test cases").
    *   This helps us understand the provenance of the code.

Pull requests that do not meet these requirements (including failing tests or missing reproduction cases) will be closed.
