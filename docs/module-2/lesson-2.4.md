# Lesson 2.4 — Organizing a Scene (Collections & Naming)

## Learning Goals
- Understand Blender Collections — what they are and why they matter
- Move all scene objects into logical named collections
- Use naming conventions that make large scenes manageable
- Understand how collections affect render visibility and viewport toggling
- Write organisation prompts that scale to complex scenes

---

## Theory: What is a Collection?

A **Collection** in Blender is a named group of objects — like a folder in
your file system. Collections live in the **Outliner** (top-right panel).

```
Scene Collection
├── 🗂 Environment
│   ├── Floor
│   └── StoneWall
├── 🗂 DiningSet
│   ├── DiningTable
│   ├── TableLeg_1 … TableLeg_4
│   ├── RedBook
│   ├── CoffeeMug
│   └── MugHandle
├── 🗂 Lamp
│   ├── LampPole
│   ├── LampBase
│   ├── LampGlassSphere
│   └── DustMotes
├── 🗂 Lighting
│   ├── WindowLight
│   ├── FillLight
│   ├── RimLight
│   └── LampGlow
└── 🗂 Cameras
    └── SceneCamera
```

### Why Collections Matter
| Feature | Benefit |
|---------|---------|
| **Eye icon** | Hide/show whole groups in viewport instantly |
| **Camera icon** | Exclude a group from render (e.g. proxy objects) |
| **Nested collections** | Hierarchy — DiningSet > Props > RedBook |
| **Instance collections** | Duplicate a whole group as one object |
| **View layers** | Render only selected collections |

---

## Naming Conventions

Good names follow a pattern: **Category_Description_Index**

| Bad | Good | Why |
|-----|------|-----|
| `Cube.001` | `TableLeg_1` | Tells you what and which |
| `Light` | `WindowLight` | Tells you its role |
| `Material.003` | `WalnutWood` | Self-documenting |
| `Camera` | `SceneCamera` | Explicit purpose |

Our scene already uses good names — now we organise them into collections.

---

## Collection Plan

| Collection | Objects |
|-----------|---------|
| `Environment` | Floor, StoneWall |
| `DiningSet` | DiningTable, TableLeg_1–4, RedBook, CoffeeMug, MugHandle |
| `Lamp` | LampPole, LampBase, LampGlassSphere, DustMotes |
| `Lighting` | WindowLight, FillLight, RimLight, LampGlow |
| `Cameras` | SceneCamera |

---

## Tasks

1. Create 5 named collections
2. Move all objects into the correct collections
3. Remove objects from the default "Scene Collection" root
4. Verify the outliner is clean — no orphan objects at root level
5. Demonstrate hide/show a collection via Python

---

## PE Insight — Organisational Prompts Scale to Any Scene

A well-organised scene prompt looks like:
```
Organise the scene into collections:
- "Environment": all background geometry (floor, walls, sky)
- "Props": all hero objects on the table
- "Lighting": all light objects
- "Cameras": all cameras

Name everything with Category_Description convention.
No object should remain at the Scene Collection root level.
```

This prompt works for a 20-object scene OR a 2000-object scene.
The structure scales — the language doesn't change.

---

*Lesson 2.4 — June 2026*
