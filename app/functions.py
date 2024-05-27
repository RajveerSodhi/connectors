from typing import Optional, Literal
from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import DataConnection, DataStream, FetchRequests

def get_verified_dataStream(db: Session, data_stream_id: int):
    data_stream = db.query(DataStream).filter(DataStream.id == data_stream_id).first()
    if not (data_stream.connection.is_verified and data_stream.connection.token):
        raise HTTPException(status_code = 404, detail = "Connection is not verified, please login again")
    return data_stream

def get_verified_connection(db: Session, connection_id: int):
    connection = db.query(DataConnection).filder(DataConnection.id == connection_id).first()
    if not (connection.is_verified or connection.token):
        raise HTTPException(status_code = 404, detail = "Connection is not verified, please login again")
    return connection

def set_fetch_request(db: Session, data_stream: DataStream, status: Literal["running", "finished", "failed"], fetch_id: Optional[str] = None):
    if fetch_id:
        fetch_request = db.query(FetchRequests).filter(FetchRequests.fetchId == fetch_id).first()
        fetch_request.status = status
        fetch_request.datastream = data_stream
        fetch_request.startTime = datetime.now()
    else:
        fetch_request = FetchRequests(datastream = data_stream, startTime = datetime.now(), status = status)
        db.add(fetch_request)
    db.commit()
    return fetch_request