# Lesson 2.2 — Solution & Notes
## Materials and Colors — PBR Shading

## What We Covered
Applied physically-based (PBR) materials to every object in the rustic dining
table scene using Blender's Principled BSDF shader. Learned how to map
real-world surface descriptions into shader parameters.

---

## Materials Applied

### Principled BSDF Parameters Cheatsheet
| Parameter | Adjective | Range |
|-----------|-----------|-------|
| Base Color | The surface colour | RGB 0–1 |
| Roughness | Matte (1) ↔ Mirror (0) | 0–1 |
| Metallic | Plastic (0) ↔ Metal (1) | 0–1 |
| Transmission | Opaque (0) ↔ Glass (1) | 0–1 |

---

### 1. Dark Walnut Wood (table + all 4 legs)
```python
walnut = make_principled('WalnutWood', (0.12, 0.06, 0.02), roughness=0.75)
# Shared material — one instance assigned to 5 objects
```
**Surface description:** Aged dark walnut — very dark warm brown, matte,
no shine at all.

---

### 2. White Ceramic (mug + handle)
```python
ceramic = make_principled('WhiteCeramic', (0.92, 0.92, 0.92), roughness=0.15)
```
**Surface description:** Glazed white ceramic — near-white, smooth, slightly
reflective like a coffee mug fresh from the shelf.

---

### 3. Red Book Cloth
```python
make_principled('RedBookCloth', (0.55, 0.05, 0.04), roughness=0.80)
```
**Surface description:** Cloth hardcover — deep red, fully matte, fabric texture implied.

---

### 4. Stone Concrete Floor
```python
make_principled('StoneConcrete', (0.35, 0.32, 0.28), roughness=0.85)
```
**Surface description:** Raw concrete or flagstone — warm grey-brown, very rough,
no reflections.

---

### 5. Aged Plaster Wall
```python
make_principled('AgedPlaster', (0.55, 0.50, 0.44), roughness=0.90)
```
**Surface description:** Old interior plaster — creamy off-white with a slight warm
tint, as rough as it gets.

---

### 6. Brushed Steel Lamp
```python
steel = make_principled('BrushedSteel', (0.60, 0.60, 0.60), roughness=0.35, metallic=0.9)
```
**Surface description:** Brushed industrial steel — grey, clearly metallic,
not chrome-polished but not fully matte either.

---

### 7. Frosted Glass Globe
```python
make_principled('FrostedGlass', (0.95, 0.92, 0.85), roughness=0.05, transmission=0.85)
```
**Surface description:** Frosted glass lampshade — almost clear but with a milky
warm tint that softens the light behind it.
> Transmission=0.85 lets light pass through for the lamp effect.

---

### 8. Lamp Glow (LIGHT object)
```python
lamp.data.color  = (1.0, 0.95, 0.8)
lamp.data.energy = 60
```
LampGlow is a Blender LIGHT, not a mesh — materials don't apply.
Set colour and energy directly on `lamp.data`.

---

## Key Pattern: make_principled()

```python
def make_principled(name, color, roughness, metallic=0.0, transmission=0.0):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    nodes.clear()                              # always start clean

    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    out  = nodes.new('ShaderNodeOutputMaterial')
    links.new(bsdf.outputs['BSDF'], out.inputs['Surface'])

    bsdf.inputs['Base Color'].default_value = (*color, 1.0)
    bsdf.inputs['Roughness'].default_value  = roughness
    bsdf.inputs['Metallic'].default_value   = metallic
    if transmission > 0:
        bsdf.inputs['Transmission Weight'].default_value = transmission
    return mat
```

**Why `nodes.clear()`?** Via the TCP bridge, if you try to set values on
existing nodes from a previous run, Blender may have stale node references.
Always clearing and rebuilding guarantees the node tree is in a known state.

---

## Problem Encountered: LampGlow has no `.materials`

**Error:** `'PointLight' object has no attribute 'materials'`

**Cause:** LampGlow is a `LIGHT` type object in Blender — light objects have
`obj.data` as a Light datablock, not a Mesh. Materials are a Mesh feature only.

**Fix:** Check `obj.type != 'MESH'` before calling `obj.data.materials`.
For lights, set colour via `lamp.data.color` directly.

---

## Prompt Engineering Insight — Surface Description Language

Write material prompts in artist/cinematographer language:

| Instead of... | Say... |
|--------------|--------|
| `roughness=0.15` | "slightly glossy, like a glazed ceramic mug" |
| `metallic=0.9, roughness=0.35` | "brushed steel, not shiny chrome, more industrial" |
| `transmission=0.85` | "frosted glass — you can see light through it but not detail" |
| `roughness=0.90` | "matte as chalk or rough plaster" |

Claude maps surface adjectives to PBR values automatically. The prompt doesn't
need numbers — it needs **material identity**.

---

## Final Scene Material State

| Object | Material | Roughness | Metallic | Notes |
|--------|----------|-----------|----------|-------|
| DiningTable + 4 Legs | WalnutWood | 0.75 | 0 | Shared material |
| CoffeeMug + MugHandle | WhiteCeramic | 0.15 | 0 | Shared material |
| RedBook | RedBookCloth | 0.80 | 0 | |
| Floor | StoneConcrete | 0.85 | 0 | |
| StoneWall | AgedPlaster | 0.90 | 0 | |
| LampBase + LampPole | BrushedSteel | 0.35 | 0.9 | |
| LampGlassSphere | FrostedGlass | 0.05 | 0 | Transmission=0.85 |
| LampGlow | (LIGHT) | — | — | colour=(1,0.95,0.8), energy=60 |

---

*Completed: June 2026*
