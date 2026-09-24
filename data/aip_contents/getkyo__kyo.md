## Table of Contents

- [Contributing](#contributing)
  - [Getting Started](#getting-started)
  - [Configuring Java Options](#configuring-java-options)
  - [How to Build Locally](#how-to-build-locally)
  - [Adding a New API](#adding-a-new-api)
  - [LLM Use Guide](#llm-use-guide)
- [Core Principles](#core-principles)
- [API Design](#api-design)
  - [Naming](#naming)
  - [Types](#types)
  - [Method Signatures](#method-signatures)
- [Code Conventions](#code-conventions)
  - [Pending Type (A < S)](#pending-type-a--s)
  - [Scala Conventions](#scala-conventions)
  - [Documentation](#documentation)
  - [File Organization](#file-organization)
- [Optimization](#optimization)
  - [Performance](#performance)
  - [Zero-Cost Type Design](#zero-cost-type-design)
  - [Inline Guidelines](#inline-guidelines)
- [Testing](#testing)
  - [Framework](#framework)
  - [Base Trait Hierarchy](#base-trait-hierarchy)
  - [Test Patterns by Level](#test-patterns-by-level)
  - [Platform-Conditional Tests](#platform-conditional-tests)
  - [Compile-Time Tests](#compile-time-tests)
  - [Concurrent Test Helpers](#concurrent-test-helpers)
- [Unsafe Boundary](#unsafe-boundary)
  - [The Two-Tier API Pattern](#the-two-tier-api-pattern)
  - [Unsafe API Conventions](#unsafe-api-conventions)
  - [AllowUnsafe Tiers](#allowunsafe-tiers)
  - [AllowUnsafe for Zero-Allocation Side Effects](#allowunsafe-for-zero-allocation-side-effects)
  - [Closeable Resource Pattern](#closeable-resource-pattern)
  - [Close Method Convention](#close-method-convention)
  - [Local-Backed Service Pattern](#local-backed-service-pattern)
  - [KyoException Convention](#kyoexception-convention)
- [Effect Implementation Reference](#effect-implementation-reference)
  - [Anatomy of an Effect](#anatomy-of-an-effect)
  - [Delegation Pattern for Higher-Level Types](#delegation-pattern-for-higher-level-types)
  - [Isolate Protocol for Fiber-Crossing Operations](#isolate-protocol-for-fiber-crossing-operations)

---

### LLM Use Guide
We encourage contributors to leverage Large Language Models (LLMs) responsibly:
- Do **not** submit low-effort, AI-generated code without review.
- If you use AI assistance, ensure that the submission is well-tested and meets our standards.
- Automated PRs without human oversight may be closed.

---
