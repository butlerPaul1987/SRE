# Backup Tool

A cross-platform backup utility that supports both Windows and Unix systems with configurable compression and notification options.

## Features

- **Cross-platform support**: Works on both Windows and Unix systems
- **Compression**: Uses 7-Zip for Windows backups
- **Configurable**: YAML-based configuration
- **Logging**: Coloured console output with different log levels
- **Notifications**: Support for Slack, Teams, Discord, and email notifications (configurable)
- **Space validation**: Checks available disk space before backup

## Requirements

- Python 3.6+
- 7-Zip (included in `7z/` directory for Windows)
- PowerShell (Windows)
- rsync (Unix systems)

## Installation

1. Clone or download this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Edit `config.yaml` to configure your backup settings:

```yaml
app:
  name: backup-tool
  version: 1.0.0
  log_level: info
  log_directory: "path/to/logs"
  os: windows  # or "unix"

directory:
  source: "path/to/source"
  destination: "path/to/destination"
  exclude:
    - "*.log"
    - "*.tmp"

comms:
  slack:
    webhook_url: "your-slack-webhook"
    enabled: false
  # ... other notification options
```

## Usage

Run the backup tool:

```bash
python main.py
```

The tool will:
1. Validate the configuration
2. Check available disk space
3. Create a compressed backup (Windows) or sync files (Unix)
4. Send notifications if configured

## Project Structure

```
backup-tool/
├── 7z/                 # 7-Zip executables for Windows
├── log/                # Log files directory
├── modules/            # Python modules
│   ├── log.py         # Logging functionality
│   ├── messenger.py   # Notification handlers
│   ├── validator.py   # Validation functions
│   ├── windowsBackup.py # Windows backup logic
│   └── unixBackup.py  # Unix backup logic
├── config.yaml        # Configuration file
├── main.py            # Main application entry point
├── README.md          # This file
└── requirements.txt   # Python dependencies
```

## License

This project is provided as-is for backup purposes.
