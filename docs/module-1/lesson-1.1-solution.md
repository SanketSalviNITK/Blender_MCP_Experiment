# Lesson 1.1 — Solution & Setup Notes

## What We Did
Verified and established a live connection between Claude Code and Blender 5.0.1 using the MCP addon and a custom TCP bridge script.

---

## Problems Faced & How We Solved Them

### Problem 1: Blender MCP Add-on Not Found
**Issue:** The Blender MCP add-on was not available in Blender's Add-on preferences list.

**Cause:** The add-on was never installed — it needs to be downloaded separately from GitHub.

**Solution:**
1. Downloaded `addon.py` from [https://github.com/ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp)
2. In Blender → **Edit → Preferences → Add-ons → Install** → selected `addon.py`
3. Alternatively, opened the **Script Editor** in Blender, pasted/loaded `addon.py`, and clicked **Run Script**

---

### Problem 2: MCP Server Timing Out
**Issue:** Even after the addon was running and showing `"BlenderMCP server started on localhost:9876"` in the Blender console, every call from Claude Code returned:
```
Error: MCP error -32001: Request timed out
```

**Cause:** Two things were happening:
- **Stale connections** — old Python processes were holding the connection slot, blocking new ones
- **Protocol mismatch** — Claude Code's built-in `mcp__Blender__*` tools use the standard MCP protocol (JSON-RPC), but the Blender addon uses a simpler raw TCP JSON protocol. They couldn't understand each other.

**Solution — Kill stale processes:**
```powershell
netstat -ano | findstr "9876"       # find PIDs connected to port 9876
Stop-Process -Id <PID> -Force       # kill stale Python processes
```

---

### Problem 3: Protocol Mismatch Between CCD Blender Tools and the Addon
**Issue:** The built-in `mcp__Blender__*` tools in Claude Code (FleetView/CCD) use a different wire protocol than what the `ahujasid/blender-mcp` addon expects. Every request timed out even with a clean port.

**Verified with a raw TCP test:**
```powershell
$client = New-Object System.Net.Sockets.TcpClient('localhost', 9876)
$stream = $client.GetStream()
$cmd = '{"type":"get_scene_info"}'
# ... send and read response
# Result: {"status": "success", "result": {"name": "Scene", ...}}
```
This proved Blender was responding correctly — the issue was only the built-in tools.

**Solution:** Installed the `blender-mcp` Python bridge package and created a custom helper script `blender_cmd.py` that Claude Code uses to communicate with Blender via the correct raw TCP JSON protocol.

```bash
pip3 install blender-mcp
```

---

## Final Working Setup

### Architecture
```
Claude Code
    ↓
blender_cmd.py  (TCP client, raw JSON)
    ↓  port 9876
Blender addon.py  (TCP server)
    ↓
bpy (Blender Python API)
    ↓
Blender 3D Scene
```

### How to Start Each Session
1. Open **Blender 5.0.1**
2. Go to **Scripting** workspace → open `addon.py` → click **▶ Run Script**
3. Confirm console shows:
   ```
   Server thread started
   BlenderMCP server started on localhost:9876
   BlenderMCP addon registered
   ```
4. Open Claude Code in `C:\Users\ARVR\Documents\ARVRProjects\Blender_MCP`
5. Connection is ready ✅

### Test the Connection
```bash
python3 blender_cmd.py --scene
```
Expected output:
```json
{
  "name": "Scene",
  "object_count": 3,
  "objects": [
    {"name": "Cube", "type": "MESH", "location": [0.0, 0.0, 0.0]},
    {"name": "Light", "type": "LIGHT", "location": [4.08, 1.01, 5.9]},
    {"name": "Camera", "type": "CAMERA", "location": [7.36, -6.93, 4.96]}
  ]
}
```

### blender_cmd.py Usage
```bash
# Get scene info
python3 blender_cmd.py --scene

# Run any Python/bpy code
python3 blender_cmd.py "import bpy; bpy.ops.mesh.primitive_cube_add(location=(2,0,0))"

# Check Blender version
python3 blender_cmd.py "import bpy; print(bpy.app.version_string)"
```

---

## Key Takeaway from Lesson 1.1

> The MCP connection between Claude and Blender is not automatic — it requires a running addon in Blender AND a compatible bridge on the Claude Code side. Once set up, Claude can read and control the entire Blender scene using natural language.

**Blender version confirmed:** 5.0.1
**Addon version:** 1.2 (ahujasid/blender-mcp)
**Bridge:** `blender_cmd.py` (custom TCP client)

---

*Completed: June 2026*
