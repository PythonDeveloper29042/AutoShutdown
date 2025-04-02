# AutoShutdown 使用说明

## Table of Contents / 目录

    
- [简体中文版README](#autoshutdown-使用说明)
    - [简介](#简介)
    - [安装](#安装)
        - [安装Python](#安装python)
            - [Windows上安装](#windows上安装)
            - [macOS上安装](#macos上安装)
            - [Linux上安装](#linux上安装)
        - [安装所需模块](#安装所需模块)
        - [安装Git](#安装git)
            - [Windows上安装Git](#windows上安装git)
            - [macOS上安装Git](#macos上安装git)
            - [Linux上安装Git](#linux上安装git)
        - [安装VS Code](#安装visual-studio-code-python扩展-可选但推荐)
            - [图形化安装](#图形化安装)
            - [Windows上安装VS Code](#windows上安装visual-studio-code)
            - [macOS上安装VS Code](#macos上安装visual-studio-code)
            - [Linux上安装VS Code](#linux上安装visual-studio-code)
            - [安装Python扩展](#安装python扩展)
    - [克隆代码库](#克隆仓库)
    - [运行程序](#运行程序)
        - [图形化运行程序](#图形化运行程序)
        - [Windows上运行程序](#windows上运行程序)
        - [macOS和Linux上运行程序](#macos和Linux上运行程序)
        - [如何使用程序](#如何使用程序)
    - [许可](#MIT-许可证)
    - [询问](#询问)
    - [结语](#结语)

- [English version of the README](#autoshutdown)
    - [Introduction](#introduction)
    - [Setup](#setup)
        - [Install Python](#install-python)
            - [Install on Windows](#install-on-windows)
            - [Install on macOS](#install-on-macos)
            - [Install on Linux](#install-on-linux)
        - [Install the required modules](#install-the-required-modules)
        - [Install Git](#install-git)
            - [Install Git on Windows](#install-git-on-windows)
            - [Install Git on macOS](#install-git-on-macos)
            - [Install Git on Linux](#install-git-on-linux)
        - [Install VS Code](#install-microsoft-visual-studio-code-python-extension-optional-but-recommended)
            - [Graphical Installation](#graphical-installation)
            - [Install VS Code on Windows](#install-visual-studio-code-on-windows)
            - [Install VS Code on macOS](#install-visual-studio-code-on-macos)
            - [Install VS Code on Linux](#install-visual-studio-code-on-linux)
            - [Install the Python extension](#install-the-python-extension)
    - [Clone the repository](#clone-the-repository)
    - [Run and use the program](#run-the-program)
        - [Run the program graphically](#run-the-program-graphically)
        - [Run the program in Windows](#run-the-program-in-windows)
        - [Run the program in macOS or Linux](#run-the-program-in-macos-linux)
        - [How to use the program](#how-to-use-the-program)
    - [License](#mit-license)
    - [Inquiries](#inquiries)
    - [Conclusion](#conclusion)

## 简介
此程序是一个简单的程序，可以在一定时间后关闭计算机。如果您想让计算机在一段时间后自动关闭，这很有用。此程序是用Python编写的，并使用`os`模块关闭计算机。
此项目遵循MVC设计模式。

## 安装
要使用此程序，您需要配置以下内容：
- Python 3.8+
- `tkcalendar`模块（用于日历小部件）
- Git
- `pyinstaller`模块（可选，用于创建可执行文件）
### 安装Python
#### Windows上安装
要在Windows上安装Python，您可以使用Windows包管理器安装Python。使用此命令：
```bash
winget install --id Python.Python.3.13 --source winget
```
或者，您可以从[官方网站](https://python.org)下载安装程序，并图形化安装。
#### macOS上安装
macOS有一个内置的Python。但是，版本可能过时。某些模块可能缺少或无法正常工作。因此，建议安装最新版本的Python。  
若要在macOS上安装Python，您需要从[官方网站](https://brew.sh/)安装Homebrew。然后，您可以使用以下命令安装Python：
```bash
brew install python
```
或者，您可以从[官方网站](https://python.org)下载安装程序，并图形化安装。
#### Linux上安装
您通常不需要在Linux上手动安装Python，因为大多数发行版都预装了它。但是，如果版本<= 3.8，您可以使用以下命令在Debian、Ubuntu、深度操作系统、优麒麟或其他基于Debian的发行版上安装Python：
```bash
sudo apt install python3
```
您可以使用此命令在Fedora、Red Hat、CentOS或其他基于Red Hat的发行版上安装Python：
```bash
sudo dnf install python3
```
您可以使用此命令在Arch Linux、Manjaro或其他基于Arch的发行版上安装Python：
```bash
sudo pacman -S python
```
如果您不知道您的发行版使用哪个包管理器，您可以图形化安装它，或者使用预装的Python。
### 安装所需模块
要安装所需的模块，您可以使用以下命令：
```bash
pip install -r requirements.txt
```
在macOS或Linux上，您可能需要使用`pip3`而不是`pip`：
```bash
pip3 install -r requirements.txt
```
### 安装Git
#### Windows上安装Git
要在Windows上安装适用于Windows的Git（Git for Windows），您可以使用Windows包管理器安装Git。使用此命令：
```bash
winget install --id Git.Git --source winget
```
#### macOS上安装Git
在macOS种，建议使用Apple提供的Git，它是Xcode命令行工具的一部分。您可以使用以下命令安装它：
```bash
xcode-select --install
```
如果您已经安装了Xcode，请忽略此步骤，因为它包含命令行工具。
#### Linux上安装Git
你可以使用以下命令在Debian、Ubuntu、深度操作系统、优麒麟或其他基于Debian的发行版上安装Git：
```bash
sudo apt install git
```
您可以使用此命令在Fedora、Red Hat、CentOS或其他基于Red Hat的发行版上安装Git：
```bash
sudo dnf install git
```
您可以使用此命令在Arch Linux、Manjaro或其他基于Arch的发行版上安装Git：
```bash
sudo pacman -S git
```
### 安装Visual Studio Code + Python扩展（可选但推荐）
VS Code是一个免费的开源代码编辑器，支持多种编程语言。它是一个非常强大的IDE，支持调试、版本控制、代码补全等功能。
#### 图形化安装
你可以从[官方网站](https://code.visualstudio.com/)下载安装程序并图形化安装Visual Studio Code。
如果你更喜欢命令行方法，你可以这样做：
#### Windows上安装Visual Studio Code
要在Windows上安装Visual Studio Code，您可以使用Windows包管理器安装Visual Studio Code。使用此命令：
```bash
winget install --id Microsoft.VisualStudioCode --source winget
```
#### macOS上安装Visual Studio Code
要在macOS上安装Visual Studio Code，您可以使用Homebrew安装Visual Studio Code。使用此命令：
```bash
brew install --cask visual-studio-code
```
#### Linux上安装Visual Studio Code
你可以使用以下命令在Debian、Ubuntu、深度操作系统、优麒麟或其他基于Debian的发行版上安装Visual Studio Code：
```bash
sudo apt install code
```
你可以使用以下命令在Fedora、Red Hat、CentOS或其他基于Red Hat的发行版上安装Visual Studio Code：
```bash
sudo dnf install code
```
你可以使用以下命令在Arch Linux、Manjaro或其他基于Arch的发行版上安装Visual Studio Code：
```bash
sudo pacman -S code
```
#### 安装Python扩展
要安装Python扩展，请打开Visual Studio Code并通过单击窗口侧边栏中的扩展图标转到扩展视图。然后，搜索“Python”，并安装Microsoft提供的扩展。  

**恭喜！现在您完成了环境的设置。现在让我们克隆仓库！**

## 克隆仓库
要克隆仓库，您可以使用以下命令：
```bash
git clone https://github.com/PythonDeveloper29042/AutoShutdown.git
```
这将在您当前目录中创建一个名为`AutoShutdown`的文件夹。  
您也可以使用图形化方法克隆仓库。只需打开Visual Studio Code，然后单击欢迎页面中的“克隆存储库”按钮。然后，粘贴存储库的URL并选择要克隆它的文件夹。

## 运行程序
### 图形化运行程序
若要图形化运行程序，您可以打开Visual Studio Code并打开`AutoShutdown`文件夹。然后，打开`main.py`文件并单击窗口右上角的“运行”按钮。这将运行程序并打开GUI。  
如果你更喜欢命令行方法，你可以这样做：
### Windows上运行程序
要在Windows上运行程序，您可以打开命令提示符并导航到`AutoShutdown`文件夹。然后，运行以下命令：
```bash
cd C:\path\to\AutoShutdown
python main.py
```
确保将`C:\path\to\AutoShutdown`替换为`AutoShutdown`文件夹的实际路径。
### macOS和Linux上运行程序
要在macOS或Linux上运行程序，您可以打开终端并导航到`AutoShutdown`文件夹。然后，运行以下命令：
```bash
cd /path/to/AutoShutdown
python3 main.py
```
确保将`/path/to/AutoShutdown`替换为`AutoShutdown`文件夹的实际路径。
### 如何使用程序
当您运行程序后，您将看到一个名为**AutoShutdown**的窗口。在此窗口中，您可以选择预配置的时间或输入关机时间。最后，单击**确认**按钮以设置关机时间。
例如，如果您输入**300分钟**，计算机将在5小时后关闭。

然后，窗口中将显示一个倒计时计时器。您可以单击**取消**按钮以取消关机。

如果你当初点击**自定义时间**，程序会有一个新窗口，你可以在日历小部件上选择日期，并在两个下拉框中选择时间，请注意，第一个下拉框是小时，第二个下拉框是分钟。选择日期和时间后，单击**确认**按钮以设置关机时间。

## MIT 许可证
此项目根据MIT许可证获得许可。有关详细信息，请参阅[LICENSE](LICENSE.txt)文件。

## 询问
如果你有任何疑问，你可以打开一个issue或者在[这里](mailto:pythondeveloper.29042@outlook.com)联系我。

## 结语
感谢您使用此程序！我希望您觉得它有用。如果您有任何建议或反馈，请随时告诉我。

---
---


# AutoShutdown

## Introduction
This program is a simple program that will shutdown your computer after a certain amount of time. This is useful if you want to leave your computer on for a certain amount of time and then have it automatically shutdown. This program is written in Python and uses the `os` module to shutdown the computer.

This project follows the MVC design pattern.

## Setup

To use this program, you'll need to configure that these are installed:
- Python 3.8+
- `tkcalendar` module (for the calendar widget)
- Git
- `pyinstaller` module (optional, for creating an executable)

### Install Python
#### Install on Windows
To install Python in Windows, you can use Windows package Manager to install Python. Use this command:
```bash
winget install --id Python.Python.3.13 --source winget
```
Or, you can download the installer from the [official site](https://python.org), and install it graphically. 
#### Install on macOS
macOS has a built-in Python. But, the version is likely outdated. Some modules may be missing or not work properly. So, it's recommended to install the latest version of Python.  
To install Python in macOS, you'll need to install Homebrew from the [official site](https://brew.sh/). Then, you can use the following command to install Python:
```bash
brew install python
```
Or, you can download the installer from the [official site](https://python.org), and install it graphically.
#### Install on Linux
You generally don't need to install Python manually on Linux, as it comes preinstalled with most distributions. But, if the version <= 3.8, you can use the following command to install Python in Debian, Ubuntu, Deepin, Ubuntu Kylin or other Debian-based distributions:
```bash
sudo apt install python3
```
You can use this command to install Python in Fedora, Red Hat, CentOS or other Red Hat-based distributions:
```bash
sudo dnf install python3
```
You can use this command to install Python in Arch Linux, Manjaro or other Arch-based distributions:
```bash
sudo pacman -S python
```
If you don't know which package manager your distribution uses, you can install it graphically, or use the preinstalled Python.
### Install the required modules
To install the required modules, you can use the following command:
```bash
pip install -r requirements.txt
```
On macOS or Linux, you may need to use `pip3` instead of `pip`:
```bash
pip3 install -r requirements.txt
```
### Install Git
#### Install Git on Windows
To install Git for Windows, you can use Windows package Manager to install Git. Use this command:
```bash
winget install --id Git.Git --source winget
```
#### Install Git on macOS
In macOS, it's recommended to use the Apple-provided Git, which is part of Xcode Command Line Tools. You can install it using the following command:
```bash
xcode-select --install
```
If you already have Xcode installed, ignore this step, as it contains the Command Line Tools.
#### Install Git on Linux
You can use the following command to install Git in Debian, Ubuntu, Deepin, Ubuntu Kylin or other Debian-based distributions:
```bash
sudo apt install git
```
You can use this command to install Git in Fedora, Red Hat, CentOS or other Red Hat-based distributions:
```bash
sudo dnf install git
```
### Install Microsoft Visual Studio Code + Python extension (optional but recommended)
#### Graphical Installation
You can download the installer and install Visual Studio Code graphically by heading over to the (official site)[https://code.visualstudio.com/].
If you prefer the command-line method, you can do this:
#### Install Visual Studio Code on Windows
To install Visual Studio Code on Windows, you can use Windows package Manager to install Visual Studio Code. Use this command:
```bash
winget install --id Microsoft.VisualStudioCode --source winget
```
#### Install Visual Studio Code on macOS
To install Visual Studio Code on macOS, you can use Homebrew to install Visual Studio Code. Use this command:
```bash
brew install --cask visual-studio-code
```
#### Install Visual Studio Code on Linux
You can use the following command to install Visual Studio Code in Debian, Ubuntu, Deepin, Ubuntu Kylin or other Debian-based distributions:
```bash
sudo apt install code
```
You can use this command to install Visual Studio Code in Fedora, Red Hat, CentOS or other Red Hat-based distributions:
```bash
sudo dnf install code
```
You can use this command to install Visual Studio Code in Arch Linux, Manjaro or other Arch-based distributions:
```bash
sudo pacman -S code
```
#### Install the Python extension
To install the Python extension, open Visual Studio Code and go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window. Then, search for "Python" and install the extension provided by Microsoft.    

**Congratulations! Now you finished setting up the enviornment. Now let's clone the repository!**

## Clone the repository
To clone the repository, you can use the following command:
```bash
git clone https://github.com/PythonDeveloper29042/AutoShutdown.git
```
This will create a folder named `AutoShutdown` in your current directory.  
 You can also use the graphical method to clone the repository. Just open Visual Studio Code, and click on the "Clone Repository" button in the welcome page. Then, paste the URL of the repository and select the folder where you want to clone it.

## Run the program
### Run the program graphically
To run the program graphically, you can open Visual Studio Code and open the `AutoShutdown` folder. Then, open the `main.py` file and click on the "Run" button in the top right corner of the window. This will run the program and open the GUI.
### Run the program in Windows
To run the program in Windows, you can open the command prompt and navigate to the `AutoShutdown` folder. Then, run the following command:
```bash
cd C:\path\to\AutoShutdown
python main.py
```
Make sure to replace `C:\path\to\AutoShutdown` with the actual path to the `AutoShutdown` folder.
### Run the program in macOS & Linux
To run the program in macOS or Linux, you can open the terminal and navigate to the `AutoShutdown` folder. Then, run the following command:
```bash
cd /path/to/AutoShutdown
python3 main.py
```
Make sure to replace `/path/to/AutoShutdown` with the actual path to the `AutoShutdown` folder.
### How to use the program
After you run the program, you'll see a window titled **AutoShutdown**. In this window, you can select the preconfigured time or type shutdown after which time. Finally, click the **Set** button to set the shutdown time.   
e.g. If you type **300 minutes**, the computer will shutdown after 5 hours.  

Then, there will be a countdown timer in the window. You can click the **Cancel** button to cancel the shutdown.  

If you click **Custom time**, the program will have a new window, you can select the date on the calendar widget, and select the time in the 2 comboboxes, note that the 1st combobox is hour, and the 2nd combobox is minute. After you select the date and time, click the **Set** button to set the shutdown time.

## MIT License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Inquiries
If you have any questions, feel free to open an issue or contact me at [here](mailto:pythondeveloper.29042@outlook.com).

## Conclusion
Thanks for using this program! I hope you find it useful. If you have any suggestions or feedback, feel free to let me know.