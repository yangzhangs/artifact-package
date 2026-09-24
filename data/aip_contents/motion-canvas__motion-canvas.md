## Making a Pull Request


1. Fork the motion-canvas/motion-canvas repo.
2. In your forked repo, create a new branch for your changes:
   ```shell
   git checkout -b my-fix-branch main
   ```
3. Update the code.
4. Commit your changes using a **descriptive commit message** that follows the
   [Angular Commit Message Conventions][commit-format]. We strongly discourage
   using AI to generate commit descriptions. If you believe the description is
   not worth writing then it's probably not necessary.
   ```shell
   git commit --all
   ```
   When committing the changes, our git hooks should automatically run Prettier
   and ESLint for you. If, for some reason, hooks are not supported in your
   working environement, you can run these tools using `npm run prettier:fix`
   and `npm run eslint:fix` respectively.
5. Push your branch to GitHub:
   ```shell
   git push origin my-fix-branch
   ```
6. In GitHub, send a pull request to [the main branch][main] and **request a
   review** from [aarthificial](https://github.com/aarthificial).



## Using generative AI


Using generative AI to help you write code and documentation is allowed, but use
it to enhance your work, not replace it. Pull requests that are a mindless copy
of the output of an AI model will be rejected.
