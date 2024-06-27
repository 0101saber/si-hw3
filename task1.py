import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


def copy_file(file_path, target_dir):
    ext = file_path.suffix[1:]
    target_path = target_dir / ext / file_path.name

    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file_path, target_path)


def process_directory(source_dir, target_dir, pool):
    futures = []

    for entry in source_dir.iterdir():
        if entry.is_dir():
            futures.append(pool.submit(process_directory, entry, target_dir, pool))
        elif entry.is_file():
            futures.append(pool.submit(copy_file, entry, target_dir))

    for future in as_completed(futures):
        future.result()


def main():
    dirs = input('Enter path to directory with files and folder for copy file: ').split()

    if dirs.count == 0:
        print(f"Error: enter a directory with files.")
    else:
        source_dir = Path(dirs[0])
        if not source_dir.is_dir():
            print(f"Error: {source_dir} is not a directory or does not exist.")
        else:
            target_dir = Path(dirs[1]) if len(dirs) > 1 else Path('dist')

            with ThreadPoolExecutor() as pool:
                process_directory(source_dir, target_dir, pool)


if __name__ == "__main__":
    main()
