### Contributor responsibilities

<mark>You are responsible for validating the correctness of your code. Run relevant tests locally before opening a pull request. This applies to all contributions, including those assisted by AI.</mark>

- **SDK Core**: Strict requirement for End-to-End (E2E) test coverage for all new features and bug fixes.
- **Community Package**: Ideally, include unit and/or integration tests. We are more lenient with coverage here, but tests are strongly encouraged.
- **Playground Examples**:
    - `playground/`: Must have E2E tests.
    - `community/playground/`: E2E tests are encouraged but not mandatory for contributions.

In the pull request description, specify the commands you ran to verify your changes (for example: `pnpm test:e2e -- playground/hello-world/__tests__/e2e.test.mts`).
