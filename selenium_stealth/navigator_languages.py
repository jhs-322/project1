# from pathlib import Path
# from .wrapper import evaluateOnNewDocument
# from selenium.webdriver import Chrome as Driver


# def navigator_languages(driver: Driver, languages: [str], **kwargs) -> None:
#     evaluateOnNewDocument(
#         driver, Path(__file__).parent.joinpath("js/navigator.languages.js").read_text(),
#         languages,
#     )

from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .resource_loader import resource_path


def navigator_languages(driver: Driver, languages: [str], **kwargs) -> None:
    js_path = resource_path("selenium_stealth/js/navigator.languages.js")
    evaluateOnNewDocument(
        driver, open(js_path, encoding="utf-8").read(),
        languages,
    )