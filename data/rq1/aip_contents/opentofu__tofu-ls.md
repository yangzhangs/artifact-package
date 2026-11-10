### A note on copyright

We take copyright and intellectual property very seriously. A few quick rules should help you:

1. When you submit a PR, you are responsible for the code in that pull request. You signal your acceptance of the [DCO](https://developercertificate.org/) with your sign-off.
2. If you include code in your PR that you didn't write yourself, make sure you have permission from the author. If you have permission, always add the `Co-authored-by` sign-off to your commits to indicate the author of the code you are adding.
3. <mark>Be careful about AI coding assistants! Coding assistants based on large language models (LLMs), such as ChatGPT or GitHub Copilot, are awesome tools to help. However, in the specific case of OpenTofu the training data may include the BSL-licensed Terraform. Since the OpenTofu/Terraform codebase is very specific and LLMs don't have any other training sources, they may emit copyrighted code. Please avoid using LLM-based coding assistants.</mark>
4. When you copy/paste code from within the OpenTofu code, always make it explicit where you copied from. This helps us resolve issues later on.
5. Before you copy code from external sources, make sure that the license allows this. Also make sure that any licensing requirements, such as attribution, are met. When in doubt, ask first!
6. Specifically, do not copy from the Terraform repository, or any PRs others have filed against that repository. This code is licensed under the BSL, a license which is not compatible with OpenTofu. (You may submit the same PR to both Terraform and OpenTofu as long as you are the author of both.)

> [!WARNING]
> To protect the OpenTofu project from legal issues violating these rules will immediately disqualify your PR from being merged and you from working on that area of the OpenTofu code base in the future. Repeat violations may get you barred from contributing to OpenTofu.

---
