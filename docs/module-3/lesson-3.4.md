# Lesson 3.4 — When to Guide vs. When to Let the Agent Run

## Learning Goals
- Use the 4-question framework to place any task on the guide↔autonomous spectrum
- Understand the 5 autonomy categories and when to use each
- Write guardrails that give autonomy without losing control
- Recognise which parts of a scene are "hero" (guide) vs. "background" (autonomous)

---

## The Core Spectrum

```
GUIDE ←──────────────────────────────────────→ AUTONOMOUS
"Rotate table     "Make the lamp      "Add background
 exactly 5° Z"     look more natural"   furniture to
                                         fill the room"
```

Too far left = you're micromanaging. Too far right on a critical task = broken deliverable.
**The skill is placing each task correctly.**

---

## The 4-Question Framework

Ask these before deciding how much autonomy to give:

| Question | YES → | NO → |
|----------|-------|------|
| Is there a single correct answer? | Guide — specify it | Autonomous — let Claude decide |
| Is a mistake hard to undo? | Guide — be explicit | Autonomous — can always revert |
| Does it require taste/creativity? | Autonomous — Claude's strength | Guide — you have the exact spec |
| Does it affect the hero/focal object? | Guide — too important to guess | Autonomous — background detail |

---

## The 5 Autonomy Categories

### Category 1 — Always Guide
**One correct answer. Wrong answer is hard to undo.**

Examples:
- Final camera position for a client deliverable
- Hero prop exact material colour
- Render resolution and output format
- Architectural joint dimensions

```
❌ "Position the camera nicely"
✅ "Camera: (5, -5.8, 2.4), 85mm, f/1.8, focused on mug — exactly this"
```

### Category 2 — Guide With Range
**You know the direction, not the exact value.**

```
✅ "Make the floor warmer — colour between (0.35,0.32,0.28) and (0.42,0.38,0.30).
    Keep roughness unchanged."
```
Agent picks within your range. You set the floor and ceiling.

**This lesson's example:** Floor colour shifted from (0.35,0.32,0.28) → (0.38,0.35,0.29).
Warmer, within range, roughness unchanged.

### Category 3 — Guided Autonomy
**You name the problem. Agent diagnoses and fixes it.**

```
✅ "The scene feels flat. Add some warmth to the wall."
```
Agent reads current wall state, decides what to change (colour, not roughness),
picks an appropriate shift, applies, verifies.

**This lesson's example:** Wall shifted from (0.55,0.50,0.44) → (0.60,0.54,0.46).
Agent decided: colour is the issue, not texture.

### Category 4 — Full Autonomy
**Creative/compositional decisions. Agent decides everything.**

```
✅ "The scene needs a small decorative touch near the bookshelf."
```
Agent decides: what object (stacked floor books), where (X=-0.55, Y=6.48),
what size, what colours. All from spatial reasoning.

**This lesson's example:** 2 floor books placed near bookshelf base.
Agent reasoning: "stacked books on floor = lived-in detail, common in real rooms."

### Category 5 — Autonomous with Guardrails
**Full autonomy within explicit boundaries you set.**

```
✅ "Adjust any lights that need tweaking — but:
    - Do NOT touch WindowLight (calibrated)
    - Keep all energies under 300W
    - Warm colours only (R >= G >= B)"
```

Agent reads all lights, decides which to adjust, stays within guardrails.
**This lesson's example:** Only RimLight adjusted (180→200W). WindowLight untouched.

---

## Hero vs. Background Rule

The single most useful heuristic:

| Object Type | Autonomy Level | Why |
|-------------|----------------|-----|
| Hero props (mug, book, lamp) | 1 — Always Guide | Client specified, on camera, exact matters |
| Supporting objects (side table, shelf) | 3 — Guided Autonomy | General intent matters, exact less so |
| Background/fill (floor books, plant) | 4 — Full Autonomy | Detail work, Claude's spatial reasoning shines |
| Lights (key light) | 1 or 5 | Key light = calibrated, others = adjustable |
| Background lights (fill, rim) | 5 — Guardrails | Creative latitude, but constrain direction |
| Camera (deliverable shot) | 1 — Always Guide | Final frame is non-negotiable |

---

## Guardrail Patterns

Guardrails are constraints that give autonomy a safety net:

```
Spatial:    "Stay within X=-2 to X=2"
Scale:      "Nothing taller than 0.4m on the table"
Style:      "Match the walnut wood material"
Negative:   "Do NOT touch [object]"
Range:      "Energy between 50 and 200W"
Collection: "Add to DiningSet collection only"
```

Write guardrails for anything that could go catastrophically wrong.
Write nothing for everything else — that's where the agent adds value.

---

## PE Insight — The Autonomy Brief

Structure your brief to make the autonomy level explicit:

```
AUTONOMY LEVEL: [guided / autonomous / autonomous-with-guardrails]

GOAL: [one sentence]

CONSTRAINTS (guardrails):
  - [constraint 1]
  - [constraint 2]

FREE TO DECIDE:
  - [what Claude can choose]
  - [what Claude can choose]
```

This removes all ambiguity about how much freedom you're granting.

---

*Lesson 3.4 — June 2026*
