"""
This is a simple script to call pdm-pep517's backend apis to make release artifacts.
"""
import logging

from pdm.pep517 import api

logger = logging.getLogger("pdm.pep517")
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def main():
    api.build_sdist("dist")
    api.build_wheel("dist")


if __name__ == "__main__":
    main()
