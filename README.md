Microscope Image Processing API

Overview
This is a **Flask-based API** that processes **microscope images** with functionalities like:
- **Image Stitching** → Combine multiple overlapping images into a high-resolution composite.
- **ROI Selection** → Extract a specific **Region of Interest (ROI)** for analysis.
- **Zoom Functionality** → Digitally zoom into the ROI (supports up to 20X zoom).
- **Auto-Focus Simulation** → Enhance image clarity using contrast-based sharpening.

Folder Structure
```
/microscope_image_processing
├── app.py                # Flask API implementation
├── index.html            # Web interface with embedded CSS
├── utils                 # Utility scripts for image processing
│   ├── stitching.py      # Image stitching logic
│   ├── roi.py            # ROI selection logic
│   ├── zoom.py           # Zoom functionality logic
│   └── auto_focus.py     # Auto-focus sharpening logic
└── uploads               # Folder for storing uploaded images
```

Installation
1. Clone the Repository
```bash
git clone https://github.com/your-repo/microscope-image-processing.git
cd microscope-image-processing
```

2. Create a Virtual Environment & Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. Run the Flask App
```bash
python app.py
```
The API will be available at: **`http://127.0.0.1:5000/`**

API Endpoints
| **Endpoint**        | **Method** | **Functionality** |
|---------------------|------------|--------------------------------|
| `/`                | GET        | Home page with image upload UI |
| `/upload`          | POST       | Upload microscope images |
| `/stitch_images`   | GET        | Stitch overlapping images into one |
| `/roi_selection`   | POST       | Extract ROI based on user input |
| `/zoom`            | POST       | Apply zoom (10X, 20X) to the ROI |
| `/auto_focus`      | GET        | Apply auto-focus sharpening |

Usage
1. Upload Images
- Open `http://127.0.0.1:5000/` in a browser.
- Select microscope images and upload them.

2. Use Image Processing Features
- Click on **Stitch Images** to merge uploaded images.
- Enter coordinates (x, y, width, height) to extract an **ROI**.
- Choose a **zoom factor** (e.g., 10X, 20X) for zooming.
- Apply **auto-focus sharpening** to improve clarity.

Notes
- Images **must overlap** for stitching to work.
- **Higher resolution** images produce better zoom results.
- If zoom is **too high**, it may slow down processing.

License
This project is open-source and available under the **MIT License**.

Author
- **Your Name**
- [GitHub](https://github.com/your-profile)

---
_If you encounter any issues, feel free to open an issue on GitHub._ 🚀
