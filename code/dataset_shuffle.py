import numpy as np
import pandas as pd

#dataset import
df=pd.read_csv('./(block) ton_memory.csv')

#shuffle
df = df.sample(frac=1)
df

#check cutoff (7:3 비율로 학습:검증 데이터 셋 나누기 위한 부분)
df.iloc[7000:7001,:1]
cutoff = 1554234730

#타임스탬프를 인덱스로 넣은 다음, 인덱스를 리셋 해주어서 최종적으로 시계열 정보를 모두 없앰
df = df.set_index('ts')
df
df.reset_index(drop=False, inplace=True)
df.drop(['ts'], axis=1)
df

#shuffle 데이터 셋을 csv 파일로 저장
df.to_csv("(block) shuffle dataset.csv")
