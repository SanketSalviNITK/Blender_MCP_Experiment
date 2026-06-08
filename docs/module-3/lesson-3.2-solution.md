# Lesson 3.2 — Solution & Notes
## Multi-step Scene Building (Agent Does It All)

## What We Built
A complete bookshelf with 17 books built from a 30-word brief.
The agent read the scene, derived all dimensions, built the frame and books,
caught a floating-book bug, self-corrected, and reported all checks PASS.

---

## Final Bookshelf Specs (all agent-derived)

| Property | Value | How derived |
|----------|-------|-------------|
| Position | X=0, Y=6.7, Z=0 | Wall at Y=7, centred on scene |
| Width | 1.4m | Fits between dining table leg extent (±1.4m) |
| Height | 1.8m | Taller than dining table (0.78m) — room scale |
| Depth | 0.28m | Standard bookshelf depth (real-world knowledge) |
| Shelves | 4 at Z=0.4/0.8/1.2/1.6 | Evenly spaced |
| Material | WalnutWood | Reused — "same walnut" in brief |
| Books | 17 across 4 shelves | 6 colour variants, varying height/width |

---

## Bug Found and Fixed by Agent

**Bug:** 5 books on shelf 3 were floating at Z=1.63 instead of Z=1.23.

**Cause:** Book names `Book_S3_1` through `Book_S3_5` were colliding with
previously created objects, causing Blender to rename new ones `Book_S3_x.001`
and place them in the wrong Z position.

**Fix:**
```python
# Delete all .001 suffix duplicates
to_delete = [o for o in bpy.data.objects if o.name.endswith('.001')]
bpy.ops.object.select_all(action='DESELECT')
for obj in to_delete:
    obj.select_set(True)
bpy.ops.object.delete()
```

**Lesson:** CHECK steps are what make agents reliable. Without the
floating-book check, the bug would have been invisible.

---

## The Brief → Output Gap

| Brief says | Agent produced |
|-----------|----------------|
| "bookshelf against back wall" | X=0, Y=6.7 — centred, 0.3m from wall |
| "same walnut wood" | reused WalnutWood material |
| "proportionate height" | 1.8m (2.3× the dining table height) |
| "mix of books" | 17 books, 6 colours, varying 0.20–0.33m heights |
| "visible from camera" | centred on back wall — confirmed in camera frame |

---

## Scene After Lesson 3.2

| Collection | Count | New |
|-----------|-------|-----|
| Environment | 2 | — |
| DiningSet | 13 | SideTable + 4 legs added in 3.1 |
| Lamp | 4 | — |
| Lighting | 4 | — |
| Cameras | 1 | — |
| **Bookshelf** | **26** | **NEW** |
| **Total** | **50** | |

---

*Completed: June 2026*
