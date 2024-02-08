# 서버 관리용 fastapi 의존 라이브러리
import uvicorn

# fast api 라이브러리
from fastapi import FastAPI

# 머신러닝 모델 관리용 라이브러리
import pickle

# 데이터프레임 및 수 처리 라이브러리
import pandas as pd
import numpy as np
# 인터페이스 데이터 관리를 위한 라이브러리
from pydantic import BaseModel

# 피클 형태로 모델 불러오기
with open("mldt.dump","rb") as model_file:
    mlCore = pickle.load(model_file) 

# 앱 실행
app = FastAPI(title="ML API")

class InDataset(BaseModel):
    Promotion: float
    Week: int
    Yearweek: int
    Year: int
    Hclus: int
    
@app.post("/predict", status_code=200)
async def predict_tf(x: InDataset):
    x_df = pd.DataFrame([[ x.Promotion  , x.Week, x.Yearweek, x.Year, x.Hclus  ]])
    res = mlCore.predict(x_df)[0]
    print(res)
    return {"prediction": res }

@app.get('/')
async def root():
    return {"message": "online"}


