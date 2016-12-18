## From the original creator:

### Background

I recently had occasion to print a bunch of envelopes with different
addresses.

I found that the standard word-processing software included with
Windows or Mac OS didn't support automating that, while the more
complex freely-available software (Abiword, LibreOffice) had
maddeningly complicated and buggy implementations of mail merge.

I eventually, after 10 misprints and 3 do-overs, coaxed LibreOffice
into generating a PDF that I then printed with another program (the
combination of LibreOffice's conception of print settings and the
actual print settings caused many hilariously wrong misprints when
attempting to print from LibreOffice directly).  I proudly showed
these to my wife, who then pointed out that in my last reprent I
somehow managed to swap the last two lines of every address.

And so, tasked with going through that ordeal again, it suddenly hit
me: it's not hard to generate a PDF with some text.

### The Code

The code is shorter than this README, but briefly:

1. Create a CSV with the data you want, like one address per row with
   one line per column.  (We used Google Docs, which can export CSV.)
2. Modify the constants in the `__main__` block of the code.
3. Run it, print the PDF using whatever PDF program you like.

## Modifications and Additions

Adapted to include modofications to allow passing in of from address also from a csv file. Argument checks for input and such. Pushed additions into a new script to try and preserve the original script to reference back to.

### Scripts and useage

`envelope.py`

The original script from the creator, keeping this here for reference

This script is simply run, and pulls addresses from the local fiel address.csv. The from address is set in the code. Remember the script will ignore the first line in the address.csv file as it assumes a header row. It also has a useful little feature to put a "yes" into the last column to select wether to print or not

`christmas-envelope.py`

Modified from the above script, takes two arguments of csv files for "to" addresses and "from" addresses. It also changes the size of the font anf font type to allow to different size "from" and "to" address. Generally speaking I export the addresses from google sheets into the <file name>.csv then I'll copy to `address.csv` where I can edit / alter and fine tune anything.

Note: if you have a blank field then this will show up as an empty line, so for the moment the quick hack is to edit the csv file to remove the double commas and replace for a single one eg `s/,,/,/`
