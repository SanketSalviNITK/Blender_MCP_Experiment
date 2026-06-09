# Lesson 4.2 — Using the Filesystem Connector

## Concept

The filesystem connector gives Claude the ability to **read, write, move, and inspect files and folders** on your computer — outside of Blender entirely.

In the context of a Blender workflow, this means:

| Task | Filesystem does this |
|------|----------------------|
| Save a render PNG to a specific folder | Write file |
| Check if a render already exists before re-rendering | Read / stat file |
| Load a .glb asset from disk into Blender | Read path → pass to Blender MCP |
| Version renders by timestamp | Read + rename/copy |
| Scan a folder for all .blend files | List directory |
| Save a generated Python script for reuse | Write file |

---

## How Claude Accesses the Filesystem

Claude has two routes:

1. **Bash tool** — shell commands (`dir`, `copy`, `move`, `mkdir`, Python scripts) — fast, flexible, scriptable
2. **Filesystem MCP** (`mcp__83f82eb0-*__*` tools) — structured file operations (read content, write, copy, metadata)

Both talk to the same files. Bash is better for bulk operations; Filesystem MCP is better for reading file content directly into Claude's context.

---

## The experiments/ Folder

From now on, all renders and scene exports live here:
```
Blender_MCP/
└── experiments/
    ├── render_wall_picture.png   ← already here from 4.1
    └── ...                       ← future renders go here
```

Convention: `render_<description>_<YYYYMMDD>.png`

---

## Live Demo

We'll build a small **render + archive pipeline**:
1. Render the current scene
2. Save with a timestamped filename
3. List the experiments folder to confirm
4. Read the file metadata (size, date)

---

## Your Turn — Prompt Engineering Exercise

Your scene now has a picture frame on the wall. Write a prompt that:

> Renders the scene **twice** — once from the current SceneCamera, once from a new angle looking directly at the stone wall — saves both with descriptive timestamped names to the experiments folder, then lists the folder contents so we can confirm both files are there.

Think about:
- How do you tell Claude to **name files** meaningfully?
- How do you ask Claude to **verify** without taking a screenshot — using only the filesystem?
- What's the difference between asking Claude to "save a render" vs. giving it the exact path?
