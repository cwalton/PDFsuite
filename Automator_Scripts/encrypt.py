#! /usr/bin/python
# coding: utf-8

# ENCRYPT : Encrypt PDF and lock with password.
# by Ben Byram-Wigfield v.1.1
# User Password = "" allows the file to open freely
# but copying or extracting requires the Owner Password.
# WARNING: Some versions of OS X corrupt PDF metadata after encryption.

import os, sys
from Quartz import PDFDocument, kCGPDFContextAllowsCopying, kCGPDFContextAllowsPrinting, kCGPDFContextUserPassword, kCGPDFContextOwnerPassword
from CoreFoundation import (NSURL)

password = "12345678"

def main():
	inputfile = ""
	outputfile = ""
	for filename in sys.argv[1:]:	
		inputfile =filename.decode('utf-8')
		if not inputfile:
			print 'Unable to open input file'
			sys.exit(2)
		shortName = os.path.splitext(filename)[0]
		outputfile = shortName+" locked.pdf"
		pdfURL = NSURL.fileURLWithPath_(inputfile)
		pdfDoc = PDFDocument.alloc().initWithURL_(pdfURL)
		if pdfDoc :
			options = { 
				kCGPDFContextAllowsCopying: False, 
				kCGPDFContextAllowsPrinting: False, 
				kCGPDFContextOwnerPassword: password,
				kCGPDFContextUserPassword: ""}
			pdfDoc.writeToFile_withOptions_(outputfile, options)

if __name__ == "__main__":
   main()
