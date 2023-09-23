from pydantic import BaseModel
class TrainInfo(BaseModel):
    trainName: str
    trainNumber: str
    departureTime: dict
    seatsAvailable: dict
    price: dict
    delayedBy: int