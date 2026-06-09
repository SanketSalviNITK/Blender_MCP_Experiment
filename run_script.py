"""Send any .py file to Blender via blender_cmd protocol. Usage: python3 run_script.py <file.py>"""
import socket, json, sys

HOST, PORT, TIMEOUT = 'localhost', 9876, 120

script_file = sys.argv[1] if len(sys.argv) > 1 else 'build_lab_phase1.py'
code = open(script_file, 'r', encoding='utf-8').read()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(TIMEOUT)
client.connect((HOST, PORT))
data = json.dumps({"type": "execute_code", "params": {"code": code}}).encode('utf-8')
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
        if result.get('status') == 'success':
            print(result['result'].get('result', 'Done'))
        else:
            print('Error:', result.get('message', 'Unknown'))
        sys.exit(0)
    except json.JSONDecodeError:
        continue
