# Lesson 2.5 — Solution & Notes
## PE: Chain-of-Thought Prompts

## What We Covered
Learned the four CoT prompt patterns and applied each one to the live scene.
Chain-of-thought structuring is the single biggest lever for improving
Claude's output quality on complex Blender tasks.

---

## The 4 Patterns — Quick Reference

### Pattern 1: Inspect → Act → Verify
```
STEP 1 — INSPECT: Read [object/property] current values. Print them.
STEP 2 — ACT:     Change [X] to [Y]. Touch nothing else.
STEP 3 — VERIFY:  Re-read. Print PASS/FAIL.
```
**Used when:** Changing existing scene state.  
**Prevents:** Blind changes, missing context, unverified results.

---

### Pattern 2: Plan → Execute → Report
```
PLAN:    List all N changes I will make.
EXECUTE: Apply each. Print after each: "[Object] | [prop] | [before] -> [after]"
REPORT:  Final summary table. N/N done.
```
**Used when:** Multiple changes in one task.  
**Prevents:** Partial execution, lost track of what changed.

---

### Pattern 3: Decompose → Build → Assemble
```
DECOMPOSE: Break complex object into N primitive parts with exact specs.
BUILD:     Create each part. Verify each exists after creation.
ASSEMBLE:  Parent all parts. Verify hierarchy.
```
**Used when:** Building complex multi-part objects (mug, lamp, furniture).  
**Prevents:** Tangled geometry, misaligned parts, missed pieces.

---

### Pattern 4: Hypothesise → Test → Fix
```
HYPOTHESIS: "I think [X] is wrong because [Y]."
TEST:       Check the specific property. Print result.
FIX:        Only if test confirms. State exactly what will be changed.
```
**Used when:** Debugging floating objects, wrong positions, invisible materials.  
**Prevents:** Blind fixing, making things worse, changing the wrong thing.

---

## Live Results from This Lesson

### Pattern 1 result
```
WalnutWood roughness 0.75 → 0.82    PASS
WalnutWood color (0.12,0.06,0.02) → (0.09,0.045,0.015)    PASS
```

### Pattern 2 result
```
RedBook    | location.y | 0.1 -> 0.05    DONE
CoffeeMug  | rot_z      | -35.0 -> -40.0 DONE
RimLight   | energy     | 150.0 -> 180.0 DONE
```

---

## The Universal CoT Template (save this)

```
## GOAL
[One sentence describing the desired outcome]

## CONSTRAINTS
- Do NOT use transform_apply
- Do NOT touch objects not listed
- Use world coordinates (metres)
- Use bmesh world-coordinate pattern for any new geometry

## STEPS

STEP 1 — READ STATE:
  Print: [object names] with [properties to read]

STEP 2 — [ACTION]:
  [Exact change with values]
  Print each change as: "[Object] | [property] | [old] -> [new]"

STEP 3 — VERIFY:
  Re-read all changed values.
  Print PASS/FAIL for each check.
  Final line: "X/N checks passed."
```

---

## Prompt Quality Scale

| Level | Example | Score |
|-------|---------|-------|
| 1 | "Make it look good" | ★☆☆☆☆ |
| 2 | "Rotate the table" | ★★☆☆☆ |
| 3 | "Rotate DiningTable 5° on Z" | ★★★☆☆ |
| 4 | "Rotate DiningTable 5° Z. Verify legs follow. PASS/FAIL." | ★★★★☆ |
| 5 | Full CoT template with INSPECT + ACT + VERIFY + constraints | ★★★★★ |

Your prompts should **always be at level 4 or 5** for Blender work.

---

## Key Rules Learned in Module 2 (Full List)

### Geometry
- Always use bmesh world-coordinate vertex placement
- Never use transform_apply via TCP bridge
- Verify joints: `abs(leg_top_z - table_bot_z) < 0.001`

### Materials
- Always `nodes.clear()` before rebuilding node tree
- Check `obj.type == 'MESH'` before accessing `.materials`
- LIGHT objects use `obj.data.color`, not materials

### Transforms
- Always use `math.radians()` for rotation
- Always flush depsgraph: `bpy.context.view_layer.update()`
- Parent with matrix_world preservation

### Organisation
- Unlink from all collections before linking to target
- Root Scene Collection should always be empty
- Collections ≠ parent-child (both can coexist)

### Prompting
- Inspect before acting
- State constraints explicitly
- Print as you go (crash recovery)
- Verify with PASS/FAIL
- One goal per step

---

*Completed: June 2026 — Module 2 complete!*
