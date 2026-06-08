# Lesson 2.3 — Master Lights & Camera Prompt

> Set up a three-point lighting rig and cinematic camera for the rustic
> dining table scene. Run after materials are applied (Lesson 2.2).

---

## The Prompt

```
Set up a three-point interior lighting rig for the dining table scene.
The mood is: warm late-afternoon, cosy, like a restaurant or study.
The camera is a cinematic 85mm portrait lens focused on the coffee mug.

LIGHTS:

WindowLight (KEY — already in scene, upgrade it):
  - type: AREA, size: 3m
  - location: (-6, -1, 4.5), rotation: (55°, 0°, -35°)
  - energy: 600, color: (1.0, 0.88, 0.65)  ← warm golden afternoon
  - Role: dominant light, from upper-left (window side)

FillLight (FILL — add new):
  - type: AREA, size: 2.5m
  - location: (5, 2, 3), rotation: (45°, 0°, 130°)
  - energy: 80, color: (0.72, 0.82, 1.0)   ← cool blue-grey bounce
  - Role: lifts shadows on right side, ambient room bounce

RimLight (RIM — add new):
  - type: AREA, size: 2m
  - location: (0, 5.5, 5), rotation: (130°, 0°, 0°)
  - energy: 150, color: (1.0, 0.92, 0.75)  ← warm backlight
  - Role: separates table from StoneWall, creates edge highlight

LampGlow (PRACTICAL — already in scene):
  - energy: 80, color: (1.0, 0.95, 0.8)
  - Role: table lamp — visible prop that emits light

CAMERA (SceneCamera — already in scene):
  - location: (5, -5.8, 2.4)
  - rotation: (78°, 0°, 43°)
  - lens: 85mm
  - DOF: use_dof=True, f-stop=1.8
  - focus_distance: calculate as (cam.location - mug.location).length
  - Role: 3/4 front angle, slightly elevated, focused on coffee mug

VERIFICATION:
  - Print all lights: name | type | energy | color
  - Print camera: lens, f-stop, focus_distance
  - Confirm FillLight and RimLight exist in bpy.data.objects
```

---

## Core Pattern — Add or Update a Light

```python
import bpy, math

# Update existing
win = bpy.data.objects.get('WindowLight')
win.data.energy = 600
win.data.color  = (1.0, 0.88, 0.65)

# Add new
light_data = bpy.data.lights.new(name='FillLight', type='AREA')
light_obj  = bpy.data.objects.new('FillLight', light_data)
bpy.context.scene.collection.objects.link(light_obj)
light_obj.location = (5.0, 2.0, 3.0)
light_data.energy  = 80

# Camera DOF — always calculate distance
cam = bpy.data.objects.get('SceneCamera')
mug = bpy.data.objects.get('CoffeeMug')
cam.data.dof.focus_distance = (cam.location - mug.location).length
```

---

## PE Insight — Mood-First Lighting Language

Describe the **emotional temperature** of the scene first:
- "Warm, cosy, late afternoon" → warm key, cool fill, low energy
- "Clean product studio" → three neutral whites, balanced
- "Dramatic noir" → one hard key, all shadows, no fill

Then add direction: "window from the left", "backlight from above".
Claude maps mood + direction → light types, colours, energies.

---

*Recorded: June 2026 — Lesson 2.3*
