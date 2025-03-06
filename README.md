# Google Search MCP Server

A Model Context Protocol (MCP) server that provides Google Custom Search functionality.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gradusnikov/google-search-mpc-server.git
cd google-search-mpc-server
```

2. Install dependencies:
```bash
pip install fastmcp google-api-python-client python-dotenv
```

## Configuration

Create a `.env` file in the project root with the following variables:

```
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_custom_search_engine_id
```

To obtain these credentials:
1. Create a Google Cloud project and enable the Custom Search API
2. Generate an API key from the Google Cloud Console
3. Create a Custom Search Engine at https://cse.google.com/cse/all and get its ID

## Usage

Start the server using MCP:

```bash
mcp run google_search_mcp_server.py
```

or add the server to Claude Desktop app *CLAUDE_DIRECTORY/claude_desktop_config.json*. For example if you are using Windows Subsystem for Linux (WSL) it may look like this:

```
"google-search": {
            "command": "wsl.exe",
            "args": [
                "bash",
                "-c",
                "source /home/[user]/anaconda3/etc/profile.d/conda.sh && conda activate mcp && /home/[user]/anaconda3/bin/mcp run /home/[user]/google-search-mpc-server/google_search_mcp_server.py"
            ]
        },
```

