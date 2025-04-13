import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm
import time
import urllib3
from concurrent.futures import ThreadPoolExecutor

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://love-games1.net"
SAVE_DIR = "results"
LOG_FILE = "collectedfiles.txt"
TOTAL_PAGES = 144
MAX_WORKERS = 10  # Number of threads for parallelism

os.makedirs(SAVE_DIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_soup(url):
    res = requests.get(url, headers=HEADERS, verify=False)
    res.raise_for_status()
    return BeautifulSoup(res.text, "html.parser")

def get_game_links(page_url):
    soup = get_soup(page_url)
    links = []
    for a in soup.select("a[href^='/load/igry_dlja_konsolej/igry_dlja_playstation_4/']"):
        href = a.get("href")
        if href and "42-" in href:
            full_url = urljoin(BASE_URL, href)
            if full_url not in links:
                links.append(full_url)
    return links

def extract_metadata(soup):
    metadata = {
        "Year of issue": "N/A",
        "Genre": "N/A",
        "Disk code": "N/A",
        "Game Version": "N/A",
        "Minimum firmware version": "N/A",
        "Interface language": "N/A",
        "voice language": "N/A"
    }

    # Look for spans or b tags followed by text with colon
    for row in soup.find_all(['b', 'span']):
        label = row.get_text(strip=True).rstrip(':')
        if label in metadata:
            next_text = row.find_next_sibling(text=True)
            if next_text:
                metadata[label] = next_text.strip()
    return metadata

def get_game_title_and_torrent_url(game_url):
    soup = get_soup(game_url)

    # Game title
    title_tag = soup.find("h1")
    if not title_tag:
        raise Exception("No game title found.")
    raw_title = title_tag.text.strip()

    # Clean filename
    safe_title = re.sub(r"[\[\]\(\)]", "", raw_title)
    safe_title = re.sub(r"\s+", "-", safe_title)
    safe_title = re.sub(r"[^A-Za-z0-9\-\.]", "", safe_title)
    filename = f"{safe_title}.torrent"

    # Torrent link
    torrent_page_link = soup.find("a", href=re.compile(r"^/load/0-0-0-"))
    if not torrent_page_link:
        raise Exception("No torrent page link found.")
    torrent_page_url = urljoin(BASE_URL, torrent_page_link['href'])

    metadata = extract_metadata(soup)

    return raw_title, filename, torrent_page_url, metadata

def download_torrent(torrent_page_url, filename, game_name, game_page_url, metadata):
    filepath = os.path.join(SAVE_DIR, filename)
    if os.path.exists(filepath):
        print(f"Already exists: {filename}")
        return

    try:
        with requests.get(torrent_page_url, headers=HEADERS, verify=False, stream=True, allow_redirects=True) as r:
            r.raise_for_status()
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        print(f"Saved torrent: {filename}")

        # Write to collectedfiles.txt
        with open(LOG_FILE, 'a', encoding='utf-8') as log:
            log.write(f"Game Name: {game_name.replace(' ', '-')}\n")
            for key, value in metadata.items():
                log.write(f"{key}: {value}\n")
            log.write(f"Saved As: {filepath}\n")
            log.write("-" * 50 + "\n")

    except Exception as e:
        print(f"Failed to download from {torrent_page_url}: {e}")

def process_game_page(game_link):
    try:
        game_name, filename, torrent_url, metadata = get_game_title_and_torrent_url(game_link)
        download_torrent(torrent_url, filename, game_name, game_link, metadata)
    except Exception as e:
        print(f"Error with game link {game_link}: {e}")

def main():
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for page_num in range(1, TOTAL_PAGES + 1):
            suffix = f"42-{page_num}" if page_num > 1 else "42"
            page_url = f"{BASE_URL}/load/igry_dlja_konsolej/igry_dlja_playstation_4/{suffix}"
            print(f"\n--- Scanning Page {page_num} --- {page_url}")
            try:
                game_links = get_game_links(page_url)
                # Submit all game links to be processed in parallel
                executor.map(process_game_page, game_links)
                time.sleep(1)  # Slight delay to avoid overloading server
            except Exception as e:
                print(f"Failed to load page {page_url}: {e}")

if __name__ == "__main__":
    main()
