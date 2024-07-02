from PIL import ImageGrab, Image, ImageEnhance, ImageFilter
import cv2
import pytesseract

screenshot = ImageGrab.grab()
screenshot.save("0.jpg")

im = Image.open(r"0.jpg")
width, height = im.size
left = 540
top = 940
right = -1288
bottom =- 96
im1 = im.crop((left, top, right+width, bottom+height))
im1.save('0.jpg')


pytesseract.pytesseract.tesseract_cmd = (".\\Tesseract-OCR\\tesseract.exe")

# Grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread('0.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (3,3), 0)

thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

invert = 255 - thresh

cv2.imshow('thresh', thresh)
cv2.imshow('open', opening)
cv2.imshow('invert', invert)
cv2.waitKey()

# Perform text extraction
# data = pytesseract.image_to_string(thresh, lang='eng', config=r'--oem 3 --psm 11 -c tessedit_char_whitelist=0123456789')
data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')

print(data)

file = open("recognized.txt", "a")
# Appending the text into file
file.write(data)
file.write("\n")

# Close the file
file.close()