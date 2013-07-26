
run_list = [ {'TEST_RUN' : 'r1', 'description': 'Fan1 ok, Fan2 ok at startup mode test'     , 'fan1_fault (enum)': False,  'fan2_fault (enum)': False, 'powerup': False},
             {'TEST_RUN' : 'r2', 'description': 'Fan1 Fault Fan2 ok at startup mode'        , 'fan1_fault (enum)': True ,  'fan2_fault (enum)': False, 'powerup': False},
             {'TEST_RUN' : 'r3', 'description': 'Fan1 ok Fan2 faulted at startup mode'      , 'fan1_fault (enum)': False,  'fan2_fault (enum)': True,  'powerup': False},
             {'TEST_RUN' : 'r4', 'description': 'Fan1 faulted Fan2 faulted at startup mode' , 'fan1_fault (enum)': True ,  'fan2_fault (enum)': True,  'powerup': False},
             {'TEST_RUN' : 'r5', 'description': 'Fan1 faulted Fan2 faulted at startup mode' , 'fan1_fault (enum)': False , 'fan2_fault (enum)': False, 'powerup': True}]
