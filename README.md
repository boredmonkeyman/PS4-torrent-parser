 PS4-torrent-parser
edit: i will re run and update the magnet links when i believe its needed, maybe when more ps4 games have released 

Python script to grab .torrent files for JB ps4, i collected 2067 torrents within five mins on android phone



building custom scripts for money doesn't have to be PS related 

https://t.me/boredmonkeymanschat

<a href="https://ibb.co/dJmC6XRZ"><img src="https://i.ibb.co/dJmC6XRZ/Screenshot-2025-04-13-02-32-39-61-55bef12f624c2b805189a6aa783c400d.jpg" alt="Screenshot-2025-04-13-02-32-39-61-55bef12f624c2b805189a6aa783c400d" border="0"></a>

<a href="https://ibb.co/qFktvrS6"><img src="https://i.ibb.co/qFktvrS6/Screenshot-2025-04-13-02-26-48-07-99c04817c0de5652397fc8b56c3b3817.jpg" alt="Screenshot-2025-04-13-02-26-48-07-99c04817c0de5652397fc8b56c3b3817" border="0"></a>

# **Torrent Scraper Script for ps4 pkgs**

This Python script automatically scrapes game pages from **Love-Games1.net** and downloads `.torrent` files for PlayStation 4 games. The script collects metadata such as the **Game Name**, **Disk Code**, **Game Version**, and other related details, then logs them into a file while saving the `.torrent` file in the `results/` folder.

---

## **Table of Contents**
1. [Requirements](#requirements)
2. [Installation Instructions](#installation-instructions)
3. [Running the Script](#running-the-script)
4. [Script Output and Logging](#script-output-and-logging)
5. [Customization](#customization)
6. [Troubleshooting](#troubleshooting)
7. [Disclaimer](#disclaimer)

---

## **Requirements**

Before you run the script, ensure you have the following installed:

- **Python 3.x**: The script is written in Python 3. Install Python from the [official website](https://www.python.org/downloads/).
- **Required Libraries**: Install the necessary libraries by running this command in your terminal or command prompt:
  ```bash
  pip install requests beautifulsoup4 tqdm
  ```

---

## **Installation Instructions**

1. **Download the Script**:
   - Download or clone the repository that contains the script `torrent_scraper.py` to your computer.

2. **Prepare the Environment**:
   - Ensure that Python 3.x is installed on your system.
   - Install the required libraries using the command mentioned above.

3. **Create the Results Directory**:
   - The script will download `.torrent` files and save them in a folder called `results/`. Ensure this folder exists by running:
     ```bash
     mkdir results
     ```

---

## **Running the Script**

1. Open your terminal or command prompt.

2. Navigate to the directory where the script (`torrent_scraper.py`) is located. For example:
   ```bash
   cd /path/to/script
   ```

3. Run the script with the following command:
   ```bash
   python torrent_scraper.py
   ```

   The script will begin scanning the pages of the PlayStation 4 games and downloading torrents. Each page is scraped, and the `.torrent` files are saved to the `results/` folder.

4. The script will also output logs in the `collectedfiles.txt` file, detailing the metadata of each downloaded game.

---

## **Script Output and Logging**

### **Downloaded Files:**
- Torrents are saved in the `results/` directory with filenames like:
  ```
  PS4-WWE-2K25-CUSA48576-1.07.torrent
  ```
  
### **Log File (`collectedfiles.txt`):**
- A log file is created to record the metadata of each collected game:
  ```
  Game Name: PS4-WWE-2K25-CUSA48576-1.07
  Disk code: CUSA48576
  Game Version: 1.07
  Minimum firmware version: 5.05
  Interface language: English
  voice language: English
  Saved As: results/PS4-WWE-2K25-CUSA48576-1.07.torrent
  --------------------------------------------------
  ```

This log is saved in `collectedfiles.txt` in the same directory as the script.

---

## **Customization**

1. **Number of Pages to Scrape**:
   - The script is set to scrape **144 pages** by default (`TOTAL_PAGES = 144`).
   - If you want to scrape fewer or more pages, you can change the `TOTAL_PAGES` variable in the script to your desired number.

2. **Number of Concurrent Threads**:
   - The script uses **multithreading** to download torrents concurrently, which speeds up the process. The number of concurrent threads is controlled by the `MAX_WORKERS` variable.
   - You can adjust `MAX_WORKERS` to a higher or lower value based on your system's capability:
     ```python
     MAX_WORKERS = 10  # Change to a higher number for more concurrency
     ```

3. **Output Directory**:
   - By default, torrents are saved in the `results/` folder. You can change the `SAVE_DIR` variable to a different path if needed.

---

## **Troubleshooting**

If you encounter issues, here are some common solutions:

1. **SSL Errors**:
   - If you see SSL errors when trying to fetch pages or torrents, the script disables SSL verification by default. Ensure your Python installation has the necessary SSL certificates or run the script with a secure connection.

2. **Slow Downloads**:
   - If downloading is slow, consider reducing the number of concurrent threads (`MAX_WORKERS`) to avoid overwhelming the server.

3. **404 Errors**:
   - If a page or torrent is not found, it might be due to changes on the website. In such cases, you can inspect the URLs manually to ensure they're correct.

4. **Already Downloaded Torrents**:
   - If a torrent file with the same name already exists in the `results/` directory, the script will skip downloading that file. You can delete old torrents to ensure the script downloads the latest versions.

---

## **Disclaimer**

- **Ethical Use**: This script is intended for educational and personal use only. Be sure to comply with the website's terms of service and any local laws regarding torrenting.
- **Website Changes**: The script may break if Love-Games1.net changes its layout or URL structure. In such cases, you will need to modify the script to accommodate those changes.
- **Server Load**: Running the script with too many threads could cause the server to slow down or block your IP. Use the script responsibly.

---

**Enjoy!** Feel free to modify the script as needed and share any improvements you make!
