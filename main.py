from http import HTTPStatus
from pathlib import Path
from typing import Iterable, Optional, cast

from requests import post
from requests.status_codes import codes as status_codes

from config import get_config


def send_save_file(url: str, save_file_path: Path) -> int:
    with open(save_file_path, "rb") as save_file:
        file_content = save_file.read()

    request = post(url, files={save_file_path.name: file_content})

    return cast(int, request.status_code)


def get_newest_save_file(save_files: Iterable[Path]) -> Optional[Path]:
    return max(save_files, default=None, key=lambda file: file.stat().st_mtime)


def get_save_file_path(save_folder_path_str: str, save_file_extension: str) -> Path:
    save_folder_path = Path(save_folder_path_str)
    assert save_folder_path.exists()
    assert save_folder_path.is_dir()

    save_file_path = get_newest_save_file(
        save_folder_path.glob(f"*.{save_file_extension}")
    )

    if save_file_path is None:
        raise RuntimeError(
            f"Save file in {save_folder_path_str} with the extension of {save_file_extension} was not found!"
        )

    return save_file_path


def main() -> None:
    config = get_config()
    save_file_path = get_save_file_path(
        config.save_folder_path_str, config.save_file_extension
    )

    result = send_save_file(config.webhook_url, save_file_path)

    if result == HTTPStatus.OK:
        print("File sent!")
    else:
        raise RuntimeError(
            f"Save file was found but could not be sent! Do you have active internet connection ?\nReason: {status_codes[result]}"
        )


if __name__ == "__main__":
    main()
