# Phase 3 — Code cheat routing

Two things: project type → cheat surfaces, and hybrid depth with user checkpoints.

## Project-type → cheat surfaces

Match your project. Follow the sequence. Different types have different cheat surfaces — the creative ladder already covered design/structure/approach theft. This is for the code hunt.

| Project type | Try in order | Looking for |
|---|---|---|
| **Website / landing page** | 1. Dribbble / Awwwards (design already stolen in Phase 2) 2. Tailwind UI / shadcn blocks 3. GitHub: `[name] landing page` | Layout components, existing pages |
| **Web app / SaaS** | 1. GitHub: `[name] clone`, `awesome-selfhosted` 2. ProductHunt: recent launches 3. `X alternative open source` 4. `[stack] saas template` | Existing apps, clones, templates |
| **CLI tool** | 1. npm / PyPI: keyword search 2. GitHub: `[name]-cli`, `awesome-cli` 3. Homebrew: search formulas | Existing tools, CLI structure |
| **API / backend** | 1. GitHub: `[domain]-api`, `awesome-[stack]` 2. Postman / OpenAPI specs 3. `[domain] backend open source` | Existing implementations |
| **Data pipeline / ETL** | 1. GitHub: `[source]-to-[target]`, `awesome-data-engineering` 2. Prefect / Airflow / Dagster templates | Existing pipelines |
| **Mobile app** | 1. GitHub: `[name] clone react-native` 2. Expo / Flutter templates 3. App Store / Play Store: competitor features | Existing apps, templates |
| **Library / SDK** | 1. npm / PyPI / crates.io: `[domain]` 2. GitHub: `[language] [domain]`, `awesome-[domain]` 3. `[function] polyfill` / `[function] implementation` | Existing implementations |
| **Dashboard / admin panel** | 1. GitHub: `admin dashboard [stack]` 2. Tabler / AdminLTE / shadcn blocks 3. Retool / Appsmith / Budibase: check free tier | Existing panels, templates |
| **Documentation site** | 1. Starlight / Docusaurus / VuePress themes 2. Mintlify / GitBook: check free tier 3. GitHub: `docs template [stack]` | Structure, templates |
| **Browser extension** | 1. GitHub: `[name] extension` 2. Chrome Web Store: competitor extensions 3. `[stack] extension starter` | Existing extensions |
| **Game** | 1. GitHub: `[genre] game open source` 2. itch.io: open-source tag 3. Godot / Unity asset store free 4. `[classic game] clone [engine]` | Existing games, engines |
| **AI / ML app** | 1. Hugging Face Spaces: search by task 2. Replicate: explore models 3. GitHub: `[domain] AI`, `awesome-[domain]-ai` 4. Vercel AI templates, LangChain examples | Existing apps, models |
| **Chatbot / agent** | 1. GitHub: `[platform] bot [domain]` 2. Discord Bot List / Slack App Directory 3. Botpress / Rasa / Botkit examples 4. LangChain / LlamaIndex cookbook | Existing bots, frameworks |
| **Desktop app** | 1. GitHub: `[name] electron`, `[name] tauri` 2. AlternativeTo: `[app name] open source` 3. `[app name] clone [framework]` | Existing apps, clones |

## Hybrid depth

Start shallow. Go deeper only if needed. User checkpoint at each escalation.

```
quick-scan (mental, free)
    ↓
  Found something obvious? → done. Verdict: "Use X."
    ↓ nothing obvious OR "not quite right"
standard (2-3 searches, ~30s)
    ↓
  Found something? → "Found X, Y, Z. Use one? Or go deeper?"
    ↓ nothing found OR user wants deeper
deep (6-10 searches, full landscape)
    ↓
  Verdict: Build | Fork | Contribute | Use | Investigate
```

**Rule:** Never jump to deep because it "feels thorough." Most projects are NOT novel. Quick-scan costs 0. Standard covers 80%. Deep is for genuinely uncharted territory.

**Checkpoint script:** "Found [N] options. [Best one in one line]. Want to go deeper or run with this?"

## Source registry

What each source is good for — so you know WHERE to cheat, not just that you should.

| Source | Best for | Not for |
|--------|----------|---------|
| **GitHub** | Clones, implementations, structure, libraries | Design, visual approach |
| **npm / PyPI / crates.io** | Libraries, tools, SDKs | Full apps usually |
| **Dribbble / Behance** | Visual design, layout, UX patterns | Code, implementation |
| **Awwwards** | Full-site design, structure, case studies | Code |
| **ThemeForest / Creative Market** | Design reference, layout theft | Buying usually (just screenshot) |
| **ProductHunt** | Recent launches, what's shipping, approach | Mature/stable implementations |
| **awesome-* lists** | Curated landscape, "what exists" | Implementation details |
| **Hugging Face / Replicate** | ML models, AI demos, approach | Production backends |
| **YouTube** | Approach, workflow, architecture decisions | Production code |
| **HN / Reddit** | User sentiment, what failed, honest reviews | Structured data, completeness |
| **Stack Overflow** | Specific technical problems | "What should I build?" |
| **arXiv** | Novel algorithms, academic state-of-art | Production-ready code |
| **AlternativeTo / opensourcealternative.to** | Open-source replacements for paid tools | Niche/novel projects |
| **Landing page galleries** | Design patterns, layout inspiration | Code, functionality |
| **WordPress theme demos** | Structure, layout, content organization | Modern web apps usually |
| **Discord Bot List / Slack App Directory** | Existing bot functionality, UX patterns | Code quality |
| **Expo / Flutter templates** | Mobile app structure, navigation patterns | Backend logic |
