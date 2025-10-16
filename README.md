# OpenWeather MCP Server

A Model Context Protocol (MCP) server that provides weather query tools using the OpenWeather API.

## Features

- `get_current_temperature`: Get current temperature for a city
- `get_weather_forecast`: Get weather forecast for a city

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
      "url": "https://your-app.railway.app/mcp",
      "transport": "http"
    }
  }
}
```

**Important:** MCP HTTP clients must send the header `Accept: application/json, text/event-stream` when connecting to the server.

## OpenWeather API

To get a free API key:
1. Visit [OpenWeather](https://openweathermap.org/api)
2. Create an account
3. Generate an API key

## Troubleshooting

### Error 400 - Bad Request

If you encounter a 400 error, it's likely due to one of these issues:

1. **Missing Accept Header**: The MCP client must send `Accept: application/json, text/event-stream`
2. **Missing OPENWEATHER_KEY**: Make sure you configured the environment variable in Railway
3. **Invalid API Key**: Verify your OpenWeather API key is active and valid

### Testing the Server

You can test your deployed server with curl:

```bash
# Test initialization (replace with your Railway URL)
curl -X POST \
  -H "Accept: application/json, text/event-stream" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"initialize","id":1,"params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test-client","version":"1.0"}}}' \
  https://your-app.railway.app/mcp
```

If the server is working correctly, you should see a JSON response with server info.

## Project Structure

```
railway_openweather_mcp/
├── weather_mcp_server_http.py  # Main server code
├── pyproject.toml               # Dependencies and configuration
├── uv.lock                      # UV lock file
├── Dockerfile                   # Docker configuration
├── railway.toml                 # Railway configuration
├── .env.example                 # Example environment variables
├── .gitignore                   # Git ignored files
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## License

MIT - See [LICENSE](LICENSE) file for details
