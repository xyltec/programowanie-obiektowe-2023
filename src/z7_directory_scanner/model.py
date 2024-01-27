import os
from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class File:
    path: str
    size: int
    last_modify_time: datetime

    def is_older_than(self, days: int) -> bool:
        return datetime.now() - self.last_modify_time > timedelta(days=days)

    @staticmethod
    def get_file(path: str) -> 'File':
        return File(path, os.path.getsize(path), datetime.fromtimestamp(os.path.getmtime(path)))


@dataclass
class Selector:
    min_size: int = -1
    older_than_days: int = -1
    extensions: list[str] = field(default_factory=[])

    def matches(self, file: File) -> bool:
        return True


class HardSelector(Selector):
    def matches(self, file: File) -> bool:
        return True
