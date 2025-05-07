# from pathlib import Path
# from .wrapper import evaluateOnNewDocument
# from selenium.webdriver import Chrome as Driver


# def webgl_vendor_override(
#     driver: Driver,
#     webgl_vendor: str,
#     renderer: str,
#     **kwargs
# ) -> None:
#     evaluateOnNewDocument(
#         driver, Path(__file__).parent.joinpath("js/webgl.vendor.js").read_text(),
#         webgl_vendor,
#         renderer,
#     )

from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .resource_loader import resource_path


def webgl_vendor_override(
    driver: Driver,
    webgl_vendor: str,
    renderer: str,
    **kwargs
) -> None:
    js_path = resource_path("selenium_stealth/js/webgl.vendor.js")
    evaluateOnNewDocument(
        driver, open(js_path, encoding="utf-8").read(),
        webgl_vendor,
        renderer,
    )
