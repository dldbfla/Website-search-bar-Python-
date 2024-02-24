# Website-search-bar-Python-
Programs that pop up hyperlinks in the UI/UX when a user searches for them 


![스크린샷 2024-02-24 144158](https://github.com/dldbfla/Website-search-bar-Python-/assets/89433437/ad82618e-9ef2-479c-9bc4-23ce6bc876a9)
## The command to install the libraries needed to run this code is
````
pip install PyQt5
pip install requests
pip install beautifulsoup4
````
### However, there are a few caveats

Make sure that Python and pip are installed correctly. When you install Python, pip must also be installed. To check the installation status of Python and pip, run python --version and pip --version in the terminal.


Sometimes you may have both Python 2 and Python 3 installed at the same time. In this case, you need to use Python 3 and the corresponding version of pip. To check this, run python3 --version and pip3 --version. Use pip3 install to install the required libraries.


You may encounter permissions issues when installing certain libraries. In this case, you can use sudo to run the command or use a virtual environment. Virtual environments allow you to manage the libraries you need for a specific project without affecting the entire system.

Here's how to create and use a virtual environment


python3 -m venv myenv


source myenv/bin/activate


pip install PyQt5 requests beautifulsoup4


Check which Python interpreter you are using to run the code. If you're using an IDE, you'll need to make sure that the Python interpreter you use includes the necessary libraries.


Google's user policy prohibits using its search service in an automated way, so if you want to implement this functionality in a real service or product, you'll need to use a formal API, such as Google's Custom Search JSON API, or use the API of another search service.
