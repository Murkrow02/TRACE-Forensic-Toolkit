import requests
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QTextBrowser, QLineEdit, QLabel, QComboBox, QToolBar,
                               QSizePolicy)


class VeriphoneWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.api_key = "992B162500F143DD86625474928A5764"
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Toolbar setup
        self.toolbar = QToolBar("Veriphone Toolbar", self)
        self.toolbar.setContentsMargins(0, 0, 0, 0)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.layout.addWidget(self.toolbar)

        # Phone input field
        self.phone_input = QLineEdit(self)
        # size of the input field
        self.phone_input.setFixedSize(200, 30)
        self.phone_input.setPlaceholderText("Enter phone number")
        self.toolbar.addWidget(self.phone_input)

        # spacer
        spacer = QWidget(self)
        spacer.setFixedSize(10, 10)
        self.toolbar.addWidget(spacer)

        # Default country combo box
        self.default_country_combo = QComboBox(self)
        self.default_country_combo.addItem("Auto", "")
        # Example countries, add more as needed
        self.default_country_combo.addItem("United States", "US")
        self.default_country_combo.addItem("Canada", "CA")
        self.default_country_combo.addItem("Germany", "DE")
        self.toolbar.addWidget(QLabel("Country:"))
        self.toolbar.addWidget(self.default_country_combo)

        # spacer
        spacer = QWidget(self)
        spacer.setFixedSize(10, 10)
        self.toolbar.addWidget(spacer)

        # Verify button in toolbar
        verify_button = QPushButton("Verify", self)
        verify_button.clicked.connect(self.verify_phone_number)
        self.toolbar.addWidget(verify_button)

        # Spacer widget to push the logo to the far right
        spacer = QWidget(self)
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.toolbar.addWidget(spacer)

        # Logo on the far right
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap("Icons/logo_veriphone.png")  # Make sure the path is correct
        self.logo_label.setPixmap(self.logo_pixmap.scaled(120, 70, Qt.KeepAspectRatio,
                                                          Qt.SmoothTransformation))  # Adjust 100x50 to your desired size
        self.toolbar.addWidget(self.logo_label)

        # Text browser for showing the results
        self.info_text_edit = QTextBrowser(self)
        self.info_text_edit.setReadOnly(True)
        self.layout.addWidget(self.info_text_edit)

    def verify_phone_number(self):
        phone_number = self.phone_input.text()
        default_country_code = self.default_country_combo.currentData()
        self.update_veriphone_info(phone_number, default_country_code)

    def update_veriphone_info(self, phone_number, default_country):
        data = self.verify_phone_with_veriphone(phone_number, default_country)
        if data.get('status') == 'success':
            info_text = self.format_data_as_html(data)
            self.info_text_edit.setHtml(info_text)
        else:
            self.info_text_edit.setText("Failed to fetch data or phone number is invalid.")

    def verify_phone_with_veriphone(self, phone_number, default_country):
        url = f"https://api.veriphone.io/v2/verify?phone={phone_number}&key={self.api_key}"
        if default_country:
            url += f"&default_country={default_country}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"status": "error", "message": "Failed to verify phone number."}

    def format_data_as_html(self, data):
        # Additional fields from the Veriphone API
        phone_region = data.get('phone_region', 'N/A')
        country = data.get('country', 'N/A')
        country_code = data.get('country_code', 'N/A')
        country_prefix = data.get('country_prefix', 'N/A')
        international_number = data.get('international_number', 'N/A')
        local_number = data.get('local_number', 'N/A')
        e164 = data.get('e164', 'N/A')
        carrier = data.get('carrier', 'N/A')

        html_content = f"""
        <div style="font-family: Arial;">
            <h2>Veriphone Information</h2>
            <p><strong>Phone Number:</strong> {data.get('phone', 'N/A')}</p>
            <p><strong>Valid:</strong> {data.get('phone_valid', 'N/A')}</p>
            <p><strong>Carrier:</strong> {carrier}</p>
            <p><strong>Type:</strong> {data.get('phone_type', 'N/A')}</p>
            <p><strong>Region:</strong> {phone_region}</p>
            <p><strong>Country:</strong> {country}</p>
            <p><strong>Country Code:</strong> {country_code}</p>
            <p><strong>Country Prefix:</strong> {country_prefix}</p>
            <p><strong>International Number:</strong> {international_number}</p>
            <p><strong>Local Number:</strong> {local_number}</p>
            <p><strong>E164 Format:</strong> {e164}</p>

        </div>
        """
        return html_content