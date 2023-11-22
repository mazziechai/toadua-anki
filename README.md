# toadua-anki

An Anki add-on that creates cards from Toadua entries.

## Installing

You can download the latest .ankiaddon file [here](https://github.com/mazziechai/toadua-anki/releases). If you have Anki installed, you can open this file to install the add-on.

## Usage

The add-on adds a _Toadua Cards_ action under the Tools tab. Search for words as on Toadua, and select the ones you'd like to add. They'll be added to a deck called _Toadua words_. The deck name can be configured by going to Tools → Add-ons → toadua-anki → Config.

## Development

Install Python 3.11+ and [pdm](https://pdm-project.org/latest/) and run `pdm install` in this folder. Then run `pdm run ui` to build the Qt UI, and finally `pdm run pkg` to create `toaduanki.ankiaddon`.

## To-do list

- [x] Easy to use GUI
- [x] Create cards from Toadua entries
- [x] Selecting specific entries to make cards out of in case of conflict
- [ ] Derani support
