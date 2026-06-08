# Lesson 2.2 — Master Materials Prompt

> Apply PBR materials to the rustic dining table scene.
> Run after the scene from Lesson 2.1 is already built and transforms applied.

---

## The Prompt

```
Apply physically-based materials to the dining table scene.
Use Principled BSDF for all mesh objects (nodes.clear() then rebuild).
Never patch existing nodes — always clear and reconstruct the node tree.

MATERIALS:

DiningTable + TableLeg_1–4 (shared material "WalnutWood"):
  - Surface: aged dark walnut wood, matte, no shine
  - Base Color: (0.12, 0.06, 0.02)
  - Roughness: 0.75, Metallic: 0

CoffeeMug + MugHandle (shared material "WhiteCeramic"):
  - Surface: glazed white ceramic, slightly reflective
  - Base Color: (0.92, 0.92, 0.92)
  - Roughness: 0.15, Metallic: 0

RedBook ("RedBookCloth"):
  - Surface: cloth hardcover, deep red, fully matte
  - Base Color: (0.55, 0.05, 0.04)
  - Roughness: 0.80, Metallic: 0

Floor ("StoneConcrete"):
  - Surface: raw concrete, warm grey-brown, very rough
  - Base Color: (0.35, 0.32, 0.28)
  - Roughness: 0.85, Metallic: 0

StoneWall ("AgedPlaster"):
  - Surface: old interior plaster, creamy off-white, warm tint
  - Base Color: (0.55, 0.50, 0.44)
  - Roughness: 0.90, Metallic: 0

LampBase + LampPole (shared material "BrushedSteel"):
  - Surface: brushed industrial steel, not chrome
  - Base Color: (0.60, 0.60, 0.60)
  - Roughness: 0.35, Metallic: 0.9

LampGlassSphere ("FrostedGlass"):
  - Surface: frosted glass, milky warm tint, lets light through
  - Base Color: (0.95, 0.92, 0.85)
  - Roughness: 0.05, Metallic: 0, Transmission: 0.85

LampGlow (LIGHT object — no material):
  - lamp.data.color  = (1.0, 0.95, 0.8)   # warm white
  - lamp.data.energy = 60

VERIFICATION:
  - Print: object name | material name | color | roughness | metallic
  - Skip DustMotes (intentionally no material)
  - Confirm 8 distinct material names appear in bpy.data.materials
```

---

## Core Pattern

```python
def make_principled(name, color, roughness, metallic=0.0, transmission=0.0):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()  # ALWAYS clear first

    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    out  = nodes.new('ShaderNodeOutputMaterial')
    links.new(bsdf.outputs['BSDF'], out.inputs['Surface'])

    bsdf.inputs['Base Color'].default_value = (*color, 1.0)
    bsdf.inputs['Roughness'].default_value  = roughness
    bsdf.inputs['Metallic'].default_value   = metallic
    if transmission > 0:
        bsdf.inputs['Transmission Weight'].default_value = transmission
    return mat

def assign_material(obj_name, mat):
    obj = bpy.data.objects.get(obj_name)
    if not obj or obj.type != 'MESH': return  # skip lights/cameras
    obj.data.materials.clear()
    obj.data.materials.append(mat)
```

---

## PE Insight — Surface Description Language

Describe surfaces in artist language, not numbers:
- "Aged dark walnut — almost black, matte, no reflections" → roughness=0.75
- "Glazed ceramic — white, slightly shiny" → roughness=0.15
- "Frosted glass — milky, lets light pass through" → roughness=0.05, transmission=0.85
- "Brushed steel — clearly metallic, not polished chrome" → metallic=0.9, roughness=0.35

---

*Recorded: June 2026 — Lesson 2.2*
