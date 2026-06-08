# Lesson 3.3 — Solution & Notes
## Using TaskCreate to Track Work Inside Sessions

## What We Built
A decorative terracotta plant on the side table, tracked with 5 TaskCreate
tasks. Every step was marked in_progress before starting and completed after
verification. All 5 checks passed.

---

## Task List — Final State

```
#1 [completed] Lesson 3.3: Add decorative plant to side table
#2 [completed] Step 1 — Observe side table position and dimensions
#3 [completed] Step 2 — Build ceramic plant pot
#4 [completed] Step 3 — Build plant leaves
#5 [completed] Step 4 — Verify, parent, and organise
```

---

## Plant Specs

### PlantPot
```python
outer_r = 0.05,  inner_r = 0.042
height  = 0.08m
base_z  = 0.55   (SideTable top surface)
top_z   = 0.63
material: Terracotta — (0.72, 0.32, 0.18), roughness=0.85
```

### PlantLeaf_1–5
```python
5 flat quad planes, 72° apart (i * 72°)
tilt  = 25° outward from vertical
length = 0.14m,  half-width = 0.025m
base_z = 0.63  (pot top)
top_z  = 0.757 (leaf tips)
material: LeafGreen — (0.08, 0.28, 0.06), roughness=0.65
parent: PlantPot
```

---

## Bug Encountered

**Error:** `faces.new(...): face already exists`

**Cause:** Adding a back-face to the same 4 vertices as the front face.
Bmesh doesn't allow two faces on identical vertices.

**Fix:** Duplicate the vertex set for the back face:
```python
vA = bm.verts.new(v0)
vB = bm.verts.new(v1)
vC = bm.verts.new(v2)
vD = bm.verts.new(v3)
bm.faces.new([vA, vB, vC, vD])   # front

vA2 = bm.verts.new(v0)            # fresh verts
vB2 = bm.verts.new(v1)
vC2 = bm.verts.new(v2)
vD2 = bm.verts.new(v3)
bm.faces.new([vD2, vC2, vB2, vA2])  # back (reversed winding)
```

---

## TaskCreate Patterns Learned

### Basic lifecycle
```python
TaskCreate(subject="Step N — do X", description="full spec here",
           activeForm="Doing X")
TaskUpdate(id, status="in_progress")   # before starting
# ... do the work ...
TaskUpdate(id, status="completed")     # after verifying
```

### Dependency chain
```python
t1 = TaskCreate("Step 1 — observe")
t2 = TaskCreate("Step 2 — build")
t3 = TaskCreate("Step 3 — verify")
TaskUpdate(t2.id, addBlockedBy=[t1.id])
TaskUpdate(t3.id, addBlockedBy=[t2.id])
# Now task 2 can't start until task 1 is complete, etc.
```

### Recovery (if a step fails)
```python
# If step 3 fails partway:
# - Leave it as in_progress (don't mark completed)
# - Create a new task: "Fix: step 3 error — <description>"
# - Fix the new task
# - Then return and complete task 3
```

---

## Why This Matters at Scale

For a 3-step task, TaskCreate adds structure but isn't critical.
For a 20-step scene build, it becomes essential:

- You can see exactly where the agent is mid-run
- If the session context gets full, you can restart and read TaskList
  to know exactly what's done and what to continue from
- You can share the task list as documentation of what was built and how

---

*Completed: June 2026*
