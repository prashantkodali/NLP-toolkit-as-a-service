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
