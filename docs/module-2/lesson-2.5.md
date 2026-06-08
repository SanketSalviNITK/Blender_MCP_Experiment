# Lesson 2.5 — PE: Chain-of-Thought Prompts

## Learning Goals
- Understand why prompt structure determines output quality
- Learn the 4 core CoT patterns for Blender work
- Practice each pattern on the real scene
- Build a personal prompt template library

---

## What is Chain-of-Thought Prompting?

Chain-of-Thought (CoT) means **structuring your prompt so that reasoning
happens in explicit, ordered steps** rather than one undifferentiated block.

Claude is an autoregressive model — it reads left to right, builds context
as it goes. A well-structured prompt forces Claude to:
1. Gather information before acting
2. Act one step at a time (not everything at once)
3. Verify after acting

This dramatically reduces errors, hallucinations, and missed steps.

---

## The Problem With Vague Prompts

| Prompt Quality | Example | Problem |
|---------------|---------|---------|
| Too vague | "Make the scene look better" | Claude guesses the goal |
| Too dense | "Move mug, fix materials, add light, rename everything" | Claude loses track mid-way |
| No verification | "Rotate the table 5 degrees" | No way to confirm it worked |
| No context | "Fix the floating object" | Claude doesn't know which one |

---

## The 4 Core CoT Patterns

---

### Pattern 1 — Inspect → Act → Verify

**Use when:** Making changes to existing state.  
**The rule:** Never modify what you haven't read first.

```
STEP 1 — INSPECT:
  Read the current [material/transform/light] values for [objects].
  Print them so I can see the before state.

STEP 2 — ACT:
  Change [specific property] from [old value] to [new value].
  Only touch what I specified — leave everything else alone.

STEP 3 — VERIFY:
  Re-read the same properties.
  Print PASS if the change was applied, FAIL if not.
```

**Real example from this lesson:**
```
STEP 1 — INSPECT: Print WalnutWood material: color, roughness
STEP 2 — ACT: Darken WalnutWood to (0.09, 0.045, 0.015), roughness 0.82
STEP 3 — VERIFY: Re-read WalnutWood and confirm new values. PASS/FAIL.
```
→ Result: PASS. Deterministic, auditable, no surprises.

---

### Pattern 2 — Plan → Execute → Report

**Use when:** Making multiple changes in one go.  
**The rule:** State the full plan first, then execute, then summarise.

```
PLAN: I will make these N changes:
  1. [Object A] — [what will change]
  2. [Object B] — [what will change]
  3. [Object C] — [what will change]

EXECUTE: Apply all changes. Print each as it happens.

REPORT: Summarise what changed:
  [Object] | [property] | [before] -> [after] | DONE
```

**Why print-as-you-go?** If Claude crashes mid-execution (or the TCP bridge
drops), you can see exactly which changes landed and which didn't.

---

### Pattern 3 — Decompose → Build → Assemble

**Use when:** Creating a complex object from parts.  
**The rule:** Never try to build everything in one go.

```
DECOMPOSE: Break [complex object] into primitive parts:
  - Part A: [shape, dimensions, position]
  - Part B: [shape, dimensions, position]
  - Part C: [shape, dimensions, position]

BUILD: Create each part individually using bmesh.
  After each part: verify it exists and is at the right position.

ASSEMBLE: Parent all parts to Part A (the root object).
  Verify the hierarchy: parent → [child, child, child]
```

**Real example:** The coffee mug was built this way:
1. Decompose → outer cylinder + inner cylinder + torus handle
2. Build → CoffeeMug (hollow bmesh), MugHandle (torus ring)
3. Assemble → both objects at same XY centre, handle on +X side

---

### Pattern 4 — Hypothesise → Test → Fix

**Use when:** Debugging something wrong in the scene.  
**The rule:** State your hypothesis before testing it.

```
HYPOTHESIS: I think [object] is floating because [reason].

TEST: Check [specific property] to confirm or deny:
  - Print [object].location
  - Print [object] vertex world Z coordinates
  - Compare against expected value [X]

FIX (only if hypothesis confirmed):
  - If vertices are at wrong Z: rebuild with bmesh at correct Z
  - If location is offset: reset location to (x, y, correct_z)
  - Do NOT change anything until the test confirms the issue
```

**Real example from Lesson 1.5:**
- Hypothesis: "RedBook is floating because vertices were baked at wrong Z"
- Test: print `[(obj.matrix_world @ v.co).z for v in obj.data.vertices]`
- Result: Z=0.84 confirmed → rebuild with z0=0.78 baked into bmesh

---

## The Universal Blender CoT Template

```
## GOAL
[What you want the final result to look like — one sentence]

## CONSTRAINTS
- Do NOT use transform_apply (TCP bridge issue)
- Do NOT modify objects not listed below
- All positions in world coordinates (metres)

## STEPS

STEP 1 — READ STATE:
  Print current values for: [list objects/properties]

STEP 2 — [ACTION NAME]:
  [Specific change with exact values]
  Print confirmation as each item is done.

STEP 3 — [NEXT ACTION]:
  [Next specific change]
  Print confirmation.

STEP N — VERIFY:
  Re-read all changed properties.
  Print PASS/FAIL for each.
  Print final summary: N/N checks passed.
```

---

## Prompt Length vs Prompt Quality

A common mistake: thinking shorter prompts are better prompts.

| Prompt | Length | Quality | Why |
|--------|--------|---------|-----|
| "Make it look nice" | 5 words | Very low | Undefined goal |
| "Rotate table 5 degrees on Z" | 7 words | Medium | No verify, no context |
| "Rotate DiningTable 5 deg on Z. Verify all 4 legs follow (world Z = 5deg). Print PASS/FAIL." | 22 words | High | Clear, scoped, verified |

**The sweet spot:** Long enough to eliminate ambiguity, short enough to stay focused.
A 50-word prompt with clear steps beats a 200-word dump of requirements.

---

## Prompt Engineering Rules from Module 2

| Rule | Why It Matters |
|------|---------------|
| Always inspect before modifying | You can't fix what you haven't measured |
| State constraints explicitly | "do NOT use transform_apply" prevents a known bug |
| Print as you go | Crash recovery — see what landed |
| Verify with PASS/FAIL | Forces Claude to check its own work |
| One goal per step | Multi-goal steps get partially done |
| Use world coordinates | Local coordinates are meaningless without context |
| Name the technique | "use bmesh world-coordinate pattern" invokes learned knowledge |

---

*Lesson 2.5 — June 2026*
