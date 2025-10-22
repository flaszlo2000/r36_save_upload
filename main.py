from http import HTTPStatus
from urllib.request import urlopen

from config import get_config
from msg import MsgWithSaveFile


def send_msg(url: str, msg: MsgWithSaveFile) -> HTTPStatus:
    with urlopen(f"{url}?wait=true") as raw_response:
        response = raw_response.read().decode()
        print(response)

    return HTTPStatus.OK


def main() -> None:
    config = get_config()
    save_file_msg = MsgWithSaveFile()

    print(save_file_msg)
    # send_msg(config.webhook_url, save_file_msg)

if __name__ == "__main__":
    main()
