from pydantic import BaseModel
from datetime import datetime, time


class ohlcv(BaseModel):
    type:str
    close: float
    date: datetime
    high: float
    low: float
    oi: str
    open: float
    symbol: str
    time: time
    volume: float
