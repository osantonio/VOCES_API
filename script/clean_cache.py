from pathlib import Path
import shutil
import argparse

def delete_cache_dirs(root: Path):
    count = 0
    for p in sorted(root.rglob("__pycache__")):
        shutil.rmtree(p, ignore_errors=True)
        print(f"Eliminado: {p}")
        count += 1
    if count == 0:
        print("No se encontraron carpetas __pycache__")

def delete_pyc_files(root: Path):
    count = 0
    for p in sorted(root.rglob("*.pyc")):
        try:
            p.unlink(missing_ok=True)
            print(f"Eliminado: {p}")
            count += 1
        except Exception:
            pass
    if count == 0:
        print("No se encontraron archivos .pyc")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    parser.add_argument("--pyc", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    delete_cache_dirs(root)
    if args.pyc:
        delete_pyc_files(root)

if __name__ == "__main__":
    main()
