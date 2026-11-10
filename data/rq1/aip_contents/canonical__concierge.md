## AI

<mark>You're welcome to submit pull requests that are partly or entirely generated using generative AI tools. However, you must review the code yourself before moving the PR out of draft -- by submitting the PR, you are claiming personal responsibility for its quality and suitability. If you are not capable of reviewing the PR (for example, if you are not fluent in Go, or are not familiar with Concierge), please do not submit the PR (maybe you'd like to open an issue instead). PRs that are clearly (co-)authored by tools will be closed without review unless there is a human author that claims responsibility for the PR.</mark>

<mark>Please do not use tools (such as GitHub Copilot) to provide PR reviews. The Charm Tech team also has access to these tools, and will use them when appropriate.</mark>

---

## Creating a release

To release, simply create a new release in GitHub.

1. [Draft a new GitHub release](https://github.com/canonical/concierge/releases/new)
2. Enter the version tag (for example `v1.28.0`) and select "Create new tag: on publish".
3. Enter a release title: include the version tag and a short summary of the release.
4. <mark>Write release notes - start with the draft provided by GitHub, drop the `by @author` credit for anyone in the Charm Tech team (including Copilot and other AI users), and include a short summary of the new features and bug fixes at the top. Leave the link to the full list of commits and any acknowledgement of new contributors.</mark>
5. Click "Publish release".
6. Monitor the release [GitHub Action](https://github.com/canonical/concierge/actions) and check that the [snap](https://snapcraft.io/concierge) is uploaded correctly (it will have been published to all risks, including `stable`)
7. Run the appropriate security scan and SBOM generation, as described in the Canonical library's SSDLC process. Upload artifacts to the [SSDLC Concierge folder in Drive](https://drive.google.com/drive/folders/1RtAn7x0EX97C6eV66xs74Pwth3KW7NHI). Open the artifact and verify that the security scan has not found any vulnerabilities.
