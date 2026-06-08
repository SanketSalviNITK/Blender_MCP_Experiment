# Lesson 1.4 — Solution & Notes

## What We Covered
How Claude reads Blender's Python API docs to write accurate code, and the "Show Me First" technique for reviewing code before running it.

---

## Demos Completed

### Demo 1 — API Discovery: All Available Modifiers
**Prompt:** `Show me the Blender APIs for modifiers and tell me which ones are available. Refer to Blender API docs.`

**How Claude got the list:**
1. Searched bundled API docs via `search_api_docs`
2. Queried Blender directly for the full enum list:
```python
types = [item.identifier for item in bpy.types.Modifier.bl_rna.properties['type'].enum_items]
```

**Result:** 80+ modifiers across 4 categories:

| Category | Key Modifiers |
|----------|--------------|
| Generate | ARRAY, BEVEL, BOOLEAN, MIRROR, SOLIDIFY, SUBSURF, WIREFRAME |
| Deform | ARMATURE, CAST, DISPLACE, SHRINKWRAP, SIMPLE_DEFORM, SMOOTH, WAVE |
| Physics | CLOTH, FLUID, OCEAN, PARTICLE_SYSTEM, SOFT_BODY |
| Grease Pencil | GREASE_PENCIL_ARRAY, GREASE_PENCIL_SUBDIV, etc. |

---

### Demo 2 — Show Me First Technique ⭐
**Prompt:** `Write Python code to add a Subdivision Surface modifier to RedCube with 2 levels. Show me the code before running it.`

**Code reviewed and approved:**
```python
import bpy

cube = bpy.data.objects.get('RedCube')

if cube:
    subsurf = cube.modifiers.new(name='Subdivision', type='SUBSURF')
    subsurf.levels = 2
    subsurf.render_levels = 2
    subsurf.subdivision_type = 'CATMULL_CLARK'
```

**Result:** Smooth rounded RedCube with Catmull-Clark subdivision applied ✅

---

### Demo 3 — Run It
**Prompt:** `run it`

Claude executed the reviewed code. Modifier confirmed:
- Name: `Subdivision`
- Viewport levels: `2`
- Render levels: `2`
- Algorithm: `CATMULL_CLARK`

---

## Key API Patterns Learned

### Adding any modifier
```python
obj = bpy.data.objects.get('ObjectName')
mod = obj.modifiers.new(name='ModifierName', type='TYPE_ID')
```

### Common modifier type IDs
```python
'SUBSURF'       # Subdivision Surface - smooths mesh
'ARRAY'         # Array - creates copies along an axis
'MIRROR'        # Mirror - mirrors across an axis
'BEVEL'         # Bevel - rounds edges
'BOOLEAN'       # Boolean - add/subtract/intersect meshes
'SOLIDIFY'      # Solidify - adds thickness
'WIREFRAME'     # Wireframe - converts to wireframe
'SIMPLE_DEFORM' # Twist, bend, taper, stretch
'DISPLACE'      # Displace with texture
```

### Subdivision Surface specifically
```python
subsurf = obj.modifiers.new(name='Subdivision', type='SUBSURF')
subsurf.levels = 2              # viewport levels
subsurf.render_levels = 2       # render levels
subsurf.subdivision_type = 'CATMULL_CLARK'  # or 'SIMPLE'
```

---

## The "Show Me First" Technique

> Always ask Claude to show the code before running it.

**Benefits:**
- You learn what the bpy API looks like
- You catch mistakes before they affect your scene  
- You get a reusable code snippet to save to `/scripts`
- You build understanding of Blender Python over time

**Prompt pattern:**
```
Write Python code to [do something]. Show me the code before running it.
```
Then: `run it` or `looks good, run it` to execute.

---

## Key Takeaways

- Claude reads real Blender API docs — not guessing
- 80+ modifiers available, all accessible via `modifiers.new(type='TYPE_ID')`
- "Show Me First" = review → approve → run
- Every reviewed script is worth saving to `/scripts`

---

*Completed: June 2026*
