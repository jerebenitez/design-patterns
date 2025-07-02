from threading import Lock
import yaml
import json
import sys
import os


class SingletonMeta(type):
    """
    source: https://refactoring.guru/design-patterns/singleton/python/example#example-1
    """
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


class ConfigManager(metaclass=SingletonMeta):
    config = None

    def __init__(self, config_path):
        if not os.path.exists(config_path):
            sys.exit(f"Config file not found: {config_path}")

        _, ext = os.path.splitext(config_path)
        ext = ext.lower()

        with open(config_path, "r") as stream:
            try:
                if ext == ".json":
                    self.config = json.load(stream)
                elif ext in {".yaml", ".yml"}:
                    self.config = yaml.safe_load(stream)
                else:
                    sys.exit(f"Unsupported config file extension: {ext}")
            except (yaml.YAMLError, json.JSONDecodeError) as exc:
                sys.exit(f"Failed to parse config file: {exc}")

    def get(self, field: str) -> str:
        # It should only accept valid settings, but since its a mock...
        return self.config[field]

    def __repr__(self):
        return str(self.config)
