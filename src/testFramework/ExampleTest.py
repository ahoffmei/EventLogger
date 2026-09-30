"""
Example Test: 
Requirement Text: The software shall only record values of RECORDED_MEASUREMENTS
                  that are GTE 1.0 volts. 
"""

from runTests import g_Test_Sumbission_Module
from TestBase import TestBase, TestResult
from pathlib import Path
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

class ExampleTest(TestBase): 
    def __init__(self):
        # Define variables relevant to the test at hand that will be used in both runTest() and generatePlot()
        self.data = None
        self.values = [] 
        self.timestamps = []

        super().__init__("ExampleTest")


    def runTest(self, data : pd.DataFrame) -> TestResult:
        self.data = data.copy()

        # TODO: This specific parse would be so common make a function to do it
        measurements_df = data[
            (data["DATA_CATEGORY"] == "INFO") 
                and 
            (data["SUBCATEGORY"] == "RECORDED_MEASUREMENT") 
        ]

        self.values = measurements_df["VALUES"].tolist()

        # TODO: Interface to convert timestamps to a double or something
        self.timestamps = measurements_df["TIMESTAMP"].tolist() 

        if ( len(self.values) == 0 ):
            self.reasoning = "No values recorded. Implies test pre-condition was never met."
            self.result = TestResult.NO_TEST

        elif ( all(self.values) >= 1.0 ):
            self.reasoning = "All recorded values were GTE 1.0"
            self.result = TestResult.PASS

        else:
            self.reasoning = "All recorded values were not GTE 1.0"
            self.result = TestResult.FAIL

            for i, value in enumerate(self.values):
                if value < 1.0:
                    self.log += f"Value at timestamp {self.timestamps[i]}"


    def generatePlot(self, save_path = Path("DNE")) -> None:
        plt.plot(self.values, self.timestamps)
        plt.xlabel("Values (V)")
        plt.ylabel("Timestamps (s)")
        plt.title(self.req_name)
        plt.grid(True)

        if save_path.exists():
            plt.savefig(save_path)
        else:
            plt.show()




# Do this or your test won't be captured :D 
g_Test_Sumbission_Module.addTest(ExampleTest())    