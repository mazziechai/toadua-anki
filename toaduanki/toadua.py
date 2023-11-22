import json
import os
from typing import Any

import requests
from anki.collection import Collection

from .config import config


def search_toadua(query) -> list[dict[str, Any]]:
    body = {"action": "search", "query": query, "limit": 30}

    request = requests.post("https://toadua.uakci.pl/api", json=body)

    response = request.json()

    results: list[dict[str, Any]] = response["results"]

    return [
        {
            "id": entry["id"],
            "word": entry["head"],
            "def": entry["body"],
            "notes": [
                f"{note['user']}: {note['content']}\n" for note in entry["notes"]
            ],
        }
        for entry in results
    ]


def get_toadua_entries_by_id(ids: list[str]) -> list[dict[str, Any]]:
    search_param = ["or"]

    for word_id in ids:
        search_param.append(["id", word_id])  # type: ignore
    return search_toadua(search_param)


def get_toadua_entries_by_word(word: str) -> list[dict[str, Any]]:
    if not word:
        return []
    if "scope:" not in word:
        word = "scope:" + config["scope"] + " " + word
    return search_toadua(word)


def add_notes_to_col(col: Collection, words: list[dict[str, Any]]) -> int:
    """
    Creates a deck and a note type if they aren't found, then creates the notes.
    Returns the number of notes added.
    """

    deck = col.decks.by_name(config["deck"])

    if deck is None:
        deck = col.decks.new_deck()
        deck.name = config["deck"]
        col.decks.add_deck(deck)

        deck = col.decks.by_name(config["deck"])

    notetype = col.models.by_name("Toadua")

    if notetype is None:
        notetype = col.models.new("Toadua")

        json_path = os.path.dirname(__file__) + "/json/notetype.json"
        with open(json_path) as f:
            notetype_json = json.load(f)

        notetype.update(notetype_json)

        col.models.save(notetype)

    notes = []

    for word in words:
        note = col.new_note(col.models.by_name("Toadua"))  # type: ignore

        note["ID"] = word["id"]
        note["Word"] = word["word"]
        note["Definition"] = word["def"]
        note["Notes"] = "\n".join(word["notes"])

        col.add_note(note, deck["id"])  # type: ignore
        notes.append(note)

    return len(notes)
