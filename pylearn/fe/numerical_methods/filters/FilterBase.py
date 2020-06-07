class FilterBase:
    READY_COUNT_INIT = 100000
    initialValue = 0.0
    initialized = False
    gainAdjustment = 0.0
    initialValueGainAdjustment = 0.0
    warmupCount = READY_COUNT_INIT
    readyCounter = READY_COUNT_INIT
    outputValue = 0.0

    def reset(self):
        self.initialValue = 0.0
        self.initialized = False
        self.readyCounter = self.warmupCount
        self.outputValue = 0.0

    def relevel(self, v=0.0):
        self.reset()
        self.swallow_initial_value(v)

    def value(self):
        return self.gainAdjustment * self.outputValue + self.initialValueGainAdjustment * self.initialValue

    def initial_value(self):
        return self.initialValue

    def swallow_initial_value(self, v):
        if not self.initialized:
            self.initialValue = v
            self.initialized = True
        return v - self.initialValue

    def decrement_ready_counter(self):
        self.readyCounter = 0 if self.readyCounter == 0 else self.readyCounter - 1
