## AI Disclosure

> [!IMPORTANT]
>
> If you are using **any kind of AI assistance** to contribute to Absurd,
> it must be disclosed in the pull request.  A template is provided.

If you are using any kind of AI assistance while contributing to this project
you must disclose this in the pull request and the extent to which it was.  When
you use AI for PR descriptions you also must disclose that.

It is rude not to disclose AI usage to the reviewer and it makes it hard to
understand how much scrutiy needs to be placed on the contribution.

We are strong supporters and users of AI, however we also recognize the
challenges that lack of disclosure presents on Open Source projects.  Please be
respectful to maintainers and your fellow humans.

---

## Migrations

During development the changes should just only land in `sql/absurd.sql`.  We
use a Claude Code command (`/make-migrations`) which helps creating migrations.
They should be made when a release is made unless the change is very gnarly,
in which case the PR should already incorporate the migrations.
