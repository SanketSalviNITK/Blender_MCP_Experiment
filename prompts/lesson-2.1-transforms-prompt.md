# Lesson 2.1 — Master Transforms Prompt

> Apply all transforms from Lesson 2.1 to the rustic dining table scene.
> Run this after the scene from Lesson 1.5 is already built.

---

## The Prompt

```
Apply the following transforms to the existing dining table scene:

PARENTING (do this first):
- Parent TableLeg_1, TableLeg_2, TableLeg_3, TableLeg_4 to DiningTable
- Use matrix_world preservation so legs don't move during parenting:
    world_mat = leg.matrix_world.copy()
    leg.parent = table
    leg.matrix_world = world_mat

ORIGINS:
- Set origin to geometry centre for all mesh objects using bounding box centre method
- Shift mesh vertices in local space so object.location matches world centre

TRANSFORMS:
- RedBook: rotation Z = 18 degrees (casual placement)
- LampPole, LampBase, LampGlassSphere, LampGlow: rotation Y = 2 degrees (slight tilt)
- CoffeeMug + MugHandle: location.x += 0.3 (closer to book), rotation Z = -35 degrees (handle faces camera)
- RedBook: scale X = 1.3, scale Y = 1.3, scale Z unchanged (bigger book, same thickness)
- DiningTable: rotation Z = 5 degrees (legs follow via parent)
- StoneWall: location.y += 1.0 (Y=6 to Y=7, more depth)

VERIFICATION:
- Print full transform report: name, location, rotation (degrees), scale for all objects
- Call bpy.context.view_layer.update() before reading dimensions
- Confirm all 4 legs show world rotation Z = 5 degrees
```

---

## Key Rules for Transforms

```python
# Always use radians
obj.rotation_euler.z = math.radians(18)

# Always flush depsgraph after scale
bpy.context.view_layer.update()

# Parent with world matrix preservation
world_mat = leg.matrix_world.copy()
leg.parent = table
leg.matrix_world = world_mat

# Read world transform (not local)
world_rot_z = math.degrees(leg.matrix_world.to_euler().z)
```

---

*Recorded: June 2026 — Lesson 2.1*
