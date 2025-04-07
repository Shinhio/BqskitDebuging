from bqskit import Circuit
from bqskit.compiler import Compiler, Workflow, GateSet
from bqskit.passes import QuickPartitioner, LEAPSynthesisPass, UnfoldPass
from bqskit.ext import model_from_backend
from bqskit.ir.gates import SXGate, RZGate, ECRGate, XGate

import numpy as np
import pickle

from qiskit_ibm_runtime import QiskitRuntimeService

## Getting the ibm_backedn for the  QPU we're targeting.
## Removed my api key for the moment for the debugging.  
backend = ibm_service.backend("ibm_sherbrooke")


## IBM Sherbooke machine model missing ECRGate, adding it in. 
machineModel = model_from_backend(backend)
machineModel.gate_set = GateSet({SXGate(), XGate(), ECRGate(), RZGate()})

print("IBM QPU Native Gates:", backend.configuration().basis_gates)
print("Set Native Gate Set for Optimizer:", machineModel.gate_set)


circuit_file_path = "Spin12_circs"

## Using what I think is the workflow that Dr. Iancu recomended.
Costin_workflow = Workflow([QuickPartitioner(4), LEAPSynthesisPass()])

circs = []

## Optimizing the <sigma_x> circuits over the full temperature range.
for i in np.arange(0.1, 2, 0.1):

  ## Reading in the qasm circuit to optimize.
  print(circuit_file_path + "/sigma_x/sigma_x_" + str(round(i, 1)) + "_circ.qasm")
  circuit_x = Circuit.from_file(circuit_file_path + "/sigma_x/sigma_x_" + str(round(i, 1)) + "_circ.qasm")
  print("Loaded in circuit #", i)

  with Compiler() as compiler:
    circs.append(compiler.compile(circuit_x, workflow=Costin_workflow))
    print("Gate Counts:", circuit_x.gate_counts)


## Save the array containing the optimized circuits to disk.
pickle.dump(circs, open(circuit_file_path + "bqskit_spin12_circs_sigmax", 'wb'))

circs = []

## Optimizing the <sigma_y> circuits over the full temperature range.
for i in np.arange(0.1, 2, 0.1):

  ## Reading in the qasm circuit to optimize.
  print(circuit_file_path + "/sigma_y/sigma_y_" + str(round(i, 1)) + "_circ.qasm")
  circuit_x = Circuit.from_file(circuit_file_path + "/sigma_y/sigma_y_" + str(round(i, 1)) + "_circ.qasm")
  print("Loaded in circuit #", i)

  with Compiler() as compiler:
    circs.append(compiler.compile(circuit_x, workflow=Costin_workflow))
    print("Gate Counts:", circuit_x.gate_counts)

## Save the array containing the optimized circuits to disk.
pickle.dump(circs, open(circuit_file_path +"bqskit_spin12_circs_sigmay", 'wb'))
