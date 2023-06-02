from aqt import QMessageBox
from aqt.operations import QueryOp
from aqt.qt import QDialog
from aqt.utils import showInfo

from .entry_ui import Ui_Entry
from .toadua import add_notes_to_col, get_toadua_entries_by_id


class EntryDialog(QDialog, Ui_Entry):
    def __init__(self, *args, **kwargs):
        super(EntryDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def accept(self):
        """
        After the words are submitted, we get the definitions from Toadua and
        send it over to `success` to be processed into cards.
        """

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

        try:
            op = QueryOp(
                parent=self,
                op=lambda _: get_toadua_entries_by_id(ids),
                success=self.create_notes,
            )

            op.with_progress().run_in_background()

        except IndexError:
            button = QMessageBox(self)
            button.setWindowTitle("Toadua Error")
            # TODO: Explain which words were invalid
            button.setText("No valid words found")

            button.exec()

        self.close()

    def create_notes(self, words: list[dict[str, str]]):
        self.words = words

        print(words)

        op = QueryOp(
            parent=self,
            op=lambda col: add_notes_to_col(col, words),
            success=self.success,
        )

        op.with_progress().run_in_background()

    def success(self, number_added: int):
        showInfo(f"Added {number_added} words!")
