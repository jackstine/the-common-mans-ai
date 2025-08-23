# MCP Server Setup Commands

## 1. Serena MCP Server
### Initial setup
You will need `uv` from python to start.
```bash
pip install uv
```

### Installation Command:
```bash
claude mcp add serena --transport stdio -- uvx --from git+https://github.com/oraios/serena serena start-mcp-server
```

### Alternative Installation:
```bash
# Clone and run locally
git clone https://github.com/oraios/serena
cd serena
uv run serena start-mcp-server
```

### Configuration:
- Global config: `~/.serena/serena_config.yml`
- Project config: `.serena/project.yml`

## 2. Sequential Thinking MCP Server

### Installation Command:
```bash
claude mcp add sequential-thinking --transport stdio -- npx -y @modelcontextprotocol/server-sequential-thinking
```

### Environment Variables:
```bash
# To disable thought logging
export DISABLE_THOUGHT_LOGGING=true
```

## 3. Claude Task Master MCP Server

### Installation Command:
```bash
claude mcp add task-master-ai --env ANTHROPIC_API_KEY=YOUR_KEY --env OPENAI_API_KEY=YOUR_KEY -- npx -y --package=task-master-ai task-master-ai
```

### Note: 
Replace `YOUR_KEY` with your actual API keys for Anthropic and OpenAI.

## 4. Playwright MCP Server

### Installation Command:
```bash
claude mcp add playwright --transport stdio -- npx @playwright/mcp@latest
```

### Alternative Standalone Server:
```bash
# Run as standalone server on port 8931
npx @playwright/mcp@latest --port 8931
```

### Key Features:
- Browser automation (Chromium, Firefox, WebKit)
- Persistent and isolated browser profiles
- Headless/headed mode support
- Network origin restrictions
- PDF generation and vision capabilities
- Browser extension for existing tabs

### Requirements:
- Node.js 18 or newer

## 5. Context7 MCP Server

Obtain an API via context7.com/dashboard

### Installation Command (Remote Server - Recommended):
- add in `API_KEY`
```bash
claude mcp add context7 --transport http context7 https://mcp.context7.com/mcp --header "CONTEXT7_API_KEY:API_KEY"
```

### Local Server Installation:
```bash
claude mcp add context7 --env CONTEXT7_API_KEY=YOUR_API_KEY -- npx -y @upstash/context7-mcp --api-key YOUR_API_KEY
```

### Smithery CLI Installation (Claude Desktop):
```bash
npx -y @smithery/cli@latest install @upstash/context7-mcp --client claude --key YOUR_SMITHERY_KEY
```

### Alternative Runtime (Bun):
```bash
claude mcp add context7 --env CONTEXT7_API_KEY=YOUR_API_KEY -- bunx -y @upstash/context7-mcp --api-key YOUR_API_KEY
```

### Key Features:
- Dynamic up-to-date documentation injection
- Version-specific code examples
- Real-time library documentation fetching
- Universal MCP client compatibility

### Usage:
Add "use context7" to your prompts to fetch current documentation for libraries mentioned in your code.

### Requirements:
- Node.js ≥ v18.0.0
- API Key from context7.com/dashboard (optional but recommended)

## Verification Commands

```bash
# List all configured MCP servers
claude mcp list

# Get details for a specific server
claude mcp get serena
claude mcp get sequential-thinking
claude mcp get task-master-ai
claude mcp get playwright
claude mcp get context7

# Remove a server if needed
claude mcp remove <server-name>
```

## References

1. **Serena**: https://github.com/oraios/serena
   - AI-powered code assistant with project indexing
   - Supports multiple contexts and transports

2. **Sequential Thinking**: https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
   - Enables step-by-step reasoning in conversations
   - Part of the official MCP servers collection

3. **Claude Task Master**: https://github.com/eyaltoledano/claude-task-master
   - Task management and automation for AI assistants
   - Requires API keys from AI providers

4. **Claude Code MCP Documentation**: https://docs.anthropic.com/en/docs/claude-code/mcp
   - Official documentation for MCP server configuration
   - Covers local, project, and user scopes

5. **Playwright MCP**: https://github.com/microsoft/playwright-mcp
   - Browser automation and web testing capabilities
   - Supports multiple browsers (Chromium, Firefox, WebKit)
   - Persistent profiles and headless/headed modes

6. **Context7 MCP**: https://github.com/upstash/context7
   - Dynamic up-to-date documentation injection
   - Fetches real-time library documentation and version-specific examples
   - Triggered by adding "use context7" to prompts
   - Prevents outdated or hallucinated code suggestions