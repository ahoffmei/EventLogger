import pandas as pd 

from abc import ABC 
from eventBase import * # I'm lazy 


class EventDatasetBase(ABC): 
    def __init__(self, col_names) -> None:
        self.dataset  = pd.DataFrame(columns=col_names)
    
    
    def addRow(self, event_obj : EventBase): 
        self.dataset = pd.concat(
            [
                self.dataset,
                event_obj.generateDataframeColumn()
            ], 
            ignore_index = True
        ) 

    
class Msg1553_Dataset(EventDatasetBase):
    def __init__(self) -> None:
        super().__init__( Msg1553EventBase.getColumnSpecs() )


class DiscreteDataset(EventDatasetBase):
    def __init__(self) -> None:
        super().__init__( DiscreteEvent.getColumnSpecs() ) 



