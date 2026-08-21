# Modular monolith with vertical slices

We build a single deployable application. This is a modular monolith. We organize `src/` in vertical slices by business capability. One folder holds one capability. Complex slices get ports and adapters at the seam. CRUD slices stay transaction scripts. A slice depends on shared infrastructure. A slice never depends on another slice. We enforce these boundaries with tooling.

We chose this shape for team growth and traffic. It avoids microservice overhead. The team breaking point is merge conflicts, not traffic. Real scaled codebases use an enforced monolith. AI-navigation is a context legibility strategy, not a pattern label. We keep the root CLAUDE.md lean and scope rules to directories.

## Considered options

- **Microservices** — rejected. Too much operational overhead for our scale.
- **Hexagonal or clean architecture in every slice** — rejected. Over-engineering for CRUD slices. Ports and adapters only where complexity varies.
- **Atomic-composable architecture** — rejected. Single source targets agent-building code. No evidence it improves AI navigation.
