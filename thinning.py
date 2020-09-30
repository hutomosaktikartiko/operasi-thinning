import cv2

show_images = 1

def fastThin(img_ori):
  img = img_ori.copy()

  img = morphology(img)

  return img

def morphology(img):
  
  # Menentukan nilai treshhold
  a, img = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV) 
  
  # Mengubah bentuk dan ukuran kernel
  kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

  # iteration 
  iteration = 0
  print ("Starting fast thin...")
  while 1:
    iteration += 1
    print ("Running iteration",iteration,"of morphology")
    
    #erosion
    last_img = img.copy()
    ero = cv2.erode(img,kernel,iterations = 1)
    
    #dilation
    dil = cv2.dilate(ero,kernel,iterations = 1)
    
    # result
    img -= dil
    img += ero
    
    # Mengakhiri loop jika hasilnya sama dari iterasi terakhir
    if cv2.compare(img, last_img, cv2.CMP_EQ).all():
      break

  a, img = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV) 
  return img
