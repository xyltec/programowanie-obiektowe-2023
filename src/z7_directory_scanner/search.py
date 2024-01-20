import os
from dataclasses import dataclass, field
from datetime import datetime, timedelta

from text_tools import file_verbose
from model import *


def is_accessible(file: str) -> bool:
    if not os.access(file, os.R_OK):
        return False
    return True
    # todo: does this work ok for folders which are readable, but not executable (cannot enter them)
    # try:
    #     if os.path.isfile(file):
    #         pass
    #     return True
    # except PermissionError:
    #     return False


class SearchEngine:
    def traverse_path(self, start_path: str, depth: int, selector: Selector) -> list[File]:
        matching_files = []

        for f in os.listdir(start_path):
            full_f = os.path.join(start_path, f)

            if not is_accessible(full_f):
                continue

            if os.path.isfile(full_f):
                file = File.get_file(full_f)
                if not file.is_older_than(selector.older_than_days):
                    continue
                if not file.size >= selector.min_size:
                    continue
                if len(selector.extensions) > 0:
                    ok = False
                    name = file.path.upper()
                    for ext in selector.extensions:
                        if name.endswith(ext.upper()):
                            ok = True
                            break
                    if not ok:
                        continue
                matching_files.append(file)

            if os.path.isdir(full_f):
                if depth > 0:
                    extra = self.traverse_path(start_path=full_f, depth=depth - 1, selector=selector)
                    matching_files.extend(extra)
        return matching_files


if __name__ == '__main__':
    selector = Selector(extensions=['zip', 'pdf'])
    engine = SearchEngine()
    files = engine.traverse_path('/home', depth=2, selector=selector)
    files = sorted(files, key=lambda f: -f.size)
    files = files[:20]
    for f in files:
        print(file_verbose(f))
