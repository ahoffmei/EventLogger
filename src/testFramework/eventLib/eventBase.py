from abc import ABC, abstractmethod
from enum import Enum

# Lol sure 
R_MSG = True 
T_MSG = False

# I almost want these initialized and defined in like a json that is shared with the embedded but maybe this is ok
class EventType(Enum):
    TBD_EVENT       = "TBD_EVENT"
    MSG_1553_EVENT  = "MSG_1553_EVENT"
    DISCRETE_EVENT  = "DISCRETE_EVENT"
    POWER_EVENT     = "POWER_EVENT"

EVENT_TYPES_SET  = {event.value for event in EventType}
EVENT_TYPES_LIST = [event.value for event in EventType]


class DiscreteTypes(Enum):
    EGSE_BLS_ABORT  = "EGSE_BLS_ABORT"
    EGSE_BLS_LAUNCH = "EGSE_BLS_LAUNCH"
    BLS_EGSE_LAUNCH = "BLS_EGSE_LAUNCH"
    BLS_EGSE_ABORT  = "BLS_EGSE_ABORT"


class PowerEventTypes(Enum):
    ...


BASE_COLUMNS = ["EventName", "Timestamp"] 

class EventBase(ABC):
    def __init__(
            self,
            event_name          : EventType, 
            raw_timestamp       : str, 
            relative_timestamp  : float
        ) -> None:

        self.event_name     = event_name
        self.raw_timestamp  = raw_timestamp
        self.timestamp      = relative_timestamp # may need to be computed separately idk 


    @staticmethod
    @abstractmethod
    def getColumnSpecs(self) -> list:
        pass


    @abstractmethod
    def generateDataframeColumn(self):
        pass 
    

# ****************************************************************************************
# Other event types here for now 
# ****************************************************************************************

class Msg1553EventBase(EventBase):
    def __init__(
            self, 
            isRorT              : bool, # true for R msg, false for T msg 
            word                : int,
            bits                : list,
            rtMsgName           : str,
            raw_timestamp       : str,
            relative_timestamp  : float
        ) -> None:

        self.isRorT  = isRorT
        self.word    = word 
        self.bits    = bits 
        self.msgName = rtMsgName

        super().__init__(EventType.MSG_1553_EVENT, raw_timestamp, relative_timestamp)
    

    @staticmethod
    def getColumnSpecs(self) -> list:
        return BASE_COLUMNS + []


    def generateDataframeColumn(self):
        pass 



class R_MsgEvent(Msg1553EventBase):
    def __init__(
            self, 
            word                : int, 
            bits                : list, 
            rtMsgName           : str, 
            raw_timestamp       : str, 
            relative_timestamp  : float
        ) -> None:

        super().__init__(R_MSG, word, bits, rtMsgName, raw_timestamp, relative_timestamp)


class T_MsgEvent(Msg1553EventBase):
    def __init__(
            self, 
            word                : int, 
            bits                : list, 
            rtMsgName           : str, 
            raw_timestamp       : str, 
            relative_timestamp  : float
        ) -> None:

        super().__init__(T_MSG, word, bits, rtMsgName, raw_timestamp, relative_timestamp)


class DiscreteEvent(EventBase):
    def __init__(
            self, 
            discrete_type       : DiscreteTypes,
            is_high             : bool,  # maybe unnecessary: TODO Check requirements -- maybe submitting an event assumes we are high inherently
            voltage_reading     : float, # maybe rename 
            raw_timestamp       : str, 
            relative_timestamp  : float
        ) -> None:
        
        self.discrete_type      = discrete_type
        self.is_high            = is_high
        self,voltage_reading    = voltage_reading

        super().__init__(EventType.DISCRETE_EVENT, raw_timestamp, relative_timestamp)


    @staticmethod
    def getColumnSpecs(self) -> list:
        return BASE_COLUMNS + ["Discrete_Type"] # TODO 


class PowerEvent(EventBase):
    def __init__(
            self, 
            event_type          : PowerEventTypes, 
            raw_timestamp       : str, 
            relative_timestamp  : float
        ) -> None:

        self.event_type = event_type

        super().__init__(EventType.POWER_EVENT, raw_timestamp, relative_timestamp)


    @staticmethod
    def getColumnSpecs(self) -> list:
        return BASE_COLUMNS + []
