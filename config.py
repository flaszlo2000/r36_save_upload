from dataclasses import dataclass
from json import JSONDecodeError
from json import load as json_load
from pathlib import Path
from typing import Any, Final, Self

DEFAULT_CONFIG_PATH: Final[Path] = Path("./config.json")


@dataclass(frozen=True)
class ConfigModel:
    webhook_url: str
    save_folder_path_str: str
    save_file_extension: str

    def __post_init__(self) -> None:
        required_keys = filter(
            lambda k: not k.startswith("_"), self.__dataclass_fields__
        )
        for key in required_keys:
            required_value = self.__getattribute__(key)
            # XXX: this is going to become an issue if other types are introduced
            assert isinstance(required_value, str)

            if required_value is None or len(required_value) == 0:
                raise AttributeError(f"Empty config parameter named {key}!")

    @classmethod
    def createFromParsedData(cls, data: dict[str, Any]) -> Self:
        required_keys = set(
            filter(lambda key: not key.startswith("_"), cls.__dataclass_fields__.keys())
        )
        given_keys = set(data.keys())

        all_required_keys_are_present = required_keys.issubset(given_keys)
        if not all_required_keys_are_present:
            missing = required_keys.difference(given_keys)

            raise RuntimeError(
                f"Not all required config parameters are present!\nMissing: {missing}"
            )

        cls_data = {required_key: data[required_key] for required_key in required_keys}

        return cls(**cls_data)


def get_config(config_path: Path = DEFAULT_CONFIG_PATH) -> ConfigModel:
    assert config_path.exists()
    assert config_path.is_file()

    with open(config_path, "r") as config_file:
        try:
            data = json_load(config_file)
        except JSONDecodeError:
            raise RuntimeError("Badly formatted config file!")

        return ConfigModel.createFromParsedData(data)
