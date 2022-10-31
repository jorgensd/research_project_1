"""Console script for research_project_1."""

import argparse


def main():
    """Console script for research_project_1."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "research_project_1.cli.main")
    return 0
