The purpose of this project was to learn and experiment with object oriented Python.

**4 Pillars of Python OOP:**

[*Encapsulation*]: This is the practice of keep class variables and methods safe from outside interference
- Example: Wasn't used in my code but I could change `def build_deck(self)` to `def __build_deck(self)` which then could be used by doing
           `something._Deck__build_deck()` (mangling)

[*Abstraction*]: Essentially this describes a class that contains blueprints, no functionality, to future sub-classes
- Example: I was considering using abstraction in `Class Card` but ultimately decided not to 

[*Inheritance*]: When a sub-class inherits all the functionality of a parent class
- Example: `class Game(Deck)` where `super().__init__` allows me access to parent class functionality

[*Polymorphism*]: Overwriting a method 
- Example: If you have 2 classes where 1 of them is the subclass (no methods) and the other the parent, and when you go to instantiate
           an instance of the 2 classes, the sub-class which currently has no methods is able to take on methods from its parent class
