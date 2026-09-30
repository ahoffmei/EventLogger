import pathlib
import argparse
import pandas as pd 


class TestSubmission:
    def __init__(self):
        self.testModules = []


    def addTest(self, test_module):
        self.testModules.append(test_module)


g_Test_Sumbission_Module = TestSubmission()


class TestRunner:
    def __init__(self):
        self.results_dict = {}


    def runAllTests(self, data_path : pathlib.Path) -> None:
        df = pd.read_csv(data_path)
        
        for test in g_Test_Sumbission_Module:
            result = test.runTest(df)
            name   = test.getName()
            self.results_dict[name] = result
            test.generatePlot()


    def genResultRollup(self, output_path : pathlib.Path) -> None:
        df = pd.DataFrame([self.results_dict])
        df.to_csv(output_path, index = False)


def SetupArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--report-path-xlsx", type=pathlib.Path, dest="report_path", required=True)
    parser.add_argument("-d", "--data-path", type=pathlib.Path, dest="data_path", required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args        = SetupArgs
    test_runner = TestRunner() 

    test_runner.runAllTests(args.data_path)
    test_runner.genResultRollup(args.report_path)
