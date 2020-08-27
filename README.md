# Overlay PDF

This [Drawbot](https://www.drawbot.com) script will take two PDFs and overlay them to help highlight differences. 

Each PDF is converted to a specified color, and then layered with a multiply effect. The result is saved to a new PDF file. 

![Example](readmeImg/example-image-for-readme.png)


### Notes
- Multiple page PDFs are supported.
- The source PDFs are rasterized, so you should adjust the `pdfScale` variable as needed, to balance quality with speed and file size.
- My use case is in showing differences in versions of typeface proofs, but it will accept and B&W PDF.
- It hasn’t been extensively tested, outside of my specific use case.


