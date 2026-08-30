import yaml

from .rules import run_rules


def load_config(file_path):
    """Load a deployment configuration from a YAML file."""

    with open(file_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config or {}


def calculate_score(findings):
    """Calculate a deployment security score."""

    deductions = {
        "HIGH": 20,
        "MEDIUM": 10,
        "LOW": 5,
    }

    score = 100

    for finding in findings:
        score -= deductions.get(
            finding["severity"],
            0,
        )

    return max(score, 0)


def determine_status(score):
    """Determine whether a deployment should pass or be blocked."""

    if score >= 80:
        return "PASS"

    if score >= 60:
        return "WARNING"

    return "BLOCKED"


def analyze_config(file_path):
    """Load and analyze a deployment configuration."""

    config = load_config(file_path)

    findings = run_rules(config)

    score = calculate_score(findings)

    status = determine_status(score)

    return {
        "configuration": str(file_path),
        "score": score,
        "status": status,
        "findings": findings,
    }