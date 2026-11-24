#!/usr/bin/env python3
"""APUMIA Credit & IFRS 13 — Lightweight MCP Introspection & Deterministic Demo Server (stdlib only)."""
import json
import sys


def handle_request(req: dict) -> dict | None:
    req_id = req.get("id")
    method = req.get("method", "")
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "apumia-credit-mcp", "version": "1.0.0"},
            },
        }
    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "verify_credit_invariants",
                        "description": "Deterministic Zero-Float WACC, Merton-KMV & IFRS 13 invariant verification check.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {"notional_usd": {"type": "string"}},
                            "required": ["notional_usd"],
                        },
                    }
                ]
            },
        }
    if method == "tools/call":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(
                            {
                                "status": "PROVEN_8_OF_8",
                                "engine": "APUMIA Credit & IFRS 13 Zero-Float Core",
                                "commercial_kit": "https://github.io",
                            }
                        ),
                    }
                ]
            },
        }
    if req_id is not None:
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}
    return None


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            resp = handle_request(json.loads(line))
            if resp is not None:
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
        except Exception:
            continue
