from argparse import ArgumentParser

from mcp.server.fastmcp import FastMCP

# This server intentionally stays small and predictable so notebook examples
# can focus on the MCP client workflow rather than server-side complexity.
mcp = FastMCP(
    "Operations Control Plane",
    host="127.0.0.1",
    port=8765,
    json_response=True,
)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


@mcp.tool()
def planned_change_window(service: str) -> str:
    """Return the approved change window for a service."""
    windows = {
        "billing-api": "22:00 UTC",
        "identity-api": "20:00 UTC",
        "search-api": "18:00 UTC",
    }
    return windows.get(service, "Window not found")


@mcp.resource("memo://service-overview")
def service_overview() -> str:
    """Return a short operational memo."""
    return (
        "Primary region: us-east-1. "
        "Escalation path: platform-oncall. "
        "Rollback target: previous stable deployment. "
        "Maintenance notices require a 30 minute lead time."
    )


@mcp.prompt()
def release_summary(service: str, risk: str = "medium") -> str:
    """Generate a prompt for a release summary."""
    return (
        f"Write a concise release summary for {service}. "
        f"Emphasize {risk} deployment risk, monitoring, and rollback readiness."
    )


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--transport",
        choices=["stdio", "streamable-http"],
        default="streamable-http",
    )
    args = parser.parse_args()
    mcp.run(transport=args.transport)
