# Lesson 2.2 — Materials and Colors

## Learning Goals
- Understand the Principled BSDF shader and its key parameters
- Apply physically-based (PBR) materials to every object in the scene
- Use color, roughness, metallic, and transmission to describe real-world surfaces
- Write clear material prompts using surface-description language

---

## Theory: Principled BSDF

Blender's **Principled BSDF** shader is a single node that mimics how light
behaves on real surfaces. You only need 4 parameters for most materials:

| Parameter | Range | Meaning |
|-----------|-------|---------|
| Base Color | RGB 0–1 | Albedo — the raw colour of the surface |
| Roughness | 0–1 | 0 = mirror smooth, 1 = fully diffuse/matte |
| Metallic | 0–1 | 0 = non-metal (plastic, wood), 1 = metal |
| Transmission | 0–1 | 0 = opaque, 1 = fully transparent glass |

### The Node Tree Pattern (always use this via TCP bridge)
```python
mat = bpy.data.materials.new(name="WalnutWood")
mat.use_nodes = True
nodes = mat.node_tree.nodes
links = mat.node_tree.links

nodes.clear()  # always start clean

bsdf   = nodes.new('ShaderNodeBsdfPrincipled')
output = nodes.new('ShaderNodeOutputMaterial')
links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])

bsdf.inputs['Base Color'].default_value  = (0.12, 0.06, 0.02, 1.0)
bsdf.inputs['Roughness'].default_value   = 0.75
bsdf.inputs['Metallic'].default_value    = 0.0
```
> RULE: Always `nodes.clear()` then rebuild. Never patch existing nodes —
> the TCP bridge may see stale state and produce invisible materials.

---

## Scene Material Plan

| Object | Surface | Color (RGB) | Roughness | Metallic | Notes |
|--------|---------|-------------|-----------|----------|-------|
| DiningTable, TableLeg_1–4 | Dark walnut wood | (0.12, 0.06, 0.02) | 0.75 | 0 | Matte grain |
| Floor | Stone/concrete | (0.35, 0.32, 0.28) | 0.85 | 0 | Rough surface |
| StoneWall | Aged plaster | (0.55, 0.50, 0.44) | 0.90 | 0 | Warm neutral |
| RedBook | Fabric/cloth cover | (0.55, 0.05, 0.04) | 0.80 | 0 | Deep red matte |
| CoffeeMug | White ceramic | (0.92, 0.92, 0.92) | 0.15 | 0 | Slightly glossy |
| MugHandle | White ceramic | (0.92, 0.92, 0.92) | 0.15 | 0 | Match mug |
| LampBase | Brushed steel | (0.6, 0.6, 0.6) | 0.35 | 0.9 | Metallic |
| LampPole | Brushed steel | (0.6, 0.6, 0.6) | 0.35 | 0.9 | Metallic |
| LampGlassSphere | Frosted glass | (0.95, 0.92, 0.85) | 0.05 | 0 | Transmission=0.85 |
| LampGlow | Emission | (1.0, 0.95, 0.8) | — | — | Warm white emission |

---

## Prompt Engineering Insight — Surface Description Language

Instead of specifying raw numbers, describe surfaces as you would to an artist:

> "The dining table should look like aged dark walnut — deep brown almost
>  black, matte finish, warm wood grain. Not shiny at all."

Claude translates this to:
- Base Color ≈ (0.12, 0.06, 0.02) — very dark warm brown
- Roughness ≈ 0.75 — matte
- Metallic = 0 — definitely not metal

The key is that **physical properties map to real-world adjectives**:
- "Glossy" → lower roughness
- "Matte / diffuse" → higher roughness
- "Metallic / chrome" → metallic near 1
- "Frosted / translucent" → transmission + roughness combo
- "Glowing / emissive" → Emission shader

---

## Tasks

1. Apply walnut material to DiningTable + all 4 legs (shared material)
2. Apply ceramic material to CoffeeMug + MugHandle (shared material)
3. Apply book cloth material to RedBook
4. Apply stone/concrete to Floor
5. Apply aged plaster to StoneWall
6. Apply brushed steel to LampBase + LampPole
7. Apply frosted glass to LampGlassSphere
8. Apply warm emission to LampGlow
9. Verify all objects have non-default materials

---

*Lesson 2.2 — June 2026*
