import argparse
from pathlib import Path


def source_path(folder):
    try:
        path = Path(folder)

        if not path.exists():
            print(f"Error: Source directory does not exist: {path}")
            exit(1)

        if not path.is_dir():
            print(f"Error: Source path is not a directory: {path}")
            exit(1)

        print(f"Source directory: {path}")
        return path

    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        exit(1)


def destination_path(folder):
    try:
        path = Path(folder)

        if path.exists() and path.is_dir():
            print(f"Directory already exists: {path}")
        else:
            path.mkdir(parents=True, exist_ok=True)
            print(f"Directory successfully created: {path}")

        return path

    except PermissionError:
        print("Permission denied: Unable to create directory.")
        exit(1)

    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        exit(1)


# Парсинг аргументов
parser = argparse.ArgumentParser(
    description="Copy files recursively and organize them by file type.")
parser.add_argument("source_path", help="Path to the source directory.")
parser.add_argument("--destination_path", default="dist",
                    help="Path to the destination directory (default: 'dist').")
args = parser.parse_args()

# Вызов функций
source = source_path(args.source_path)
destination = destination_path(args.destination_path)

# Запусти скрипт в терминале
# python script.py /path/to/source --destination_path /path/to/destination
