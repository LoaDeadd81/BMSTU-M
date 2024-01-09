import random
import bisect

from event import Event, EventType

class FutureEvents:

    def __init__(self):
        self.events = list()

    def all_events(self):
        return self.events

    # вставка в список будущих событий в нужное место (отсортированно)
    def add(self, event: Event):
        bisect.insort(self.events, event)

    def next(self) -> Event:
        return self.events.pop(0)


class EventModel:

    def __init__(self
                 , generator
                 , memory
                 , processor
                 , requests_num=1000
                 , repeat_percent=0):
        self.generator = generator
        self.memory = memory
        self.processor = processor
        self.requests_num = requests_num
        self.repeat_percent= repeat_percent


    def run(self):
        self.processor.set_available(True)

        processed_requests = 0
        total_requests = self.requests_num
        events = FutureEvents()

        events.add(Event(self.generator.next_time(), EventType.GENERATOR))

        gen_num = 0

        while processed_requests < total_requests:
            cur_event = events.next()

            if cur_event.event_type == EventType.GENERATOR:
                self.memory.insert_request()
                events.add(Event(cur_event.time + self.generator.next_time(),
                                 EventType.GENERATOR))
                gen_num += 1

            if cur_event.event_type == EventType.PROCESSOR:
                processed_requests += 1
                if random.randint(0, 100) < self.repeat_percent:
                    self.memory.insert_request()
                self.processor.set_available(True)

            if self.processor.is_available():
                if not self.memory.is_empty():
                    self.memory.remove_request()
                    self.processor.set_available(False)
                    events.add(Event(cur_event.time +
                                     self.processor.process_time(),
                                     EventType.PROCESSOR))

        print("\nEVENT MODEL")
        print(f"Repeat %: {self.repeat_percent}")
        print(f"Requests: {total_requests}")
        #print(f"Repeats: {total_requests - self.requests_num}")
        print(f"Max len: {self.memory.max_len}")

        return self.memory.max_len
