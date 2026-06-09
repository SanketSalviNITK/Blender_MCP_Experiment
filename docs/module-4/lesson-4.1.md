# Lesson 4.1 — What are MCP Connectors?

## Concept

MCP (Model Context Protocol) is not just one connection — it's an **ecosystem of connectors**.

Each connector is a bridge between Claude and a specific capability or system:

| Connector | What it gives Claude access to |
|-----------|-------------------------------|
| **Blender MCP** | The 3D scene — objects, materials, lights, camera, render |
| **Filesystem MCP** | Files and folders on your computer — read, write, copy, move |
| **Computer-Use** | Your actual screen — see it, click it, type into it |
| **Browser / Chrome** | Web pages — navigate, read content, interact with web apps |
| **Gmail / Calendar** | Email, events (used for notifications, logging) |
| **Custom MCP servers** | Anything you build — e.g. Hunyuan3D on localhost:8081 |

The key insight: **Claude doesn't have one tool, it has a toolbox.** The power comes from knowing which tool to reach for — and from chaining them together.

---

## The Three Tiers (How Claude Chooses)

When given a task, Claude picks tools in priority order:

```
1. Dedicated MCP  →  fastest, most precise  (e.g. mcp__Blender__ for Blender tasks)
2. Browser MCP    →  for web apps without a dedicated connector
3. Computer-Use   →  for native desktop apps, visual verification, anything else
```

You've already experienced all three tiers in this course:
- **Blender MCP** — every `execute_blender_code` call in modules 1–3
- **Filesystem MCP** — reading/writing `.glb`, `.py`, `.md` files
- **Computer-Use** — screenshots to verify scene renders visually

---

## What Makes a Good Connector?

A connector is useful when it offers:
- **Precision** — operates at the data level, not pixel level
- **Speed** — API calls are faster than simulating clicks
- **Reversibility** — can undo or inspect before committing

Computer-use is the fallback of last resort — powerful, but slow. You reach for it when nothing more precise exists.

---

## The Connector Map for This Course

```
Your Prompt
     │
     ▼
  Claude
     │
     ├──► mcp__Blender__          ← Scene manipulation
     ├──► Filesystem (Bash/MCP)   ← Save renders, load assets
     ├──► mcp__computer-use__     ← Visual verification, UI control
     ├──► Hunyuan3D (localhost)   ← AI mesh generation (custom MCP)
     └──► GitHub (gh CLI)         ← Version control, sharing
```

---

## Live Demo

We'll inspect exactly which connectors are active in this session and what each one can do — without writing a single line of Blender code.

---

## Your Turn (Prompt Engineering Exercise)

Write a prompt that explicitly names which connector Claude should use for each step of this task:

> *"I want to add a red sphere to my Blender scene, render it, save the render as a PNG to the experiments folder, and take a screenshot to confirm the file was saved."*

Think about:
- Which step needs the Blender connector?
- Which step needs the filesystem?
- Which step needs computer-use?

---

## Key Takeaways

1. MCP is an ecosystem — every capability is a named, addressable connector
2. Connectors have a priority order: dedicated > browser > computer-use
3. You've been using all three tiers since Module 1 — now you can name and direct them
4. Chaining connectors is where real pipelines are built (→ Lesson 4.4)
