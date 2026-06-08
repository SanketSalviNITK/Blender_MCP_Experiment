# Lesson 3.3 — Using TaskCreate to Track Work Inside Sessions

## Learning Goals
- Understand when and why to use TaskCreate
- Use the full task lifecycle: create → in_progress → completed
- See how task tracking makes complex agent work auditable
- Learn the dependency and blocking pattern for ordered tasks

---

## What is TaskCreate?

TaskCreate is Claude Code's built-in session task tracker. It's a to-do list
that lives inside the conversation, visible to both you and the agent.

```
TaskCreate  → add a task (starts as "pending")
TaskUpdate  → change status: pending → in_progress → completed
TaskList    → see all tasks with current status at a glance
TaskGet     → read a specific task's full description
```

When a task is marked `in_progress`, a **spinner chip appears in the UI**.
When marked `completed`, it turns **green**. This is how you supervise a
long agent run without losing track of what's happened.

---

## When to Use It

| Situation | Use TaskCreate? |
|-----------|----------------|
| Single quick change ("rotate table 5°") | No — overkill |
| 3+ sequential steps, each depending on previous | Yes |
| Long agent run that might span multiple messages | Yes |
| Anything that could partially fail and need recovery | Yes |
| Complex build with parallel or ordered sub-tasks | Yes |

**Rule of thumb:** if you'd write a numbered list to plan it, use TaskCreate.

---

## The Task Lifecycle

```
TaskCreate("Step 1 — do X")
    → status: pending

TaskUpdate(id, status="in_progress")
    → spinner appears in UI

[do the work]

TaskUpdate(id, status="completed")
    → green tick in UI

TaskList()
    → see all tasks and their status
```

Always mark `in_progress` BEFORE starting work — this is what shows the
spinner so you know Claude is actively on a step, not stalled.

---

## Task Fields

```python
TaskCreate(
    subject="Step 2 — Build ceramic plant pot",
    description="Hollow cylinder using bmesh. outer_r=0.05, h=0.08m. 
                 Terracotta material. Sits on SideTable top at Z=0.55.",
    activeForm="Building plant pot"   # shown in spinner
)
```

- **subject** — the title (imperative: "Build X", "Verify Y")
- **description** — full spec with dimensions, constraints, expected outcome
- **activeForm** — present-continuous label for the spinner ("Building plant pot")

---

## Task Dependencies (advanced)

For tasks that must run in order, use `addBlockedBy`:

```python
# Task 3 cannot start until task 2 is done
TaskUpdate("3", addBlockedBy=["2"])
```

This prevents accidentally starting step 3 before step 2 is verified.

---

## What We Built This Lesson

A decorative plant on the side table — tracked with 5 tasks:

| Task | Status | What happened |
|------|--------|---------------|
| #1 Parent task | ✅ | "Add plant to side table" |
| #2 Observe | ✅ | SideTable at X=2.8, top Z=0.55 |
| #3 Build pot | ✅ | Terracotta hollow cylinder, r=0.05, h=0.08m |
| #4 Build leaves | ✅ | 5 leaf planes, 72° apart, tilted 25°, LeafGreen mat |
| #5 Verify + organise | ✅ | 5/5 checks PASS, parented, DiningSet collection |

**Bug encountered and fixed during leaf building:**
- First attempt: `faces.new()` threw "face already exists" error
- Cause: trying to add a back-face to the same 4 vertices
- Fix: duplicate vertex set for each face — bmesh requires unique verts per face

---

## PE Insight — Task Descriptions as Micro-Specs

The task description field is a hidden prompt. Write it as a mini spec:

```
"Hollow cylinder pot using bmesh. Outer radius 0.05m, inner 0.042m,
 height 0.08m. Sits on SideTable top surface. Terracotta material
 (roughness 0.85, colour (0.72, 0.32, 0.18))."
```

This means if the agent ever reads the task mid-session (via TaskGet),
it has everything it needs to execute — no need to re-read earlier messages.

---

*Lesson 3.3 — June 2026*
