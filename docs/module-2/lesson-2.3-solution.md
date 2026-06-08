# Lesson 2.3 — Solution & Notes
## Lights and Cameras

## What We Covered
Built a proper **three-point lighting rig** for the dining table scene and
configured the camera for a cinematic, shallow-DOF product shot.
Learned to describe lighting with cinematography language instead of raw numbers.

---

## The Three-Point Lighting Rig

```
                    [RimLight]
                        ↓ (from behind, above)
        [WindowLight] → [SCENE] ← [FillLight]
           KEY              SUBJECT       FILL
        (warm, strong)               (cool, soft)
                        [LampGlow]
                       (practical, warm)
```

### Light 1 — WindowLight (KEY)
```python
win.location = (-6.0, -1.0, 4.5)
win.rotation_euler = (math.radians(55), 0, math.radians(-35))
win.data.energy = 600
win.data.color  = (1.0, 0.88, 0.65)   # warm golden afternoon
win.data.size   = 3.0                   # large = soft shadows
```
**Role:** Dominant light source. Warm golden colour simulates late-afternoon
sunlight streaming through a window. Large size = soft, painterly shadows.

### Light 2 — FillLight (FILL) — new
```python
fill_obj.location = (5.0, 2.0, 3.0)
fill_obj.rotation_euler = (math.radians(45), 0, math.radians(130))
fill_obj.data.energy = 80
fill_obj.data.color  = (0.72, 0.82, 1.0)   # cool blue-grey
fill_obj.data.size   = 2.5
```
**Role:** Opposite side from key. Prevents pure black shadows — lifts them to
a cool blue. Real rooms have ambient bounce from sky or cool walls.
Energy 80 = about 1/7 of key. Visible but not competitive.

### Light 3 — RimLight (RIM) — new
```python
rim_obj.location = (0.0, 5.5, 5.0)
rim_obj.rotation_euler = (math.radians(130), 0, 0)
rim_obj.data.energy = 150
rim_obj.data.color  = (1.0, 0.92, 0.75)   # warm rim
rim_obj.data.size   = 2.0
```
**Role:** Behind and above the scene. Creates a warm edge highlight on the
table and objects. Visually separates the table from the StoneWall behind it.

### Light 4 — LampGlow (PRACTICAL)
```python
lamp.data.energy = 80
lamp.data.color  = (1.0, 0.95, 0.8)
```
**Role:** The table lamp in the scene — a "practical" light (one that's visible
as a prop AND emits light). Warm white, low energy — just enough to see the
lamp is on without blowing out the scene.

---

## Final Lighting Summary

| Name | Type | Energy | Colour | Role |
|------|------|--------|--------|------|
| WindowLight | AREA 3m | 600 | (1.0, 0.88, 0.65) warm | Key |
| FillLight | AREA 2.5m | 80 | (0.72, 0.82, 1.0) cool | Fill |
| RimLight | AREA 2m | 150 | (1.0, 0.92, 0.75) warm | Rim/Back |
| LampGlow | POINT | 80 | (1.0, 0.95, 0.8) warm | Practical |

---

## Camera Setup

```python
cam_obj.location       = (5.0, -5.8, 2.4)
cam_obj.rotation_euler = (math.radians(78), 0, math.radians(43))
cam_obj.data.lens      = 85.0
cam_obj.data.dof.use_dof        = True
cam_obj.data.dof.aperture_fstop = 1.8
cam_obj.data.dof.focus_distance = dist   # calculated to mug: ~8.46m
```

### Why 85mm?
- 85mm is the classic portrait/product focal length
- Minimal perspective distortion (objects don't look stretched)
- Naturally compresses background — wall feels closer and more present
- Standard for product photography and food photography

### Why f/1.8?
- Very wide aperture = very shallow depth of field
- Mug is sharp, book slightly soft, wall beautifully blurred (bokeh)
- Creates that "expensive" cinematic look

### DOF Focus Distance
```python
dist = (cam_obj.location - mug_obj.location).length
cam_obj.data.dof.focus_distance = dist
```
Always **calculate from actual positions**, not guessing. The mug is at
(-0.9, 0.05, 0.82), camera at (5, -5.8, 2.4) → 8.46m. Any hardcoded
number would drift if the mug ever moved.

---

## Prompt Engineering Insight — Cinematography Language

| Mood you want | Prompt phrase | What Claude does |
|--------------|---------------|-----------------|
| Cosy evening | "warm amber practicals, barely any ambient" | Key=low warm, fill=very dim, rim=off |
| Bright studio | "clean white three-point, no colour cast" | All lights neutral white, balanced |
| Dramatic | "one hard key from above, rest in shadow" | Key=very high, no fill, no rim |
| Golden hour | "warm window light, long shadows" | Key=warm high-angle area, fill=cool low |

**The rule:** lighting has an **emotional temperature** — warm = cosy/intimate,
cool = clean/sterile/sad. Name the mood first, then describe light positions.

---

## Rules Learned

1. **Three-point rig is the baseline** — Key (dominant) + Fill (soften shadows)
   + Rim (separate from background). Add/remove from there.

2. **Colour temperature tells the story** — warm key + cool fill = golden hour.
   Cool key + warm fill = overcast/moonlit.

3. **Calculate DOF focus distance programmatically** —
   `(cam.location - subject.location).length` always stays accurate.

4. **Practical lights are props that also emit** — their energy should be low
   enough to feel realistic, not blow out the scene.

5. **Area light size controls shadow softness** — 3m area = very soft,
   diffused shadows. 0.1m area = hard, sharp shadows.

---

*Completed: June 2026*
