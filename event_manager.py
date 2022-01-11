
# !These are all necessary imports
import pygame
from typing import Any, Union

class events_sync:
    """
    Allows for pygame to be handled at the same time
    and with coordination; otherwise every system
    who wanted to listen for a particular event
    would be stepping on each other toes and the
    events may be taken from the queue accidentally
    and interfere with other systems
    """
    def __init__(self) -> None:
        """Sets up events_sync program
        """
        #  Register is for events to be acted on immediately
        self._register = []

        # Latch register is for events to be added to queue
        # and then to be acted upon when polled
        self._latch_register = {}

        # The remapping register
        self._remapping = {}

    def __call__(self):
        """
        Goes through each event in the queue
        and does appropriate actions
        """

        for event in pygame.event.get():
            for _x in [r for r in self._register if r[0][0] == event.type]:
                # Goes through a modifed register with items that match the current event type

                # This is the key/s for the item polled from the register
                _k = list(_x[0])
                # This is the value/s for the item polled from the register
                _v = tuple(_x[1])


                # If a keyphrase if provided with the item it converts
                # it into the pygame key
                if len(_k) == 2 and type(_k[1]) is str:
                    _remapped_k = self._remapping[_k[1]]
                else:
                    _remapped_k = None

                print(_x, _k, _v, _remapped_k)

                # These are for 'normal' events
                if len(_k) < 2:
                    # This triggers the action passing through
                    # any args or kwargs
                    print('calling1')
                    _v[0](*_v[1], **_v[2])

                # These are for keyboard input events with the key specified
                elif event.key == _k[1]\
                        and len(_k) == 2 and type(_k[1]) is int:
                    # This triggers the action passing through
                    # any args or kwargs
                    print('calling2')
                    _v[0](*_v[1], **_v[2])

                # These are for keyboard input events with the
                # key phrase specified
                elif event.key == _remapped_k\
                        and len(_k) == 2 and type(_k[1]) is str:
                    # This triggers the action passing through
                    # any args or kwargs
                    print('calling3')
                    _v[0](*_v[1], **_v[2])

            if event.type in self._latch_register.keys():
                self._latch_register[event.type].append(event)

    def config(self, key_phrase: str, key_to_map_to: int):
        """This allows for key to be remapped based on a key phrase

        Parameters
        ----------
        key_phrase : str
            The name of phrase for the key to be designated
        key_to_map_to : int
            The key assigned to the phrase
        """
        # Adds the key phrase to the remapping list
        self._remapping[key_phrase] = key_to_map_to

    def listen(self, event: int, action: Any,
               key: Union[int, str] = None,
               *args, **kwargs):
        """Allows for an action to be performed when the associated event occurs
        if passed the listen function can also listen for specific keys, it
        also allows for args or kwargs to be passed into the action

        Parameters
        ----------
        event : int
            The pygame event that should be listened too
        action : Any
            The function that should be called when the event occurs
        key : int, optional
            If the event is a keyboard event, so on what key should
            the event occur, by default None
        """
        if type(key) is str and key not in self._remapping.keys():
            raise Exception(
                f'The provided key phrase: {key}, was not defined or set, '
                f'did you use *.config(\'{key}\', *)?')

        if key is None:
            # If there is no key provided, for keyboard input events, it
            # shouldn't be added into the register with the event
            self._register.append([(event), (action, args, kwargs)])
        else:
            # If there is a key provide, for keyboard input events, it
            # should be added into the register
            self._register.append([(event, key), (action, args, kwargs)])

    def latch(self, event: int):
        """This allows for events to be listened too and recorded
        when events are heard, the occurrence is noted in latch
        register for the respective event and can be retrieved at anytime

        Parameters
        ----------
        event : int
            The pygame event that should be listened for
        """
        self._latch_register[event] = []

    def retrieve(self, event: int):
        """Retrieves all the events stored in the register from the requested
        event type, this function is designed to be called frequently (most
        likely once per tick) so it unlikely to have multiple events in the
        register

        Parameters
        ----------
        event : int
            The pygame event that should be retrieved

        Returns
        -------
        list
            All the events that occurred in the registers
        """
        r = self._latch_register[event]
        self._latch_register[event] = []
        return r
