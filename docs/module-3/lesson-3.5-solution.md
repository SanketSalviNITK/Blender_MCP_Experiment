# Lesson 3.5 — Solution & Notes
## PE: Writing Agentic Briefs

## What We Built
Executed a full agentic brief: "make the scene feel lived-in."
Agent observed, planned, built 4 human-touch props, verified 10/10 checks.

---

## The Brief That Drove This Run

```
INTENT: Make the scene feel lived-in and inhabited. Add small human
touches — things people actually leave around. Keep it subtle: nothing
distracts from the dining table as hero.

SCOPE:
  Touch: side table surface, floor between tables, bookshelf shelf gaps
  Leave alone: camera, WindowLight, CoffeeMug, RedBook, DiningTable, legs

CONSTRAINTS:
  - X=-4 to X=4
  - Nothing > 0.5m tall on tables
  - Everyday domestic objects only
  - New props into DiningSet or Bookshelf collection

VERIFICATION:
  - All 4 props exist
  - Protected objects untouched
  - All within X bounds
  - Collections assigned
  Final: 10/10 checks passed
```

---

## Agent's Decisions

| Prop | Position | Reasoning |
|------|----------|-----------|
| LinenNapkin | Side table, right of plant | "Folded cloth on side table = someone uses this room" |
| GlassesCase | Side table, front edge | "Implies a specific person lives here — personal item" |
| LoosePaper | Floor at X=1.85, 15deg | "Universal human mess — all real floors have stray paper" |
| Candle | Bookshelf shelf 2, X=0.45 | "Books + candle = intimate inhabited reading shelf" |

All 4 props are **narrative objects** — each one implies a human story.
That's the difference between a 3D model and a real room.

---

## Verification Results

```
[PASS] All 4 props exist
[PASS] DiningTable untouched (Z rot=5.0)
[PASS] WindowLight untouched (energy=600.0)
[PASS] LinenNapkin within X bounds [2.9, 3.1]
[PASS] GlassesCase within X bounds [2.6, 2.7]
[PASS] LoosePaper within X bounds [1.6, 2.0]
[PASS] Candle within X bounds [0.4, 0.5]
[PASS] LinenNapkin height 0.005m (< 0.5m)
[PASS] GlassesCase height 0.025m (< 0.5m)
[PASS] Props assigned to collections
10/10 checks passed
```

---

## Module 3 Complete — All Patterns Together

| Lesson | Concept | Applied Here |
|--------|---------|-------------|
| 3.1 | Agent loop | Observe → Think → Act → Check → Report |
| 3.2 | Multi-step build | 4 props in sequence, each verified |
| 3.3 | TaskCreate | Task #6 tracked the full run |
| 3.4 | Guide vs. autonomous | Protected list + free zones |
| 3.5 | Agentic brief | All 4 layers in one prompt |

---

## Final Scene State

| Collection | Objects |
|-----------|---------|
| Environment | 2 |
| DiningSet | 16 (+ napkin, case, paper) |
| Lamp | 4 |
| Lighting | 4 |
| Cameras | 1 |
| Bookshelf | 27 (+ candle) |
| **Total** | **62** |

---

*Completed: June 2026 — Module 3 complete!*
