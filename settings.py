
import os
from os.path import expanduser

from donkey import cameras
from donkey import recorders
from donkey import predictors
from donkey import vehicles
from donkey import controllers


DRIVE_LOOP_DELAY = .2 #seconds between vehicle updates

DATA_DIR = expanduser('~/donkey_data/')
RECORDS_DIR = os.path.join(DATA_DIR, 'records')
MODELS_DIR = os.path.join(DATA_DIR, 'models')


''' 
Camera - Takes pictures.
'''
try:
    import picamera
    camera = cameras.PiVideoStream #Raspberry Pi Camera
except ImportError:
    print("Cound not load PiCamera. Using FakeCamera for testing.")
    FAKE_CAMERA_IMG_DIR = os.path.dirname(os.path.realpath(__file__))+'/img/'
    camera = cameras.FakeCamera #For testing


'''
Vehicle
Updates the vehicle's steering angle and throttle.
'''
vehicle = vehicles.BaseVehicle


'''
Recorder
Save images and vehicle variables to a filesytem or webserver
'''
recorder = recorders.FileRecorder


'''
Predictor
Accepts image arrays and returns steering angle and throttle.
'''
#predictor = predictors.RandomPredictor
predictor = predictors.ConvolutionPredictor


'''
Controller
Get the users input to control vehicle. 
'''

controller = controllers.BaseController


