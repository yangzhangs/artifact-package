## Project Structure

```
airunway/
├── frontend/          # React frontend application
│   ├── src/
│   │   ├── components/  # UI components
│   │   ├── pages/       # Page components
│   │   ├── hooks/       # React hooks
│   │   └── lib/         # Utilities and API client
│   └── ...
├── backend/           # Hono backend API (runs on Bun)
│   ├── src/
│   │   ├── hono-app.ts  # All API routes consolidated
│   │   ├── index.ts     # Bun.serve() entry point
│   │   ├── routes/      # API route handlers
│   │   │   ├── installation.ts # Provider installation (reads from CRDs)
│   │   │   ├── deployments.ts  # Deployment management
│   │   │   └── ...
│   │   ├── services/    # Core services
│   │   │   ├── kubernetes.ts # K8s client
│   │   │   ├── config.ts     # ConfigMap persistence
│   │   │   ├── helm.ts       # Helm CLI integration
│   │   │   ├── metrics.ts    # Prometheus metrics fetching
│   │   │   ├── autoscaler.ts # Cluster autoscaler detection
│   │   │   ├── buildkit.ts   # BuildKit builder management
│   │   │   └── registry.ts   # In-cluster registry management
│   │   ├── lib/         # Utility libraries
│   │   │   ├── k8s-errors.ts # K8s error handling
│   │   │   ├── prometheus-parser.ts # Prometheus text parser
│   │   │   └── retry.ts      # Retry logic for K8s calls
│   │   └── data/        # Static model catalog
│   └── ...
├── shared/            # Shared TypeScript types
├── controller/        # Go-based Kubernetes controller (kubebuilder)
│   ├── api/v1alpha1/  # CRD type definitions
│   ├── internal/      # Reconciliation logic
│   ├── cmd/main.go    # Controller entrypoint
│   └── config/        # Kustomize manifests
├── providers/         # Out-of-tree provider operators (Go)
│   ├── kaito/         # KAITO provider
│   ├── dynamo/        # NVIDIA Dynamo provider
│   └── kuberay/       # KubeRay provider
│   └── llmd/          # llm-d provider
└── docs/              # Documentation
```

---

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`bun run test`)
5. Run linting (`bun run lint`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request
9. **Share AI Prompts** — If you used AI assistance, include the prompt in your PR (see below)

---

## AI-Assisted Contributions & Prompt Requests

We embrace AI-assisted development! Whether you use GitHub Copilot, Claude, Cursor, or other AI tools, we welcome contributions that leverage these capabilities.

---

### What is a Prompt Request?

A **prompt request** is a contribution where you share the AI prompt that generates code, rather than (or in addition to) the code itself. This approach:

- **Captures intent** — The prompt often explains *why* better than a code diff
- **Enables review before implementation** — Maintainers can validate the approach
- **Supports iteration** — Prompts can be refined before code is generated
- **Improves reproducibility** — Anyone can run the prompt to verify results

---

### Contributing with AI Assistance

---

#### Option 1: Traditional PR with AI Prompt Disclosure

Submit code as usual, but include the AI prompt in the PR template's "AI Prompt" section. This helps reviewers understand your approach and intent.

---

#### Option 2: Prompt Request (Prompt-Only)

Create an issue using the **Prompt Request** template if you:
- Have a well-crafted prompt but haven't run it yet
- Want feedback on your approach before implementation
- Prefer maintainers to run and merge the prompt themselves
