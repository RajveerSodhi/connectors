from pydantic import BaseModel
from typing import Optional, Literal, Union

allChannels = Literal[
    "gAds",
    "dv360",
    "gSheets",
    "gAnalytics",
    "appAnalytics",
    "ytAnalytics",
    "fbAds",
    "mAds",
    "tAds",
    "aAds",
    "lAds",
    "snapAds",
    "pinAds",
    "ttAds",
    "gTrends",
    "sib",
    "fInsights",
    "instaInsights",
    "moengage",
    "callRail",
    "sprinklr",
    "Direct Upload",
]

# Model for dataconnection
class DataConnectionIn(BaseModel):
    id: int
    name: str
    email: str
    userId: str
    channel: allChannels

# DataStream data types for all channels
class gAds(BaseModel):
    mcc: str
    client: str

class gSheets(BaseModel):
    sheetId: str
    pageTitle: str

class gTrends(BaseModel):
    kw1: str
    kw2: str
    kw3: str

class gAnalytics(BaseModel):
    accId: str
    propId: str
    viewId: str

class ytAnalytics(BaseModel):
    accId: str
    propId: str
    viewId: str

class appAnalytics(BaseModel):
    propId: str

class dv360(BaseModel):
    partnerId: str
    advertiserId: str

class fbAds(BaseModel):
    accId: str

class mAds(BaseModel):
    customerId: str
    parentCustomerId: str

class aAds(BaseModel):
    profileId: str

class sib(BaseModel):
    campaignId: str

class fInsights(BaseModel):
    pageId: str
    pageAccessToken: str

class instaInsights(BaseModel):
    instaId: str

class lAds(BaseModel):
    accountId: str

class snapAds(BaseModel):
    accountId: str

class pinAds(BaseModel):
    accountId: str

class ttAds(BaseModel):
    accountId: str

class tAds(BaseModel):
    profileId: str

# Model for DataStream
class DataStreamIn(BaseModel):
    id: int
    name: str
    data: Union[
        gAds,
        gSheets,
        gAnalytics,
        appAnalytics,
        ytAnalytics,
        fbAds,
        dv360,
        mAds,
        aAds,
        gTrends,
        lAds,
        snapAds,
        pinAds,
        ttAds,
        tAds,
        sib,
        fInsights,
        instaInsights,
    ]
    connectionId: int

class adDetailsQuery(BaseModel):
    dataStreamId: str
    startDate: Optional[str]
    endDate: Optional[str]
    schedule: Literal["hourly", "daily"]