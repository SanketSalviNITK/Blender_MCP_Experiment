# Lesson 2.1 — Solution & Notes
## Object Transforms: Move, Rotate, Scale

## What We Covered
The three fundamental transforms in Blender — Location, Rotation, Scale —
applied to our dining table scene with precision. Also introduced parenting
as the correct way to group objects for collective transforms.

---

## Transforms Applied to Scene

### 1. RedBook — Casual Rotation (Z axis)
```python
import bpy, math
book = bpy.data.objects.get('RedBook')
book.rotation_euler.z = math.radians(18)
```
**Why:** 18° rotation makes the book look casually placed by a human, not computer-aligned.

### 2. Lamp — Slight Tilt (Y axis)
```python
for name in ['LampPole', 'LampBase', 'LampGlassSphere', 'LampGlow']:
    obj = bpy.data.objects.get(name)
    obj.rotation_euler.y = math.radians(2)
```
**Why:** Tall lamps are never perfectly vertical — 2° tilt adds realism.

### 3. CoffeeMug — Moved Closer + Handle Facing Camera
```python
mug    = bpy.data.objects.get('CoffeeMug')
handle = bpy.data.objects.get('MugHandle')
for obj in [mug, handle]:
    obj.location.x += 0.3              # closer to book
    obj.rotation_euler.z = math.radians(-35)  # handle faces camera
```
**Why:** Handle should face the viewer. Camera is at +X/-Y so -35° on Z points it outward.

### 4. RedBook — Non-Uniform Scale (XY only)
```python
book = bpy.data.objects.get('RedBook')
book.scale.x = 1.3
book.scale.y = 1.3
# Z unchanged — thickness stays the same
bpy.context.view_layer.update()  # always flush depsgraph after scale
```
**Result:** 0.220 → 0.286m (W), 0.160 → 0.208m (D), 0.025m (H unchanged)

### 5. StoneWall — Pushed Back for Depth
```python
wall = bpy.data.objects.get('StoneWall')
wall.location.y += 1.0   # Y=6 → Y=7
```
**Why:** More distance between table and wall = softer background blur at f/1.8 DOF.

---

## Key Concept: Parenting for Group Transforms

### The Problem
Rotating `DiningTable` alone left the 4 legs behind.
Each object needed to be transformed individually — fragile and error-prone.

### The Solution — Parent-Child Hierarchy
```python
import bpy

table = bpy.data.objects.get('DiningTable')
legs  = ['TableLeg_1', 'TableLeg_2', 'TableLeg_3', 'TableLeg_4']

for name in legs:
    leg = bpy.data.objects.get(name)
    world_mat = leg.matrix_world.copy()   # preserve world position
    leg.parent = table                     # set parent
    leg.matrix_world = world_mat           # restore world position
```

### Result
```
DiningTable  ← parent
  ├── TableLeg_1  ← child
  ├── TableLeg_2  ← child
  ├── TableLeg_3  ← child
  └── TableLeg_4  ← child
```

Any transform on `DiningTable` now cascades to all 4 legs automatically.

**Verified:**
```
table.rotation_euler.z = math.radians(5)
→ All 4 legs: world rotation Z = 5.0 deg ✅
```

---

## Transform Prompt Patterns

| Intent | Prompt |
|--------|--------|
| Move absolute | "Move RedBook to position (0.5, 0.2, 0.78)" |
| Move relative | "Shift CoffeeMug 0.3 units in the +X direction" |
| Rotate | "Rotate RedBook 18 degrees around the Z axis" |
| Non-uniform scale | "Scale RedBook to 1.3x on X and Y axes only" |
| Group transform | "Rotate the DiningTable 5 degrees on Z" (legs follow via parent) |
| Push back | "Move StoneWall 1 unit further back (Y direction)" |

---

## Rules Learned

1. **Always call `bpy.context.view_layer.update()`** after scale changes — dimensions
   won't reflect the new value until the dependency graph is flushed.

2. **Parent before transforming groups** — set up parent-child once, then transform
   only the parent forever after.

3. **`matrix_world` preservation** — always copy `leg.matrix_world` BEFORE setting
   `leg.parent`, then restore it after. Otherwise Blender moves the leg to a wrong position.

4. **Rotation uses radians** — always use `math.radians(degrees)` when setting
   `rotation_euler` values.

---

## Final Scene State After Lesson 2.1

| Object | Location | Rotation | Scale |
|--------|----------|----------|-------|
| DiningTable | (0, 0, 0.75) | Z=5° | (1,1,1) |
| TableLeg_1–4 | corners | Z=5° (via parent) | (1,1,1) |
| RedBook | (0.3, 0.1, 0.79) | Z=18° | (1.3,1.3,1.0) |
| CoffeeMug | (-0.9, 0.05, 0.82) | Z=-35° | (1,1,1) |
| MugHandle | (-0.83, 0.05, 0.83) | Z=-35° | (1,1,1) |
| LampPole/Base/Sphere | X=-3.8 | Y=2° | (1,1,1) |
| StoneWall | (0, 7, 5) | X=90° | (1,1,1) |

---

*Completed: June 2026*
