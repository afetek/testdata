from rttlib import scheduler

enableCapturing   = True
enableMaintenance = True
enableEventCheck  = True
testName = 'script1'

def RunScript(self):
    self.Print("signal1: " + str(self.s1))
    self.Print("signal2: " + str(self.s2))
    
    c1 = 'self.model.c1'
    c2 = 'self.model.c2'
    c3 = 'self.model.c3'
    d1 = 'self.model.d1'
    d2 = 'self.model.d2'
    d3 = 'self.model.d3'
    
    self.Print("Waitng ...")
    yield self.Prompt()
    self.Print("... Ok")

    self.Assignment(model_var = c1, value = 2)
    self.Assignment(model_var = c1, value = 2)
    self.Assignment(model_var = c3, value = 3)
    
    yield scheduler.Parallel(self.Validation(model_var = d1, hi = 6.0, lo = 4.0, timeout = 1000, duration = 0, pass_criteria = 'EQUAL', description = 'set c1'),
                             self.Validation(model_var = d2, hi = 6.0, lo = 4.0, timeout = 1000, duration = 0, pass_criteria = 'EQUAL', description = 'set c2'),
                             self.Validation(model_var = d3, hi = 6.0, lo = 4.0, timeout = 1000, duration = 0, pass_criteria = 'EQUAL', description = 'set c3'))

    yield self.Prompt()
