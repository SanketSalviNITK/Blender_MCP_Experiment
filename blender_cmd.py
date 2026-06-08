"""
Helper script to send commands to Blender via TCP socket.
Usage: python blender_cmd.py "<python code>"
       python blender_cmd.py --scene
       python blender_cmd.py --screenshot <output_path>
"""
import socket
import json
import sys
import base64

HOST = 'localhost'
PORT = 9876
TIMEOUT = 10

def send_command(command: dict) -> dict:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(TIMEOUT)
    client.connect((HOST, PORT))
    data = json.dumps(command).encode('utf-8')
    client.sendall(data)

    response = b''
    while True:
        chunk = client.recv(8192)
        if not chunk:
            break
        response += chunk
        try:
            result = json.loads(response.decode('utf-8'))
            client.close()
            return result
        except json.JSONDecodeError:
            continue
    client.close()
    return json.loads(response.decode('utf-8'))

def run_code(code: str) -> str:
    result = send_command({"type": "execute_code", "params": {"code": code}})
    if result.get("status") == "success":
        return result["result"].get("result", "Done")
    return f"Error: {result.get('message', 'Unknown error')}"

def get_scene() -> str:
    result = send_command({"type": "get_scene_info"})
    if result.get("status") == "success":
        return json.dumps(result["result"], indent=2)
    return f"Error: {result}"

def get_screenshot(output_path: str = None) -> str:
    code = """
import bpy, tempfile, os
path = bpy.app.tempdir + 'screenshot.png'
bpy.ops.screen.screenshot(filepath=path)
print(path)
"""
    result = send_command({"type": "execute_code", "params": {"code": code}})
    return result.get("result", {}).get("result", "Failed")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python blender_cmd.py '<code>'")
        print("       python blender_cmd.py --scene")
        sys.exit(1)

    if sys.argv[1] == "--scene":
        print(get_scene())
    elif sys.argv[1] == "--screenshot":
        path = sys.argv[2] if len(sys.argv) > 2 else None
        print(get_screenshot(path))
    else:
        code = sys.argv[1]
        print(run_code(code))
