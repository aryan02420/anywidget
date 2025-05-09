import importlib.metadata
import pathlib

import anywidget
import traitlets

try:
    __version__ = importlib.metadata.version("vue_demo")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class CounterWidget(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "dist" / "counter-widget.mjs"
    _css = pathlib.Path(__file__).parent / "dist" / "counter-widget.css"
    value = traitlets.Int(0).tag(sync=True)
