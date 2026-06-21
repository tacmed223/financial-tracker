#!/usr/bin/env python3
"""
Study Tracker - Main Entry Point

This script launches the CLI application for the Study Tracker system.
Usage: python main.py
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent))

from src.cli import StudyTrackerCLI


def main():
    """Launch the Study Tracker application."""
    print("Starting Study Tracker...")
    print("=" * 50)
    
    try:
        app = StudyTrackerCLI()
        app.main()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
