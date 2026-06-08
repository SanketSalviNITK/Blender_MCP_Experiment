# Lesson 2.4 — Master Collections Prompt

> Organise the dining table scene objects into named collections.
> Run after all scene objects, materials, and lights exist (Lessons 1.5–2.3).

---

## The Prompt

```
Organise the Blender scene into named collections.
No object should remain at the Scene Collection root after this.
Remove the empty default 'Collection' if it exists.

COLLECTIONS TO CREATE:

"Environment":
  - Floor, StoneWall
  - Role: all background / set-dressing geometry

"DiningSet":
  - DiningTable, TableLeg_1, TableLeg_2, TableLeg_3, TableLeg_4
  - RedBook, CoffeeMug, MugHandle
  - Role: the hero dining table and all objects on it

"Lamp":
  - LampPole, LampBase, LampGlassSphere, DustMotes
  - Role: the floor lamp prop and atmosphere

"Lighting":
  - WindowLight, FillLight, RimLight, LampGlow
  - Role: all light sources

"Cameras":
  - SceneCamera
  - Role: all cameras

RULES:
- Use get_or_create pattern (don't create duplicate collections)
- Unlink from all current collections before linking to target
- Print final outliner structure: [CollectionName] (count) -> [object list]
- Confirm root is clean (zero objects at Scene Collection level)
```

---

## Core Pattern

```python
import bpy

def get_or_create_collection(name):
    col = bpy.data.collections.get(name)
    if not col:
        col = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(col)
    return col

def move_to_collection(obj_name, col):
    obj = bpy.data.objects.get(obj_name)
    if not obj: return
    for c in bpy.data.collections:          # remove from everywhere
        if obj.name in c.objects:
            c.objects.unlink(obj)
    if obj.name in bpy.context.scene.collection.objects:
        bpy.context.scene.collection.objects.unlink(obj)
    col.objects.link(obj)                   # place in target

# Visibility control (bonus)
col.hide_viewport = True/False             # eye icon
col.hide_render   = True/False             # camera icon
view_layer_col.exclude = True              # full exclusion from view layer
```

---

## PE Insight

Describe organisation by **intent**:
- "Background geometry" → Environment
- "Hero objects" → DiningSet
- "All lights" → Lighting

Claude picks the right objects from the name/type.
You don't need to list every object — describe the category.

---

*Recorded: June 2026 — Lesson 2.4*
