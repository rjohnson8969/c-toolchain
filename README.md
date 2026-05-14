# C Toolchain

Small practice project to connect a C program and a Python build script. Using git and VS Code tasks/launch configs.

## Requirements

- `gcc` (or another C compiler available on `PATH`)
- Python 3.8+ with `python` on `PATH`

## Project structure

- `main.c` – simple C program that prints a message and sums two integers from the command line.
- `build.py` – Python CLI that compiles `main.c` into an executable using `gcc`.

## Build and run from the terminal

From the project root:

```bash
# Compile the C program using the Python build script
python build.py --source main.c --output main

# Run the resulting executable
./main 2 3
```

You should see output similar to:

```text
2 + 3 = 5
```