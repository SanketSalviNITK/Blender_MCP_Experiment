# Lesson 2.3 — Lights and Cameras

## Learning Goals
- Understand the three main light types in Blender (Point, Area, Sun)
- Build a three-point lighting rig for interior scenes
- Understand camera properties: focal length, DOF, aperture
- Use the camera as a storytelling tool — what you include/exclude matters
- Write lighting prompts using cinematography language

---

## Theory: Light Types

| Type | Shape | Best For |
|------|-------|----------|
| POINT | Sphere (omni) | Lamp bulbs, candles, localised warmth |
| AREA | Rectangle/disk | Window light, soft fill, studio key light |
| SUN | Infinite parallel | Outdoor sunlight, strong directional shadows |
| SPOT | Cone | Stage lights, focused highlights |

### The Three-Point Lighting Rig
Classic cinematography setup for any scene:

```
          [KEY]
         /
[subject] ← strong, directional, creates form
         \
          [FILL]  ← soft, opposite side, lifts shadows
          
[BACKLIGHT / RIM]  ← behind subject, separates from background
```

For our interior dining scene:
- **Key light:** A large warm area light (simulates window or softbox)
- **Fill light:** Small cool area light from opposite side (ambient bounce)
- **Rim/Back:** The table lamp itself (LampGlow point light)

---

## Theory: Camera Properties

| Property | API | Effect |
|----------|-----|--------|
| Focal length | `camera.data.lens` | 85mm = portrait/product, 35mm = wider context |
| F-stop | `camera.data.dof.aperture_fstop` | Lower = more blur, f/1.8 = cinematic bokeh |
| Focus distance | `camera.data.dof.focus_distance` | Distance to sharp subject |
| Sensor | `camera.data.sensor_width` | 36mm = full-frame equivalent |

**Our scene:** 85mm, f/1.8 DOF focused on the mug — already cinematically correct.

---

## Lighting Plan for the Scene

### Current State (from Lesson 1.5)
- `LampGlow` — POINT, energy=60, warm white (1.0, 0.95, 0.8) — table lamp
- `WindowLight` — AREA, energy=800, pure white — left window

### What We'll Build
1. Upgrade `WindowLight` → warm golden-hour colour, better angle
2. Add `FillLight` — cool blue area light from right side (low energy)
3. Add `RimLight` — warm back light above scene, separates table from wall
4. Tune `LampGlow` — raise energy slightly for more lamp presence
5. Verify camera DOF is focused on the mug

---

## Tasks

1. Upgrade WindowLight (key) — warm colour, angled down at table
2. Add FillLight (soft cool bounce from right)
3. Add RimLight (warm backlight above scene)
4. Tune LampGlow energy
5. Point camera DOF focus object at CoffeeMug
6. Take a viewport render preview

---

## PE Insight — Cinematography Language for Lighting

| Description | Translation |
|-------------|-------------|
| "Warm golden afternoon window light" | AREA, energy≈600, color=(1.0,0.85,0.6) |
| "Soft cool fill, barely there" | AREA, energy≈80, color=(0.7,0.8,1.0) |
| "Warm practical lamp, strong glow" | POINT, energy≈100, color=(1.0,0.9,0.7) |
| "Rim light, separates subject from BG" | AREA/SPOT, behind subject, energy≈150 |
| "Cinematic shallow DOF on the mug" | f/1.8, focus on mug, 85mm lens |

The key rule: **describe the mood, not the numbers.**
"A cosy evening scene, one warm lamp, cool ambient from outside"
tells Claude exactly what energies and colours to use.

---

*Lesson 2.3 — June 2026*
