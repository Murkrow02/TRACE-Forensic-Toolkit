<h1 align="center">Toolkit for Retrieval and Analysis of Cyber Evidence (TRACE)</h1>

<p align="center">
  TRACE is a digital forensic tool I developed as my final year project. It provides an intuitive interface for analyzing disk images and includes a range of functionalities to assist forensic examiners in extracting and viewing the contents of various image file formats.
</p>

<p align="center">
  <img src="Icons/logo_prev_ui.png" alt="TRACE Logo" width="400"/>
</p>

## Navigation 🧭

- [Preview 👀](#preview-)
- [Features 🌟](#features-)
- [Screenshots 📸](#screenshots-)
- [Supported Image Formats 💾](#supported-image-formats-)
- [Cross-Platform Compatibility 🖥️💻](#cross-platform-compatibility-)
- [Getting Started 🚀](#getting-started-)
  - [Prerequisites](#prerequisites)
  - [Configuration ⚙️](#configuration-)
  - [Running the Tool ▶️](#running-the-tool-)
- [Built With 🧱](#built-with-)
- [Work in Progress 🛠️](#work-in-progress-)
- [Testing & Feedback 🧪](#testing--feedback-)
- [Socials 👨‍💻](#socials-)

## Preview 👀
<p>
  <br/>
  <img src="Icons/readme/Preview.png" alt="TRACE Preview" width="100%"/>
  <br/>
</p>

<br>

## Features 🌟

✅ **Image Mounting & Dismounting**: Seamlessly mount and dismount forensic disk images for analysis.\
✅ **Tree Viewer**: Navigate through the disk image structure, including partitions and files.\
✅ **Detailed File Analysis**: View file content in different formats, such as HEX, text, and application-specific views.\
✅ **EXIF Data Extraction**: Extract and display EXIF metadata from image files.\
✅ **Registry Viewer**: View and analyze Windows registry files.\
✅ **Basic File Carving**: Recover deleted files from disk images.\
✅ **Virus Total API Integration**: Check files for malware using the Virus Total API.\
✅ **E01 Image Verification**: Verify the integrity of E01 disk images.\
✅ **Convert E01 to Raw**: Convert E01 disk images to raw format.\
✅ **Message Decoding**: Decode messages from base64, binary, and other encodings.

<br>

## Screenshots 📸

### Registry Browser 🗂️

<p>
  <br/>
  <img src="Icons/readme/registry.png" alt="Registry Browser" width="90%"/>
  <br/>
</p>


### File Carving 🔪

<p>
  <br/>
  <img src="Icons/readme/carving.png" alt="File Carving" width="90%"/>
  <br/>
</p>

### File Search 🔍
<p>
  <br/>
  <img src="Icons/readme/file_search.png" alt="Image Verification" width="80%"/>
  <br/>
</p>

### Image Verification ✅

<p>
  <br/>
  <img src="Icons/readme/trace_verify.png" alt="Image Verification" width="70%"/>
  <br/>
</p>

<br>



## Supported Image Formats 💾

| Image Format                                   | Extensions             | Split   |  Unsplit |
|------------------------------------------------|------------------------|---------|----------|
| EnCase® Image File (EVF / Expert Witness Format)| `*.E01` `*.Ex01`       | ✔️      | ✔️       |
| SMART/Expert Witness Image File                | `*.s01`                | ✔️      | ✔️       |
| Single Image Unix / Linux DD / Raw             | `*.dd`, `*.img`, `*.raw` | ✔️      | ✔️       |
| ISO Image File                                 | `*.iso`                |         | ✔️       |
| AccessData Image File                          | `*.ad1`                | ✔️       | ✔️        |

<br>


## Cross-Platform Compatibility 🖥️💻

| Operating System       | Screenshot                                                                                                                     |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **macOS Sonoma** 🍏    | <a href="Icons/readme/macos.png"><img src="Icons/readme/macos.png" alt="macOS Screenshot" width="900"/></a>                    |
| **Kali Linux 2024** 🐧 | <a href="Icons/readme/kali.png"><img src="Icons/readme/kali.png" alt="Kali Linux Screenshot" width="900"/></a>      |
| **Windows 10** 🗔     | <a href="Icons/readme/windows10.png"><img src="Icons/readme/windows10.png" alt="Windows Screenshot" width="900"/></a> |


## Getting Started 🚀


### Prerequisites

- Ensure you have all the necessary Python libraries installed.

```bash
pip install -r requirements.txt
  ```

### Configuration ⚙️

- **API Keys Configuration**: The tool integrates with VirusTotal and Veriphone APIs, and you will need to provide your own API keys to use these features. Update the API keys in the following files:

  - For VirusTotal: Update the API key in `modules/virus_total_tab.py`
  - For Veriphone: Update the API key in `modules/veriphone_api.py`


### Running the Tool ▶️


```bash
python main.py
```
<br>

## Built With 🧱

- [pytsk3](https://pypi.org/project/pytsk3/) - Python bindings for the SleuthKit
- [libewf-python](https://github.com/libyal/libewf) - Library to access the Expert Witness Compression Format (EWF)
- [PySide6](https://pypi.org/project/PySide6/) - Used for the GUI components.
- [Arsenal Image Mounter](https://arsenalrecon.com/products/image-mounter/) - For mounting forensic disk images.



## Work in Progress 🛠️

- **Direct Video/Audio Playback**: Currently, the video and audio player saves files temporarily before playing them, which can cause delays. The goal is to enable direct playback for faster performance.
- **Integrated File Search and Viewer**: The file search functionality is not yet connected to the "Viewer Tab," which displays HEX, text, application-specific views, metadata, and other details. This integration needs to be implemented.
- **Cross-Platform Image Mounting**: Image mounting currently works only on Windows using the Arsenal Image Mounter executable. The aim is to make this feature work across all platforms without relying on external executables.
- **File Carving and Viewer Integration**: The file carving functionality is not yet connected to the "Viewer Tab," where users can view HEX, text, application-specific views, and metadata. Additionally, the current file carving process does not distinguish between deleted and non-deleted files; it will "carve" all files of the selected type from the disk image.

## Testing & Feedback 🧪

- **Tested Formats**: The tool has primarily been tested with `dd` and `E01` files. While these formats are well-supported, additional testing with other formats, such as `Ex01`, `Lx01`, `s01`, and others, is needed.
- **Call for Samples**: If you have disk images in formats that are less tested (`Ex01`, `Lx01`, `s01`, etc.), your contributions would be greatly appreciated to help improve the tool's compatibility and robustness.
- **Feedback Welcome**: Please report any issues or unexpected behavior to help improve the tool. Contributions and testing feedback are encouraged and welcomed.


## Socials 👨‍💻


[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/radoslav-gadzhovski)

<br>


![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)


