import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextBrowser
import requests
from bs4 import BeautifulSoup

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("""
            QWidget {
                font-family: 'Arial';
            }
            QPushButton {
                background-color: #2980b9;
                color: white;
                border: none;
                padding: 5px;
                min-width: 50px;
            }
            QPushButton:hover {
                background-color: #3498db;
            }
            QTextBrowser {
                background-color: #ecf0f1;
            }
        """)

        self.search_line = QLineEdit()
        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search_website)
        self.result_browser = QTextBrowser()
        self.result_browser.setOpenExternalLinks(True)  # Enable hyperlinks

        vbox = QVBoxLayout()
        vbox.addWidget(self.search_line)
        vbox.addWidget(self.search_button)
        vbox.addWidget(self.result_browser)

        self.setLayout(vbox)
        self.setWindowTitle('Google Search')
        self.setGeometry(300, 300, 350, 500)
        self.show()

    def search_website(self):
        keyword = self.search_line.text()
        url = f"https://www.google.com/search?q={keyword}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = soup.select(".yuRUbf a")
        for result in search_results:
            title = result.select_one("h3").text
            link = result["href"]
            self.result_browser.append(f'<a href="{link}"><b>{keyword}</b> in {title}</a>\n\n')  # Add hyperlink to the title with keyword highlighted

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
