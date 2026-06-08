"""
workflow_config.py — runtime settings for: Support-mailbox-automation
All values are read from environment variables (set in local.settings.json for local testing).
Never commit secrets to source control.
"""

import os

# Logging: set to true to log to console only (useful for local runs)
LOG_TO_CONSOLE = os.getenv("LOG_TO_CONSOLE", "true").lower() == "true"

# ---------------------------------------------------------------------------
# Azure AI Foundry — project endpoint & credentials
# ---------------------------------------------------------------------------
PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT", "")
AZURE_AI_API_KEY = os.getenv("AZURE_AI_API_KEY", "")

# Agent identifiers (name and version as deployed in Foundry)
# Support Email Intent Classifier
AGENT_ID_DETERMINE_THE_EMAIL_INTENT      = os.getenv("AGENT_ID_DETERMINE_THE_EMAIL_INTENT", "")
AGENT_VERSION_DETERMINE_THE_EMAIL_INTENT = os.getenv("AGENT_VERSION_DETERMINE_THE_EMAIL_INTENT", "1")

# ---------------------------------------------------------------------------
# MCP server endpoints
# (one variable per MCP server instance; set in local.settings.json)
# ---------------------------------------------------------------------------
MCP_MYEMAILMCPSERVER_ENDPOINT = os.getenv("MCP_MYEMAILMCPSERVER_ENDPOINT", "https://mcp-myemailmcpserver.blueisland-4facbb28.eastus.azurecontainerapps.io/mcp")

# ---------------------------------------------------------------------------
# Cosmos DB — execution tracing
# ---------------------------------------------------------------------------
COSMOS_DB_ENDPOINT = os.getenv("COSMOS_DB_ENDPOINT", "")
COSMOS_DB_DATABASE = os.getenv("COSMOS_DB_DATABASE", "")
COSMOS_DB_KEY      = os.getenv("COSMOS_DB_KEY", "")
WORKFLOW_ID        = os.getenv("WORKFLOW_ID", "")
WORKFLOW_NAME      = os.getenv("WORKFLOW_NAME", "")

