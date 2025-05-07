# from pathlib import Path
# from .wrapper import evaluateOnNewDocument
# from selenium.webdriver import Chrome as Driver


# def navigator_vendor(driver: Driver, vendor: str, **kwargs) -> None:
#     evaluateOnNewDocument(
#         driver, Path(__file__).parent.joinpath("js/navigator.vendor.js").read_text(), vendor
#     )

from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .resource_loader import resource_path


def navigator_vendor(driver: Driver, vendor: str, **kwargs) -> None:
    js_path = resource_path("selenium_stealth/js/navigator.vendor.js")
    evaluateOnNewDocument(
        driver, open(js_path, encoding="utf-8").read(), vendor
    )
