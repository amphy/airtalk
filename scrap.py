import numpy as np
import csv

if __name__ == "__main__":
	inFile = open("./data/Sample Flight Data.csv", "r")
	inFile.readline()
	maxVal = [0] * 
	for line in inFile.readlines():
		lineData = [len(v) for v in line.strip().split(",")]
		print lineData
