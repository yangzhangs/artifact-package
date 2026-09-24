## Adding new features

We recommend using GitHub Copilot Agent mode when adding new features,
as this project includes an [AGENTS.md](AGENTS.md) file
that instructs Copilot (and other coding agents) about how to generate code for common code changes.

If you are not using Copilot Agent mode, consult both that file and suggestions below.

---

### Adding new azd environment variables

When adding new azd environment variables, please remember to update:

1. [main.parameters.json](./infra/main.parameters.json)
1. [appEnvVariables in main.bicep](./infra/main.bicep)
1. [ADO pipeline](.azdo/pipelines/azure-dev.yml).
1. [Github workflows](.github/workflows/azure-dev.yml)

---

### Adding new UI strings

When adding new UI strings, please remember to update all translations.
For any translations that you generate with an AI tool,
please indicate in the PR description which language's strings were AI-generated.

Here are community contributors that can review translations:

| Language | Contributor         |
|----------|---------------------|
| Danish   | @EMjetrot           |
| French   | @manekinekko        |
| Japanese | @bnodir             |
| Norwegian| @@jeannotdamoiseaux |
| Portugese| @glaucia86          |
| Spanish  | @miguelmsft         |
| Turkish  | @mertcakdogan       |
| Italian  | @ivanvaccarics      |
| Dutch    |                     |
| Polish   | @michuhu            |
