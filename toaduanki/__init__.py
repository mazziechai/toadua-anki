from aqt import mw
from aqt.qt import QAction, qconnect

from .ui import EntryDialog


def testFunction() -> None:
    mw.entry_dialog = entry_dialog = EntryDialog()  # type: ignore
    entry_dialog.show()


action = QAction("test", mw)
qconnect(action.triggered, testFunction)
mw.form.menuTools.addAction(action)
