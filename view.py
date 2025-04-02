'''
@author: PythonDeveloper29042
@project: AutoShutdown 
@file: view.py
@file-description: This file is the view of the application. It is responsible for displaying the user interface and getting input from the user.
'''

from tkinter import Tk, Label, Button, Entry, ttk, Toplevel, messagebox, StringVar
from tkcalendar import Calendar
from datetime import datetime
import controller

root = Tk()
end_time = StringVar()  # Variable to store the end time
end_time.set('')  # Set the default value of the end time to an empty string
count_time = StringVar()  # Variable to store the countdown time
count_time.set('')  # Set the default value of the countdown time to an empty string


def setup():
    '''
    This function is responsible for setting up the user interface.
    '''
    root.title('AutoShutdown')  # Set the title of the window
    sceen_width = root.winfo_screenwidth()  # Get the width of the screen
    screen_height = root.winfo_screenheight()  # Get the height of the screen
    width = 400  # Set the width of the window
    height = 300  # Set the height of the window
    pos_x = (sceen_width - width) // 2  # Calculate the x-coordinate of the window
    pos_y = (screen_height - height) // 2  # Calculate the y-coordinate of the window
    root.geometry(f'{width}x{height}+{pos_x}+{pos_y}')  # Set the size and position of the window
    root.iconbitmap(r'.\assets\icons\AutoShutdown_16x16.ico')  # Set the icon of the window
    root.resizable(False, False)  # Disable resizing of the window


def add_components_to_main_window():
    '''
    This function is responsible for adding the components to the main window.
    '''
    global model_time  # Make model_time a global variable to access it in other functions
    for child in root.winfo_children():
        child.destroy()  # Destroy all the child widgets in the main window
    # The label that displays the title of the application
    title = Label(root, text='AutoShutdown', font=('SimSun', 18, 'bold'))
    title.pack(pady=20)

    # The label that displays the description of the operation
    # label = Label(root, text='Choose the time at which the system should be shut down:')
    label = Label(root, text='选择系统应该关机的时间:', font=('SimSun',10,'normal'))
    label.pack()

    # # button = Button(root, text='Set')
    # button = Button(root, text='确认', font=('SimSun',10,'normal'))
    # button.pack()

    # Add example time
    model_time = ttk.Combobox(root, values=['5分钟', '10分钟', '20分钟', '30分钟', '1小时', '2小时', '3小时'], font=('SimSun',10,'normal'))
    model_time.pack(pady=10)

    # Add another label that displays 'Shutdown after:'
    shutdown_after_label = Label(root, text='后关机', font=('SimSun',10,'normal'))
    shutdown_after_label.pack()

    # Add another button to set the time
    set_button = Button(root, text='确认', font=('SimSun',10,'normal'), command=confirm_shutdown)
    set_button.pack()

    # Add another button to customize the time
    custom_button = Button(root, text='自定义', font=('SimSun', 10, 'normal'), command=add_components_to_customize_window)
    custom_button.pack(pady=20)


def add_components_to_customize_window():
    global calendar, hours, minutes
    customize_window = Toplevel(root)  # Create a new window
    customize_window.title('自定义时间')  # Set the title of the new window
    sceen_width = customize_window.winfo_screenwidth()  # Get the width of the screen
    screen_height = customize_window.winfo_screenheight()  # Get the height of the screen
    width = 400  # Set the width of the window
    height = 300  # Set the height of the window
    pos_x = (sceen_width - width) // 2  # Calculate the x-coordinate of the window
    pos_y = (screen_height - height) // 2  # Calculate the y-coordinate of the window
    customize_window.geometry(f'{width}x{height}+{pos_x}+{pos_y}')  # Set the size and position of the window
    # customize_window.geometry('400x300+100+100')  # Set the size and position of the new window
    customize_window.iconbitmap(r'.\assets\icons\AutoShutdown_16x16.ico')  # Set the icon of the new window
    customize_window.resizable(False, False)  # Disable resizing of the new window

    # Add the prompt to the new window
    prompt = Label(customize_window, text='请选择系统关机的时间：', font=('SimSun', 10, 'normal'))
    prompt.pack()

    # Add the calendar to choose the date
    calendar = Calendar(customize_window, font=('SimSun', 10, 'normal'))
    calendar.pack(pady=10)

    # Add the comboboxes to choose the time
    hours = ttk.Combobox(customize_window, values=[str(i).zfill(2) + '时' for i in range(24)], font=('SimSun', 10, 'normal'))
    hours.pack(pady=2)
    minutes = ttk.Combobox(customize_window, values=[str(i).zfill(2) + '分' for i in range(60)], font=('SimSun', 10, 'normal'))
    minutes.pack(pady=2)
    # seconds = ttk.Combobox(customize_window, values=[str(i).zfill(2) + '秒' for i in range(60)], font=('SimSun', 10, 'normal'))
    # seconds.pack(pady=2)

    # Add the button to set the time
    set_button = Button(customize_window, text='确认', font=('SimSun', 10, 'normal'), command=confirm_shutdown_custom)
    set_button.pack(pady=2)


