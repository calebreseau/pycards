# pycards

## Presentation

PyCards is a python flask card game engine.
Without any modding, it can just browse a basic deck of cards.
With modding, it can play any cards game.

## Usage

* **/pycards/**
Creates a new game (by default in free mode)
    * ?game=somename
        Uses game mode *somename*, using file jeusomename.py (**case sensitive !!**)

* **/draw/**
Draw a card; returns raw data, used as an api (with ajax for example)
    * ?move=somemove
        Used to pass data to /draw/ when playing a special game


## Modding

Parent class for mods is **jeu.py**
Game modes classes have two main functions (its advised to call super() function when overriding):
* **__init__()**
    Here you can define variables or consts specific to your mod.
    Most important here is the **self.controls** array, which defines the game controls.
    It's an list of lists; each sublist contains attributes for a button:
    * str:id
    * str:path to texture
    * str:js on click function
        * str:move(remember ?move parameter) if needed
    
