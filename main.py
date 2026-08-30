import argparse
import json
import sys
import yaml

from guard.analyzer import analyze_config
from guard.report import create_summary, print_report


def main():
    parser = argparse.ArgumentParser(
        description="Cloud Deployment Guard - AWS deployment configuration analyzer."
    )

    parser.add_argument(
        "config",
        help="Path to the YAML deployment configuration.",
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output the analysis result as JSON.",
    )

    args = parser.parse_args()

    try:
        result = analyze_config(args.config)

    except FileNotFoundError:
        print(
            f"Error: Configuration file not found: {args.config}",
            file=sys.stderr,
        )
        return 1

    except yaml.YAMLError as error:
        print(
            f"Error: Invalid YAML configuration: {error}",
            file=sys.stderr,
        )
        return 1

    if args.json:
        output = {
            "tool": "Cloud Deployment Guard",
            "result": result,
            "summary": create_summary(result),
        }

        print(json.dumps(output, indent=4))

    else:
        print_report(result)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())