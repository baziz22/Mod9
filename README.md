# CS3030 Python Modle 9 Assignment 3 Homework 7
# Group Assignment:
	Group2 member's
		Bader Binsunbil
		Grace Borges
		Juan Santos

# DISCRIPTION:

	Module 1 Task 1 ===> minivan.py
	This module is going to check if doors are open or not.

	Module 1 Task 2 ===> minivantest.py
	This module is going to test minivan.py using csv file data.

	Module 2 Task 1 ===> barcode.py
	This module is going to get digits as a zipcode and it will convert it to barcode.

	Module 2 Task 2 ===> barcodetest.py
	This module is going to get digits as a zipcode from a text file and it will convert it to barcode.


# FUNCTIONS:
---------------------------------------------------------------------------------------------------------------------
	On minivan.py

	doors_lockers()

		This function will check if the doors of the minivan is open or not using the following data:

		ld => left dashboard switch
		rd => right dashboard switch
		cl => child lock switch
		ml => master lock switch
		li => left inside handle
		lo => left outside handle
		ri => right inside handle
		ro => right outside handle

    main()
		It will assign "R1" value to switch list in the first index which is index[0].
		It will take user input and assign it to the switch list.
		It will call doors_lockers()
---------------------------------------------------------------------------------------------------------------------
	On minivantest.py

	testMinivan()

	    This function will test the minivan doors which they are open or not using getFile variable.
	    It will open the file from the web.
	    It will call doors_lockers function from minivan.py
	    Then, It will read the record and print it out.

	main()
		Run the app and invoke testMinivan function
---------------------------------------------------------------------------------------------------------------------
    on barcode.py

    printBarCode(zipCode):

        This function will convert the zip code to bar code format.
        1. Incodes zipcode to bar format
        2. Validates user input if it is match the format of US zip code.
        3. Parses the numbers.
        4. Calculates the check digit for the barcode
        5. Invoke printDigit function to print out the zip code numbers and check digit as  bar code format.
        Args:
            zipCode: string of zipcode to be validated and parsed.
        Returns:
            0 if zip code is valid.
            1 if zip code is not valid.

    printDigit(d):

        This function will converts digits into barcode format and returns the result.
        Args:
            d: zip code passed in from printBarCode function to be reformatted
        Returns:
            barcode: The string representing the barcode of the digit.

    main():

        Run the python app.
        1. Prompt the user to enter a zipcode.
        2. Invoke printBarCode function.
        3. Pass the user input to the printBarCode function.
---------------------------------------------------------------------------------------------------------------------
    on barcodetest.py

    testBarcode():

        This function will:
        1. get a URL text file and assign it to getTextFile veriable.
        2. Open the URL text file.
        3. Decode the text file and assigne the decode to textLine veriable.
        4. Add all lines to record list.
        5. Print out the barcode.
        Args:
            No arguments are needed.
        Retrun:
            No return is needed.

    main():

        Run the app and invoke testBarcode function.
