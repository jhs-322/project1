# from pathlib import Path
# from .wrapper import evaluateOnNewDocument
# from selenium.webdriver import Chrome as Driver


# def chrome_runtime(driver: Driver, run_on_insecure_origins: bool = False, **kwargs) -> None:
#     evaluateOnNewDocument(
#         driver, Path(__file__).parent.joinpath("js/chrome.runtime.js").read_text(),
#         run_on_insecure_origins,
#     )

from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .resource_loader import resource_path


def chrome_runtime(driver: Driver, run_on_insecure_origins: bool = False, **kwargs) -> None:
    js_path = resource_path("selenium_stealth/js/chrome.runtime.js")
    evaluateOnNewDocument(
        driver, open(js_path, encoding="utf-8").read(),
        run_on_insecure_origins,
    )
