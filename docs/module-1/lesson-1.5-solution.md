# Lesson 1.5 — Solution & Notes
## Prompt Engineering: Specificity vs. Vagueness

## What We Built
A complete rustic dining table scene built entirely through natural language prompts —
demonstrating the full spectrum from cinematic description to precise technical constraints.

---

## The Two Prompts That Built Everything

### Prompt 1 — Establishing Shot (Cinematic)
```
A medium shot establishing the setting: a large, flat, rectangular wooden dining table 
made of dark walnut is placed in the center of a rustic, sunlit room. Resting flat on 
the tabletop is a single, hardbound red book. To the left, stands a tall, minimalist 
table lamp with a dark metal thin pole stem and an unlit, translucent glass sphere on 
top. The background shows a soft-focus stone wall. Diffuse light from a window to the left.
```

### Prompt 2 — Refinement Shot (Cinematic + Technical)
```
The scene from Blender but viewed from a slightly lower angle. We add a clean, white 
ceramic coffee mug sitting on the wooden tabletop, placed directly between the red book 
and the base of the lamp. The lamp is now turned on, casting a warm, soft glow from the 
glass sphere over the mug and the texture of the book. Dust motes dance in the warm light. 
Depth of field is tightened on the mug.
```

---

## Issues Found and Fixed

### 1. Table legs all at origin (0,0,0)
**Cause:** `transform_apply` via TCP bridge resets object location to origin.
**Fix:** Rebuild all geometry using direct bmesh vertex placement at exact world coordinates.
**Rule learned:** Never use `transform_apply` via the TCP bridge. Always use bmesh.

### 2. Coffee mug hanging off table edge
**Cause:** Mug centre at X=-1.6, outer radius 0.045 → mug edge at X=-1.645, outside table edge at X=-1.5.
**Fix:** Shifted mug to X=-1.2 (0.255 unit clearance from edge).
**Rule learned:** Always verify XY bounds of objects against table bounds after placement.

### 3. RedBook floating 0.84 units above table
**Cause:** Primitive cube created with a location, then location updated multiple times — mesh vertices baked at wrong world Z.
**Fix:** Rebuilt book using bmesh with exact world vertex coordinates (z0=0.78, z1=0.805).
**Rule learned:** Use bmesh world-coordinate construction for all geometry — no primitives + scale.

### 4. Materials not visible in viewport
**Cause:** Blender default viewport is Solid mode — doesn't show materials.
**Fix:** Press Z → Material Preview, or click sphere icon top-right of viewport.

---

## Key Prompt Engineering Lessons

### The Specificity Scale
```
Level 1: "Add some stuff to a table"
Level 2: "Add a book and mug to a wooden table"  
Level 3: "Add a red book and white mug to a dark walnut dining table"
Level 4: "Add a red hardbound book at X=0.3 and white ceramic mug at X=-1.2 on a walnut table"
Level 5: "Add a red book (0.22x0.16x0.025m, roughness=0.65) at (0.3, 0.1), bottom flush 
          with table top Z=0.78. Verify XY bounds stay within table [-1.5,1.5]x[-0.75,0.75]"
```

Your prompts in this lesson averaged **4.5–5/5** — cinematic intent + technical precision.

### The Cinematic Brief Pattern
Write prompts like a film director:
- **Shot type** → camera position and angle
- **Subject** → what's in focus, what's soft
- **Lighting mood** → direction, quality, colour temperature
- **Materials** → surface quality words (walnut, ceramic, translucent glass)
- **Atmosphere** → dust motes, warmth, time of day

### Iterative Refinement
Prompt 1 = establish the world
Prompt 2 = refine, add detail, adjust mood
Each prompt **builds on the previous state** — Claude holds the scene between prompts.

### Verification Requests
Always end complex build prompts with:
> *"Verify all joint gaps < 0.001 and all object XY bounds within table surface. Report pass/fail."*

This catches floating objects and misplacements before they compound.

---

## Technical Patterns Established

### The bmesh World-Coordinate Pattern (use for all geometry)
```python
import bpy, bmesh
me = bpy.data.meshes.new('MyMesh')
bm = bmesh.new()
verts = [
    bm.verts.new((x0, y0, z0)), bm.verts.new((x1, y0, z0)),
    # ... all 8 corners at exact world positions
]
bm.faces.new([...])
bm.to_mesh(me); bm.free(); me.update()
obj = bpy.data.objects.new('MyObject', me)
bpy.context.scene.collection.objects.link(obj)
```

### The Hollow Cylinder Mug Pattern
```python
# Build hollow cylinder with outer wall, inner wall, bottom ring, top rim
# Use SEGS=32 for smooth appearance
# Verify: bottom Z = table_top, outer radius clears table edge
```

### The Verification Pattern
```python
from mathutils import Vector
world_z = [(obj.matrix_world @ v.co).z for v in obj.data.vertices]
gap = abs(min(world_z) - TABLE_TOP)
print(f'FLUSH = {gap < 0.001}')
```

---

## Final Scene
See full prompt in: [`/prompts/lesson-1.5-scene-prompt.md`](../../prompts/lesson-1.5-scene-prompt.md)

---

## Module 1 Complete!
All 5 lessons done. You can now:
- Connect Claude to Blender via MCP ✅
- Navigate Claude Code tools and CLI ✅  
- Build scenes using natural language prompts ✅
- Read and use Blender API docs via Claude ✅
- Write Level 5 specific prompts with verification ✅

**Next:** [Module 2 — Scene Basics](../module-2/overview.md)

---

*Completed: June 2026*
