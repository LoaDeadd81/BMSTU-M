from distributions import Distribution

class Processor:

    def __init__(self, distribution: Distribution):
        self.distribution = distribution
        self.available = True

    def process_time(self):
        return self.distribution.generate()

    def set_available(self, state=True):
        self.available = state

    def is_available(self) -> bool:
        return self.available
