from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal


class CalculationInput(BaseModel):
    firstName: str
    lastName: str
    city: str
    age: int = Field(ge=18, le=100)
    insuranceType: Literal['Car']|Literal['Home']|Literal['Travel']
    vehicleProductionYear: int | None = Field(default=None)
    coverageAmount: float = Field(ge=1000)
    additionalOptions: bool

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post(
    "/calculate-risk",
)
def read_assets(data: CalculationInput) -> dict[Literal["riskLevel"],Literal['low']|Literal['medium']|Literal['high']]:
    insuranceTypeFactor = None
    riskLevelCategory = None

    match data.insuranceType:
        case 'Car':
            insuranceTypeFactor = 3
        case 'Home':
            insuranceTypeFactor = 2
        case 'Travel':
            insuranceTypeFactor = 1

    riskLevel = (data.age / 10) + (data.coverageAmount / 10000) + insuranceTypeFactor

    if riskLevel <= 5:
        riskLevelCategory = 'low'
    elif riskLevel > 5 and riskLevel < 8:
        riskLevelCategory = 'medium'
    else:
        riskLevelCategory = 'high'

    return {"riskLevel": riskLevelCategory}

