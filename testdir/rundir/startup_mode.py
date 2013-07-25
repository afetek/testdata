from rttlib import scheduler

enableCapturing   = True
enableMaintenance = True
enableEventCheck  = True
testName = ''

def RunScript(self):

    self.Print("Powerup Test Script")
    self.Print("Testing Requirements: Statrup Mode - 5 through 8")

    self.Assignment(model_var = 'self.model.fan1FaultRead', value = 1 if self.fan1_fault else 0)
    self.Assignment(model_var = 'self.model.fan2FaultRead', value = 1 if self.fan2_fault else 0)
    self.Assignment(model_var = 'self.model.powerECU', value = 1)

    if not self.fan1_fault and not self.fan2_fault:
        f1_pass    = 'EQUAL'
        f1_lo      = 1
        f1_hi      = 1
        f1_msg     = 'fan 1 should power on'
        f2_pass    = 'NOT_EQUAL'
        f2_lo      = 1
        f2_hi      = 1
        f2_msg     = 'fan 2 should not power on'
        e_pass     = 'EQUAL'
        e_lo       = 3
        e_hi       = 3
        e_msg      = 'both fans are available'
        assign_var = 'self.model.fan1_power_status'

    elif self.fan1_fault and not self.fan2_fault:
        f1_pass    = 'NOT_EQUAL'
        f1_lo      = 1
        f1_hi      = 1
        f1_msg     = 'fan 1 should not power on'
        f2_pass    = 'EQUAL'
        f2_lo      = 1
        f2_hi      = 1
        f2_msg     = 'fan 2 should power on'
        e_pass     = 'EQUAL'
        e_lo       = 3
        e_hi       = 3
        e_msg      = 'only fan 2 is available'
        assign_var = 'self.model.fan2_power_status'

    elif not self.fan1_fault and self.fan2_fault:
        f1_pass    = 'EQUAL'
        f1_lo      = 1
        f1_hi      = 1
        f1_msg     = 'fan 1 should power on'
        f2_pass    = 'NOT_EQUAL'
        f2_lo      = 1
        f2_hi      = 1
        f2_msg     = 'fan 2 should not power on'
        e_pass     = 'EQUAL'
        e_lo       = 3
        e_hi       = 3
        e_msg      = 'only fan 1 is available'
        assign_var = 'self.model.fan1_power_status'

    elif self.fan1_fault and self.fan2_fault:
        f1_pass    = 'NOT_EQUAL'
        f1_lo      = 1
        f1_hi      = 1
        f1_msg     = 'fan 1 should not power on'
        f2_pass    = 'NOT_EQUAL'
        f2_lo      = 1
        f2_hi      = 1
        f2_msg     = 'fan 2 should not power on'
        e_pass     = 'EQUAL'
        e_lo       = 3
        e_hi       = 3
        e_msg      = 'no fans available'
        assign_var = None
        
    yield scheduler.Parallel(
        self.Validation(model_var = 'self.model.fan1_power_enable', 
                        hi = f1_hi, 
                        lo = f1_lo, 
                        timeout = 1000, 
                        duration = 0, 
                        pass_criteria = f1_pass, 
                        description = f1_msg),
        self.Validation(model_var = 'self.model.fan2_power_enable', 
                        hi = f2_hi, 
                        lo = f2_lo, 
                        timeout = 1000, 
                        duration = 0, 
                        pass_criteria = f2_pass, 
                        description = f2_msg))

    if assign_var:
        self.Assignment(model_var = assign_var, value = 1)

    self.Validation(model_var = 'self.model.eicas',
                    hi = e_hi, 
                    lo = e_lo, 
                    timeout = 1000, 
                    duration = 0, 
                    pass_criteria = e_pass, 
                    description = e_msg)

