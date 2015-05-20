# -*- coding: UTF-8 -*-

class State:
    
    def execute(self, miner):
        pass

    def enter(self, miner):
        pass

    def exit(self, miner):
        pass


#挖矿状态
class DigForNuggetState(State):

    def execute(self, miner):
        print u"挖啊挖"
        miner.addToGoldCarried(1) 
        miner.inceaseFatigue()

        if miner.isPocketIsFull():
            miner.changeState(VisitBankAndDepositGoldState())

        if miner.isThirsty():
            miner.changeState(VisitBarAndDrinkState())

    def enter(self, miner):
        print u"我来挖矿了" 

    def exit(self, miner):
        print u"挖矿工作结束了" 

#银行存钱状态
class VisitBankAndDepositGoldState(State):

    def execute(self, miner):
        print u"老板，存钱"
        miner.depositGold(5) 
        
        if miner.isRichEnough():
            miner.changeState(GoHomeAndSleepState())
        else:
            miner.changeState(DigForNuggetState())

    def enter(self, miner):
        print u"我来存钱了" 

    def exit(self, miner):
        print u"钱存完了"

#酒吧喝酒状态
class VisitBarAndDrinkState(State):

    def execute(self, miner):
        print u"喝了一杯" 
        miner.drinkACup()

        if not miner.isThirsty():
            miner.changeState(DigForNuggetState())

    def enter(self, miner):
        print u"我来喝洒了"

    def exit(self, miner):
        print u"酒喝完了"

#回家睡觉
class GoHomeAndSleepState(State):

    def execute(self, miner):
        print u"ZZZ"
        miner.sleep() 

        if not miner.isTied():
            miner.changeState(DigForNuggetState())

    def enter(self, miner):
        print u"我回家睡觉了"

    def exit(self, miner):
        print u"睡醒了"

