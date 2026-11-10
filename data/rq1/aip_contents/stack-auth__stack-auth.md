## Vibecoding setup

<mark>NOTE: Every line of code should be reviewed by a human BEFORE you submit a PR. DO NOT waste our time by creating and submitting an AI-generated PR.</mark>

<mark>For vibecoding, it can help to have multiple parallel copies of the codebase open in different windows. For this, you can set the environment variable `NEXT_PUBLIC_STACK_PORT_PREFIX` to a different value (default 81). To do this consistently across all coding agents (Claude Code/Cursor Agent/Codex),we recommend you use `direnv` with a `.envrc` file:</mark>

1. Install `direnv` if you haven't already. On Mac, the easiest way is to install it with Homebrew: `brew install direnv`.
2. Update ALL your shell configs to append the following lines. On most Mac setups, this is `~/.bash_profile`, `~/.bashrc`, `~/.zprofile`, `~/.zshrc`, and `~/.zshenv`.
  ```sh
  # ~/.bash_profile, ~/.bashrc, ~/.zprofile, ~/.zshrc, ~/.zshenv, etc.
  # note that different coding agents use a different shell in a different mode (login, non-login, interactive, non-interactive, etc.); from my experimentation, as of 2025-10-17 on a Mac, Cursor uses non-interactive zsh (requiring ~/.zshenv), whereas Codex uses a non-interactive login bash (requiring ~/.bash_profile). It's easiest to just add these lines of code to all of your shell configs.
  # also, make sure to use the correct path to the direnv binary; for example, on a Mac with Homebrew installed, it is /opt/homebrew/bin/direnv
  eval "$(/path/to/direnv hook <bash|zsh>)"
  eval "$(/path/to/direnv export <bash|zsh>)"
  ```
3. Now, create a `.envrc` file in the root of Stack Auth's codebase with the following content:
  ```sh
  # .envrc
  # make sure to install direnv and add it to your shell rc file (e.g. ~/.bashrc or ~/.zshrc)
  export NEXT_PUBLIC_STACK_PORT_PREFIX=181

  # with this many processes running, it can be useful to add a custom title to all Node.js processes
  # export NODE_OPTIONS="--require=<path-to-the-workspace-folder>/scripts/set-process-title.js $NODE_OPTIONS"
  ```

When you do this, it is recommended that you give all workspaces a port prefix other than 81, to prevent accidental conflicts when you forgot to make a feature support the $NEXT_PUBLIC_STACK_PORT_PREFIX environment variable. (for example: first workspace at 181, second workspace at 182, etc.)

Also, the cookies on different ports may conflict with each other. To prevent this, open `a.localhost:18101` and `b.localhost:18201` instead or normal localhost, so the cookies are scoped differently.
