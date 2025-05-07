# from pathlib import Path
# from .wrapper import evaluateOnNewDocument
# from selenium.webdriver import Chrome as Driver


# def window_outerdimensions(driver: Driver, **kwargs) -> None:
#     evaluateOnNewDocument(
#         driver, Path(__file__).parent.joinpath("js/window.outerdimensions.js").read_text()
#     )

from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .resource_loader import resource_path


def window_outerdimensions(driver: Driver, **kwargs) -> None:
    js_path = resource_path("selenium_stealth/js/window.outerdimensions.js")
    evaluateOnNewDocument(
        driver, open(js_path, encoding="utf-8").read()
    )
