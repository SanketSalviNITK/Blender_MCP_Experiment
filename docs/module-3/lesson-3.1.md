# Lesson 3.1 — What is an Agent? How Claude Breaks Down Tasks

## Learning Goals
- Understand the difference between conversational and agentic Claude
- Learn the agent loop: Observe → Think → Act → Check → Repeat
- See task decomposition in action on a real Blender scene
- Understand the three levels of autonomy

---

## Conversational vs Agentic Mode

| Mode | You say | Claude does |
|------|---------|-------------|
| **Conversational** | "Rotate the table 5°" | Executes exactly that instruction |
| **Guided** | "Make the lamp look more realistic" | Interprets goal, picks approach, executes |
| **Autonomous** | "Add a side table to the scene" | Observes, plans, builds, verifies — all independently |

Modules 1–2 were conversational. Module 3 is autonomous.

---

## The Agent Loop

```
┌─────────────────────────────────────────┐
│  OBSERVE — read the current scene state │
│  THINK   — what needs to happen next?   │
│  ACT     — execute one concrete step    │
│  CHECK   — did it work? any issues?     │
│  REPEAT  — loop until goal is reached   │
└─────────────────────────────────────────┘
```

Each iteration of the loop calls tools:
- **OBSERVE** → `blender_cmd.py` to read scene state
- **THINK** → Claude reasons about the data (printed as comments)
- **ACT** → `blender_cmd.py` to execute a change
- **CHECK** → `blender_cmd.py` to verify the result

---

## What the Agent Decided — Side Table Example

**Brief given:**
> *"Add a small side table to the scene."*

**What the agent observed:**
- Dining table: 3.0 x 1.5m, top at Z=0.78
- Scene X span: -3.8 (lamp) to +1.38 (table edge)
- Right side (X ≈ 2.8) is empty and visible from camera

**What the agent decided:**
- Position: X=2.8, Y=0 (right side, in camera frame)
- Size: 0.6 x 0.4 x 0.55m (proportionate — not competing with dining table)
- Height: 0.55m (standard side table, shorter than dining table at 0.78m)
- Material: WalnutWood (reuse existing — visual consistency)
- Legs: 0.04m square (thinner than dining table legs at 0.08m — appropriate scale)

**What the agent verified:**
- Top Z = 0.550 ✅
- All 4 legs exist ✅
- WalnutWood material assigned ✅
- Gap from dining table = 0.94m (no overlap) ✅
- Placed in DiningSet collection ✅

---

## Why "Think Out Loud" Matters

When the agent prints its reasoning:
```python
print("""
Decision: Place side table at X=2.8 (right side, visible from camera)
Why: dining table occupies X=-1.5 to +1.5, lamp at X=-3.8.
     Right side is empty and within camera frame.
""")
```

This is called **chain-of-thought reasoning** — and it does two things:

1. **Makes decisions auditable** — you can see WHY it made each choice
2. **Improves accuracy** — writing out the reasoning catches logical errors
   before acting on them

An agent that acts silently is a black box. An agent that narrates is a
collaborator you can correct.

---

## The Three Levels of Autonomy

### Level 1 — Instructed
```
You: "Rotate DiningTable 5 degrees on Z."
Claude: [executes exactly that]
```
Best for: Precise adjustments, known transformations, final tweaks.

### Level 2 — Guided
```
You: "The lamp looks too dim. Fix it."
Claude: [reads current energy, estimates appropriate increase, applies, verifies]
```
Best for: Improvements with a clear direction but no exact spec.

### Level 3 — Autonomous
```
You: "Add some furniture to fill out the right side of the scene."
Claude: [observes scene, decides what furniture, sizes, positions, builds, verifies]
```
Best for: Creative/compositional decisions where you trust Claude's judgement.

---

## When to Use Each Level

| Situation | Level | Why |
|-----------|-------|-----|
| Final exact position of hero prop | 1 | Too important to guess |
| "Make the wall material rougher" | 1–2 | Simple change, you know the direction |
| "Add background detail to fill the scene" | 3 | Creative, low-stakes |
| "Debug why the mug is floating" | 2 | Agent needs to investigate first |
| "Build a completely new room" | 3 | Agent plans the whole thing |

---

*Lesson 3.1 — June 2026*
