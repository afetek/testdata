from rttlib import scheduler

ENABLE_CAPTURING   = True
ENABLE_MAINTENANCE = True
ENABLE_EVENTCHECK  = True
TEST_NAME         = 'FANSPEED'
REQUIREMENTS      = '16, 17, 18, 19, 20'

def RunScript(self):

    self.Assignment(model_var = 'self.model.fan1FaultRead', value = 0 if self.fan == 'fan1' else 1)
    fan_on                    = 'self.model.%s_power_enable'      % self.fan
    fan_pwr                   = 'self.model.%s_power_status'      % self.fan
    airflow                   = 'self.model.%s_airflow_sensor_fb' % self.fan
    fan_speed                 = 'self.model.%s_high_low'          % self.fan


    # Turn on the ECS
    self.Assignment(model_var = 'self.model.powerECU', value = 1)

    # wait one second
    yield self.model.Delay(1000) 

    self.Assignment(model_var = airflow, value = 3)
    self.Assignment(model_var = fan_pwr, value = 1)

    yield scheduler.Parallel(
        self.Validation(model_var = fan_on, 
                        hi = 1, 
                        lo = 1, 
                        timeout = 1000, 
                        duration = 0, 
                        pass_criteria = "EQUAL", 
                        description = "%s Should be ON" % self.fan.upper()),
        self.Validation(model_var = fan_speed,
                        hi = 0, 
                        lo = 0, 
                        timeout = 1000, 
                        duration = 0, 
                        pass_criteria = "EQUAL", 
                        description = "%s Should be Low Speed" % sefl.fan.upper()))

    yield self.model.Delay(1000)

