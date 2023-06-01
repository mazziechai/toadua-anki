import io
from aqt import QFile, mw
from aqt.utils import showInfo
from aqt.qt import qconnect, QAction

from .ui import EntryDialog

def testFunction() -> None:
    mw.entry_dialog = entry_dialog = EntryDialog() # type: ignore
    entry_dialog.show()


action = QAction("test", mw)
qconnect(action.triggered, testFunction)
mw.form.menuTools.addAction(action)
