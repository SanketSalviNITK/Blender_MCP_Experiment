# Lesson 3.5 — PE: Writing Agentic Briefs

## Learning Goals
- Write a brief that drives a full multi-step autonomous agent run
- Understand the 4 layers of an effective brief
- Distinguish intent, scope, constraints, and verification in a prompt
- See how briefs encode autonomy level implicitly through their structure

---

## What is an Agentic Brief?

A brief is a **single self-contained prompt** that an agent can execute
completely without you present for each step. Like a director's brief to a
crew — you describe the result, they figure out the technique.

### The 4 Layers

```
1. INTENT      — what feeling/result you want (the "why")
2. SCOPE       — what to touch and what to leave alone
3. CONSTRAINTS — guardrails that prevent bad outcomes
4. VERIFICATION — how the agent proves it worked
```

Every good brief has all 4. Missing any one layer causes problems:

| Missing layer | Result |
|--------------|--------|
| No INTENT | Agent does something technically correct but wrong mood |
| No SCOPE | Agent modifies protected hero objects |
| No CONSTRAINTS | Agent adds out-of-scale or off-style props |
| No VERIFICATION | Silent failures — floating objects, wrong colours |

---

## Brief Quality Spectrum

### Level 1 — Vague (avoid)
```
"Make the scene feel more cosy."
```
No scope, no constraints, no verification. Results are random.

### Level 2 — Over-specified (avoid)
```
"Change RimLight to 210W, wall to (0.61,0.55,0.47), add book at
 X=-0.62, Y=6.49, Z=0.0 rotated 12deg..."
```
You did all the thinking. Claude is just a copy-paste machine.

### Level 5 — True Agentic Brief
```
INTENT: Make the scene feel lived-in and inhabited.
SCOPE:  Touch lighting, colours, small props.
        Do NOT touch: camera, WindowLight, dining table objects.
CONSTRAINTS: X=-4 to X=4, nothing > 0.5m on tables, match existing style.
VERIFICATION: 10/10 checks passed, protected objects untouched.
```
Agent plans everything. You supervise the report.

---

## The Agentic Brief Template

```
## BRIEF: [one-sentence goal]

## INTENT
[2-3 sentences: desired feeling, mood, style. Artist language, not technical.]

## AUTONOMY LEVEL
[guided / autonomous / autonomous-with-guardrails]

## SCOPE
TOUCH:
  - [what the agent is allowed to modify]
LEAVE ALONE:
  - [protected objects — hero props, calibrated lights, camera]

## CONSTRAINTS
  - Spatial: [bounds]
  - Scale:   [size limits]
  - Style:   [match existing or palette]
  - Collection: [where new objects go]

## AGENT BEHAVIOUR
  - Observe: read current state before modifying anything
  - Think out loud: print reasoning before each decision
  - Act one step at a time: verify each before next
  - Self-fix: if a check fails, diagnose before reporting done

## VERIFICATION
  - [specific measurable check 1]
  - [specific measurable check 2]
  - Final: "N/N checks passed"
```

---

## What the Agent Decided (This Lesson)

**Brief:** *"Make the scene feel lived-in. Don't touch the camera, WindowLight,
or objects on the dining table."*

**Agent observed:** side table has plant pot + clear space, floor between
tables is empty, bookshelf shelf 2 has gaps between books.

**Agent planned 4 human-touch props:**

| Prop | Reasoning |
|------|-----------|
| LinenNapkin | Common on side tables. Cream cloth implies someone uses this room |
| GlassesCase | Dark leather case implies a person lives here — subtle, specific |
| LoosePaper | Universal human mess — floors in real rooms have stray paper |
| Candle | Warm, intimate bookshelf detail — books + candles = inhabited room |

**All 4 passed 10 constraint checks.**

---

## PE Insight — Intent Language

The INTENT section is where prompt quality multiplies.

Compare:
```
❌ "Add some small props to the scene"
✅ "The scene still feels like a 3D model, not a real room.
    Add small human touches — things people actually leave around.
    Keep it subtle: nothing should distract from the dining table."
```

The second version gives the agent:
- A **problem diagnosis** ("feels like a 3D model")
- A **solution approach** ("human touches, things people leave around")
- A **constraint of scale** ("subtle, nothing distracting")

From this alone, the agent can select appropriate objects (napkin, glasses case)
and reject inappropriate ones (sculpture, vase, laptop).

---

## Module 3 — All Patterns in One Brief

This lesson's brief used every Module 3 concept:

| Concept | Where it appeared |
|---------|------------------|
| Agent loop (3.1) | Observe → Think → Act → Check → Report |
| Multi-step build (3.2) | 4 props built in sequence with verification |
| TaskCreate (3.3) | Task #6 tracked the full brief execution |
| Guide vs. Autonomous (3.4) | Protected list + free zones clearly separated |
| Agentic brief (3.5) | All 4 layers: intent, scope, constraints, verification |

---

*Lesson 3.5 — June 2026*
