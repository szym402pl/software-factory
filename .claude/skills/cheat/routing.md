# Phase 3 — Code cheat routing

Two things: fixed-mechanism sourcing by project type, and hybrid depth with user checkpoints.

**This phase is for fixed mechanisms only** (per PHILOSOPHY.md #5/#6 and the ladder in SKILL.md) — libraries, packages, stdlib functions that solve a well-defined, interchangeable sub-problem. It is not for finding whole apps or features to clone; that's prior-art research (Phase 2, → [[prior-art-ladder]]), and even there it's study-only, never adopted as code.

## Project-type → fixed-mechanism sources

Match your project. These surface *libraries and packages* — things you install as a dependency, not code you copy in. If what you actually need is architecture/approach inspiration for the project as a whole, that's Phase 2, not this list.

| Project type | Try in order | Looking for |
|---|---|---|
| **Website / landing page** | 1. Tailwind UI / shadcn/ui component primitives (copy-in UI primitives, not page/product structure) 2. npm: animation/form/validation libs as needed | Reusable UI primitives, not page structure |
| **Web app / SaaS** | 1. npm / PyPI: auth, billing, email, queue libs 2. `awesome-[stack]` for known-good libraries in that ecosystem | Libraries for auth/billing/etc., not the app itself |
| **CLI tool** | 1. npm / PyPI: argument-parsing, terminal-UI libs 2. `awesome-cli` for known-good CLI libraries | Libraries, not full CLI clones |
| **API / backend** | 1. npm / PyPI: validation, ORM, auth middleware libs 2. Postman / OpenAPI specs — as a reference for conventions, not code | Libraries for cross-cutting concerns |
| **Data pipeline / ETL** | 1. npm / PyPI: connector/transform libs 2. Prefect / Airflow / Dagster — as orchestration dependencies if already adopted | Libraries and orchestration tools |
| **Mobile app** | 1. npm (React Native) / pub.dev (Flutter): navigation, state, native-bridge libs | Libraries, not full app clones |
| **Library / SDK** | 1. npm / PyPI / crates.io: `[domain]` — is this mechanism itself already a published, well-maintained package? 2. `[function] polyfill` / `[function] implementation` for a narrow missing piece | Whether the whole mechanism already exists as a dependency |
| **Dashboard / admin panel** | 1. Tabler / AdminLTE / shadcn blocks (UI primitives) 2. npm: charting/table libs | Reusable UI primitives, not full panel structure |
| **Documentation site** | 1. Starlight / Docusaurus / Mintlify — as the doc-generation dependency itself, config-driven | The doc tool as a dependency, not hand-built docs |
| **Browser extension** | 1. npm: extension-manifest/messaging helper libs | Libraries for the extension APIs |
| **Game** | 1. Godot / Unity asset store: art/audio assets, physics/math libs 2. Well-established algorithm libs (pathfinding, collision) | Libraries and assets, not full game clones |
| **AI / ML app** | 1. Hugging Face / Replicate: is the model itself the fixed mechanism you need? 2. LangChain / LlamaIndex as orchestration dependencies if already adopted | Models and orchestration libraries |
| **Chatbot / agent** | 1. npm / PyPI: platform SDKs (Slack, Discord, Telegram) 2. LangChain / LlamaIndex if already adopted | Platform SDKs, not full bot clones |
| **Desktop app** | 1. npm: Electron/Tauri plugin ecosystem for native OS integration | Plugins for OS-level mechanisms |

## Hybrid depth

Start shallow. Go deeper only if needed. User checkpoint at each escalation.

```
quick-scan (mental, free)
    ↓
  Obvious fixed mechanism, known library? → done. Verdict: "Use X."
    ↓ nothing obvious OR "not quite right"
standard (2-3 searches, ~30s)
    ↓
  Found something? → "Found X, Y, Z. Use one, or is this actually our own logic to build?"
    ↓ nothing found OR user wants deeper
deep (6-10 searches, full landscape)
    ↓
  Verdict: our own logic — build it | Fixed mechanism — use library X | Investigate further
```

**Rule:** Never jump to deep because it "feels thorough." Most sub-problems are NOT novel mechanisms. Quick-scan costs 0. Standard covers 80%. Deep is for unclear cases (is this actually a fixed mechanism, or did it just look like one?).

**Checkpoint script:** "Found [N] library options. [Best one in one line]. Use it, or is this actually specific enough to our product that we should build it ourselves?"

## Source registry

What each source is good for — so you know WHERE to look for fixed mechanisms, not just that you should.

| Source | Best for | Not for |
|--------|----------|---------|
| **npm / PyPI / crates.io** | Libraries, tools, SDKs — the actual dependency to install | Full apps, our own product logic |
| **GitHub (code search, not clones)** | Finding which library solves a mechanism, reading a library's own source when docs are thin | Cloning whole projects/features |
| **awesome-* lists** | Curated landscape of libraries for an ecosystem | Implementation details, full apps |
| **Hugging Face / Replicate** | ML models as the fixed mechanism itself | Production backend logic |
| **Stack Overflow** | Specific technical problems with a library/API | "What should I build?" |
| **arXiv** | Novel algorithms, academic state-of-art (research the algorithm, then implement it ourselves or find a library that already does) | Production-ready code to copy |
| **AlternativeTo / opensourcealternative.to** | Discovering whether a whole mechanism (e.g. "self-hosted analytics") already exists as an installable tool | Niche/novel projects, our own product |
