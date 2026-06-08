# Lesson 1.2 — Solution & Notes

## What We Covered
A hands-on tour of Claude Code's three layers — CLI, Tools, and Agents — with live demonstrations in the Blender scene.

---

## The Three Layers — In Practice

### 1. CLI
The interface you type into. Key commands used in this course:
```
/help     - show all commands
/mcp      - check MCP server status
/memory   - view Claude's saved memories
/clear    - fresh context start
/review   - review git changes
```

### 2. Tools — Observed Firing Live
Every action Claude takes uses a tool. During this lesson these tools fired:

| Tool | When it fired |
|------|--------------|
| `Read` | Reading lesson-1.2.md when asked to summarize it |
| `Glob` | Finding files in the scripts/ folder |
| `PowerShell` | Running blender_cmd.py to add a sphere to Blender |
| `PowerShell` | Verifying the scene after adding the sphere |

**Key insight:** Tools chain automatically — Claude picks the right tool based on your prompt, runs it, reads the result, and decides what to do next. You never have to say "use PowerShell" or "use Read".

### 3. Agents
Not used yet — that's Module 3. But the foundation is clear:
- Conversational = one prompt → one response
- Agentic = one prompt → Claude plans + executes many steps autonomously

---

## Live Demos Completed

### Demo 1: Read a file and summarize it
**Prompt:** `Please read the lesson-1.2.md and summarize it`
**Tools used:** `Read`
**Result:** Claude read the file and produced a structured summary

### Demo 2: Inspect the scripts folder
**Prompt:** `What is in the scripts folder?`
**Tools used:** `Glob`
**Result:** `scripts/.gitkeep` — folder is empty, ready to fill in Module 5

### Demo 3: Add a UV Sphere to Blender ⭐
**Prompt:** `Add a UV sphere to the Blender scene at position (3, 0, 0)`
**Tools used:** `PowerShell → blender_cmd.py → Blender TCP → bpy → PowerShell (verify)`

**Full tool chain:**
```
Prompt
  ↓
PowerShell: python3 blender_cmd.py "bpy.ops.mesh.primitive_uv_sphere_add(location=(3,0,0))"
  ↓
Blender executes Python, sphere appears in viewport
  ↓
PowerShell: python3 blender_cmd.py --scene  (verification)
  ↓
Scene confirmed: 4 objects including UVSphere at (3.0, 0.0, 0.0)
```

**Scene after lesson:**
| Object | Type | Location |
|--------|------|----------|
| Cube | MESH | (0, 0, 0) |
| UVSphere | MESH | (3, 0, 0) ← added this lesson |
| Light | LIGHT | (4.08, 1.01, 5.9) |
| Camera | CAMERA | (7.36, -6.93, 4.96) |

---

## Key Takeaways

- Claude Code = CLI + Tools + Agents — three layers working together
- Tools fire automatically — you never have to name them in your prompt
- The full Blender tool chain: `Claude → PowerShell → blender_cmd.py → TCP:9876 → bpy`
- `scripts/` folder is empty and ready — we fill it from Module 5 onwards
- Agents (Module 3) = chaining many tool calls autonomously from a single prompt

---

*Completed: June 2026*
