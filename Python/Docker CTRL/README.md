# Docker Dashboard

A modern, real-time web dashboard for monitoring and managing Docker containers. Built with FastAPI and vanilla JavaScript.

## Features

### Container Management
- **Real-time monitoring** - Auto-refreshes every 5 seconds
- **Start/Stop containers** - Quick container lifecycle control
- **Restart containers** - Restart running containers with one click
- **Remove containers** - Delete containers with confirmation prompts
- **View logs** - Display last 500 lines of container logs in a modal

### Search & Filtering
- **Search** - Find containers by name, ID, or image
- **Filter by status** - Show all, running, or stopped containers
- **Sortable columns** - Click headers to sort by ID, Image, Name, or Status

### User Interface
- **Dark/Light mode** - Toggle theme with persistent preference
- **Toast notifications** - Modern feedback for all actions
- **Responsive design** - Clean, minimal interface with Tailwind CSS
- **Container statistics** - Overview of total, running, stopped containers and unique images

## Prerequisites

- Python 3.7+
- Docker installed and running
- Docker CLI accessible from command line

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd docker-tool
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Open in browser**
   Navigate to `http://localhost:8000`

## Usage

### Viewing Containers
The dashboard automatically displays all Docker containers on your system, updating every 5 seconds.

### Managing Containers
- **Start/Stop**: Click `[start]` or `[stop]` buttons - stopping requires confirmation
- **Restart**: Click `[restart]` on running containers
- **View Logs**: Click `[logs]` to see the last 500 lines in a modal
- **Remove**: Click `[remove]` with a strong confirmation warning

### Search & Filter
- Use the search bar to filter by container name, ID, or image
- Click filter buttons (All, Running, Stopped) to filter by status
- Click column headers to sort the table
