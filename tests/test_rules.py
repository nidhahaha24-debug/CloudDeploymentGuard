from guard.analyzer import (
    calculate_score,
    determine_status,
)
from guard.rules import (
    check_public_ssh,
    check_encryption,
    check_database_backup,
    check_https,
    check_health_check,
    check_required_tags,
)


def test_public_ssh_detection():
    config = {
        "server": {
            "port": 22,
            "public_access": True,
        }
    }

    result = check_public_ssh(config)

    assert result["severity"] == "HIGH"


def test_encryption_detection():
    config = {
        "server": {
            "encryption": False,
        }
    }

    result = check_encryption(config)

    assert result["severity"] == "HIGH"


def test_database_backup_detection():
    config = {
        "database": {
            "backup": False,
        }
    }

    result = check_database_backup(config)

    assert result["severity"] == "HIGH"


def test_https_detection():
    config = {
        "server": {
            "https": False,
        }
    }

    result = check_https(config)

    assert result["severity"] == "MEDIUM"


def test_health_check_detection():
    config = {
        "server": {
            "health_check": False,
        }
    }

    result = check_health_check(config)

    assert result["severity"] == "MEDIUM"


def test_required_tags_detection():
    config = {
        "tags": {
            "owner": "",
            "environment": "production",
        }
    }

    result = check_required_tags(config)

    assert result["severity"] == "LOW"


def test_score_calculation():
    findings = [
        {"severity": "HIGH"},
        {"severity": "MEDIUM"},
        {"severity": "LOW"},
    ]

    assert calculate_score(findings) == 65


def test_status_blocked():
    assert determine_status(50) == "BLOCKED"


def test_status_warning():
    assert determine_status(70) == "WARNING"


def test_status_pass():
    assert determine_status(90) == "PASS"