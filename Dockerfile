FROM python:3.12-slim
WORKDIR /app
COPY mcp_demo_server.py /app/mcp_demo_server.py
ENTRYPOINT ["python3", "/app/mcp_demo_server.py"]
