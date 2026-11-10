### Option 2: Developing Inside a Devcontainer

<mark>[Devcontainers](https://code.visualstudio.com/docs/devcontainers/containers) provide a pre-configured development environment with all necessary tools installed and ready to use. They are supported by many editors, including [VS Code](https://code.visualstudio.com/docs/devcontainers/containers), [PyCharm](https://www.jetbrains.com/help/pycharm/connect-to-devcontainer.html), [Zed](https://zed.dev/docs/dev-containers), [Cursor](https://www.vcluster.com/blog/cursor-with-devpod) and [Windsurf](https://docs.windsurf.com/windsurf/advanced#dev-containers).</mark>

**Why use a devcontainer?**
- **Consistent environment** across different machines and contributors - no "works on my machine" issues
- **Isolated sandbox** perfect for running AI agents and experimental tools without affecting your host system
- **Zero local setup** - no need to install Python, uv, just, or other dependencies on your machine

**Quick Start:**
1. Open the repository a supported editor
2. When prompted, click "Reopen in Container" (or use Command Palette: "Dev Containers: Reopen in Container")
3. Wait for the container to build and start
4. Run `just test` to verify

<mark>**Want to add custom tools like AI agents?**: You could add for example these features to add claude-code, codex and custom firewall rules (Edit [settings.json](https://code.visualstudio.com/docs/getstarted/settings#_settingsjson) in VS Code):</mark>

```
{
  "dev.containers.defaultFeatures": {
    "ghcr.io/w3cj/devcontainer-features/firewall@sha256:f8ae63faf64094305ef247befc0a9c66eecd7a01768df0cc826c7d4a81a92bfc": {
      "verbose": true,
      "pypi": true,
      "anthropicApi": true,
      "openaiApi": true,
      "googleAiApi": true,
      "vscodeMarketplace": true
    },
    "ghcr.io/fohrloop/devcontainer-features/codex@sha256:7d78dad69447100e6694d4eb73b4307566c07e678f3f346d06e0c6fe37ef959c": {},
    "ghcr.io/fohrloop/anthropics-devcontainer-features-fork/claude-code@sha256:f76bc7179de085269881172935f6c5541321478f607c129872b0881d7109d5bf": {}
  }
}
```

For more details on adding extensions, dotfiles, and features, see [.devcontainer/CUSTOMIZATIONS.md](.devcontainer/CUSTOMIZATIONS.md).

---

## 13. AI Agents
- <mark>If you want to use AI Agents for coding, there is AGENTS.md for guiding the agents, as well as more specific instructions in `.planning/`. The planning older was generated and can be updated using [GSD](https://github.com/gsd-build/get-shit-done) `/gsd:map-codebase`. These files should (in theory) make the AI to produce better suited code.</mark>
- <mark>Each contributor is expected to review their AI generated code themselves. Only provide code you have read, understood and reviewed yourself first.</mark>
- Since the ".planning" was generated using GSD, GSD might be the best suited tool for this project currently. Also other SDD tools/frameworks can be suggested. Related discussion: [#602](https://github.com/wakepy/wakepy/discussions/602)
