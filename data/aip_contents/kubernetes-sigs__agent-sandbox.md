## Pull Request and Code Review Policy

To maintain high velocity and prevent our review queue from stagnating, this project enforces the following guidelines for all Pull Requests:

- **CLA Requirement:** All contributors must sign the [Contributor License Agreement](https://git.k8s.io/community/CLA.md). PRs without a signed CLA will not be reviewed.
- **AI-Assisted Code Reviews:** We use GitHub Copilot to provide automated, first-pass code reviews to help identify low-hanging fruit and improve review velocity.
  - If Copilot provides a code suggestion in your PR, **do not click the "Commit suggestion" button** in the GitHub UI. Doing so adds Copilot as a co-author to the commit. Since Copilot cannot sign the Kubernetes CLA, this will cause the CLA check to fail and block your PR. Instead, please manually apply the suggested changes in your local environment and push the commit yourself.
- **Fast-Track Delivery (PR Takeovers):** To focus on delivering features faster, maintainers may take over community PRs that are approved or highly important. If a PR is close to completion, a maintainer might push the final changes and merge it directly.
- **Stale Management:** We have shifted to a more aggressive rule for inactive PRs to reduce queue clutter. Any PR that is inactive for 30 days will be automatically marked stale (`lifecycle/stale` label) and closed after 15 more days of inactivity. Closed PRs can always be reopened if the author returns to continue the work.
