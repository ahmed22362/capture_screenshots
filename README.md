# Web Scraping Script: Capture Screenshots from Website

This script uses Selenium to capture screenshots from a website and saves them with timestamps. It automates the process of entering a national ID and selecting a dropdown value on the website `http://online-services.fayoum.edu.eg/pg_show_result_test/`.

## Prerequisites

- Python 3.x
- Selenium library
- Chrome WebDriver
- Chrome browser

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ahmed22362/capture_screenshots.git
   ```

2. Install the required Python libraries:
   ```bash
   pip install selenium
   ```
3. Download the Chrome WebDriver suitable for your Chrome browser version from [here](<(https://link-url-here.org)>). Make sure to place the WebDriver executable in your system's PATH or provide its path in the script.

## Usage

1. Open the script file capture_screenshots.py in a text editor.

2. Modify the values of my_national_id and my_collage_value variables with your desired national ID and dropdown value.

3. Optionally, uncomment the Chrome options (chrome_options.add_argument(...)) if you want to run the script in headless mode or disable notifications.

4. Save the script file.

5. Run the script:

```bash
python capture_screenshots.py
```

6. The script will launch Chrome, navigate to the website, enter the national ID, select the dropdown value, capture screenshots, and repeat the process with a refresh every 2 seconds.

7. The screenshots will be saved in the same directory with filenames in the format my_screenshot_YYYY-MM-DD_HH-MM-SS.png.

## License

This project is licensed under the MIT License.
