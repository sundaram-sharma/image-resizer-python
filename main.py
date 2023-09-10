import cv2

#Configurable Parameters
inputValue = int(input("Enter the scale value to resize the image: (0 - 100): "))
if inputValue >= 0 and inputValue <= 100:

    source = "wx.jpg"
    destination = 'newImage.png'
    scale_percent = inputValue

    src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
    #cv2.imshow("title", src)

    #Percentage by which the image is resize

    #Calculate the 50 percent of original dimensions
    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    dsize = (new_width, new_height)

    output = cv2.resize(src, dsize)

    cv2.imwrite(destination, output)
    #cv2.waitKey(0)
else:
    print("Enter correct values")
