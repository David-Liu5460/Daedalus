import sys
from pathlib import Path

from dotenv import load_dotenv

from daedalus.cli.app import ConsoleApp

from .project import project

load_dotenv()


def main():
    """Main entry point for daedalus."""
    if len(sys.argv) > 1:
        project.root_dir = Path(sys.argv[1])
    app = ConsoleApp()
    app.run()


if __name__ == "__main__":
    main()
