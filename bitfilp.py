#!pip install qiskit
#!pip install qiskit[visualization]
#!pip install qiskit-aer
#!pip install qiskit-ibm-provider
#!pip install qiskit-ibm-runtime
#reference:https://github.com/qiskit-community/ibm-quantum-challenge-2021/blob/main/content/ex3/ex3-ko.ipynb

from qiskit import QuantumCircuit
from qiskit_aer import Aer 

qc_init = QuantumCircuit(2)
qc_init.h(0)
qc_init.cx(0,1)

display(qc_init.draw('mpl'))

qc=qc_init.copy()
qc.measure_all()
job=Aer.get_backend('aer_simulator').run(qc)
job.result().get_counts


# bit filp 오류 만들기
qc_insert=QuantumCircuit(2)
qc_insert.x(0)

# 기존 회로에 추가하기
qc=qc_init.copy()
qc.compose(qc_insert)
# 회로 그리기
display(qc.draw('mpl'))
# 출력얻기
qc.measure_all()
job=Aer.get_backend('aer_simulator').run(qc)
job.result().get_counts()

# 얽힘 풀기
qc_syn=QuantumCircuit(2)
qc_syn.cx(0,1)
qc_syn.h(0)
# 오류 이후에 이것을 추가하기
qc=qc_init.copy()
qc=qc.compose(qc_syn)
# 회로 그리기
display(qc.draw('mpl'))
# 출력 얻기
qc.measure_all() 
job = Aer.get_backend('qasm_simulator').run(qc)
job.result().get_counts()

# 오류 정의하기

qc_insert=QuantumCircuit(2)
qc_insert.x(0)
# 얽힘 풀기
qc_syn=QuantumCircuit(2)
qc_syn.cx(0,1)
qc_syn.h(0)

# 오류 이후에 이것을 추가하기
qc=qc_init.copy()
qc=qc.compose(qc_insert)
qc=qc.compose(qc_syn)

# 회로 그리기
display(qc.draw('mpl'))

# 출력 얻기
qc.measure_all() 
job = Aer.get_backend('qasm_simulator').run(qc)
job.result().get_counts()
