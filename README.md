# pycards [Hosted on pythonanywhere](http://calebreseau.pythonanywhere.com/)

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
To create a mod named example, create the file jeuexample.py, contaning class jeuexample.
Game modes classes have two main functions (its advised to call super() function when overriding):
* **\_\_init\_\_(self)**

    Here you can define variables or consts specific to your mod.
    Most important here is the **self.controls** array, which defines the game controls.
    It's an list of lists; each sublist contains attributes for a button:
    * str:id
    * str:path to texture
    * str:js on click function (for now; functions tirer (draws a card) and vider (empties the dump))
        * str:move(remember ?move parameter) if needed
    
    #### Example

    ```python
        self.controls=[
        ['paquet','/static/cards/PNG/Cards/cardBack_red5.png','tirer',''],
        ['trash','/static/cards/PNG/Cards/cardBack_blue5.png','vider']]
    ```

    You can specify a JS script (in the /static/ dir) for your mod, using **self.script='filename.js'**
    If you code a function **spec_update(data)** in here, it will be called at the end of **tirer()**,
    where *data* is the */draw/* raw response.
    
* **update(self,str:moves)**

    Main function, that is called on */draw/*.
    *moves* is the content of the 4th attribute if the clicked button.
    
    This function should always return something like this: 
    ```python
        [String data,''.join(self.terrain.getDefausse())]
    ```

