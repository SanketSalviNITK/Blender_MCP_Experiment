# Lesson 2.4 — Solution & Notes
## Organizing a Scene: Collections & Naming

## What We Covered
Organised the dining table scene into 5 named collections.
Learned how collections map to the Outliner, why naming conventions matter,
and how to control visibility per-collection from Python.

---

## Final Outliner Structure

```
Scene Collection  (0 objects at root — clean)
├── [Environment]  (2)
│   ├── Floor          MESH
│   └── StoneWall      MESH
├── [DiningSet]    (8)
│   ├── DiningTable    MESH
│   ├── TableLeg_1–4   MESH
│   ├── RedBook        MESH
│   ├── CoffeeMug      MESH
│   └── MugHandle      MESH
├── [Lamp]         (4)
│   ├── LampPole       MESH
│   ├── LampBase       MESH
│   ├── LampGlassSphere MESH
│   └── DustMotes      MESH
├── [Lighting]     (4)
│   ├── WindowLight    LIGHT
│   ├── FillLight      LIGHT
│   ├── RimLight       LIGHT
│   └── LampGlow       LIGHT
└── [Cameras]      (1)
    └── SceneCamera    CAMERA
```

**Root is clean** — zero orphan objects at the Scene Collection level.

---

## Core Pattern: Create Collection + Move Object

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
    # Remove from all current collections
    for c in bpy.data.collections:
        if obj.name in c.objects:
            c.objects.unlink(obj)
    if obj.name in bpy.context.scene.collection.objects:
        bpy.context.scene.collection.objects.unlink(obj)
    col.objects.link(obj)
```

**Why unlink first?** In Blender, an object can exist in multiple collections
simultaneously. You must explicitly remove it from everywhere before linking
to the target — otherwise it shows up in two places.

---

## Collection Visibility Controls

```python
# Viewport visibility (eye icon in outliner)
col.hide_viewport = True   # hide all objects in viewport
col.hide_viewport = False  # show

# Render visibility (camera icon in outliner)
col.hide_render = True    # exclude from all renders

# View layer exclusion (most powerful — fully skips the collection)
vl = bpy.context.view_layer.layer_collection.children.get('Environment')
vl.exclude = True   # environment not rendered, not in scene at all
```

**Use case examples:**
- Hide `Lighting` collection to preview the scene without any lights
- Hide `DustMotes` during test renders for speed
- Exclude `Cameras` from render so camera objects don't cast shadows

---

## Naming Convention Used

| Pattern | Example | Explanation |
|---------|---------|-------------|
| `Category_Index` | `TableLeg_1` | Type + number |
| `CategoryDescription` | `DiningTable` | PascalCase, no spaces |
| `RoleDescription` | `WindowLight` | Role comes first |
| `SceneName` | `SceneCamera` | Explicit scope |

### Why No Spaces?
Blender allows spaces in names but Python string lookups are case-sensitive
and space-sensitive. `bpy.data.objects.get('Table Leg 1')` is fragile —
one extra space breaks it. `TableLeg_1` is safe.

---

## Prompt Engineering Insight — Organisation Prompts

Organisation prompts should describe **intent**, not implementation:

```
Group the scene into logical collections:
- Background geometry → "Environment"
- Hero objects on the table → "DiningSet"
- The floor lamp → "Lamp"
- All light sources → "Lighting"
- All cameras → "Cameras"

No object should remain at the Scene Collection root.
Remove the empty default 'Collection' if present.
```

This works for 20 objects or 2000 — the structure scales, the language stays
the same. For a city scene you'd write:
```
- Individual buildings → "Buildings"
- Street furniture → "Props"
- Road surfaces → "Ground"
- All characters → "Characters"
```

---

## Rules Learned

1. **Always unlink before linking** — Blender objects can live in multiple
   collections; unlink everywhere first, then link to the target.

2. **`get_or_create` pattern** — check `bpy.data.collections.get(name)` first.
   Creating a duplicate collection with the same name just appends `.001`.

3. **Root should be empty** — nothing should live at `Scene Collection` root.
   It's the container for sub-collections, not a dumping ground.

4. **Collections ≠ parent-child** — collections are organisational (outliner
   groups). Parent-child is a transform hierarchy. Both can coexist —
   TableLeg_1 is in the DiningSet collection AND parented to DiningTable.

5. **`hide_viewport` vs `exclude`** — `hide_viewport` just hides visually.
   `exclude` from view layer removes from rendering entirely (faster renders).

---

*Completed: June 2026*
