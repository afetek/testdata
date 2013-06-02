
enableCapturing   = True
enableMaintenance = True
enableEventCheck  = True
testName          = 'script2'

def RunScript(self):
    self.Print("signal1: " + str(self.signal1))
    self.Print("signal2: " + str(self.signal2))
    
    self.Print('1: ', self.PASS)
    self.Print('2: ', self.PASS)
    self.Print('3: ', self.PASS)
    self.Print('4: ', self.PASS)



