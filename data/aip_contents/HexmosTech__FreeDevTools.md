### 4. Generate Pages for Your Tool

```bash
make gen tool=gemini-schema-validator
```

![image](https://hackmd.io/_uploads/BkVEO4F2lx.png)

---

## Astro Project Structure

```
freedevtools/
├── frontend/                 # Astro frontend application
│   ├── src/
│   │   ├── components/      # React components
│   │   ├── pages/           # Pages
│   │       ├── t/           # Tool directory
│   │           ├── gemini-schema-validator/
│   │               ├── index.astro
│   │               ├── _GeminiSchemaValidator.tsx
│   │               ├── _GeminiSchemaValidatorSkeleton.tsx
│   ├── config/              # Config files
│   ├── styles/              # CSS and styling
│   ├── public/              # Static assets
│   └── package.json         # Dependencies
├── backend/                 # Backend services (coming soon)
├── .github/                 # GitHub workflows
├── LICENSE                  # MIT License
└── README.md                # Documentation
```

---

### <mark>AI Rules (Cursor, Copilot, etc.)</mark>

- AI can be used, but always take suggestions from Admins(discord link below), we prefer quality over quantitiy.
- Ensure generated code follows project conventions
- **Include `seo.md` in your workflow** to define and improve **titles, descriptions, and keywords** when starting to build a tool
- **Always include `design.md` in your workflow** for **consistent styling and shared UI/UX rules**
