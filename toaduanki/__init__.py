from aqt import mw
from aqt.utils import showInfo
from aqt.qt import qconnect, QAction

def testFunction() -> None:
    showInfo("Hello, world!")

action = QAction("test", mw)
qconnect(action.triggered, testFunction)
mw.form.menuTools.addAction(action)
