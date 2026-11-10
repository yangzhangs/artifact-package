### Working with Optional Dependencies

<mark>Instructor uses optional dependencies to support different LLM providers. Provider-specific utilities live under `instructor/utils`. When adding integration for a new provider:</mark>

1. **Update pyproject.toml**: Add your provider's dependencies to both `[project.optional-dependencies]` and `[dependency-groups]`:

   ```toml
   [project.optional-dependencies]
   # Add your provider here
   my-provider = ["my-provider-sdk>=1.0.0,<2.0.0"]
   
   [dependency-groups]
   # Also add to dependency groups
   my-provider = ["my-provider-sdk>=1.0.0,<2.0.0"]
   ```

2. **Create Provider Client**: Implement your provider client in `instructor/clients/client_myprovider.py`

3. <mark>**Add Tests**: Create tests in `tests/llm/test_myprovider/`</mark>

4. **Document Installation**: Update the documentation to include installation instructions:
   ```
   # Install with your provider support
   uv pip install "instructor[my-provider]"
   # or
   poetry install --with my-provider
   ```

5. **Create Provider Utilities and Handlers**:
   - Add a new module at `instructor/utils/myprovider.py`
   - Implement `reask` functions for validation errors and `handle_*` functions
     for formatting requests
   - Define `MYPROVIDER_HANDLERS` mapping `Mode` values to these functions

6. **Register the Provider**:
   - Add a value in `instructor/utils/providers.py` to the `Provider` enum
   - Extend `get_provider` with detection logic for your base URL

7. **Update `process_response.py`**:
   - Import your handler functions and include them in the `mode_handlers`
     dictionary so the library can route requests to your provider
   - `process_response.py` relies on these handlers to format arguments and
     parse results for each `Mode`

---

### Contributing to Evals

We encourage contributions to our evaluation tests:

1. <mark>Explore existing evals in the [evals directory](https://github.com/instructor-ai/instructor/tree/main/tests/llm)</mark>
2. Contribute new evals as pytest tests
3. Evals should test specific capabilities or edge cases of the library or models
4. Follow the existing patterns for structuring eval tests

---

### Conventional Comments

We use conventional comments in code reviews and commit messages. This helps make feedback clearer and more actionable:

```
<label>: <subject>

<description>
```

Labels include:
- **praise:** highlights something positive
- **suggestion:** proposes a change or improvement
- **question:** asks for clarification
- **nitpick:** minor, trivial feedback that can be ignored
- **issue:** points out a specific problem that needs to be fixed
- **todo:** notes something to be addressed later
- **fix:** resolves an issue
- **refactor:** suggests reorganizing code without changing behavior
- **test:** suggests adding or improving tests

Examples:
```
suggestion: consider using Pydantic's validator for this check
This would ensure validation happens automatically when the model is created.

question: why is this approach used instead of async processing?
I'm wondering if there would be performance benefits.

fix: correct the type hint for the client parameter
The client should accept OpenAI instances, not strings.
```

For more details, see the [Conventional Comments specification](https://conventionalcomments.org/).

---

#### Examples

```
feat(openai): add support for response_format parameter

fix(anthropic): correct tool calling format in Claude client

docs: improve installation instructions for various providers

test(evals): add evaluation for recursive schema handling
```

Breaking changes should be indicated by adding `!` after the type/scope:

```
feat(api)!: change parameter order in from_openai factory function
```

Including a scope is recommended when changes affect a specific part of the codebase (e.g., a specific provider, feature, or component).

---

# <mark>Skip LLM tests (faster for local development)</mark>
<mark>pytest tests/ -k 'not llm and not openai'</mark>

---

## <mark>Using Cursor for PR Creation</mark>

<mark>Cursor (https://cursor.sh) is a code editor powered by AI that can help you create PRs efficiently. We encourage using Cursor for Instructor development:</mark>

1. <mark>**Install Cursor**: Download from [cursor.sh](https://cursor.sh/)</mark>

2. <mark>**Create a Branch**: Start a new branch for your feature using Cursor's Git integration</mark>

3. <mark>**Use Cursor Rules**: We have Cursor rules that help with standards:</mark>
   - `new-features-planning`: Use when implementing new features
   - `simple-language`: Follow when writing documentation
   - `documentation-sync`: Reference when making code changes to keep docs in sync

4. <mark>**Generate Code with AI**: Use Cursor's AI assistance to generate code that follows our style</mark>

5. <mark>**Auto-Create PRs**: Use Cursor's PR creation feature with our template:</mark>
   ```
   # Create PR using gh CLI
   gh pr create -t "Your PR Title" -b "Description of changes" -r jxnl,ivanleomk
   ```

6. <mark>**Include Attribution**: Add `This PR was written by [Cursor](https://cursor.sh)` to your PR description</mark>

<mark>For more details, see our Cursor rules in `.cursor/rules/`.</mark>
