## Sending changes

The Zed culture values working code and synchronous conversations over long
discussion threads.

The best way to get us to take a look at a proposed change is to send a pull
request. We will get back to you (though this sometimes takes longer than we'd
like, sorry).

Although we will take a look, we tend to only merge about half the PRs that are
submitted. If you'd like your PR to have the best chance of being merged:

- Make sure the change is **desired**: we're always happy to accept bugfixes,
  but features should be confirmed with us first if you aim to avoid wasted
  effort. If there isn't already a GitHub issue for your feature with staff
  confirmation that we want it, start with a GitHub discussion rather than a PR.
- Include a clear description of **what you're solving**, and why it's important.
- Include **tests**. For UI changes, consider updating visual regression tests (see [Building Zed for macOS](./docs/src/development/macos.md#visual-regression-tests)).
- If it changes the UI, attach **screenshots** or screen recordings.
- Make the PR about **one thing only**, e.g. if it's a bugfix, don't add two
  features and a refactoring on top of that.
- Keep AI assistance under your judgement and responsibility: it's unlikely
  we'll merge a vibe-coded PR that the author doesn't understand.

The internal advice for reviewers is as follows:

- If the fix/feature is obviously great, and the code is great. Hit merge.
- If the fix/feature is obviously great, and the code is nearly great. Send PR comments, or offer to pair to get things perfect.
- If the fix/feature is not obviously great, or the code needs rewriting from scratch. Close the PR with a thank you and some explanation.

If you need more feedback from us: the best way is to be responsive to
Github comments, or to offer up time to pair with us.

If you need help deciding how to fix a bug, or finish implementing a feature
that we've agreed we want, please open a PR early so we can discuss how to make
the change with code in hand.

---

### UI/UX checklist

When your changes affect UI, consult this checklist:

**Accessibility / Ergonomics**
- Do all keyboard shortcuts work as intended?
- Are shortcuts discoverable (tooltips, menus, docs)?
- Do all mouse actions work (drag, context menus, resizing, scrolling)?
- Does the feature look great in light mode and dark mode?
- Are hover states, focus rings, and active states clear and consistent?
- Is it usable without a mouse (keyboard-only navigation)?

**Responsiveness**
- Does the UI scale gracefully on:
    - Narrow panes (e.g., side-by-side split views)?
    - Short panes (e.g., laptops with 13" displays)?
    - High-DPI / Retina displays?
- Does resizing panes or windows keep the UI usable and attractive?
- Do dialogs or modals stay centered and within viewport bounds?

**Platform Consistency**
- Is the feature fully usable on Windows, Linux, and Mac?
- Does it respect system-level settings (fonts, scaling, input methods)?

**Performance**
- All user interactions must have instant feedback.
    - If the user requests something slow (e.g. an LLM generation) there should be some indication of the work in progress.
- Does it handle large files, big projects, or heavy workloads without degrading?
- Frames must take no more than 8ms (120fps)

**Consistency**
- Does it match Zed’s design language (spacing, typography, icons)?
- Are terminology, labels, and tone consistent with the rest of Zed?
- Are interactions consistent (e.g., how tabs close, how modals dismiss, how errors show)?

**Internationalization & Text**
- Are strings concise, clear, and unambiguous?
- Do we avoid internal Zed jargon that only insiders would know?

**User Paths & Edge Cases**
- What does the happy path look like?
- What does the unhappy path look like? (errors, rejections, invalid states)
- How does it work in offline vs. online states?
- How does it work in unauthenticated vs. authenticated states?
- How does it behave if data is missing, corrupted, or delayed?
- Are error messages actionable and consistent with Zed’s voice?

**Discoverability & Learning**
- Can a first-time user figure it out without docs?
- Is there an intuitive way to undo/redo actions?
- Are power features discoverable but not intrusive?
- Is there a path from beginner → expert usage (progressive disclosure)?

---

## Things we will (probably) not merge

Although there are few hard and fast rules, typically we don't merge:

- Anything that can be provided by an extension. For example a new language, or theme. For adding themes or support for a new language to Zed, check out our [docs on developing extensions](https://zed.dev/docs/extensions/developing-extensions).
- New file icons. Zed's default icon theme consists of icons that are hand-designed to fit together in a cohesive manner, please don't submit PRs with off-the-shelf SVGs.
- Features where (in our subjective opinion) the extra complexity isn't worth it for the number of people who will benefit.
- Giant refactorings.
- Non-trivial changes with no tests.
- Stylistic code changes that do not alter any app logic. Reducing allocations, removing `.unwrap()`s, fixing typos is great; making code "more readable" — maybe not so much.
- Anything that seems AI-generated without understanding the output.
