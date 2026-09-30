import argparse
import pathlib
import csv 
import pandas as pd 

class GenReport:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []


    def parse(self):
        lines = [] 
        with open(self.file_path, 'r') as f:
            lines = f.readlines() 

        for line in lines:
            timestamp, logtype, event, val = line.strip().split(" ") 
            self.data.append([timestamp, logtype, event, float(val)])


    def createHtmlReport(self): 
        print("HTML Report not implemented yet")


    def createExcelReport(self):
        with open("logs.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.data)



def SetupArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", type=pathlib.Path, dest="file_path", required=True)
    parser.add_argument("--excel", action="store_true", dest="make_excel")
    parser.add_argument("--html", action="store_true", dest="make_html")

    return parser.parse_args()


if __name__ == "__main__":
    args = SetupArgs()
    report = GenReport(args.file_path)
    report.parse()

    print(report.data)

    if args.make_excel: report.createExcelReport()
    if args.make_html:  report.createHtmlReport()