from aqt.qt import QDialog

from .entry_ui import Ui_Entry
from .toadua import get_toadua_entry


class EntryDialog(QDialog, Ui_Entry):
    def __init__(self, *args, **kwargs):
        super(EntryDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def accept(self):
        text = self.plainTextEdit.toPlainText()
        print(f"Input: {text}")

        entries = text.splitlines()

        ids: list[str] = []
        _words: list[str] = []

        for entry in entries:
            if entry.startswith("#"):
                ids.append(entry.removeprefix("#"))
            else:
                _words.append(entry)

        # TODO: make this work with words instead of just ids

        print([get_toadua_entry(id) for id in ids])

        self.close()
