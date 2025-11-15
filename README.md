# SRE Scripts
A series of SRE scripts made to showcase language understanding 

| Script | Language |
|--------|----------|
| backup-tool |  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) |
| KubeCTL-tool | ![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?style=for-the-badge&logo=powershell&logoColor=white) |

![Bash Script](https://img.shields.io/badge/bash_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?style=for-the-badge&logo=powershell&logoColor=white)

## PowerShell:
### KubeCTL-tool (Delete pods)
This PowerShell script automates the process of restarting multiple Kubernetes pods within a specified namespace. It reads pod names from a file and restarts each pod individually.
<br>
Usage:
```powershell
.\RestartPods.ps1 -namespace <namespace> -filename <path_to_file>
```

## Python:
### backup-tool
A cross-platform backup utility that supports both Windows and Unix systems with configurable compression and notification options.
<br>
The tool will:
1. Validate the configuration
2. Check available disk space
3. Create a compressed backup (Windows) or sync files (Unix)
4. Send notifications if configured

how to start:
```python
pip install -r requirements.txt
python3 main.py
```

## Go:
