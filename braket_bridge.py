# AWS imports: Import Braket SDK modules
import boto3 
from braket.circuits import Circuit
from braket.devices import LocalSimulator
from braket.aws import AwsDevice, AwsQuantumTask

# general math imports
import math, random
import numpy as np
from scipy.fft import fft, ifft

# import convex solver
import cvxpy as cp

# enter the S3 bucket you created during onboarding (or any other bucket starting with "amazon-braket-") 
my_bucket = "amazon-braket-ac6dba3afa69" # the name of the bucket
my_prefix = "my-folder" # the name of the folder in the bucket
s3_folder = (my_bucket, my_prefix)

# set up Rigetti quantum device
rigetti = AwsDevice("arn:aws:braket:::device/qpu/rigetti/Aspen-10")

# set up IonQ quantum device
#ionq = AwsDevice("arn:aws:braket:::device/qpu/ionq/ionQdevice")

# simulator alternative: set up the managed simulator SV1
simulator = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")

#print(simulator.properties)

# AWS imports: Import Braket SDK modules
from braket.circuits import Circuit

# set up local simulator device
#device = LocalSimulator()
device = rigetti

# function for Hadamard cirquit
def hadamard_circuit(n_qubits):
    """
    function to apply Hadamard gate on each qubit
    input: number of qubits
    """

    # instantiate circuit object
    circuit = Circuit()

    # apply series of Hadamard gates
    for i in range(n_qubits):
        circuit.h(i)
    return circuit

def run_circuit():
    """
    function to execute circuit
    parameters: n qubits, n shots
    """
    # define circuit
    n_qubits = 1
    state = hadamard_circuit(n_qubits)
    # print circuit
    print(state)
    print()    
    # run circuit
    m_shots = 128
    result = device.run(state, s3_folder, shots = m_shots).result()
    #result = device.run(state, m_shots).result()
    res_array = result.measurements
    shot_str=''
    
    for i in range(m_shots):
        shot_str+=str(res_array[i][0])
    
    #print(shot_str)

    shot_arr = [shot_str]

    # get measurement shots
    counts = result.measurement_counts.keys()

    # print counts
    list_one = list(counts)[0]
    #list_one = list(counts)[0]
    array_one = np.array([list_one])
    #print("The output bit string is: ",array_one)
    #return array_one[0]
    return shot_arr[0]
