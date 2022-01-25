![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/Hystersis/Pygame-Event-Manager)
# Sushi Dodger
This is a free wrapper for the default PyGame event wrapper, with a range of functions allowing for a more streamlined use of the event system. It minimizes overdrawing - where other parts of the code take out events that are needed to be acted upon by another system. It instead uses function-based code calling on event entering.


## Contents:
- [Sushi Dodger](#sushi-dodger)
  - [Contents:](#contents)
  - [Usage:](#usage)
    - [Basic Usage:](#basic-usage)
  - [Credits:](#credits)


## Usage:
All the code is in `event_manager.py`.

### Basic Usage:
Look at the [wiki](https://github.com/Hystersis/Pygame-Event-Manager/wiki) for more advanced usage of event_manager. 

1. Copy the code from `event_manager.py` into your PyGame game
2. Call `name_of_var = events_sync()`
* Use the `listen` function to provide actions to be performed on certain events e.g. For a **keyboard down event** with a **specific key** you would use: `name_of_var.listen(pygame.KEYDOWN, name_of_function, pygame.K_a)` or using key remapping: `name_of_var.config('up', pygame.K_w)` then, `name_of_var.listen(pygame.KEYDOWN, name_of_function, 'up')`. 
* Instead for a basic function you can just use: `name_of_var.listen(pygame.QUIT, name_of_function, None, var_passed_into-name_of_function)`
3. Call `name_of_var()` in the update loop of your game to run all the events through it 


[MIT](/license) © [Hystersis](https://github.com/Hystersis)
