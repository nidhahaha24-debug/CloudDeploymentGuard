# ☁️ Cloud Deployment Guard

Cloud Deployment Guard is a Python-based static analysis tool that checks deployment configuration files for common security, reliability, and configuration issues before deployment.

It analyzes YAML configuration files without modifying or deploying any cloud resources.

## ✨ Features

- 🔐 Detects publicly exposed SSH access
- 🔒 Checks server encryption settings
- 💾 Checks database backup configuration
- 🌐 Detects missing HTTPS configuration
- ❤️ Checks application health-check configuration
- 🏷️ Validates required resource tags
- 📊 Calculates a deployment security score
- 🚦 Classifies deployments as PASS, WARNING, or BLOCKED
- 📋 Generates human-readable reports
- 📦 Supports JSON output
- 🧪 Automated testing with pytest

## 🛠️ Tech Stack

- Python 3
- PyYAML
- Pytest
- YAML
- Git & GitHub

## 📁 Project Structure

```text
CloudDeploymentGuard/
│
├── guard/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── rules.py
│   └── report.py
│
├── tests/
│   └── test_rules.py
│
├── configs/
│   └── example.yaml
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md