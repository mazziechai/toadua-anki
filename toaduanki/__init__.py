from anki.collection import Collection
from aqt import mw
from aqt.qt import QAction, qconnect

from .toadua import add_notes_to_col
from .ui import EntryDialog


def toadua_cards_tool():
    col: Collection = mw.col  # type: ignore

    mw.entry_dialog = entry_dialog = EntryDialog()  # type: ignore

    if entry_dialog.exec():
        words = entry_dialog.words
        add_notes_to_col(col, words)


action = QAction("Toadua Cards", mw)
qconnect(action.triggered, toadua_cards_tool)
mw.form.menuTools.addAction(action)
