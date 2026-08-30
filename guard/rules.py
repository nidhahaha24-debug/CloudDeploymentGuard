def check_public_ssh(config):
    """Check whether SSH is exposed to the public internet."""

    server = config.get("server", {})

    if server.get("port") == 22 and server.get("public_access") is True:
        return {
            "severity": "HIGH",
            "message": "SSH is exposed to the public internet.",
            "recommendation": (
                "Restrict SSH access to trusted IP addresses "
                "or use a secure management service."
            ),
        }

    return None


def check_encryption(config):
    """Check whether server encryption is enabled."""

    server = config.get("server", {})

    if server.get("encryption") is False:
        return {
            "severity": "HIGH",
            "message": "Server encryption is disabled.",
            "recommendation": "Enable encryption for production workloads.",
        }

    return None


def check_database_backup(config):
    """Check whether database backups are enabled."""

    database = config.get("database", {})

    if database.get("backup") is False:
        return {
            "severity": "HIGH",
            "message": "Database backup is disabled.",
            "recommendation": (
                "Enable automated database backups "
                "for production workloads."
            ),
        }

    return None


def check_https(config):
    """Check whether HTTPS is enabled."""

    server = config.get("server", {})

    if server.get("https") is not True:
        return {
            "severity": "MEDIUM",
            "message": "HTTPS is not enabled.",
            "recommendation": "Use HTTPS for secure application traffic.",
        }

    return None


def check_health_check(config):
    """Check whether a health check is configured."""

    server = config.get("server", {})

    if server.get("health_check") is not True:
        return {
            "severity": "MEDIUM",
            "message": "No health check is configured.",
            "recommendation": (
                "Configure a health check to detect "
                "unhealthy application instances."
            ),
        }

    return None


def check_required_tags(config):
    """Check whether required resource tags are present."""

    tags = config.get("tags", {})

    required_tags = ["owner", "environment"]

    missing_tags = [
        tag for tag in required_tags
        if not tags.get(tag)
    ]

    if missing_tags:
        return {
            "severity": "LOW",
            "message": (
                "Missing required tags: "
                + ", ".join(missing_tags)
            ),
            "recommendation": (
                "Add the required ownership and environment tags."
            ),
        }

    return None


RULES = [
    check_public_ssh,
    check_encryption,
    check_database_backup,
    check_https,
    check_health_check,
    check_required_tags,
]


def run_rules(config):
    """Run all deployment security and configuration rules."""

    findings = []

    for rule in RULES:
        result = rule(config)

        if result:
            findings.append(result)

    return findings