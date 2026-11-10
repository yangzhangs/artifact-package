## General

1. <mark>**Avoid vibe-coding large features** - While probably most of us use AI while coding in our day to day lives, you should try to use it in a clever and targetted manner. Avoid submitting large vibe-coded features, because in 99% of the cases they will not behave as expected. These kinds of PR-s drain our energy and time that could be focused on something more useful, because what took a few seconds for the AI assistant to pump out will take us hours to test, discuss, and ultimately scrap because it doesn't take into account half the things a real programmer probably would. If you made heavy use of AI in your pull request, **indicate it**.</mark>

2. **Do not break existing code** - WinBoat aims to provide a seamless user experience, so please avoid the breakage of any existing features to the best of your abilities. Ensure that folks potentially upgrading to a new version that includes your changes won't have any problems, and address any migrations if they're required.

3. **Do rigorous testing** - WinBoat is used by tens of thousands of folks every day on a wide range of Linux distros, make sure that the PR you submit doesn't break compatibility on any of the mainstream distros.

4. **If you're unsure, ask** - If you want to start working on something large that you then intend for us to merge into WinBoat, it may be worth asking us first in an issue to understand if the feature is compatible with the philosophy of WinBoat and whether we want to include it. The same idea applies if you're unsure how to implement a feature in a way that's compatible with how WinBoat operates.

5. **Avoid introducing new programming languages** - WinBoat uses TypeScript & Vue for the Electron app, and Go & PowerShell for the Guest Server. Use these for getting things done.

6. **Avoid introducing new foreign dependencies** - Chances are there's an NPM / Go package for what you're trying to achieve or at least something similar. If there isn't, and it's a must to include it, discuss with us first.
