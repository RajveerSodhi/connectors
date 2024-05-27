from sqlalchemy import Column, DateTime, String, Boolean, ForeignKey, JSON, BigInteger
from sqlalchemy.orm import relationship
from .database import base

class DataConnection(base):
    __tablename__ = "dataconnections"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True, nullable=True)
    channel = Column(String, index=True)
    is_verified = Column(Boolean, default=False)
    token = Column(String, nullable=True)
    userId = Column(String, index=True)

class DataStream(base):
    __tablename__ = "datastreams"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String, index=True)
    data = Column(JSON)
    md5 = Column(String, index=True)
    connection = relationship("DataConnection", back_populates="data_streams")
    latestFetchedFile = Column(String, index=True, nullable=True)

class FetchRequests(base):
    __tablename__ = "fetchrequests"
    id = Column(BigInteger, primary_key=True, index=True)
    fetchId = Column(String, index=True)
    startTime = Column(DateTime)
    status = Column(String, index=True)
    datastream = relationship("DataStream", back_populates="fetch_requests")
