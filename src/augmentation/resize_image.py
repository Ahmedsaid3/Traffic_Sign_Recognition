import cv2
image = cv2.imread("/Users/ahmedsaidgulsen/Desktop/kimlik.jpg")
result = image.shape
# print(result)
resized_image = cv2.resize(image, (1000, 1000))
cv2.imwrite('/Users/ahmedsaidgulsen/Desktop/kimlik_yeni.jpeg', resized_image)
new_result = resized_image.shape
print(new_result)