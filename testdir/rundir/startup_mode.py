from rttlib import scheduler

enableCapturing   = True
enableMaintenance = True
enableEventCheck  = True
test_name         = 'Powerup Mode'
requirements      = '1,5,6,7,8'

def RunScript(self):

    self.Assignment(model_var = 'self.model.fan1FaultRead', value = 1 if self.fan1_fault else 0)
    self.Assignment(model_var = 'self.model.fan2FaultRead', value = 1 if self.fan2_fault else 0)

    if self.powerup:
        self.Assignment(model_var = 'self.model.enableCanTx', value = 0)
        yield self.Prompt("Power OFF")
        yield self.Prompt("Power ON")
        yield self.model.Delay(5000)
    else:
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
        fan_pwr    = 'self.model.fan1_power_status'
        fan_spd    = 'self.model.fan1_high_low'
        airflow    = 'self.model.fan1_airflow_sensor_fb'

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
        e_lo       = 2
        e_hi       = 2
        e_msg      = 'only fan 2 is available'
        fan_pwr    = 'self.model.fan2_power_status'
        fan_spd    = 'self.model.fan2_high_low'
        airflow    = 'self.model.fan2_airflow_sensor_fb'

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
        e_lo       = 1
        e_hi       = 1
        e_msg      = 'only fan 1 is available'
        fan_pwr    = 'self.model.fan1_power_status'
        fan_spd    = 'self.model.fan1_high_low'
        airflow    = 'self.model.fan1_airflow_sensor_fb'

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
        e_lo       = 0
        e_hi       = 0
        e_msg      = 'no fans available'
        fan_pwr    = None
        fan_spd    = None
        
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

    if fan_pwr:
        self.Assignment(model_var = airflow, value = 3)
        self.Assignment(model_var = fan_pwr, value = 1)

    yield self.Validation(model_var = 'self.model.eicas',
                          hi = e_hi, 
                          lo = e_lo, 
                          timeout = 1000, 
                          duration = 0, 
                          pass_criteria = e_pass, 
                          description = e_msg)

    if fan_spd:
        yield self.Validation(model_var = fan_spd,
                              hi = 0, 
                              lo = 0, 
                              timeout = 1000, 
                              duration = 0, 
                              pass_criteria = 'EQUAL', 
                              description = 'low fan speed')
