# Lesson 3.4 — Solution & Notes
## When to Guide vs. When to Let the Agent Run

## What We Covered
The 4-question framework for deciding autonomy level.
The 5 autonomy categories demonstrated live on the scene.
The hero-vs-background rule and guardrail pattern.

---

## Live Demonstrations

| Category | Task | Prompt | Result |
|----------|------|--------|--------|
| 1 — Always Guide | Render resolution | "1920x1080 @ 100%" | Exact spec applied |
| 2 — Guide with Range | Floor colour | "Warmer — between X and Y" | (0.38,0.35,0.29) — midpoint |
| 3 — Guided Autonomy | Wall warmth | "Scene feels flat, add warmth" | Colour shifted, roughness kept |
| 4 — Full Autonomy | Bookshelf detail | "Small decorative touch near shelf" | 2 floor books placed |
| 5 — Guardrails | Light tuning | "Adjust lights — not WindowLight, <300W" | Only RimLight tweaked |

---

## The 4-Question Cheatsheet

```
1. Single correct answer?  YES → Guide    NO → Autonomous
2. Hard to undo?           YES → Guide    NO → Autonomous
3. Requires creativity?    YES → Autono.  NO → Guide
4. Hero/focal object?      YES → Guide    NO → Autonomous
```

If 2+ answers say "Guide" → Guide it.
If 2+ answers say "Autonomous" → let it run.

---

## Hero vs. Background — Scene Map

```
Our dining scene:
  GUIDE EVERYTHING:
    → Camera position (final frame)
    → CoffeeMug material (hero prop)
    → DiningTable dimensions
    → WindowLight (calibrated key light)

  GUIDED AUTONOMY:
    → Wall and floor colour (mood, not exact)
    → SideTable position (general area)
    → Fill/Rim lights (direction given, values flexible)

  FULL AUTONOMY:
    → Floor books (background detail)
    → Plant on side table (decorative fill)
    → Bookshelf book colours (variety, not exact)
```

---

## The Autonomy Brief Template

```
AUTONOMY LEVEL: [1=always-guide / 2=range / 3=guided / 4=autonomous / 5=guardrails]

GOAL: [one sentence describing outcome]

CONSTRAINTS (if level 5):
  - Do NOT touch: [list]
  - Keep within: [range]
  - Style match: [existing material/pattern]

FREE TO DECIDE (if level 4/5):
  - Object type, position, scale
  - Colour (within palette)
  - Material (reuse existing or new)
```

---

## Rules Learned

1. **Hero objects get Level 1.** Never let the agent guess the exact position
   of the focal prop, the camera, or the key light.

2. **Background is Level 4.** Floor detail, shelf books, plant pots —
   trust the agent's spatial reasoning completely.

3. **Guardrails are not micromanagement.** "Do NOT touch WindowLight" is
   one constraint that protects a calibrated result while freeing everything else.

4. **Name the problem, not the solution.** "Scene feels flat" is better than
   "change wall roughness to 0.88" — unless you're certain that's the fix.

5. **The agent's reasoning is visible.** When the agent prints its analysis
   before acting, you can catch wrong reasoning before it executes.

---

*Completed: June 2026*
