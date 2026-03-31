from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_calculate_risk_returns_correct_calculation():
    response = client.post(
        "/calculate-risk",
        json={
            "firstName": "X",
            "lastName": "Y",
            "city": "Z",
            "age": "40",
            "coverageAmount": "1000",
            "insuranceType": "Car",
            "vehicleProductionYear": "1999",
            "additionalOptions": "false",
        },
    )
    assert response.json()["riskLevel"] == "medium"


def test_calculate_risk_returns_error_for_underage():
    response = client.post(
        "/calculate-risk",
        json={
            "firstName": "X",
            "lastName": "Y",
            "city": "Z",
            "age": "17",
            "coverageAmount": "1000",
            "insuranceType": "Car",
            "vehicleProductionYear": "1999",
            "additionalOptions": "false",
        },
    )
    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "Input should be greater than or equal to 18"
    )


def test_calculate_risk_returns_error_for_too_low_coverage():
    response = client.post(
        "/calculate-risk",
        json={
            "firstName": "X",
            "lastName": "Y",
            "city": "Z",
            "age": "40",
            "coverageAmount": "999",
            "insuranceType": "Car",
            "vehicleProductionYear": "1999",
            "additionalOptions": "false",
        },
    )
    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "Input should be greater than or equal to 1000"
    )
