# HTML Report Scaffold

Self-contained HTML file. Tailwind and Mermaid from CDN. No other scripts.

## Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Architecture Review — <repo> — <date></title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
</head>
<body class="bg-white text-gray-900 font-sans antialiased">
  <main class="max-w-4xl mx-auto px-6 py-12">
    <!-- Header -->
    <!-- Candidates -->
    <!-- Top Recommendation -->
  </main>
</body>
</html>
```

## Header

- Repo name, date.
- Legend: solid box = module, dashed line = seam, red arrow = leakage, thick dark box = deep module.
- No intro paragraph — the diagrams carry the message.

## Candidate cards

Each is one `<article>`:

- **Title** — short, describes the deepening (e.g. "Extract PaymentGateway adapter")
- **Badge row** — recommendation strength (`Strong` = emerald, `Worth exploring` = amber, `Speculative` = slate) + dependency category tag
- **Files** — monospaced list of involved files/modules
- **Before/After diagram pair** — side by side. Before shows the shallowness/leakage; after shows the deepened module
- **Problem** — one sentence
- **Solution** — one sentence
- **Wins** — bullet list, each under 6 words, naming glossary gains ("locality: bugs concentrate in one module")
- **ADR callout** (optional) — amber warning when contradicting an ADR

No explanatory paragraphs. If the diagram needs a paragraph to be understood, redraw the diagram.

## Diagram patterns

Mix approaches — don't default to Mermaid for everything.

### Mermaid (graph-shaped relationships)
Use `mermaid` code blocks for dependency call flows. Style with classDef: red for leakage, dark/thick for the deep module. Wrap in a Tailwind-styled card.

### Hand-built boxes-and-arrows
When Mermaid layout fights — thick-bordered deep module with greyed-out internals, side-by-side comparison. Inline SVG or absolutely-positioned divs.

### Cross-section
Horizontal bands showing layers a call passes through. Before: many bands. After: few bands, complexity hidden.

### Mass diagram
Interface rectangle vs implementation rectangle. Before: big interface, small impl. After: small interface, big impl.

### Call-graph collapse
Before: nested call tree reaching across modules. After: one box with faded internal calls behind the interface.

## Style

- Editorial, generous whitespace.
- Serif optional for headings.
- Colour sparingly — one accent, red for leakage, amber for warnings.
- Diagrams ~320px tall.
- Module labels: `text-xs uppercase tracking-wider`.
- No scripts beyond the two CDNs.

## Vocabulary

Exactly the `/codebase-design` terms: module, interface, implementation, depth, deep, shallow, seam, adapter, leverage, locality.

Forbidden: component, service, unit (for module); API, signature (for interface); boundary (for seam); layer, wrapper (for module).

## Wins bullets

Name the glossary gain, not vague praise:
- Good: "locality: bugs concentrate in one module"
- Bad: "easier to maintain"
- Good: "leverage: one `charge()` call replaces 5-step manual flow"
- Bad: "cleaner code"
