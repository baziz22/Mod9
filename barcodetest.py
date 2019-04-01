#!/usr/bin/env python3
"""
    Module 2 Task 2
    barcodetest.py
    This app will test barcode.py file.
"""
from __future__ import print_function
from urllib.request import urlopen
from barcode import printBarCode

def testBarcode():
    """
        This function will:
        1. get a URL text file and assign it to getTextFile veriable.
        2. Open the URL text file.
        3. Decode the text file and assigne the decode to textLine veriable.
        4. Add all lines to record list.
        5. Print out the barcode.
        Args:
            No arguments needed.
        Retrun:
            No return needed.
    """
    # Get text file from a URL
    getTextFile = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/barCodeData.txt"
    #  open the text file
    with urlopen(getTextFile) as text:
        # Declare and Store the output in a record list.
        record = []
        # Loop over each line in the text file
        for line in text:
            # Decode the line.
            textLine = line.decode('utf-8').strip()
            # Add new decoded line to the record list.
            record.append(textLine)
        # Loop over each element in the record list.
        for el in record:
            # Print out the bar code
            print("Enter a zipcode: " + el)
            printBarCode(el)
            print()
def main():
    """
        Run the app and invoke testBarcode function
    """
    testBarcode()


if __name__ == "__main__":
    main()
    exit(0)
