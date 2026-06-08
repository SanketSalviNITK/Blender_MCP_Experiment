# Lesson 1.3 — Solution & Notes

## What We Built
A complete lit 3D scene using only natural language prompts — no Python written manually, no clicking in Blender.

---

## Final Scene

| Object | Type | Location | Material | Details |
|--------|------|----------|----------|---------|
| Floor | MESH | (0, 0, 0) | Grey matte | Plane, size 10, roughness 0.9 |
| RedCube | MESH | (0, 0, 1) | Solid red | 2-unit cube, bottom face at Z=0 |
| BlueSphere | MESH | (3, 0, 1) | Solid blue | Radius 1, resting on floor |
| SceneLight | LIGHT | (0, 0, 5) | — | Point light, 1000W |

---

## Prompts Used

### Prompt 1 — Floor
```
Create a flat plane named 'Floor' with dimensions 10x10 units. Set its position 
to Z=0 and apply a flat grey material/color to the surface.
```

### Prompt 2 — RedCube
```
Create a cube named 'RedCube'. Set its position to (0, 0, 1) and apply a solid 
red material to the object. Ensure it is resting on the 'Floor'.
```

### Prompt 3 — BlueSphere
```
Create a sphere named 'BlueSphere'. Set its position to (3, 0, 1) and apply a 
solid blue material to the object.
```

### Prompt 4 — SceneLight
```
Add a point light named 'SceneLight' at position (0, 0, 5). Configure the light 
intensity/energy to 1000 units to illuminate the scene.
```

---

## Issues Faced & Fixed

### Material not showing in viewport
**Problem:** Red material was assigned but not visible in Blender.

**Cause:** Blender's default viewport mode is **Solid** — it doesn't show materials.

**Fix:**
- Press `Z` in viewport → select **Material Preview**
- Or click the 🔵 sphere icon (top-right of viewport)

**Also fixed:** Rebuilt the material node tree explicitly to ensure correct wiring:
```python
nodes.clear()
bsdf = nodes.new('ShaderNodeBsdfPrincipled')
output = nodes.new('ShaderNodeOutputMaterial')
mat.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
```
Always clear and rebuild nodes rather than using the default node tree — more reliable.

---

## Key Learnings

### Z positioning for objects resting on floor
When the floor is at Z=0:
- A **cube** of size 2 → center at Z=1 (half-height = 1)
- A **sphere** of radius 1 → center at Z=1 (radius = 1)
- Formula: `Z = object_half_height`

### Material node tree pattern
```python
mat = bpy.data.materials.new(name='MyMaterial')
mat.use_nodes = True
nodes = mat.node_tree.nodes
nodes.clear()

bsdf = nodes.new('ShaderNodeBsdfPrincipled')
bsdf.inputs['Base Color'].default_value = (R, G, B, 1.0)
bsdf.inputs['Roughness'].default_value = 0.4

output = nodes.new('ShaderNodeOutputMaterial')
mat.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])

obj.data.materials.append(mat)
```
Save this to `/scripts` — it's reusable for every material.

---

## Prompt Quality Analysis

| Prompt | Specificity Score | What was good |
|--------|------------------|---------------|
| Floor | 4/5 | Named, sized, positioned, material described |
| RedCube | 5/5 | Named, positioned, material, intent ("resting on Floor") |
| BlueSphere | 4/5 | Named, positioned, material described |
| SceneLight | 5/5 | Named, positioned, energy value, purpose ("illuminate the scene") |

**Average: 4.5/5** — excellent first scene prompts.

---

*Completed: June 2026*
