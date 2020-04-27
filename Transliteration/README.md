<p align="center">
  <b>Transliteration</b><br>
</p>

In this service we have deployed a ISO 15919 standard for converting Devnagri script to Roman characters. Transliteration is of crucial importance when we are dealing with multilingual setup or code mix setup. 

The service takes following inputs, in a JSON format:
- Input text, in devnagri script, for which transliteration is to be generated.

The service outputs the following:
- Transliteration of the input text as mentioned in the inputText

Following is the brief summary of the method used for generating the summary:

1. A map is written to map devnagri charaters to roman characters.
2. Check the script information of the string based on unicode character ranges.
3. Based on the input character it is mapped to roman characters. 
4. These characters are stitched together and the output is generated. 

No additional packages or libraries were used to generate the transliteration. This can be extended to all the other scripts. 

Error handling is built into the system. 

Two error cases are handled:
a) If the input is not in native script. 
b) if the input is empty. 
In both these cases we generate a json with error key as "error". If there is no error, then the value of "error" key in returned json will be "None".

<p><b><u>Components</u></b><br></p>
Code base of this service consists of three files:
1. main.py: here flask component of the service is kept, which orchestrates the whole trnsliteration process by calling the following pieces of code. 
2. charmap.py: consits of the dictionary which maps the native script character to the roman script equivalent. This can be edited if there is any change or addition to the script. 
3. errorCheck.py: implements the class for error checking. Currently two error handling cases, as described above, are added. Additional error test cases can be added to this class. There is a method in this class, called CheckInput() which orchestrates each error case check. Writing a seperate class ensures that we can add more test cases without much change to code base. 
4. isotrans.py: A class implemnted which does the actual transliteraton. Consits of two mehtods: one for script detection based on unicode ranges, and another method for doing the character mapping using dictionary in charmap.py.
