from distributions import Distribution
from event import Event

class Generator:

    def __init__(self, distribution: Distribution, receivers: list['Processor']):
        self.distribution = distribution
        self.receivers = receivers
        self.nextEvent = Event(-1, self)

    def GenerateNextEvent(self, curTime):
        self.nextEvent.Time = curTime + self.distribution.Generate()

    def TransmitRequest(self):
        for receiver in self.receivers:
            if receiver.TakeRequest(self.nextEvent.time):
                return True

        return False

    @property
    def NextEvent(self):
        return self.nextEvent