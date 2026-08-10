import json
import os
import socket
import subprocess
import sys

def is_port_in_use(port: int, host: str = "127.0.0.1") -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) == 0

def run_flask_api(script_path: str, port: int = 5000, host: str = "127.0.0.1", debug: bool = True) -> str:
    abs_path = os.path.abspath(script_path)
    if not os.path.exists(abs_path):
        return f"Error: Target script not found at '{abs_path}'"

    if is_port_in_use(port, host):
        return f"Error: Port {port} on {host} is already in use."

    env = os.environ.copy()
    env["FLASK_APP"] = abs_path
    env["FLASK_RUN_PORT"] = str(port)
    env["FLASK_RUN_HOST"] = host
    if debug:
        env["FLASK_DEBUG"] = "1"

    cmd = [sys.executable, "-m", "flask", "run"]
    
    try:
        proc = subprocess.Popen(
            cmd,
            env=env,
            cwd=os.path.dirname(abs_path) or None,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            start_new_session=True if os.name != "nt" else False
        )
        return (
            f"Flask API successfully launched.\n"
            f"- PID: {proc.pid}\n"
            f"- Target: {abs_path}\n"
            f"- URL: http://{host}:{port}"
        )
    except Exception as e:
        return f"Failed to execute Flask process: {str(e)}"

def handle_request(request: dict):
    # Notifications (messages without an 'id') must not yield a response
    if "id" not in request:
        return None

    req_id = request.get("id")
    method = request.get("method")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "flask-launcher-py39",
                    "version": "1.0.0"
                }
            }
        }

    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [{
                    "name": "run_flask_api",
                    "description": "Launches a Python Flask application on a background process.",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "script_path": {"type": "string", "description": "Path to app.py"},
                            "port": {"type": "integer", "default": 5000},
                            "host": {"type": "string", "default": "127.0.0.1"},
                            "debug": {"type": "boolean", "default": True}
                        },
                        "required": ["script_path"]
                    }
                }]
            }
        }

    elif method == "tools/call":
        params = request.get("params", {})
        if params.get("name") == "run_flask_api":
            args = params.get("arguments", {})
            output = run_flask_api(**args)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": output}]
                }
            }
        
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32601,
                "message": f"Tool '{params.get('name')}' not found"
            }
        }

    # Fallback for unknown request methods
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {
            "code": -32601,
            "message": f"Method '{method}' not found"
        }
    }

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            if res is not None:
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()
        except json.JSONDecodeError:
            continue

if __name__ == "__main__":
    main()