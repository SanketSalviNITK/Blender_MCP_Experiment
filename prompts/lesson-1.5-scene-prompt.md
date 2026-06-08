# Lesson 1.5 — Master Scene Prompt

> A single prompt that builds the complete rustic dining table scene.
> This is the result of iterative refinement across Lesson 1.5.

---

## The Prompt

```
Build a rustic, sunlit interior scene in Blender with the following:

SETTING:
- A large flat floor plane (20x20 units) with a warm brown tone (roughness 0.85)
- A stone wall background plane behind the scene, soft grey tone (roughness 0.95)

DINING TABLE (centre of scene):
- Dark walnut rectangular table, 3.0m wide x 1.5m deep x 0.06m thick
- Table top bottom surface at Z=0.72, top surface at Z=0.78
- Four square walnut legs, 0.08x0.08m cross-section, 0.72m tall
- Legs inset 0.12m from each table edge, placed at all four corners
- All leg tops must be flush with table bottom (Z=0.72) — no gaps
- Build all geometry using direct bmesh vertex placement at exact world coordinates
  (do NOT use transform_apply — it is unreliable via TCP bridge)

ON THE TABLE (all objects bottom Z = 0.78, flush with table top):
- A flat hardbound red book (0.22 x 0.16 x 0.025m) lying flat, 
  positioned at X=0.3, Y=0.1 on the table. Deep red matte material (roughness 0.65)
- A white ceramic coffee mug at X=-1.2, Y=0.05 on the table:
    - Hollow cylinder body: outer radius 0.045m, inner radius 0.038m, height 0.09m
    - Upright torus handle on the +X side: major radius 0.028m, minor radius 0.007m,
      ring in the XZ plane, vertically centred on the mug
    - Glossy white ceramic material (roughness 0.12, specular 0.9)
    - Verify mug X extent stays within table X bounds [-1.5 to 1.5]

TABLE LAMP (left of table, standalone floor lamp):
- Thin dark metal pole: 0.025m radius, 1.4m tall, at X=-3.8, Y=0
- Flat circular dark metal base: 0.18m radius, 0.04m thick, at X=-3.8, Y=0, Z=0
- Translucent glass sphere on top: 0.22m radius, at X=-3.8, Y=0, Z=1.62
  Material: mix of Principled BSDF (transmission=0.7) + Emission (strength=3, warm amber)
- Point light inside sphere: warm amber color (1.0, 0.75, 0.4), energy=120W, at Z=1.62

LIGHTING:
- Area light simulating window: position (-8, 0, 3.5), energy=800W, size=3.0m,
  rotation (60 degrees X, 0, 90 degrees Z) — diffuse daylight from left

CAMERA (medium shot, slightly low angle):
- Location: (5, -5.8, 2.4)
- Rotation: (72 degrees X, 0, 43 degrees Z)
- Focal length: 85mm
- Depth of field ON: f/1.8 aperture, focused on mug

ATMOSPHERE:
- Dust mote particle system: plane at (-3.0, 0, 2.2), 300 particles, HALO render type

VERIFICATION REQUIRED after building:
- All table leg tops flush with table bottom (gap < 0.001)
- All tabletop objects bottom Z = 0.78 (gap < 0.001)
- All tabletop objects XY bounds within table XY bounds [-1.5 to 1.5] x [-0.75 to 0.75]
- Report pass/fail for each check
```

---

## What Makes This a Level 5 Prompt

| Element | How it appears in this prompt |
|---------|------------------------------|
| **Exact dimensions** | Every object has precise measurements in metres |
| **Exact positions** | World coordinates for every object |
| **Material specs** | Roughness, metallic, transmission, emission values |
| **Constraints** | "flush with table top", "within table XY bounds" |
| **Technical notes** | "do NOT use transform_apply" — learned from debugging |
| **Verification** | Explicit pass/fail checks requested at the end |
| **Intent** | Cinematic context: focal length, DOF, lighting mood |

---

## Prompt Engineering Lessons from This Scene

### 1. Cinematic language works
Your original prompt used film direction vocabulary:
> *"A medium shot establishing the setting... diffuse light from a window to the left"*

Claude translated this directly into camera position, focal length, and area light angle.

### 2. Iterative refinement beats one perfect prompt
This scene was built across two prompts — one to establish the world, one to refine it.
Each iteration added: mug, DOF, lower camera angle, lamp glow, dust motes.

### 3. Technical constraints prevent errors
Adding *"do NOT use transform_apply — it is unreliable via TCP bridge"* 
prevents a known bug from recurring in future sessions.

### 4. Verification requests catch floating objects early
Asking Claude to *"report pass/fail for joint checks"* caught the floating
book (0.84 units above table!) and misplaced mug before they became hard to debug.

---

## Scene Object Summary

| Object | Type | Key Dimensions | Position |
|--------|------|---------------|----------|
| Floor | Plane | 20x20m | Z=0 |
| StoneWall | Plane | 20x20m | Y=6, vertical |
| DiningTable | Box | 3.0x1.5x0.06m | Z=0.72–0.78 |
| TableLeg 1–4 | Box | 0.08x0.08x0.72m | 4 corners |
| RedBook | Box | 0.22x0.16x0.025m | X=0.3, Z=0.78 |
| CoffeeMug | Hollow cylinder | r=0.045, h=0.09m | X=-1.2, Z=0.78 |
| MugHandle | Torus | major=0.028, minor=0.007m | X side of mug |
| LampPole | Cylinder | r=0.025, h=1.4m | X=-3.8 |
| LampBase | Cylinder | r=0.18, h=0.04m | X=-3.8, Z=0 |
| LampGlassSphere | UV Sphere | r=0.22m | X=-3.8, Z=1.62 |
| WindowLight | Area Light | 3m, 800W | X=-8, Z=3.5 |
| LampGlow | Point Light | 120W, amber | X=-3.8, Z=1.62 |
| SceneCamera | Camera | 85mm, f/1.8 DOF | (5,-5.8,2.4) |
| DustMotes | Particles | 300 HALO | Z=2.2 |

---

*Recorded: June 2026 — Lesson 1.5*
