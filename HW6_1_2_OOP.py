#region imports
from scipy.optimize import fsolve
from HW6_1_OOP import ResistorNetwork,Loop,Resistor,VoltageSource
#endregion

#region class definitions
class ResistorNetwork2(ResistorNetwork):
    def __init__(self):
        super().__init__()


    def AnalyzeCircuit(self):
        """
      Overriding this method for the new circuit
        """
        # need to set the currents to that Kirchoff's laws are satisfied
        num_loops = len(self.Loops)
        i0 = [1.0, 1.0, 1.0, 1.0, 1.0]   #define an initial guess for the currents in the circuit
        i = fsolve(self.GetKirchoffVals,i0)
        for index, current in enumerate(i):
            print(f"Type of i[{index}] is {type(current)} with value {current}")
        # print output to the screen
        print("I1 = {:0.1f}".format(i[0]))
        print("I2 = {:0.1f}".format(i[1]))
        print("I3 = {:0.1f}".format(i[2]))
        print("I4 = {:0.1f}".format(i[3]))
        print("I5 = {:0.1f}".format(i[4]))
        return i

    def GetKirchoffVals(self,i):
        """
        This function uses Kirchoff Voltage and Current laws to analyze this specific circuit
        KVL:  The net voltage drop for a closed loop in a circuit should be zero
        KCL:  The net current flow into a node in a circuit should be zero
        :param i: a list of currents relevant to the circuit
        :return: a list of loop voltage drops and node currents
        """

        # set current in resistors in the top loop.
        self.GetResistorByName('ad').Current=i[0]  #I_1 in diagram
        self.GetResistorByName('bc').Current=i[0]  #I_1 in diagram
        self.GetResistorByName('cd').Current= i[0]+i[4]  #I_3 in diagram
        #set current in resistor in bottom loop.
        self.GetResistorByName('de').Current = i[1]-i[4]
        self.GetResistorByName('ce').Current= i[4] #I_5 in diagram

        #calculate net current into node c
        Node_c_Current = sum([i[0],i[4],-i[2]])
        Node_e_Current = sum([i[1],-i[4],-i[3]])

        KVL = self.GetLoopVoltageDrops()  # three equations here
        KVL.append(Node_c_Current)# two equation here
        KVL.append(Node_e_Current)
        return KVL


def main():
    """
    This program solves for the unknown currents in the circuit of the homework assignment.
    :return: nothing
    """
    Net = ResistorNetwork2() # JES MISSING CODE  #Instantiate a resistor network object
    filename = 'ResistorNetwork2.txt'
    Net.BuildNetworkFromFile(filename)  # JES MISSING CODE #call the function from Net that builds the resistor network from a text file
    IVals = Net.AnalyzeCircuit()
    print(IVals)
# endregion

# region function calls
if __name__=="__main__":
    main()
# endregion