# Contributing Guide

Thank you for your interest in contributing!

## AI Usage

The Databuddy project has strict rules for AI usage. Please see
the [AI Usage Policy](AI_POLICY.md). **This is very important.**

## 🚀 Getting Started

### Installation

1. Clone the repository:

```bash
git clone https://github.com/databuddy-analytics/Databuddy.git
cd databuddy
```

2. Install dependencies:

```bash
bun install
```

3. Set up environment variables:

```bash
cp .env.example .env
```

4. Start Docker services (PostgreSQL, Redis, ClickHouse):

```bash
docker compose up -d
```

> **Note:** This starts the **development** infrastructure only (`docker-compose.yaml`).
> For self-hosting with all application services, use `docker compose -f docker-compose.selfhost.yml up -d` instead — see the [Self-Hosting section](README.md#-self-hosting) in the README.

5. Set up the database:

```bash
bun run db:push        # Apply database schema
bun run clickhouse:init # Initialize ClickHouse basket
```

6. Build the SDK:

```bash
bun run sdk:build
```

7. Start development servers:

```bash
bun run dev:dashboard
```

8. Seed the database with sample data (optional):

```bash
bun run db:seed <WEBSITE_ID> [EVENT_COUNT]
```

**Examples:**

```bash
bun run db:seed g0zlgMtBaXzIP1EGY2ieG 10000
bun run db:seed d7zlgMtBaSzIL1EGR2ieR 5000
```

**Note:** 
- The domain is automatically fetched from the database based on the website ID
- Default event count is 10,000 if not specified
- Seeds events, outgoing links, errors, and web vitals data
- You can find your website ID in your website overview settings

## 💻 Development

### Available Scripts

Check the root `package.json` for available scripts. Here are some common ones:

- `bun run dev` - Start all applications in development mode
- `bun run build` - Build all applications
- `bun run start` - Start all applications in production mode
- `bun run lint` - Lint all code with Ultracite
- `bun run format` - Format all code with Prettier
- `bun run check-types` - Type check all TypeScript code
- `bun run db:studio` - Open Drizzle Studio for database management
- `bun run db:push` - Apply database schema changes
- `bun run db:migrate` - Run database migrations
- `bun run db:deploy` - Deploy database migrations
- `bun run sdk:build` - Build the SDK package
- `bun run email:dev` - Start the email development server

You can also `cd` into any package and run its scripts directly.

### Development Workflow

1. Create a new branch:

```bash
git checkout -b feature/your-feature
```

2. Make your changes

3. Run tests:

```bash
bun run test
```

4. Create a changeset:

```bash
bun run changeset
```

5. Commit your changes:

```bash
git add .
git commit -m "feat: your feature"
```

6. Push your changes:

```bash
git push origin feature/your-feature
```

Note: Open a pull request to the STAGING branch

7. Create a Pull Request


## Code Style

- Use Biome for linting and formatting
- Follow the coding standards in the README
- Keep it simple and type-safe

---

# Standalone AI policy file

# AI Usage Policy

The Databuddy project has strict rules for AI usage:

- **All AI usage in any form must be disclosed.** You must state
  the tool you used (e.g. Claude Code, Cursor, GitHub Copilot, ChatGPT) along with
  the extent that the work was AI-assisted.

- **Pull requests created in any way by AI can only be for accepted issues.**
  Drive-by pull requests that do not reference an accepted issue will be
  closed. If AI isn't disclosed but a maintainer suspects its use, the
  PR will be closed. If you want to share code for a non-accepted issue,
  open a discussion or attach it to an existing discussion.

- **Pull requests created by AI must have been fully verified with
  human use.** AI must not create hypothetically correct code that
  hasn't been tested. Importantly, you must not allow AI to write
  code for platforms or environments you don't have access to manually
  test on.

- **Issues and discussions can use AI assistance but must have a full
  human-in-the-loop.** This means that any content generated with AI
  must have been reviewed _and edited_ by a human before submission.
  AI is very good at being overly verbose and including noise that
  distracts from the main point. Humans must do their research and
  trim this down.

- **No AI-generated media is allowed (art, images, videos, audio, etc.).**
  Text and code are the only acceptable AI-generated content, per the
  other rules in this policy.

- **Bad AI drivers will be banned and ridiculed in public.** You've
  been warned. We love to help junior developers learn and grow, but
  if you're interested in that then don't use AI, and we'll help you.
  I'm sorry that bad AI drivers have ruined this for you.

These rules apply only to outside contributions to Databuddy. Maintainers
are exempt from these rules and may use AI tools at their discretion;
they've proven themselves trustworthy to apply good judgment.

## There are Humans Here

Please remember that Databuddy is maintained by humans.

Every discussion, issue, and pull request is read and reviewed by
humans (and sometimes machines, too). It is a boundary point at which
people interact with each other and the work done. It is rude and
disrespectful to approach this boundary with low-effort, unqualified
work, since it puts the burden of validation on the maintainer.

In a perfect world, AI would produce high-quality, accurate work
every time. But today, that reality depends on the driver of the AI.
And today, most drivers of AI are just not good enough. So, until either
the people get better, the AI gets better, or both, we have to have
strict rules to protect maintainers.

## AI is Welcome Here

Databuddy is written with plenty of AI assistance, and many maintainers embrace
AI tools as a productive tool in their workflow. As a project, we welcome
AI as a tool!

**Our reason for the strict AI policy is not due to an anti-AI stance**, but
instead due to the number of highly unqualified people using AI. It's the
people, not the tools, that are the problem.

I include this section to be transparent about the project's usage about
AI for people who may disagree with it, and to address the misconception
that this policy is anti-AI in nature.

---

_This policy is adapted from the [Ghostty project's AI Usage Policy](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md), originally created by [mitchellh](https://github.com/mitchellh) and the Ghostty team. Thanks for setting the standard._

