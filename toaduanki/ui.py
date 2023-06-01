from aqt.qt import QDialog

from .entry_ui import Ui_Entry

class EntryDialog(QDialog, Ui_Entry):
    def __init__(self, *args, **kwargs):
        super(EntryDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
