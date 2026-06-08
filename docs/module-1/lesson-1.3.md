# Lesson 1.3 — Your First Prompt: Add a Cube to the Scene

## Concept

This is where it gets real. You will control Blender for the first time using only natural language. No Python. No clicking. Just a prompt.

---

## What Claude Does Under the Hood

When you say *"add a red cube at position (2, 0, 0)"*, Claude:

1. Inspects the current scene to understand context
2. Looks up the correct `bpy` API call
3. Writes Python code like this:
```python
import bpy

bpy.ops.mesh.primitive_cube_add(location=(2, 0, 0))
obj = bpy.context.active_object
mat = bpy.data.materials.new(name="RedMaterial")
mat.diffuse_color = (1, 0, 0, 1)
obj.data.materials.append(mat)
```
4. Executes it in Blender via MCP
5. Confirms the result by checking the scene

You never see the Python unless you ask for it. But understanding it exists helps you write better prompts.

---

## The Golden Rule of First Prompts

> **Be specific about position, size, name, and color. Vague prompts = vague results.**

| Vague | Better |
|-------|--------|
| "Add a cube" | "Add a red cube named 'TestCube' at position (0, 0, 1) with scale 2" |
| "Make it bigger" | "Scale TestCube to 3x on all axes" |
| "Change the color" | "Change TestCube's material to a glossy blue" |

---

## Live Demo — Step by Step

### Step 1: Check the current scene
```
What objects are currently in the Blender scene?
```

### Step 2: Add a cube
```
Add a cube to the scene at position (0, 0, 0), name it 'MyCube', and give it a bright red material.
```

### Step 3: Verify
```
Take a screenshot of the Blender viewport so I can see the result.
```

### Step 4: Move it
```
Move MyCube to position (3, 0, 0) and scale it up by 1.5x on all axes.
```

### Step 5: Add a second object
```
Add a UV sphere named 'MySphere' at position (-3, 0, 0) with a blue metallic material.
```

---

## Your Turn

Build this scene using only prompts:
- A grey concrete floor plane (large, flat, at Z=0)
- A red cube sitting on the floor
- A yellow sphere floating 2 units above the floor
- A point light above the scene

After building it, ask:
```
Take a screenshot and describe everything you see in the scene.
```

---

## Saving Your Work

Once the scene looks good:
```
Save a summary of the objects in this scene to experiments/lesson-1-3-first-scene.md
```

---

## Key Takeaways

- Claude reads the scene, writes Python, runs it, and confirms the result
- Specific prompts = reliable results
- You can chain multiple actions in one prompt
- Always verify with a screenshot after changes

---

## Next Lesson
[1.4 — Reading Blender's Python API docs via Claude](lesson-1.4.md)
