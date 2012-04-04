import opencv
# Magic convenience class from OpenCV with a method for grabbing images
from opencv import highgui

# This is how you get access to the first webcam your system finds.
camera = highgui.cvCreateCameraCapture(-1)

# This function grabs a frame from the webcam, runs 'detect' on the OpenCV image, and
# converts the result to a PIL based image, suitable for reuse/blitting/storing
def get_image():
    im = highgui.cvQueryFrame(camera)
    detect(im)
    #convert Ipl image to PIL image
    return opencv.adaptors.Ipl2PIL(im)

# The detection routine:
def detect(image):
    # Find out how large the file is, as the underlying C-based code
    # needs to allocate memory in the following steps
    image_size = opencv.cvGetSize(image)

    # create grayscale version - this is also the point where the allegation about
    # facial recognition being racist might be most true. A caucasian face would have more
    # definition on a webcam image than an African face when greyscaled.
    # I would suggest that adding in a routine to overlay edge-detection enhancements may
    # help, but you would also need to do this to the training images as well.
    grayscale = opencv.cvCreateImage(image_size, 8, 1)
    opencv.cvCvtColor(image, grayscale, opencv.CV_BGR2GRAY)

    # create storage (It is C-based so you need to do this sort of thing)
    storage = opencv.cvCreateMemStorage(0)
    opencv.cvClearMemStorage(storage)

    # equalize histogram
    opencv.cvEqualizeHist(grayscale, grayscale)

    # detect objects - Haar cascade step
    # In this case, the code uses a frontal_face cascade - trained to spot faces that look directly
    # at the camera. In reality, I found that no bearded or hairy person must have been in the training
    # set of images, as the detection routine turned out to be beardist as well as a little racist!
    cascade = opencv.cvLoadHaarClassifierCascade('haarcascade_frontalface_alt.xml', opencv.cvSize(1,1))

    faces = opencv.cvHaarDetectObjects(grayscale, cascade, storage, 1.2, 2, opencv.CV_HAAR_DO_CANNY_PRUNING, opencv.cvSize(50, 50))

    if faces:
        for face in faces:
            # Hmm should I do a min-size check?
            # Draw a Chartreuse rectangle around the face - Chartruese rocks 
            opencv.cvRectangle(image, opencv.cvPoint( int(face.x), int(face.y)),
                         opencv.cvPoint(int(face.x + face.width), int(face.y + face.height)),
                         opencv.CV_RGB(127, 255, 0), 2) # RGB #7FFF00 width=2

#[PyGame stuff - snip -]

#demo image preparation aka how to load any image and run the detection routine on it
cv_im = highgui.cvLoadImage("demo.jpg")
detect(cv_im)
pil_im = opencv.adaptors.Ipl2PIL(cv_im)

def read_demo_image():
    return pil_im

while True:
    # Fixed demo for when you have no Webcam
    #im = read_demo_image()

    # UNCOMMENT this and comment out the demo when you wish to use webcam
    im = get_image()

    pil_img = pygame.image.frombuffer(im.tostring(), im.size, im.mode)
    screen.blit(pil_img, (0,0))
    pygame.display.flip()
    pygame.time.delay(int(1000.0/fps))
