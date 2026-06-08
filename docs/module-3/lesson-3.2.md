# Lesson 3.2 — Multi-step Scene Building (Agent Does It All)

## Learning Goals
- Give a high-level brief and let the agent plan everything
- Watch the agent observe → think → act → check → self-fix
- Understand how agents handle unexpected issues (self-correction)
- See spatial reasoning: deriving positions from scene geometry

---

## The Brief

```
"Add a bookshelf against the back wall. It should look like it belongs
in the same room as the dining table — same walnut wood, proportionate
height. Fill it with a mix of books of varying heights and colours.
The shelf should be visible from the camera."
```

30 words. No dimensions. No positions. No colour specs. The agent
derived everything from the scene.

---

## What the Agent Derived (vs What You'd Have to Specify)

| Decision | Agent derived it from... |
|----------|--------------------------|
| X position: 0 (centred) | Read wall position + empty X space map |
| Y position: 6.7 (near wall) | Wall at Y=7.0 → 0.3m gap for depth |
| Width: 1.4m | Dining table legs at X=±1.4 → shelf fits between |
| Height: 1.8m | Dining table = 0.78m → shelf should be taller (room scale) |
| Material: WalnutWood | "same walnut wood" in brief → reuse existing |
| 4 shelves at 0.4/0.8/1.2/1.6m | Evenly spaced in 1.8m height |
| 6 book colours | Brief said "varying colours" → chose a natural palette |
| Y depth: 0.28m | Standard bookshelf depth (real-world knowledge) |

---

## Self-Correction in Action

The agent found its own bug during CHECK:

```
[FAIL] No floating books
Floating: Book_S3_1.001 bot_z=1.630 (expected 1.230)
```

**Root cause:** When building books in a loop, 5 names collided (Book_S3_x
existed from a previous run fragment), so Blender auto-renamed them with
`.001` suffix — and placed them at the wrong Z.

**Fix the agent applied:**
1. Identified all `.001` suffix duplicates
2. Deleted them
3. Re-verified shelf 3 books — all PASS

**The lesson:** Agents catch and fix their own mistakes — but only if you
write CHECK steps. Without verification, the floating books would have
silently appeared in the scene.

---

## The Agent Loop — Full Trace

```
OBSERVE →  wall at Y=7, table at X=0 width=3, scene X free at X=0 near wall
THINK  →   width=1.4m (fits between table legs), Y=6.7, height=1.8m
ACT 1  →   build 9 frame parts (sides, top, bottom, back, 4 shelves)
ACT 2  →   build 22 books (4 shelves × 5-6 books, 6 colour variants)
ACT 3  →   parent all to Shelf_Left, create Bookshelf collection
CHECK  →   5/6 PASS — shelf 3 books floating
FIX    →   delete .001 duplicates, re-verify — all PASS
REPORT →   17 books, 9 frame parts, all checks pass
```

---

## Key Principle: Agents Derive, Not Assume

The agent never hardcoded X=0 or width=1.4 without checking.
It read the scene first:

```python
# Read wall position
wall_y = min((wall.matrix_world @ v.co).y for v in wall.data.vertices)

# Read table leg X extent to know where shelf can fit
for obj in bpy.data.objects:
    xs = [(obj.matrix_world @ v.co).x for v in obj.data.vertices]
    occupied_x.append((obj.name, min(xs), max(xs)))
```

Then it reasoned: *"table legs reach ±1.4m, so 1.4m shelf fits between them".*

This means the bookshelf would place itself correctly even if you had moved
the dining table — because the agent reads actual positions, not assumed ones.

---

*Lesson 3.2 — June 2026*
