# Lesson 2.5 — Chain-of-Thought Prompt Templates

> Reference card for the 4 CoT patterns. Copy-paste as needed.

---

## Pattern 1 — Inspect → Act → Verify
*Use when modifying existing scene state*

```
STEP 1 — INSPECT:
  Read and print current values for [object/property list].
  Show me the before state clearly.

STEP 2 — ACT:
  Change [specific property] on [specific object] to [exact value].
  Touch ONLY the listed objects. Leave everything else unchanged.
  Print: "[Object] | [property] | [old] -> [new]"

STEP 3 — VERIFY:
  Re-read the same properties from step 1.
  Print PASS if within 0.001 of target, FAIL otherwise.
```

---

## Pattern 2 — Plan → Execute → Report
*Use when making multiple changes*

```
PLAN:
  I will make these changes:
  1. [Object A] — [property] — [change]
  2. [Object B] — [property] — [change]
  3. [Object C] — [property] — [change]

EXECUTE:
  Apply each change in order.
  After each: print "[Object] | [property] | [before] -> [after] | DONE"

REPORT:
  Print summary table of all changes.
  Final line: "[N/N changes applied successfully]"
```

---

## Pattern 3 — Decompose → Build → Assemble
*Use when building complex multi-part objects*

```
DECOMPOSE:
  Break [object name] into primitive parts:
  - [Part A]: [shape], [exact dimensions], [world position]
  - [Part B]: [shape], [exact dimensions], [world position]
  - [Part C]: [shape], [exact dimensions], [world position]

BUILD:
  Create each part using bmesh world-coordinate pattern.
  After each part: verify it exists and print its bounding box.
  Do NOT use transform_apply.

ASSEMBLE:
  Parent [Part B, C] to [Part A].
  Use matrix_world preservation during parenting.
  Print final hierarchy: [parent] -> [child list]
```

---

## Pattern 4 — Hypothesise → Test → Fix
*Use when debugging*

```
HYPOTHESIS:
  I think [object] has [issue] because [reason].
  Expected value: [X]. Current suspected value: [Y].

TEST:
  Check [specific property] on [object].
  For geometry issues: print [(obj.matrix_world @ v.co).z for v in obj.data.vertices]
  For material issues: print node tree state
  Print: "Hypothesis CONFIRMED" or "Hypothesis DENIED"

FIX (only if confirmed):
  [Exact fix with values — do NOT guess or change other things]
  Verify after fix.
```

---

## Universal Template (combine all patterns)

```
## GOAL
[One sentence: what the scene should look like after this runs]

## CONSTRAINTS
- Do NOT use transform_apply (TCP bridge issue — will reset locations)
- Do NOT modify objects not explicitly listed below
- All positions in world coordinates (metres)
- Use bmesh world-coordinate pattern for any new geometry
- Use math.radians() for all rotation values

## STEP 1 — READ STATE
Print current values for:
- [Object A]: [properties]
- [Object B]: [properties]

## STEP 2 — [MAIN ACTION]
[What to do, with exact values]
Print each change as: "[Object] | [property] | [old] -> [new]"

## STEP 3 — [SECONDARY ACTION if needed]
[What to do]

## STEP 4 — VERIFY
Re-read all changed properties.
Print PASS/FAIL for each.
Final line: "[X/N checks passed]"
```

---

## Prompt Quality Examples

### ❌ Level 1 — Too vague
```
Make the table scene nicer.
```

### ❌ Level 2 — No verification
```
Rotate the table 5 degrees on Z.
```

### ✅ Level 4 — Scoped + verified
```
Rotate DiningTable 5 degrees on Z axis.
Verify all 4 legs also show world rotation Z = 5 degrees (they are children).
Print PASS/FAIL for each leg.
```

### ✅ Level 5 — Full CoT
```
STEP 1 — INSPECT: Print DiningTable and all TableLeg rotation_euler.z values.
STEP 2 — ACT: Set DiningTable.rotation_euler.z = math.radians(5).
             Call bpy.context.view_layer.update() to flush.
STEP 3 — VERIFY: Read world rotation Z for DiningTable and all 4 legs.
                 Print PASS if each is within 0.1 deg of 5.0. FAIL otherwise.
```

---

*Recorded: June 2026 — Lesson 2.5*
