# Text-extraction-from-image-pytesseract
# Optical character recognition, or for short OCR

What **OCR** does? It extracts the text from Image or PDF. In many cases we need to do some actions with texts in images, and OCR able us in these situations. For example, in Automated driving the car need to know how the Traffic signs means.

What did I do in this code? I had some word documents, I took a screenshot from a specific page (to input to code) and made a copy from the same page and paste it to .txt file (to compare with output).
I did some preprocessing on screenshot, like resize and threshold, then using pytesseract ectract the text.

The two last sections are accuracy measurement.
