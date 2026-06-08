# Lesson 3.5 — Agentic Brief Template

> The master template for driving full autonomous agent runs.
> Copy and fill in for any complex Blender task.

---

## The Template

```
## BRIEF
[One sentence: what you want done]

## INTENT
[2-3 sentences describing the desired feeling, mood, or result.
 Use artist/director language — not technical specs.
 Example: "The room should feel warm and lived-in, as if someone
 has been working here all evening. Nothing sterile or perfect."]

## AUTONOMY LEVEL
[ ] Guided           — I specify exact values, agent executes
[ ] Autonomous       — Agent decides everything
[x] With guardrails  — Agent decides freely within my constraints

## SCOPE

AGENT MAY TOUCH:
  - [lighting]
  - [background geometry / floor dressing]
  - [small props in specific areas]

AGENT MUST NOT TOUCH:
  - [hero objects — exact list]
  - [calibrated lights — e.g. WindowLight]
  - [camera]

## CONSTRAINTS

Spatial:
  - All new objects within X=[min] to X=[max]
  - All new objects within Y=[min] to Y=[max]

Scale:
  - Nothing taller than [X]m on table surfaces
  - Minimum size [Y]m (nothing too tiny to see)

Style:
  - Reuse existing materials where possible
  - New materials must match the room's colour temperature (warm, neutral, cool)
  - No sci-fi, fantasy, or anachronistic props

Organisation:
  - New props go in [CollectionName] collection
  - Remove from Scene Collection root after linking

## AGENT BEHAVIOUR REQUIRED

1. OBSERVE before acting — read scene state first, derive positions from geometry
2. THINK OUT LOUD — print reasoning for each decision before executing it
3. ONE STEP AT A TIME — verify each prop after building before moving to next
4. SELF-FIX — if a check fails, diagnose and correct before marking done
5. REPORT — final summary: what was added, what was changed, why

## VERIFICATION

For each new prop:
  - [ ] Object exists in bpy.data.objects
  - [ ] Bottom Z is flush with surface (gap < 0.002m)
  - [ ] XY position within scene bounds
  - [ ] Height within constraint
  - [ ] Material assigned
  - [ ] In correct collection

For protected objects:
  - [ ] [ProtectedObject1] location/rotation unchanged
  - [ ] [ProtectedObject2] energy/colour unchanged

Final line: "[N/N checks passed]"
```

---

## Filled Example — This Lesson's Brief

```
## BRIEF
Make the dining room scene feel lived-in and inhabited.

## INTENT
The scene is technically well-built but still reads as a 3D model.
Add small human touches — things people actually leave around a room.
Keep it subtle: nothing should distract from the dining table as the hero.

## AUTONOMY LEVEL
[x] With guardrails

## SCOPE

AGENT MAY TOUCH:
  - Side table surface (clear space around plant pot)
  - Floor between dining table and side table
  - Bookshelf shelves (gaps between books)

AGENT MUST NOT TOUCH:
  - SceneCamera
  - WindowLight (calibrated key light)
  - CoffeeMug, RedBook (hero props on dining table)
  - DiningTable, TableLeg_1-4

## CONSTRAINTS
Spatial:   All new objects within X=-4 to X=4
Scale:     Nothing taller than 0.5m on any table surface
Style:     Everyday domestic objects only — no decor pieces or art
Org:       Side table/floor props -> DiningSet, shelf props -> Bookshelf

## VERIFICATION
- All 4 props exist
- DiningTable rotation unchanged (5deg Z)
- WindowLight energy unchanged (600W)
- All new props within X bounds
- Heights under 0.5m
- Collections assigned
Final: "10/10 checks passed"
```

---

## Brief Writing Rules

1. **Intent before specs** — describe the feeling first, constraints second
2. **Explicit protected list** — name every object the agent must not touch
3. **Positive + negative scope** — say what to touch AND what not to touch
4. **Measurable verification** — every check must be yes/no, not subjective
5. **Behaviour instructions** — tell the agent to think out loud and self-fix

---

*Recorded: June 2026 — Lesson 3.5*
