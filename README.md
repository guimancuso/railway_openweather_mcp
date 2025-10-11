# OpenWeather MCP Server

A Model Context Protocol (MCP) server that provides weather query tools using the OpenWeather API.

## Features

- `buscar_temperatura_atual`: Get current temperature for a city
- `buscar_previsao_tempo`: Get weather forecast for a city

## Technologies

- **Python 3.11+**
- **FastMCP**: Framework for building MCP servers
- **UV**: Modern Python package manager
- **OpenWeather API**: Weather data provider

## Deploy to Railway

### Step 1: Repository Setup

This project comes pre-configured with:
- `Dockerfile` optimized for UV
- `railway.toml` with deployment settings
- Proper `.gitignore`

### Step 2: Configure Environment Variables in Railway

In the Railway dashboard, configure the following variables:

**Required:**
- `OPENWEATHER_KEY`: Your OpenWeather API key

**Optional (if using LLM integrations):**
- `ANTHROPIC_API_KEY`: Anthropic API key
- `AWS_DEFAULT_REGION`: AWS region (e.g., us-east-1)
- `AWS_ACCESS_KEY_ID`: AWS Access Key ID
- `AWS_SECRET_ACCESS_KEY`: AWS Secret Access Key

### Step 3: Deploy

1. Connect your GitHub repository to Railway
2. Railway will automatically detect the Dockerfile
3. Configure the environment variables
4. Automatic deployment will begin

### Step 4: Get the URL

After deployment, Railway will provide a public URL for your MCP server.

## Using with MCP Clients

Configure your MCP client (such as Claude Desktop) to connect to the server:

```json
{
  "mcpServers": {
    "openweather": {
      "url": "https://your-app.railway.app",
      "transport": "http"
    }
  }
}
```

## OpenWeather API

To get a free API key:
1. Visit [OpenWeather](https://openweathermap.org/api)
2. Create an account
3. Generate an API key

## Project Structure

```
railway_openweather_mcp/
├── weather_mcp_server_http.py  # Main server code
├── pyproject.toml               # Dependencies and configuration
├── uv.lock                      # UV lock file
├── Dockerfile                   # Docker configuration
├── railway.toml                 # Railway configuration
├── .gitignore                   # Git ignored files
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## License

MIT - See [LICENSE](LICENSE) file for details
