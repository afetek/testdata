
run_list = [ {'TEST_RUN' : 'r1', 'description': 'Fan1 ok, Fan2 ok at startup mode test'     , 'fan1_fault': False, 'fan2_fault': False},
             {'TEST_RUN' : 'r2', 'description': 'Fan1 Fault Fan2 ok at startup mode'        , 'fan1_fault': True , 'fan2_fault': False},
             {'TEST_RUN' : 'r3', 'description': 'Fan1 ok Fan2 faulted at startup mode'      , 'fan1_fault': False, 'fan2_fault': True},
             {'TEST_RUN' : 'r4', 'description': 'Fan1 faulted Fan2 faulted at startup mode' , 'fan1_fault': True , 'fan2_fault': True}]
