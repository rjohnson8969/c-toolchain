import argparse
import subprocess
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description="C Builder")
    parser.add_argument(
        "--source",
        required=True,
        help="Path to the C source file"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Name or path of the output exe",
    )

    args = parser.parse_args()

    source = Path(args.source).resolve()
    output = Path(args.output).resolve()

    if not source.exists():
        print(f"Source file does not exist: {source}")
        sys.exit(1)
    
    cmd = ["gcc", "-g", str(source), "-o", str(output)]
    print(f"Running: {' '.join(cmd)}")

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Build failed with code {e.returncode}")
        sys.exit(e.returncode)

    print(f"Build successful. Executable at: {output}")


if __name__ == "__main__":
    main()
