# Lesson 1.2 — Tour of Claude Code: CLI, Tools, and Agents

## Concept

Claude Code is not just a chatbot. It's a **full agentic coding environment** that can read files, run code, browse the web, control your computer, and talk to external tools like Blender — all from a single session.

---

## The Three Layers of Claude Code

### 1. The CLI (Command Line Interface)
This is what you're using right now. You type prompts, Claude responds and takes actions. It has access to your entire file system, git, terminal, and any connected MCP servers.

**Key commands:**
```
/help          - Show available commands
/clear         - Clear the conversation context
/config        - Open settings
/memory        - View saved memories
/review        - Review current code changes
```

### 2. Tools
Tools are the individual capabilities Claude can use. Think of them as Claude's hands. Each tool has a specific job:

| Tool | Purpose |
|------|---------|
| `Read` | Read any file on your system |
| `Write` | Create or overwrite files |
| `Edit` | Make precise changes to existing files |
| `Bash` | Run shell commands |
| `Glob` | Find files by pattern |
| `Grep` | Search file contents |
| `WebSearch` | Search the internet |
| `WebFetch` | Fetch a specific URL |
| Blender MCP tools | Talk to Blender |
| Computer-use tools | Control the desktop (screenshots, clicks) |

When Claude uses a tool, you see it in the session. You can **approve or deny** any tool use.

### 3. Agents
An **agent** is Claude working autonomously across multiple steps. Instead of one prompt = one response, an agent:
- Breaks the task into sub-tasks
- Uses tools to gather information
- Makes decisions along the way
- Loops until the job is done

You'll use agents heavily from Module 3 onwards.

---

## Permission Modes

Claude Code has three permission levels:

| Mode | Behavior |
|------|---------|
| **Default** | Asks before running destructive/risky actions |
| **Auto-approve** | Runs everything without asking (faster, riskier) |
| **Manual** | You approve every single tool call |

For Blender experiments, default mode is recommended — Claude will ask before modifying your scene destructively.

---

## The Tool Call Flow

When you type a prompt, here's what happens:

```
Your prompt
    ↓
Claude understands intent
    ↓
Claude decides which tools to use
    ↓
Tools run (you see them in the session)
    ↓
Claude reads the results
    ↓
Claude responds / takes next action
```

---

## Live Demo

We will explore the tool call flow live:

**Try this prompt:**
```
Show me all the files in this project and summarize what each one does.
```

Watch which tools Claude uses (Glob, Read) and how it chains them together.

---

## Your Turn

1. Type `/help` and read through the available commands
2. Ask: `What tools do you have available right now?`
3. Ask: `What MCP servers are connected to this session?`

---

## Key Takeaways

- Claude Code = CLI + Tools + Agents working together
- Tools are Claude's hands — each one has a specific job
- You can see and approve every tool call
- Agents chain tool calls autonomously to complete complex tasks

---

## Next Lesson
[1.3 — Your first prompt: Add a cube to the scene](lesson-1.3.md)
