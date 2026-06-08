# Lesson 1.1 — What is MCP? How Claude Talks to Blender

## Concept

### The Old Way
Traditionally, to automate Blender you had to:
1. Learn Python
2. Learn the `bpy` API
3. Write scripts manually
4. Run them inside Blender's text editor

### The MCP Way
**MCP (Model Context Protocol)** is a standard that lets AI models like Claude talk directly to external tools and applications — including Blender.

Think of it like this:

```
You (natural language)
    ↓
Claude Code (understands your intent)
    ↓
MCP Server (translates to Blender commands)
    ↓
Blender (executes Python via bpy)
    ↓
Result appears in the 3D viewport
```

Claude doesn't just guess — it reads the Blender API docs, inspects your current scene, writes correct Python, and executes it live.

---

## The MCP Tools Available for Blender

When connected, Claude has access to these Blender MCP tools:

| Tool | What it does |
|------|-------------|
| `execute_blender_code` | Runs arbitrary Python in Blender |
| `get_objects_summary` | Lists all objects in the current scene |
| `get_object_detail_summary` | Gets details of a specific object |
| `get_screenshot_of_window_as_image` | Takes a screenshot of the Blender window |
| `render_viewport_to_path` | Renders the viewport and saves to a file |
| `get_python_api_docs` | Reads Blender's Python API reference |
| `search_api_docs` | Searches the API docs for a specific topic |
| `jump_to_view3d_object_by_name` | Selects and focuses an object in the viewport |

---

## Key Mental Model

> **Claude is a director. Blender is the actor. MCP is the script.**

You tell Claude *what* you want in plain English. Claude figures out *how* to do it using Blender's Python API, and MCP delivers the instructions to Blender.

---

## Live Demo

We will verify your MCP connection is working by asking Claude to:
1. List all objects currently in the Blender scene
2. Take a screenshot of the Blender window

**Try this prompt:**
```
List all the objects currently in the Blender scene and take a screenshot of the viewport.
```

---

## Your Turn

Try these prompts and observe what happens:

1. `What objects are in my Blender scene right now?`
2. `Take a screenshot of the current Blender window and describe what you see.`

---

## Key Takeaways

- MCP is the bridge between Claude and Blender
- Claude reads the scene before making changes
- You never have to write Python — Claude does it
- Every action goes through: You → Claude → MCP → Blender

---

## Next Lesson
[1.2 — Tour of Claude Code: CLI, tools, agents](lesson-1.2.md)
