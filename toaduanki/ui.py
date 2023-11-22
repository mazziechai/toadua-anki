from aqt import QMessageBox
from aqt.operations import QueryOp
from aqt.qt import QDialog
from aqt.utils import showInfo

from PyQt6 import QtCore, QtGui, QtWidgets

from .toadua_ui import Ui_Dialog
from .toadua import add_notes_to_col, get_toadua_entries_by_id, get_toadua_entries_by_word


class EntryDialog(QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(EntryDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.onchange)
        self.words = []

    def onchange(self):
        word = self.lineEdit.text()

        op = QueryOp(
            parent=self,
            op=lambda _: get_toadua_entries_by_word(word),
            success=self.update_list,
        )
        op.run_in_background()

    def update_list(self, words: list[dict[str, str]]):
        self.words = words
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)

        for w in words:
            item = QtGui.QStandardItem(w["word"] + ": " + w["def"])
            model.appendRow(item)


    def accept(self):
        indexes = self.listView.selectedIndexes()
        words = [self.words[i.row()] for i in indexes]
        op = QueryOp(
            parent=self,
            op=lambda col: add_notes_to_col(col, words),
            success=self.success,
        )

        op.with_progress().run_in_background()

        self.close()

    def success(self, number_added: int):
        showInfo(f"Added {number_added} words!")
