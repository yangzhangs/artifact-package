## <mark>AI Disclosure</mark>

> [!IMPORTANT]
>
> <mark>If you are using **any kind of AI assistance** to contribute to Absurd,</mark>
> it must be disclosed in the pull request.  A template is provided.

<mark>If you are using any kind of AI assistance while contributing to this project</mark>
you must disclose this in the pull request and the extent to which it was.  When
<mark>you use AI for PR descriptions you also must disclose that.</mark>

<mark>It is rude not to disclose AI usage to the reviewer and it makes it hard to</mark>
understand how much scrutiy needs to be placed on the contribution.

<mark>We are strong supporters and users of AI, however we also recognize the</mark>
challenges that lack of disclosure presents on Open Source projects.  Please be
respectful to maintainers and your fellow humans.

---

## Migrations

During development the changes should just only land in `sql/absurd.sql`.  We
<mark>use a Claude Code command (`/make-migrations`) which helps creating migrations.</mark>
They should be made when a release is made unless the change is very gnarly,
in which case the PR should already incorporate the migrations.
