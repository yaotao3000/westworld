# -*- coding: UTF-8 -*-
from State import *


class BaseGameEntity:
    
    iNextValidId = 0
    def __init__(self, id):
        self._id = id

    def _setId(self, id):
        self._id = id

    def update(self):
        pass

class Miner(BaseGameEntity):

    def __init__(self, id):
        BaseGameEntity.__init__(self, id)
        self._curState = GoHomeAndSleepState() 
        self._prevState = None 
        self._globeState = None 
        self._location = -1
        self._iGoldCarried = 0
        self._iMoneyInBank = 0
        self._iThirst = 0
        self._iFatigue = 0

    def update(self):
        self._iThirst += 1
        if self._curState:
            self._curState.execute(self)

    def changeState(self, newState):
        assert(self._curState)
        assert(newState)
        self._curState.exit(self)
        self._prevState = self._curState
        self._curState = newState
        self._curState.enter(self)

    def revertToPrevState(self):
        changeState(self._prevState)

    def addToGoldCarried(self, i):
        self._iGoldCarried += i

    def inceaseFatigue(self):
        self._iFatigue += 1

    def isPocketIsFull(self):
        if self._iGoldCarried > 10:
            return True
        else:
            return False

    def isThirsty(self):
        if self._iThirst > 8:
            return True
        else:
            return False
    
    def depositGold(self, i):
        self._iGoldCarried -= i
        self._iMoneyInBank += i

    def isRichEnough(self):
        if self._iMoneyInBank > 20:
            return True
        else:
            return False

    def drinkACup(self):
        self._iThirst -= 3

    def sleep(self):
        self._iFatigue -= 2

    def isTied(self):
        if self._iFatigue > 7:
            return True
        return False
