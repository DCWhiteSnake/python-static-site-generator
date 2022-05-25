from pathlib import Path

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = f"{self.dest}",
        f"/{path.relative_to(self.source)}")

        directory.mkdir(parents=True, exist_ok = True)

    def build():
        self.dest.mkdir(parents=True, exist_ok=True)

        _=(for curr_path in self.source.rglob("*")
        self.create_dir(curr_path) if curr_path.isdir())
