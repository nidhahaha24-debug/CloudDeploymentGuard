def print_report(result):
    """Print a human-readable deployment guard report."""

    print("\n========================================")
    print("       CLOUD DEPLOYMENT GUARD")
    print("========================================")

    print(f"\nConfiguration: {result['configuration']}")

    print("\nDeployment Score")
    print("----------------")
    print(f"{result['score']}/100")

    print("\nDeployment Status")
    print("-----------------")
    print(result["status"])

    print("\nFindings")
    print("--------")

    if not result["findings"]:
        print("No issues found.")
    else:
        for finding in result["findings"]:
            print(
                f"\n{finding['severity']}: "
                f"{finding['message']}"
            )

            print(
                f"Recommendation: "
                f"{finding['recommendation']}"
            )

    print("\n========================================")


def create_summary(result):
    """Create a compact summary of the analysis."""

    severity_counts = {
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0,
    }

    for finding in result["findings"]:
        severity = finding["severity"]

        if severity in severity_counts:
            severity_counts[severity] += 1

    return {
        "configuration": result["configuration"],
        "score": result["score"],
        "status": result["status"],
        "severity_summary": severity_counts,
        "total_findings": len(result["findings"]),
    }