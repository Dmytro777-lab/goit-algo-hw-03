import argparse
from pathlib import Path
import shutil


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


def copy_file(file_path, destination):
    try:
        extension = file_path.suffix[1:] if file_path.suffix else "no_extension"
        dest_folder = destination / extension
        dest_folder.mkdir(parents=True, exist_ok=True)
        shutil.copy(file_path, dest_folder)
        print(f"Copied: {file_path} -> {dest_folder}")

    except Exception as e:
        print(f"Error copying file {file_path}: {e}")


def process_directory(source, destination):
    try:
        for item in source.iterdir():
            if item.is_dir():
                process_directory(item, destination)
            elif item.is_file():
                copy_file(item, destination)
    except Exception as e:
        print(f"Error processing directory {source}: {e}")

parser = argparse.ArgumentParser(
    description="Copy files recursively and organize them by file type.")
parser.add_argument("source_path", help="Path to the source directory.")
parser.add_argument("--destination_path", default="dist",
                    help="Path to the destination directory (default: 'dist').")
args = parser.parse_args()

source = source_path(args.source_path)
destination = destination_path(args.destination_path)

process_directory(source, destination)

print("File copying completed.")