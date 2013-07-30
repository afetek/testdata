
run_list = [ {'TEST_RUN' : 'r1', 'DESCRIPTION': 'Fans OK at startup'              , 'fan1_fault (enum)': False,  'fan2_fault (enum)': False, 'powerup (enum)': False},
             {'TEST_RUN' : 'r2', 'DESCRIPTION': 'Fan1 faulted at startup'         , 'fan1_fault (enum)': True ,  'fan2_fault (enum)': False, 'powerup (enum)': False},
             {'TEST_RUN' : 'r3', 'DESCRIPTION': 'Fan2 faulted at startup'         , 'fan1_fault (enum)': False,  'fan2_fault (enum)': True,  'powerup (enum)': False},
             {'TEST_RUN' : 'r4', 'DESCRIPTION': 'Fan1 and Fan2 faulted at startup', 'fan1_fault (enum)': True ,  'fan2_fault (enum)': True,  'powerup (enum)': False},
             {'TEST_RUN' : 'r5', 'DESCRIPTION': 'Fans OK, powerup to startup'     , 'fan1_fault (enum)': False , 'fan2_fault (enum)': False, 'powerup (enum)': True}]
