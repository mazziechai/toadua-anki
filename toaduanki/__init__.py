from aqt import mw
from aqt.qt import QAction, qconnect

from .ui import EntryDialog


def toadua_cards_tool():
    mw.entry_dialog = entry_dialog = EntryDialog()  # type: ignore
    entry_dialog.show()


action = QAction("Toadua Cards", mw)
qconnect(action.triggered, toadua_cards_tool)
mw.form.menuTools.addAction(action)
