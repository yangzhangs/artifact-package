### <mark>AI usage</mark>

<mark>If you use AI tools (such as GitHub Copilot, Claude, Cursor, etc.) while</mark>
contributing, you must disclose this in your pull request description and/or
commit messages.  See *[AI_POLICY.md]* for the complete policy.

[AI_POLICY.md]: AI_POLICY.md

[=== 独立AI政策文件: AI_POLICY.md ===]

<!-- deno-fmt-ignore-file -->

<mark>AI usage policy</mark>
===============

<mark>This policy is inspired by [Ghostty's AI policy][1].</mark>

<mark>The Fedify project has the following rules for AI usage:</mark>

 -  <mark>*All AI usage in any form must be disclosed.*  You must state the tool you</mark>
<mark>used (e.g., Claude, Cursor, GitHub Copilot) along with the extent that</mark>
<mark>the work was AI-assisted in both your pull request description and commit</mark>
    messages.  For commit messages, use the `Assisted-by` trailer (see below
    for the required format).

 -  *Pull requests created in any way by AI can only be for accepted issues.*
    Drive-by pull requests that do not reference an accepted issue will be
    closed.  If AI isn't disclosed but a maintainer suspects its use, the PR
    will be closed.  If you want to share code for a non-accepted issue, open
    a discussion or attach it to an existing discussion.

 -  *Pull requests created by AI must have been fully verified with human use.*
    AI must not create hypothetically correct code that hasn't been tested.
<mark>Importantly, you must not allow AI to write code for platforms or</mark>
    environments you don't have access to manually test on.

 -  <mark>*Issues and discussions can use AI assistance but must have a full</mark>
    human-in-the-loop.*  This means that any content generated with AI must
    have been reviewed and edited by a human before submission.  AI is very
    good at being overly verbose and including noise that distracts from
    the main point.  Humans must do their research and trim this down.

 -  <mark>*AI-generated media (images, diagrams, etc.) is allowed only in</mark>
<mark>documentation, and must be clearly labeled as AI-generated.*  Text and</mark>
<mark>code are acceptable AI-generated content per the other rules in this</mark>
    policy.  For documentation visuals like diagrams or illustrations,
<mark>AI-generated content is permitted but must include clear attribution</mark>
    (e.g., “Diagram generated with DALL-E” or “Created using Midjourney”).

 -  *Violations of this policy may result in being banned from contributing.*
    We want to help contributors learn and grow, but repeated or intentional
    violations of this policy undermine trust and burden maintainers.

These rules apply only to outside contributions to Fedify.  Maintainers are
<mark>exempt from these rules and may use AI tools at their discretion; they've</mark>
proven themselves trustworthy to apply good judgment.

[1]: https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md


<mark>Disclosing AI assistance in commit messages</mark>
-------------------------------------------

<mark>When AI tools assist with a commit, add an `Assisted-by` trailer to the commit</mark>
message.  Do *not* use `Co-authored-by` for AI assistants; that trailer is
reserved for human co-authors.

The format is:

~~~~
Assisted-by: AGENT_NAME:MODEL_VERSION
~~~~

For example:

~~~~
Assisted-by: OpenCode:qwen3.6-plus
<mark>Assisted-by: Claude Code:claude-sonnet-4-6</mark>
<mark>Assisted-by: Gemini CLI:gemini-3.1-pro-preview</mark>
Assisted-by: Codex:gpt-5.4
~~~~

<mark>If multiple AI tools were used, include one `Assisted-by` line per tool.</mark>


There are humans here
---------------------

Please remember that Fedify is maintained by humans.

Every discussion, issue, and pull request is read and reviewed by humans
(and sometimes machines, too).  It is a boundary point at which people interact
with each other and the work done.  It is rude and disrespectful to approach
this boundary with low-effort, unqualified work, since it puts the burden of
validation on the maintainer.

In a perfect world, AI would produce high-quality, accurate work every time.
But today, that reality depends on the driver of the AI.  And today, most
drivers of AI are just not good enough.  So, until either the people get
better, the AI gets better, or both, we have to have rules to protect
maintainers.


<mark>AI is welcome here</mark>
------------------

<mark>Fedify is written with plenty of AI assistance, and many maintainers embrace</mark>
<mark>AI tools as a productive tool in their workflow.  As a project, we welcome</mark>
AI as a tool!

<mark>*Our reason for this policy is not due to an anti-AI stance*, but instead due</mark>
<mark>to the number of highly unqualified people using AI.  It's the people, not</mark>
the tools, that are the problem.

We include this section to be transparent about the project's usage of AI for
people who may disagree with it, and to address the misconception that this
<mark>policy is anti-AI in nature.</mark>

---

# Standalone AI policy file

<!-- deno-fmt-ignore-file -->

<mark>AI usage policy</mark>
===============

<mark>This policy is inspired by [Ghostty's AI policy][1].</mark>

<mark>The Fedify project has the following rules for AI usage:</mark>

 -  <mark>*All AI usage in any form must be disclosed.*  You must state the tool you</mark>
<mark>used (e.g., Claude, Cursor, GitHub Copilot) along with the extent that</mark>
<mark>the work was AI-assisted in both your pull request description and commit</mark>
    messages.  For commit messages, use the `Assisted-by` trailer (see below
    for the required format).

 -  *Pull requests created in any way by AI can only be for accepted issues.*
    Drive-by pull requests that do not reference an accepted issue will be
    closed.  If AI isn't disclosed but a maintainer suspects its use, the PR
    will be closed.  If you want to share code for a non-accepted issue, open
    a discussion or attach it to an existing discussion.

 -  *Pull requests created by AI must have been fully verified with human use.*
    AI must not create hypothetically correct code that hasn't been tested.
<mark>Importantly, you must not allow AI to write code for platforms or</mark>
    environments you don't have access to manually test on.

 -  <mark>*Issues and discussions can use AI assistance but must have a full</mark>
    human-in-the-loop.*  This means that any content generated with AI must
    have been reviewed and edited by a human before submission.  AI is very
    good at being overly verbose and including noise that distracts from
    the main point.  Humans must do their research and trim this down.

 -  <mark>*AI-generated media (images, diagrams, etc.) is allowed only in</mark>
<mark>documentation, and must be clearly labeled as AI-generated.*  Text and</mark>
<mark>code are acceptable AI-generated content per the other rules in this</mark>
    policy.  For documentation visuals like diagrams or illustrations,
<mark>AI-generated content is permitted but must include clear attribution</mark>
    (e.g., “Diagram generated with DALL-E” or “Created using Midjourney”).

 -  *Violations of this policy may result in being banned from contributing.*
    We want to help contributors learn and grow, but repeated or intentional
    violations of this policy undermine trust and burden maintainers.

These rules apply only to outside contributions to Fedify.  Maintainers are
<mark>exempt from these rules and may use AI tools at their discretion; they've</mark>
proven themselves trustworthy to apply good judgment.

[1]: https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md


<mark>Disclosing AI assistance in commit messages</mark>
-------------------------------------------

<mark>When AI tools assist with a commit, add an `Assisted-by` trailer to the commit</mark>
message.  Do *not* use `Co-authored-by` for AI assistants; that trailer is
reserved for human co-authors.

The format is:

~~~~
Assisted-by: AGENT_NAME:MODEL_VERSION
~~~~

For example:

~~~~
Assisted-by: OpenCode:qwen3.6-plus
<mark>Assisted-by: Claude Code:claude-sonnet-4-6</mark>
<mark>Assisted-by: Gemini CLI:gemini-3.1-pro-preview</mark>
Assisted-by: Codex:gpt-5.4
~~~~

<mark>If multiple AI tools were used, include one `Assisted-by` line per tool.</mark>


There are humans here
---------------------

Please remember that Fedify is maintained by humans.

Every discussion, issue, and pull request is read and reviewed by humans
(and sometimes machines, too).  It is a boundary point at which people interact
with each other and the work done.  It is rude and disrespectful to approach
this boundary with low-effort, unqualified work, since it puts the burden of
validation on the maintainer.

In a perfect world, AI would produce high-quality, accurate work every time.
But today, that reality depends on the driver of the AI.  And today, most
drivers of AI are just not good enough.  So, until either the people get
better, the AI gets better, or both, we have to have rules to protect
maintainers.


<mark>AI is welcome here</mark>
------------------

<mark>Fedify is written with plenty of AI assistance, and many maintainers embrace</mark>
<mark>AI tools as a productive tool in their workflow.  As a project, we welcome</mark>
AI as a tool!

<mark>*Our reason for this policy is not due to an anti-AI stance*, but instead due</mark>
<mark>to the number of highly unqualified people using AI.  It's the people, not</mark>
the tools, that are the problem.

We include this section to be transparent about the project's usage of AI for
people who may disagree with it, and to address the misconception that this
<mark>policy is anti-AI in nature.</mark>
