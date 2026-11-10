## Pull Requests

> [!Warning]
> <mark>**About AI Assistance**:\</mark>
> Pull Requests failing to meet the following requirements will be **closed immediately**:
> - Manually review and test all code to prevent hallucinated logic or syntax
> - Ensure PR descriptions provide clear, meaningful value to the review process
> - Maintain strict adherence to the established workflow and commit specifications
> <mark>- Disclose any use of AI tools for code or documentation generation within the PR description</mark>

- An Issue describing the problem or feature is **required** before submitting a Pull Request.
- A **single problem** or a **single feature** per Pull Request to avoid bundling unrelated changes.
- Updated documentation for any new **user-facing features** or **configuration options**.
- Separate Pull Requests for **code refactoring** before submitting a new feature.
- Compliance with **basic tests** and the project's existing **code style**.

> [!Note]
> This project uses [Biome](https://biomejs.dev/) as the primary formatter and linter.\
> Due to current limitations in Biome's formatting for **Astro** and **Svelte** files, Prettier is used as a fallback for those specific file types.\
> Please format with Prettier first, then run Biome.

---

### Development Workflow

1. [Fork](https://github.com/tuyuritio/astro-theme-thought-lite/fork) this repository to your own GitHub account.
2. Create a new branch for your changes: `git checkout -b feat/your-feature`
3. Make your changes and [commit](#commit-convention) them: `git commit -m "feat: add new feature"`.
4. Pull the latest changes from the base repository to avoid conflicts: `git pull origin main`
5. Push your branch to your fork: `git push origin feat/your-feature`
6. Open a Pull Request from your branch to the appropriate base branch in this repository.

---

### Commit Convention

Using [Conventional Commits](https://www.conventionalcommits.org/). The commit message format is:

```
<type>[(<scope>)]: <description>
```

**Common Types**:

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring

---

Thank you for your contribution ❤️
