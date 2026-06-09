# Lesson 4.1 — Solution & Notes

## What We Built
A framed picture on the StoneWall, rendered from SceneCamera, saved to experiments/, confirmed via filesystem.

## Pipeline Executed
1. **Blender MCP** → `PictureFrame` (dark walnut cube) + `PictureCanvas` (warm ochre plane) added to wall at eye level (z≈3.4m, y≈6.79)
2. **Blender MCP** → Rendered 1280×720 from SceneCamera
3. **Filesystem** → Saved to `experiments/render_wall_picture.png`
4. **Computer-Use** → Visual confirmation of render output

## Key Lesson Learned
The base prompt ("Add a framed picture… render… save… confirm") was a good *task description* but not tool-aware.

A tool-aware version explicitly names the connector at each step:
- "Using the Blender MCP connector: add…"
- "Using the filesystem: save to `C:\...\experiments\render_wall_picture.png`"
- "Using computer-use: take a screenshot to confirm…"

## Bonus Insight
The camera was aimed at the dining table, not the wall — so the picture frame was barely visible in the render. A precise prompt would have added: *"reposition the SceneCamera to face the StoneWall before rendering."* This is the gap that Lesson 4.5 (tool-aware prompting) addresses.

## Objects Added to Scene
- `PictureFrame` — dark walnut frame, 0.64m × 0.44m, Environment collection
- `PictureCanvas` — warm ochre canvas, parented to frame, Environment collection
