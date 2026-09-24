## **The Codebase Map**

The following table details the most important paths in the repository, their purpose, and the key technologies associated with them.

| Path | Purpose |
| :---- | :---- |
| app.py, app_*.py | The main entry point for the Flask web application. It handles the initialization of the Flask app, database connections, and the registration of API routes and blueprints. |
| tasks/ | **The Core Logic Hub.** This is where the most intensive computations occur. Each API or async task then point to an specific implementation in this directory|
| tasks/mediaserver.py | In this fail the generic method to interact with the mediaservers are specialized to call the specific one |
| ai.py | This module centralizes all interactions with Large Language Models (LLMs). It contains the logic for communicating with services like self-hosted Ollama or the Google Gemini API for tasks such as AI-powered playlist naming and translating natural language requests into SQL queries. |
| config.py | Contains the application's default, non-sensitive configuration parameters. These values serve as fallbacks and can be easily overridden by environment variables, providing a flexible and secure configuration system. |
| Authentication | Configured in `config.py` by `AUTH_ENABLED`, `AUDIOMUSE_USER`, `AUDIOMUSE_PASSWORD`, `API_TOKEN`, and `JWT_SECRET`. Enforcement happens in `app.py` and `app_helepr.py` functionality |
| static/ & templates/ | These directories contain all frontend assets. |
| deployment/ | This contains deployment example but also the supervisord configuration |
| Dockerfile, Dockerfile.nvidia | These files contain the instructions for building the OCI-compatible container images for the application. |
| .github/ | This directory holds GitHub-specific configuration files, such as issue templates, pull request templates, and potentially continuous integration/continuous deployment (CI/CD) workflows.1 |

---

### PR Requirements
When submitting a pull request, ensure:

* **Clear description:** Explain what the PR achieves and why the change is needed with **HUMAN generated** text. Also cleary explain how you tested it and how to replicate those test
* **Link the PR to an existing issue:** in this way you work on something already agreed on and you avoid many rework.
* **Testing:** Verify core features work on at least one architecture (Intel/ARM) and one media server:
  * Analysis and Clustering
  * Instant Playlist
  * Playlist from Similar Song
  * Song Path
  * Sonic Fingerprint
  * *(Basically, test each function in the integrated front-end menu at least once)*
* **License compliance:** Your code must align with AudioMuse-AI's license
* **CPU Compatibility:** AudioMuse-AI supports both Intel and ARM CPUs, including older Intel processors. PRs that introduce dependencies breaking compatibility with older CPUs will not be merged
* **Documentation:** If needed, update the documentation

> Important: Prefear opening small PR, focused on specific functionality that directly add value. Avoid to change multiple unrelated functionality to facilitate test.

> <mark>Contributions generated with AI are welcome, provided that a qualified human reviewer verifies, tests, and understands the code. AI tools can assist in development, but all pull requests must be submitted by someone capable of ensuring correctness and maintainability. </mark>

> Missing requirements may lead to requests for additional information and, if not provided, the PR may be closed. Regardless of the above, the final decision to merge a pull request is at the maintainer’s discretion.
