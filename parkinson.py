"""
@author: Mbaka JohnPaul
"""

from pydantic import BaseModel

class Parkinson(BaseModel):
    MDVPFo: float
    MDVPFhi: float
    MDVPFlo: float
    MDVPJitter: float
    MDVPJitterAbs: float
    MDVPRAP: float
    MDVPPPQ: float
    JitterDDP:  float
    MDVPShimmer:  float
    MDVPShimmerdB:  float
    ShimmerAPQ3:  float
    ShimmerAPQ5:  float
    MDVPAPQ:  float
    ShimmerDDA:  float
    NHR:  float
    HNR:  float
    RPDE:  float
    DFA:  float
    spread1:  float
    spread2:  float
    D2:  float
    PPE:  float