def add_components_to_countdown_window():
    global calendar
    # countdown_window = Toplevel(root)  # Create a new window for the countdown
    # Replace all elements from the main window with the countdown window
    for child in root.winfo_children():
        child.destroy()
    root.title('倒计时')  # Set the title of the countdown window
    width = 400  # Set the width of the window
    height = 300  # Set the height of the window
    sceen_width = root.winfo_screenwidth()  # Get the width of the screen
    screen_height = root.winfo_screenheight()  # Get the height of the screen
    pos_x = (sceen_width - width) // 2  # Calculate the x-coordinate of the window
    pos_y = (screen_height - height) // 2  # Calculate the y-coordinate of the window
    root.geometry(f'{width}x{height}+{pos_x}+{pos_y}')  # Set the size and position of the window
    # root.geometry('400x300+100+100')  # Set the size and position of the countdown window
    root.iconbitmap(r'.\assets\icons\AutoShutdown_16x16.ico')  # Set the icon of the countdown window
    root.resizable(False, False)  # Disable resizing of the countdown window

    # Add a label to display the countdown message
    countdown_label = Label(root, textvariable=end_time, font=('SimSun', 10, 'normal'))
    countdown_label.pack(pady=10)

    # Add a label to display "Remaining time:"
    remaining_time_text = Label(root, text='剩余时间:', font=('SimSun', 10, 'normal'))
    remaining_time_text.pack(pady=10)

    # Add a label to display the remaining time (this will be updated dynamically)
    remaining_time_label = Label(root, textvariable=count_time, font=('SimSun', 40, 'bold'))
    remaining_time_label.pack(pady=20)

    # Add a button to cancel the shutdown
    cancel_button = Button(root, text='取消关机', font=('SimSun', 10, 'normal'), command=cancel_shutdown)
    cancel_button.pack(pady=20)


def confirm_shutdown():
    global model_time  # Make model_time a global variable to access it in other functions
    time_selected = model_time.get()  # Get the selected time from the combobox
    # messagebox.showinfo('确认', f'系统将在{time_selected}后关机')  # Show a confirmation message
    add_components_to_countdown_window()  # Add the components to the countdown window
    controller.shutdown_model(time_selected, end_time=end_time, count_time=count_time)  # Call the controller to set the shutdown time


        
def cancel_shutdown():
    '''
    This function is responsible for cancelling the scheduled shutdown.
    '''
    controller.cancel_shutdown()
    # print('cancel shutdown')  # Print the message for debugging purposes
    add_components_to_main_window()  # Add the components back to the main window



def confirm_shutdown_custom():
    '''
    This function is responsible for confirming the custom shutdown time.
    '''
    global calendar, hours, minutes, seconds  # Make the variables global to access them in other functions
    selected_date = calendar.get_date()  # Get the selected date from the calendar
    month, day, year = selected_date.split('/')  # Split the date into month, day, and year
    date = datetime.now()
    hour = hours.get()  # Get the selected hour from the combobox
    minute = minutes.get()  # Get the selected minute from the combobox
    if not hour or not minute:
        messagebox.showerror('警告', '小时和时间不能为空！你是不是傻逼？')  # Show an error message if the hour or minute is empty
        return
    target_time = date.replace(year=int(year)+2000, month=int(month), day=int(day), hour=int(hour[:-1]), minute=int(minute[:-1]), second=0)
    controller.shutdown_custom(target_time, end_time=end_time, count_time=count_time, callback=add_components_to_countdown_window)  # Call the controller to set the custom shutdown time
    

def main():
    '''
    This function is responsible for running the main event loop.
    '''
    setup()
    add_components_to_main_window()
    # add_components_to_customize_window()
    # add_components_to_countdown_window()
    root.mainloop()


if __name__ == '__main__':
    main()