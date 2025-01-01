# Qiskit IBM Provider를 설치 (터미널로 실행)
!pip install qiskit_ibm_provider

# Qiskit의 주피터 관련 툴 가져오기
import qiskit.tools.jupyter

# 현재 Qiskit 버전 정보 출력
%qiskit_version_table

# 설치된 Qiskit의 세부 정보 출력
!pip show qiskit

# Qiskit 업그레이드
!pip install --upgrade qiskit

# Qiskit의 버전을 변수에 저장하고 출력
from qiskit import __version__ as qiskit_version
print("Qiskit version:", qiskit_version)

# 데이터 분석 및 수학 연산 라이브러리 가져오기
import numpy as np
import pandas as pd

# Qiskit 모듈과 시각화 도구 가져오기
from qiskit import *
from qiskit.visualization import plot_histogram, plot_distribution, plot_error_map

# Hellinger fidelity 계산 도구 가져오기
from qiskit.quantum_info import hellinger_fidelity

# Qiskit IBM Provider 가져오기
from qiskit_ibm_provider import IBMProvider

# Qiskit Aer 시뮬레이터 설치
!pip install qiskit-aer

# 그래프 시각화를 위한 Matplotlib 가져오기
import matplotlib.pyplot as plt

# 스타일 설정 (quantum-light 스타일이 설치되어 있다면 적용)
try:
    plt.style.use('quantum-light')
except:
    pass

# 주피터 노트북의 그래프 해상도를 레티나로 설정
%config InlineBackend.figure_fomat='retina'

# 베르사비아 알고리즘(Bernstein-Vazirani Algorithm) 구현
# 측정할 이진 문자열 정의
a = '1101'

# 큐비트 개수: 이진 문자열 길이 + 1
nq = len(a) + 1

# 퀀텀 회로 생성
bv = QuantumCircuit(nq, nq - 1)

# 마지막 큐비트에 X 게이트 적용 (|1> 상태 준비)
bv.x(nq - 1)

# 모든 큐비트에 H 게이트 적용 (초기화 상태)
bv.h(range(nq))

# 상태를 구분하기 위한 장벽 추가
bv.barrier()

# 비밀 이진 문자열을 cx 게이트로 인코딩
bv.cx([0, 2, 3], nq - 1)

# 상태를 구분하기 위한 장벽 추가
bv.barrier()

# 다시 모든 큐비트에 H 게이트 적용
bv.h(range(nq))

# 상태를 구분하기 위한 장벽 추가
bv.barrier()

# 측정: 앞의 큐비트들(비밀 문자열 길이)만 측정
bv.measure(range(nq - 1), range(nq - 1))

# Qiskit Aer 시뮬레이터 실행
# pylatexenc 설치 (시각화 지원)
!pip install pylatexenc

# Qiskit Aer 가져오기
from qiskit_aer import Aer

# Aer 시뮬레이터 백엔드 선택
backend = Aer.get_backend('aer_simulator')

# 회로 실행
job = backend.run(bv)

# 실행 결과 가져오기
result = job.result()

# 측정 결과 (count_bv) 출력
count_bv = result.get_counts()
print(count_bv)

# 결과를 히스토그램으로 시각화
plot_histogram(count_bv)

# IBM 퀀텀 디바이스로 실행
# IBM Provider와 백엔드 가져오기
from qiskit_ibm_provider import IBMProvider, IBMBackend
from qiskit import QuantumCircuit, transpile

# Aer 시뮬레이터 다시 가져오기
from qiskit_aer import Aer

# IBM Provider 설정 (토큰 입력 필요)
provider = IBMProvider(token=token)

# Aer 시뮬레이터 백엔드 가져오기
backend = Aer.get_backend('aer_simulator')

# 퀀텀 회로를 백엔드에 맞게 변환
transpiled_bv = transpile(bv, backend)

# 실행
job = backend.run(transpiled_bv)

# 실행 결과 가져오기
result = job.result()

# 측정 결과 출력
count_bv = result.get_counts()
print(count_bv)
