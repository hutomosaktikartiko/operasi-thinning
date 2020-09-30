import cv2
import thinning as tn

# Binary dan grayscale image
img = cv2.imread('image/pohon[1].jpg',0)

# Melakukan operasi thihning
thinned_image = tn.fastThin(img)

# Menampilkan gambar asli
cv2.imshow('original image',img)

# Menampilkan gambar hasil thinned
cv2.imshow('thinned image',thinned_image)

# Mennyimpan Image
cv2.imwrite('save_image/save_image.png',thinned_image)

# Menunda Windows terdestroy
cv2.waitKey(0)

# Mendestroy windows
cv2.destroyAllWindows()