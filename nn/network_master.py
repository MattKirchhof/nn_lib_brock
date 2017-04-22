'''
Created on Apr 21, 2017

@author: Matth

The master class users will import into their projects. They will only call commands from this
class, where this class will manage the network and perform the desired actions
'''
from nn.network_data import network_data
from nn.network_trainer import network_trainer
import sys

class network_master():
    global nd, nt
    
    
    def __init__(self):        
        return
    
    #Accepts two files, one with the training data and one with the expected results
    #sends the data to network_data
    def loadData(self, fileName, expectedName, delim):
        global nd
        
        #If nd doesnt exist (user hasnt initialized the network data), catch the error
        try:
            nd.loadTrainingData(fileName, expectedName, delim)
            print ("Data loaded...")
            print (nd.trainingData)
            
        except NameError:
            sys.stderr.write("  ERROR: Must create network before loading in data!")
            return
    
    #Creates our network data object and sets its values accordingly
    def createNetwork(self, learningTechnique, layers, learningRate, randWeightRange):
        global nd
        
        nd = network_data()
        nd.setLearningTechnique(learningTechnique)
        nd.setLearningRate(learningRate)
        nd.setRandomRange(randWeightRange)
        
        print() #to space out our console text
        nd.buildNetwork(layers) #always build the network after setting network values
        print()
        
    #Creates our network trainer object, passes it our network data
    #calls its training method
    def trainNetwork(self):
        global nd
        
        if (nd.trainingData is None):
            sys.stderr.write("  ERROR: Must load training data!")
            return
            
        nt = network_trainer(nd)
        nt.trainNetwork()
        

##RAW CODE FOR TESTING PURPOSES
layers = [[4,"sigmoid"],[3,"sigmoid"],[1,"sigmoid"]]

testNetwork = network_master()
testNetwork.createNetwork("backprop", layers, 0.2, 0.6)
testNetwork.loadData("parity4.txt","parity4Expected.txt", ',')
testNetwork.trainNetwork()
        
        
        