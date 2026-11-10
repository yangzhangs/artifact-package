## Guidelines

- **Backwards compatible:** We strive for a great deal of backwards compatibility here at `pygame-ce`. If you desire to change an existing behavior, then you'll need to
provide a strong reason why we might consider it. Someone out there might be using the current behavior and we don't want to break their stuff. A usually better
alternative is to keep the default behavior the same, but add an option to run the new behavior somehow. It can be a new function, a kwarg, etc.
- **Accurate information:** Ensure that all information is accurate and up-to-date.  Double-check links and descriptions before submitting your changes.
- **Clear descriptions:** Write concise and informative descriptions for each change.  Explain what the change does and what its key features are.
- <mark>**Do not lie:** If you use AI to generate part or all of your changes, state that in your pull request. Also state exactly how much of your change was written by AI and how</mark>
you verified that the changes don't have any unintended side-effects and that they do what they're supposed to do.
- **New functionality always gets new tests:** You should always write new unit tests in the appropriate file in the test directory for any added/changed functionality, if at all
possible. Sometimes it's not possible to test things, but that's a minuscule minority of the changes we see. Write tests, or explain why no new tests are added.
- **Join the [PGC Discord](https://pyga.me/discord):** Besides the role you can get in the server upon your first pull request being merged, regular contributors are active members of the discord server and are willing to give you a hand if crafting your pull request gets to be painful.

Thank you for contributing!
