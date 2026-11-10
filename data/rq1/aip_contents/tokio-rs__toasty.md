## <mark>Using AI assistants</mark>

Using an AI assistant to write code, issue descriptions, or PR
descriptions is welcome. The human author is responsible for
understanding the submitted code and defending it in review. A PR whose
author cannot discuss the change gets closed.

---

### Before you push

```bash
cargo fmt
cargo clippy
cargo test
```

`cargo test` runs the SQLite-backed integration suite and needs no
external services. When you touch driver code, also run the suite against
<mark>the affected driver — see [`CLAUDE.md`](CLAUDE.md) for the cargo</mark>
invocations.
