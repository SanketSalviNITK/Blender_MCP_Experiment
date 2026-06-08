# Lesson 3.1 — Solution & Notes
## What is an Agent? How Claude Breaks Down Tasks

## What We Covered
Learned the difference between conversational and agentic Claude.
Ran a live agent loop — Claude observed the scene, planned a side table,
built it, verified every check, and reported its decisions.

---

## The Agent Loop — Live Results

### Step 1: OBSERVE
```
DiningTable  loc=(0,0,0.75)   dims=(3.0, 1.5, 0.06)
LampPole     loc=(-3.8,0,..)  → lamp is on far left
Scene X span: -3.8 to +1.38  → right side (X≈2.8) is empty
Table top Z: 0.78
```

### Step 2: THINK
```
Decision: side table at X=2.8, Y=0
  - Right side is empty and within camera frame (camera at X=5)
  - Size: 0.6x0.4x0.55m — proportionate, not competing
  - WalnutWood reused — visual consistency
  - Legs 0.04m (thinner than dining table's 0.08m — correct scale)
```

### Step 3: ACT
```
SideTable built at X=2.8, top Z=0.55
SideTableLeg_1–4 built, joints flush
Material WalnutWood assigned
```

### Step 4: CHECK
```
Top Z = 0.550        PASS
All 4 legs exist     PASS
WalnutWood material  PASS
Gap from dining=0.94m (no overlap)  PASS
Added to DiningSet collection  DONE
```

---

## Key Insight: The Agent Reasons About the Scene

The agent didn't use hardcoded positions. It:
1. Read the dining table dimensions and position
2. Found the empty space in the scene
3. Chose a proportionate size relative to the main table
4. Placed it where the camera could see it

This is **spatial reasoning** — making decisions based on the geometry of
the scene, not from a script.

---

## The "Think Out Loud" Pattern

Always have agents print their reasoning:
```python
print('''
Decision: X=2.8 because:
  - Dining table ends at X=+1.5
  - Camera at (5,-5.8) faces left — X=2.8 is in frame
  - Lamp at X=-3.8 means left side is occupied
''')
```

Benefits:
- You can see WHY each decision was made
- You can correct reasoning before it acts
- Debugging is much easier when the agent narrated its thought process

---

## Rules Learned

1. **Agents observe before acting** — never hardcode positions; read the
   scene first and derive positions from actual geometry.

2. **Think out loud** — print reasoning before executing. This makes agents
   auditable and correctable.

3. **Verify after every act** — each agent step should end with a CHECK
   that confirms the action succeeded.

4. **Reuse scene resources** — materials, collections, naming conventions.
   An agent that invents new names/materials creates inconsistency.

5. **Report at the end** — a final summary tells you exactly what changed
   and why, so you can decide what to do next.

---

## New Objects Added to Scene

| Object | Position | Dimensions | Material |
|--------|----------|------------|----------|
| SideTable | (2.8, 0, 0.51–0.55) | 0.6×0.4×0.04m | WalnutWood |
| SideTableLeg_1–4 | corners at X=2.8 | 0.04×0.04×0.51m | WalnutWood |

Collection: DiningSet

---

*Completed: June 2026*
