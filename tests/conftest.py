"""Fixtures for DK client tests."""

from pathlib import Path

import pytest
from requests_mock.mocker import Mocker as RequestsMock

from pyecotrend_ista import PyEcotrendIstaDK
from pyecotrend_ista.const import API_BASE_URL_DK, GRAPHS_API_BASE_URL_DK

TEST_EMAIL = "max.istamann@test.com"
TEST_PASSWORD = "password"


@pytest.fixture
def ista_client_dk() -> PyEcotrendIstaDK:
    """Create a DK client instance."""
    return PyEcotrendIstaDK(email=TEST_EMAIL, password=TEST_PASSWORD)


@pytest.fixture
def mock_requests_login_dk(requests_mock: RequestsMock) -> RequestsMock:
    """Mock requests to Login Endpoints."""
    requests_mock.post(
        API_BASE_URL_DK + "token",
        json={
            "access_token": "ACCESS_TOKEN",
            "token_type": "bearer",
            "expires_in": "3600",
            ".issued": "9999-12-24 00:00:00Z",
            ".expires": "9999-12-24 00:00:00Z",
            "Email": "",
            "Phone": "",
            "FirstName": "Max Istamann",
            "InstanceId": "0",
            "Language": "da-DK",
            "Username": "0000000000000",
            "PortalAdminId": "0",
            "ConsId": "00000000000",
            "isTenant": "true",
            "InstId": "000000000",
            "isAdmin": "false",
            "Key": "Value"
        },
    )
    requests_mock.get(
        f"{API_BASE_URL_DK}api/GetUserInfo",
        json={
            "Username": "00000000000",
            "Name": "Max Istamann",
            "Phone": "max.istamann@example.com",
            "Email": "max.istamann@example.com",
            "Language": "da-DK",
            "Address": "Nørrebrogade 56",
            "ZipCity": "København N",
            "ShowEconomy": True,
            "ShowClimate": False
        },
    )

    requests_mock.get(
        f"{API_BASE_URL_DK}api/GetUserSettings",
        json={
            "Mail": "max.istamann@example.com",
            "Phone": "max.istamann@example.com",
            "UseDayValues": True,
            "UseHourValues": True,
            "TenantCount": 1,
            "PreferredProgram": 1,
            "receiveNotification": True,
            "receiveNotificationByMail": True,
            "receiveNotificationByPhone": True
        },
    )

    requests_mock.get(
        f"{API_BASE_URL_DK}api/Meters",
        json={
            "errorMessage": {
                "ErrorType": "",
                "UserMessage": "",
                "InternalMessage": ""
            },
            "Meters": {
                "Value": [
                    {
                        "Message": " ",
                        "Headline": "Varme",
                        "MeterText": "Varme",
                        "MeterType": "HCA",
                        "Unit": "Delinger",
                        "INST_NO": 0000,
                        "Last_Meter_Reading": 8151,
                        "Reading_date": "03-02-2026",
                        "Last_Meter_Consumption": 15,
                        "METER_ID": 00000000000,
                        "ROOM_DESCR": "Bathroom",
                        "METER_NO": "000000000",
                        "METCAT_LABEL": "Doprimo 3 SoC",
                        "METTYPE_CODE": None,
                        "Deactivation_date": "3000-01-01T00:00:00",
                        "Activation_date": "2018-04-06T00:00:00"
                    },
                    {
                        "Message": " ",
                        "Headline": "Varme",
                        "MeterText": "Varme",
                        "MeterType": "HCA",
                        "Unit": "Delinger",
                        "INST_NO": 0000,
                        "Last_Meter_Reading": 4485,
                        "Reading_date": "03-02-2026",
                        "Last_Meter_Consumption": 16,
                        "METER_ID": 00000000000,
                        "ROOM_DESCR": "Family kitchen",
                        "METER_NO": "000000000",
                        "METCAT_LABEL": "Doprimo 3 SoC/fj",
                        "METTYPE_CODE": None,
                        "Deactivation_date": "3000-01-01T00:00:00",
                        "Activation_date": "2018-04-06T00:00:00"
                    },
                    {
                        "Message": " ",
                        "Headline": "El",
                        "MeterText": "El",
                        "MeterType": "EL",
                        "Unit": "kWh",
                        "INST_NO": 0000,
                        "Last_Meter_Reading": 0,
                        "Reading_date": None,
                        "Last_Meter_Consumption": 0,
                        "METER_ID": 00000000000,
                        "ROOM_DESCR": "",
                        "METER_NO": "000000",
                        "METCAT_LABEL": "ABB",
                        "METTYPE_CODE": None,
                        "Deactivation_date": "3000-01-01T00:00:00",
                        "Activation_date": "2018-04-06T13:12:32"
                    },
                    {
                        "Message": None,
                        "Headline": None,
                        "MeterText": "Røg",
                        "MeterType": "SMOKE",
                        "Unit": " ",
                        "INST_NO": 0000,
                        "Last_Meter_Reading": 0,
                        "Reading_date": None,
                        "Last_Meter_Consumption": 0,
                        "METER_ID": 00000000000,
                        "ROOM_DESCR": "",
                        "METER_NO": "0000000",
                        "METCAT_LABEL": "Fumonic",
                        "METTYPE_CODE": None,
                        "Deactivation_date": "3000-01-01T00:00:00",
                        "Activation_date": "2020-02-25T00:00:00"
                    }
                ]
            }
        },
    )

    requests_mock.get(
        f"{GRAPHS_API_BASE_URL_DK}MeterType/GetMeterTypes",
        json={
            "electricity": {
                "unit": "kWh",
                "useEcoData": True,
                "interval": {
                    "hour": False,
                    "day": True,
                    "week": True,
                    "month": True,
                    "year": True
                },
                "compare": {
                    "comparePeriode": True,
                    "property": True,
                    "installation": False,
                    "national": False,
                    "outsideTemperature": False,
                    "aconto": False
                }
            },
            "heat": {
                "unit": "Delinger",
                "useEcoData": True,
                "interval": {
                    "hour": False,
                    "day": True,
                    "week": True,
                    "month": True,
                    "year": True
                },
                "compare": {
                    "comparePeriode": True,
                    "property": True,
                    "installation": False,
                    "national": False,
                    "outsideTemperature": False,
                    "aconto": False
                }
            },
            "waterCold": None,
            "waterHot": None,
            "energy": None,
            "co2": None,
            "humidity": None,
            "noise": None,
            "temperature": None,
            "temperatureOut": None,
            "humonic": None
        },
    )
    
    return requests_mock
