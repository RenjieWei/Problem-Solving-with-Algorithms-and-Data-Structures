class LogitGate:
    def __init__(self, n):
        self.label = n
        self.output = None 

    def getLabel(self):
        return self.label

    def getOutout(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogitGate):
    def __init__(self, n):
        LogitGate.__init__(self, n)

        self.pinA = None 
        self.pinB = None
    
    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin A input for gate"+ self.getLabel()+"-->"))

class UnaryGate(LogitGate):
    def __init__(self, n):
        LogitGate.__init__(self, n)
        # super(UnaryGate,self).__init__(n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate"+ self.getLabel()+"-->"))



class AndGate(BinaryGate):
    
    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)
    
    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

g1 = AndGate("G1")
g1.getOutout()
