'''
@author: PythonDeveloper29042
@project: AutoShutdown 
@file: controller.py
@file-description: This file is the controller of the application. It is responsible for the communication between the model and the view.
'''

from datetime import datetime, timedelta
from tkinter import messagebox
from threading import Thread
from time import sleep
import model

count_secs = None  # Variable to store the number of seconds
running = False  # Variable to store the running state of the countdown


def shutdown_model(time: datetime, **countdown_data):
    '''
    This function is responsible for shutting down the system at the specified model time.
    Args:
        time (datetime): The time at which the system should be shut down.
        **countdown_data: The data required for the countdown.
    '''
    global running, count_secs  # Get the global variable running and count_secs
    # Check if the time is empty or not
    if time.strip() == '':
        messagebox.showerror('错误', '你个傻逼，选择的时间不能为空！')  # Show error message if time is empty
        return
    current_time = datetime.now()  # Get the current time
    if '秒' in time:  # Check if the time contains '秒' ('seconds')
        future_time = timedelta(seconds=int(time[:-1]))  # Get the future time in seconds
    if '分钟' in time:  # Check if the time contains '分钟' ('minutes')
        future_time = timedelta(minutes=int(time[:-2]))  # Get the future time in minutes
    if '小时' in time:  # Check if the time contains '小时' ('hours')
        future_time = timedelta(hours=int(time[:-2]))  # Get the future time in hours
    current_time += future_time  # Add the future time to the current time        
    running = True  # Set the running state to True
    count_secs = future_time.total_seconds()  # Get the total number of seconds

    #
    year = current_time.year
    month = current_time.month
    day = current_time.day
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    countdown_data['end_time'].set(f'系统将于{year}年{month}月{day}日{hour}:{minute}:{second}关机')
    th = Thread(target=countdown, args=(countdown_data,))  # Create a new thread for the countdown function
    th.start()  # Start the thread


def shutdown_custom(time: datetime, **countdown_data):
    '''
    This function is responsible for shutting down the system at the specified custom time.
    Args:
        time (datetime): The time at which the system should be shut down.
        **countdown_data: The data required for the countdown.
    '''
    print(time, countdown_data)
    current_time = datetime.now()  # Get the current time
    if time <= current_time:  # Check if the selected time is in the past
        messagebox.showerror('错误', '选择的时间已经过去了！你他妈只能选择未来的时间！')  # Show error message if the selected time is in the past
        return
    total_secs = (time - current_time).total_seconds()  # Calculate the total number of seconds
    


def cancel_shutdown():
    '''
    This function is responsible for cancelling the scheduled shutdown.
    '''
    pass


def change_time():
    '''
    This function is responsible for changing the time at which the system should be shut down.
    '''
    pass


def countdown(countdown_data):
    '''
    This function is responsible for the countdown to the shutdown of the system.
    '''
    global count_secs  # Get the global variable count_secs
    while running:
        if count_secs <= 0:  # Check if the countdown has reached 0
            model.send_shutdown()  # Send the shutdown signal to the model
            break
        count_secs -= 1  # Decrement the number of seconds
        temp = count_secs  # Store the number of seconds in a temporary variable
        hour = int(temp // 3600)  # Calculate the number of hours
        temp %= 3600  # Get the remaining seconds
        minute = int(temp // 60)  # Calculate the number of minutes
        minute %= 60  # Get the remaining minutes
        seconds = int(temp)  # Calculate the number of seconds
        seconds %= 60  # Get the remaining seconds
        countdown_data['count_time'].set(f'{hour:02d}:{minute:02d}:{seconds:02d}')  # Update the countdown window with the remaining time
        sleep(1)  # Sleep for 1 second