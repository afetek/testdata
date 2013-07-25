from rttlib import scheduler

enableCapturing   = True
enableMaintenance = True
enableEventCheck  = True
testName = ''

def RunScript(self):

    self.Print("Powerup Test Script")
    self.Print("Testing Requirements: Statrup Mode - 5 through 8")

    if self.fan1_fault:
        self.Assignment(model_var = 'self.model.fan1FaultRead', value = 1)
    if self.fan2_fault:
        self.Assignment(model_var = 'self.model.fan2FaultRead', value = 1)
    
    self.Assignment(model_var = 'self.model.powerECU', value = 1)

    if not self.fan1_fault and not self.fan2_fault:
        yield scheduler.Parallel(
            self.Validation(model_var = 'self.model.fan1_power_enable', 
                            hi = 1, 
                            lo = 1, 
                            timeout = 1000, 
                            duration = 0, 
                            pass_criteria = 'EQUAL', 
                            description = 'fan 1 should power on'),
            self.Validation(model_var = 'self.model.fan2_power_enable', 
                            hi = 1, 
                            lo = 1, 
                            timeout = 1000, 
                            duration = 0, 
                            pass_criteria = 'NOT_EQUAL', 
                            description = 'fan 2 should not power on'),
            self.Validation(model_var = 'self.model.eicas', 
                            hi = 3, 
                            lo = 3, 
                            timeout = 1000, 
                            duration = 0, 
                            pass_criteria = 'EQUAL', 
                            description = 'Both fans are Available EICAS message'))

    if self.fan1_fault and not self.fan2_fault:
        yield scheduler.Parallel(
            self.Validation(model_var = 'self.model.fan2_power_enable', 
                            hi = 1, 
                            lo = 1, 
                            timeout = 1000, 
                            duration = 0, 
                            pass_criteria = 'EQUAL', 
                            description = 'fan 2 should power on'),
            self.Validation(model_var = 'self.model.fan1_power_enable', 
                            hi = 1, 
                            lo = 1, 
                            timeout = 1000, 
                            duration = 0, 
                            pass_criteria = 'NOT_EQUAL', 
                            description = 'fan 1 should not power on'),
            self.Validation(model_var = 'self.model.eicas', 
                            hi = 2, 
                            lo = 2, 
                            timeout = 1000, 
                            duration = 0, 
                            pass_criteria = 'EQUAL', 
                            description = 'No Fans Available EICAS message'))

    if not self.fan1_fault and self.fan2_fault:
        yield scheduler.Parallel(
            self.Validation(model_var = 'self.model.fan1_power_enable', 
                            hi = 1, 
                            lo = 1, 
                            timeout = 1000, 
                            duration = 0, 
                            pass_criteria = 'EQUAL', 
                            description = 'fan 1 should power on'),
            self.Validation(model_var = 'self.model.fan2_power_enable', 
                            hi = 1, 
                            lo = 1, 
                            timeout = 1000, 
                            duration = 0, 
                            pass_criteria = 'NOT_EQUAL', 
                            description = 'fan 2 should not power on'),
            self.Validation(model_var = 'self.model.eicas', 
                            hi = 1, 
                            lo = 1, 
                            timeout = 1000, 
                            duration = 0, 
                            pass_criteria = 'EQUAL', 
                            description = 'Both fans are Available EICAS message'))


    if self.fan1_fault and self.fan2_fault:
        yield scheduler.Parallel(
            self.Validation(model_var = 'self.model.fan2_power_enable', 
                            hi = 1, 
                            lo = 1, 
                            timeout = 1000, 
                            duration = 0, 
                            pass_criteria = 'NOT_EQUAL', 
                            description = 'fan 2 should not power on'),
            self.Validation(model_var = 'self.model.fan1_power_enable', 
                            hi = 1, 
                            lo = 1, 
                            timeout = 1000, 
                            duration = 0, 
                            pass_criteria = 'NOT_EQUAL', 
                            description = 'fan 1 should not power on'),
            self.Validation(model_var = 'self.model.eicas', 
                            hi = 0, 
                            lo = 0, 
                            timeout = 1000, 
                            duration = 0, 
                            pass_criteria = 'EQUAL', 
                            description = 'No Fans Available EICAS message'))

