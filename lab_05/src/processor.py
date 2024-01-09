from generator import Generator
from memory import Memory

class Processor(Generator):

    def __init__(self, generator: Generator, memory: Memory):
        super().__init__(generator.distribution, generator.receivers)
        self.nextEvent.eventBlock = self
        self.memory = memory
        self.available = True

    def ProcessTime(self):
        return self.GenerateNextEvent()

    def SetAviable(self, state=True):
        self.available = state

    def IsAviable(self) -> bool:
        return self.available

    def TakeRequest(self, curTime) -> bool:
        if self.available:
            self.SetAviable(False)
            self.GenerateNextEvent(curTime)
            return True

        return self.memory.InsertRequest()

    def EndProcess(self, curTime):
        self.TransmitRequest()

        if not self.memory.IsEmpty():
            self.memory.RemoveRequest()
            self.GenerateNextEvent(curTime)
        else:
            self.SetAviable(True)
            self.NextEvent.Time = -1