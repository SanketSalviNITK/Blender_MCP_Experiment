# Lesson 4.2 — Solution & Notes

## What We Built
A dual-render pipeline: two renders from different angles, saved with timestamped names, verified via filesystem — no screenshot needed.

## Files Saved
- `experiments/render_overview_20260609.png` — SceneCamera angle (dining table)
- `experiments/render_wall_20260609.png` — Temporary wall-facing camera

## Pipeline Executed
1. **Blender MCP** → Render from SceneCamera → `render_overview_20260609.png`
2. **Blender MCP** → Create temp WallCam, render, delete cam, restore SceneCamera → `render_wall_20260609.png`
3. **Filesystem (Glob)** → Listed `experiments/*.png` → confirmed 3 files present

## Key Lessons
- Filesystem verification is **independent of Blender** — works even if Blender crashes post-render
- Temporary camera pattern: create → render → delete → restore. Clean, no scene pollution
- Tool-aware prompts name **exact file paths** upfront — Claude never has to decide where to save
- Timestamped filenames (`_20260609`) prevent overwriting and make version history readable

## Naming Convention Established
`experiments/render_<description>_YYYYMMDD.png`
