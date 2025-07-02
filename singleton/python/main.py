from threading import Thread
from config_manager import ConfigManager


def test_singleton(config: str, get: str) -> None:
    config = ConfigManager(config)
    print(config)
    print(config.get(get))


if __name__ == "__main__":
    proc1 = Thread(target=test_singleton, args=("config.yaml", "features"))
    proc2 = Thread(target=test_singleton, args=("config2.yaml", "database"))
    proc1.start()
    proc2.start()
