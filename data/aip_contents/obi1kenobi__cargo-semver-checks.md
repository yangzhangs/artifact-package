## Making your first contribution

> [!IMPORTANT]
> **We have a zero-tolerance policy for low-quality AI-generated contributions.**
>
> It's very easy to use AI to generate low-quality "contributions" that are not carefully considered and do not meet the quality bar for inclusion in the codebase.
> Such "contributions" do not benefit the project's stakeholders — in fact, they are a drain on maintainers' and reviewers' time and energy.
> Instead, the "contributions" serve to boost the contributor's GitHub statistics or achieve other personal goals, at the expense of the project and its stakeholders.
>
> Contributions that appear to be low-quality AI slop will be rejected without further explanation. Further contributions by the same authors will also be rejected without review or explanation, as the good faith assumption has already been breached once.
> We express no opinion on AI assistance *in general*, and do not ban AI tools outright — we merely require that you take personal responsibility for the contribution's quality instead of relying on "the AI thought it was a good idea."

Thanks for taking the time to contribute!
The best starting point is adding a new lint.
[Here is a list](https://github.com/obi1kenobi/cargo-semver-checks/issues?q=is%3Aopen+label%3AE-mentor+label%3AA-lint)
of lints that have all their prerequisites met and are ready to be added,
and which have mentorship available.
Please make use of the mentorship opportunity by asking questions in the relevant GitHub issue!

After choosing a lint to implement, try to identify a related lint that is already implemented
and relies on similar information.
For example, if implementing a lint that uses information about attributes,
find other lints that check attribute information and use them as guides as you write your lint.

Make sure to check the ["Development Environment"](#development-environment) section, especially if you are using Windows.

The ["Adding a new lint"](#adding-a-new-lint) section of this document has a walkthrough for
defining and testing new lints.

Please see the ["Running `cargo test` for the first time"](#running-cargo-test-for-the-first-time)
section to generate the test rustdoc JSON data the tests require. Failing to run this step
will cause `cargo test` failures.

The design of `cargo-semver-checks` is documented in the [Design goals](#design-goals) section.
`cargo-semver-checks` uses the [Trustfall](https://github.com/obi1kenobi/trustfall) query engine,
which in turn uses GraphQL syntax with non-standard semantics.
These extensions were originally developed for a previous project ("GraphQL compiler"),
and have been streamlined and further developed in Trustfall.
Trustfall documentation is unfortunately still minimal and still consists largely of examples,
but most Trustfall query functionality is nearly identical
(down to trivial parameter naming differences) to the query functionality documented in
[the GraphQL compiler query reference](https://graphql-compiler.readthedocs.io/en/latest/language_specification/query_directives.html).
