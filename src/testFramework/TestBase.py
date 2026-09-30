from abc import ABC, abstractmethod
from enum import Enum
import pandas as pd 

class TestResult(Enum):
    NOT_TESTED = -1
    FAIL    = 0
    PASS    = 1
    NO_TEST = 2


class TestBase(ABC):
    def __init__(self, req_name : str):
        self.req_name   = req_name 
        self.result     = TestResult.NOT_TESTED

        # Reasoning for resulting test result 
        self.reasoning  = ""

        # For additional logging when additional detail is applicable 
        self.log        = ""


    @abstractmethod
    def runTest(self, data : pd.DataFrame) -> TestResult:
        pass 


    @abstractmethod
    def generatePlot(self) -> None:
        pass


    def getResult(self) -> TestResult:
        return self.result


    def getName(self) -> str:
        return self.req_name


    def getResultStr(self, result : TestResult) -> str: 
        s = "RESULT_STR_NOT_FOUND"

        if result == TestResult.NOT_TESTED:   
            s = "NOT_TESTED"
        elif result == TestResult.FAIL:         
            s = "FAIL"
        elif result == TestResult.PASS:         
            s = "PASS"
        elif result == TestResult.NO_TEST:      
            s = "NO_TEST"

        return s 
    
    
    def __str__(self):
        return f"{self.req_name} [{self.result}] : {self.reasoning}"

