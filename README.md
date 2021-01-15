# pycards

## Presentation

PyCards is a python flask card game engine.
Without any modding, it can just browse a basic deck of cards.
With modding, it can play any cards game.

## Usage

* **/pycards/**
Creates a new game (by default in free mode)
    * ?game=<somename>
        Uses game mode *somename*, using file jeusomename.py (**case sensitive !!**)

* **/draw/**
Draw a card; returns raw data, used as an api (with ajax for example)
    * ?move=<somemove>
        Used to pass data to /draw/ when playing a special game