# Lesson 1.5 — Prompt Engineering: Specificity vs. Vagueness

## Concept

This is your first dedicated Prompt Engineering lesson. Every module has one — they build on each other to make you a significantly more effective AI collaborator.

> **The quality of your output is directly proportional to the quality of your input.**

---

## The Spectrum of Prompts

Think of prompts on a spectrum from vague to specific:

```
VAGUE ←————————————————————————→ SPECIFIC

"Make something cool"
"Add some objects"
"Make it look better"
"Add a cube"
"Add a red cube"
"Add a red cube at position (2,0,0)"
"Add a metallic red cube named 'Hero' at position (2,0,0) with scale 1.5"
```

Vague prompts aren't always bad — sometimes you *want* Claude to be creative. But for precise 3D work, specificity matters.

---

## The 5 Elements of a Strong Blender Prompt

### 1. Object Identity
Name it. Claude will use this to reference it later.
```
❌ "Add a sphere"
✅ "Add a UV sphere named 'EarthSphere'"
```

### 2. Position & Scale
3D space is precise. Tell Claude exactly where.
```
❌ "Put it somewhere in the middle"
✅ "Place it at position (0, 0, 2) with a scale of (1.5, 1.5, 1.5)"
```

### 3. Material & Appearance
Color, roughness, metallic — be explicit.
```
❌ "Give it a nice material"
✅ "Apply a blue principled BSDF material with metallic=0.8 and roughness=0.2"
```

### 4. Context
Tell Claude what already exists or what you're building toward.
```
❌ "Add a light"
✅ "Add a point light above EarthSphere at position (0, 0, 5) with energy 1000W"
```

### 5. Verification Request
Always ask Claude to confirm.
```
✅ "...then take a screenshot so I can verify the result."
```

---

## Common Prompt Anti-Patterns

| Anti-pattern | Problem | Fix |
|-------------|---------|-----|
| "Make it better" | No clear target | "Increase the metallic value to 0.9 and reduce roughness to 0.1" |
| "Move it a bit" | Unmeasurable | "Move it 2 units along the X axis" |
| "Add some lights" | Undefined | "Add 3 point lights at positions (3,0,3), (-3,0,3), and (0,3,3) each with energy 500W" |
| Stacking too many changes | Claude may lose track | Break into separate prompts |
| No verification | You don't know if it worked | Always end with a screenshot request |

---

## The Context Sandwich Pattern

This is one of the most useful prompt patterns for 3D work:

```
[CONTEXT] Tell Claude what already exists and what you're trying to achieve.
[ACTION] Tell Claude exactly what to do.
[VERIFY] Ask Claude to confirm it worked.
```

**Example:**
```
I'm building a simple solar system scene. I already have a yellow sphere named 'Sun' 
at the origin. 

Please add a blue sphere named 'Earth' at position (5, 0, 0) with scale 0.4, 
give it a blue-green principled BSDF material (color #2E86AB), and orbit it 
around the sun by rotating it 45 degrees around the Z axis.

After you're done, take a screenshot and list all objects in the scene.
```

---

## Live Exercise

**Challenge:** Build the following scene using exactly 2 prompts (no more).

Scene target:
- A wooden table (brown box, large and flat)
- A coffee mug on the table (cylinder, white)
- A book lying flat on the table (thin box, red)
- A lamp beside the table (thin cylinder base + sphere light)

Write your 2 prompts first, then run them. Compare results with how you'd have done it in 4–5 prompts.

---

## When Vagueness is Good

Vague prompts work well when you want Claude to be creative:

```
"Create an interesting abstract sculpture using 5–8 primitive shapes. 
Be creative with the arrangement and materials."
```

The key: **be specific about the constraints, vague about the content**.

---

## Key Takeaways

- Specificity = reliability. Vagueness = creativity.
- Name everything, position everything, describe materials explicitly
- Use the Context Sandwich pattern for complex prompts
- End every prompt with a verification step
- Save prompts that work well to the `/prompts` folder

---

## Module 1 Complete!

You now understand:
- How MCP connects Claude to Blender
- The tools Claude Code has available
- How to give your first Blender commands
- How to read API docs through Claude
- How to write specific, effective prompts

**Next:** [Module 2 — Scene Basics](../module-2/overview.md)
