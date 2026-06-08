# Lesson 1.4 — Reading Blender's Python API Docs via Claude

## Concept

Claude has access to Blender's full Python API documentation bundled with the MCP server. This means you can ask Claude about any Blender feature and it will look up the exact API call rather than guessing.

This is one of the most powerful aspects of the Blender MCP setup — Claude is not working from memory alone. It reads the actual docs.

---

## Why This Matters

Blender's API is massive. Even experienced Blender Python developers look things up constantly. With Claude:

- You describe what you want in English
- Claude searches the API docs for the right call
- Claude uses the correct parameters, enums, and types
- You get working code on the first try (usually)

---

## The API Doc Tools

| Tool | When Claude uses it |
|------|-------------------|
| `get_python_api_docs` | Reads a specific module/class page |
| `search_api_docs` | Searches across all API docs for a keyword |
| `search_manual_docs` | Searches the Blender user manual |

---

## How to Trigger Doc Lookups

You can explicitly ask Claude to check the docs:

```
Before doing anything, look up the API docs for bpy.ops.mesh and tell me what primitive shapes are available.
```

Or ask about a specific feature:
```
What are the available material node types in Blender's Python API?
```

Or ask Claude to show you the code it's going to run:
```
What Python code would you use to add a subdivision surface modifier? Show me before running it.
```

---

## Live Demo

### Step 1: API Discovery
```
Search the Blender Python API docs for 'particle system' and tell me what operators and properties are available.
```

### Step 2: Learn a new feature
```
Look up how to use bpy.ops.object.modifier_add and explain what modifiers are available and how to apply them.
```

### Step 3: Apply what you learned
```
Add a Subdivision Surface modifier to MyCube with 3 levels of subdivision, then take a screenshot.
```

---

## The "Show Me First" Technique

A great habit: ask Claude to show you the code before running it.

```
Write the Python code to add an array modifier to MyCube that creates 5 copies in the X direction. Show me the code first, then I'll tell you to run it.
```

This gives you:
- A learning opportunity (you see the bpy code)
- A chance to catch mistakes before they run
- A reusable snippet you can save to `/scripts`

---

## Your Turn

1. Ask Claude to search the API docs for `bpy.ops.curve` — learn what curve types exist
2. Ask Claude to look up how to add a text object in Blender
3. Add a 3D text object to your scene that says your name, using only prompts
4. Save the Python code Claude used to `scripts/add-text-object.py`

---

## Key Takeaways

- Claude reads the real Blender API docs — it doesn't guess
- You can ask Claude to show code before running it
- The "show me first" technique is great for learning
- Every script Claude generates can be saved and reused

---

## Next Lesson
[1.5 — Prompt Engineering: Specificity vs. Vagueness](lesson-1.5.md)
