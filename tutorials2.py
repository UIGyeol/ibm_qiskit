#!pip install qiskit
#!pip install qiskit[visualization]
#!pip install qiskit-aer
#!pip install qiskit-ibm-provider

from qiskit_ibm_provider import IBMProvider
#IBM에서 복사한 토근을 로컬에 저장하기
provider = IBMProvider(token='put_your_token') 
backends = provider.backends()
from qiskit import QuantumCircuit 
from qiskit_aer import AerSimulator,Aer
from qiskit.primitives import Estimator, Sampler # qiskit.primitives에서 Estimator와 Sampler를 가져오기
from qiskit.visualization import plot_histogram

# Aer 백엔드를 사용해야 하는 경우:
from qiskit_aer import AerSimulator
simulator = AerSimulator()

# 인수 없이 Estimator를 초기화
estimator = Estimator() 
sampler = Sampler()

# 작업을 실행할 때 estimator의 'run' 메서드의 'backend' 인수를 사용하여 시뮬레이터를 지정
# result = estimator.run(circuits, observables, backend=simulator).result()  # 기대값 계산
# 또는
# result = sampler.run(circuits).result()  # 확률 샘플링

#Making circuit instance
n_input=1101
n_input=len(n_input)+1
n_output=n_input-1
circ= QuantumCircuit(n_input,n_output)
circ.measure(range(n_output), range(n_output))

#Visualizing Circuit
circ.draw(output='mpl',justify='none')
#Testing c다

# 양자 백엔드마다 기본적으로 사용하는 게이트가 다를 수 있기 때문에  
# transpile로 양자 백엔드가 사용할 수 있게 한 번 번역해 줘야한다. 
from qiskit import transpile
circ_trans=transpile(circ,backend)
# 아래는 회로를 그리는 방법들
#트랜스 파일을 mpl방식으로 보여줌--> 사용되지 않은 것도 보여줌
display(circ.draw('mpl'))
#wires을 보여주지 않는 방식
display(circ_trans.draw('mpl',idle_wires=False))
#트랜스 파일이 된 회로 
display(circ_trans.draw('mpl'))


conf=backend.configuration()
# job0=backend.run(circ,shots=conf.max_shots)
# print(job0.job_id())
# 더 이상 'qiskit.tools'을 사용하지 않음
from qiskit_ibm_provider.job import job_monitor
job0=prov.retrieve_job('cxvbz3w0v1500080fg6g')
job_monitor(job0)


#백엔드에 노이즈 특성을 널어서 확인하는 방법
sim=AerSimulator.from_backend(backend)
#sim이라는 백엔드를 새로 정의를 하고 에어시뮬레이터의 백엔드를 가져오자 

