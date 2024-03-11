# ChatGPT was used to create this code
# Dr. Smay and Ashley helped with this code
#region imports
from scipy.optimize import fsolve
from HW6_1_OOP import ResistorNetwork,Loop,Resistor,VoltageSource
#endregion

#region class definitions
class ResistorNetwork2(ResistorNetwork):
    def __init__(self):
        """
        This is an inherited class from HW6_1_OOP, it overrides AnalyzeCircuit and GetKirchoffVals to account for the
        newly added currents because of the inclusion of a 5 ohm resistor in parallel to the 32 V source.
        """
        super().__init__()





    def AnalyzeCircuit(self):
        """
      This function implements polymorphism as it changes an already defined function in a class. It includes 5 initial
      guesses for the currents. Then, performs fsolve to the equations made by the GetKirchoffVals. It then prints out
      each current.

        1. KCL:  The total current flowing into any node in the network is zero.
        2. KVL:  When traversing a closed loop in the circuit, the net voltage drop must be zero.
        :return: a list of the currents in the resistor network
        """
        # need to set the currents to that Kirchoff's laws are satisfied
        num_loops = len(self.Loops)
        i0 = [1.0, 1.0, 1.0, 1.0, 1.0]   #define an initial guess for the currents in the circuit
        i = fsolve(self.GetKirchoffVals,i0)
        print("I1 = {:0.3f} A".format(i[0]))
        print("I2 = {:0.3f} A".format(i[1]))
        print("I3 = {:0.3f} A".format(i[2]))
        print("I4 = {:0.3f} A".format(i[3]))
        print("I5 = {:0.3f} A".format(i[4]))
        return i

    def GetKirchoffVals(self,i):
        """
        This function uses Kirchoff Voltage and Current laws to analyze the second circuit. 
        It uses Polyphormism to change an existing function
        KVL:  The net voltage drop for a closed loop in a circuit should be zero
        KCL:  The net current flow into a node in a circuit should be zero
        :param i: a list of currents relevant to the circuit
        :return: a list of loop voltage drops and node currents
        """

        # set current in resistors in the top loop.
        self.GetResistorByName('ad').Current=i[0]  #I_1 in diagram
        self.GetResistorByName('bc').Current=i[0]  #I_1 in diagram
        self.GetResistorByName('cd').Current= i[2]  #I_3 in diagram
        #set current in resistor in bottom 2 loop.
        self.GetResistorByName('df').Current = i[1] #I_2 in diagram
        self.GetResistorByName('de').Current = i[3] #I_4 in diagram
        self.GetResistorByName('ce').Current= i[4] #I_5 in diagram

        #calculate net current into node c
        Node_c_Current = sum([i[0],i[4],-i[2]])


        #calculate net current into node d
        Node_d_Current = sum([i[2],i[3],-i[0],-i[1]])

        KVL = self.GetLoopVoltageDrops()  # three equations here
        KVL.append(Node_c_Current)# two equation here
        KVL.append(Node_d_Current)
        return KVL


def main():
    """
    This program solves for the unknown currents in the second circuit of the homework assignment.
    :return: nothing
    """
    Net = ResistorNetwork2() #Instantiate a resistor network object
    filename = 'ResistorNetwork2.txt'
    Net.BuildNetworkFromFile(filename) #call the function from Net that builds the resistor network from a text file
    IVals = Net.AnalyzeCircuit()
# endregion

# region function calls
if __name__=="__main__":
    main()
# endregion
