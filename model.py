'''
@author: PythonDeveloper29042
@project: AutoShutdown 
@file: controller.py
@file-description: This file is the controller of the application. It is responsible for the communication between the model and the view.'
'''

from os import system


def send_shutdown():
    '''
    This function is responsible for sending the shutdown signal to the model.
    '''
    system('shutdown /s /f /t 0')  # Send the shutdown signal to the model
    # print('The system will shut down')  # Print the message for debugging purposes


def send_cancel_shutdown():
    pass