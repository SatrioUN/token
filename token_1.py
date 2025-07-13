import requests
import logging
import sys

# Nonaktifkan peringatan SSL (hanya untuk pengujian, jangan di produksi)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

def fetch_protected_page(url: str, token: str) -> None:
    """
    Mengirim request GET ke URL dengan token autentikasi di cookie.
    Menampilkan status code dan isi response.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (PentestBot/1.0; +https://yourdomain.com/bot)",
        "Cookie": f"TOKEN={token}"
    }

    with requests.Session() as session:
        try:
            logging.info(f"Requesting URL: {url}")
            response = session.get(url, headers=headers, verify=False, timeout=15)
            logging.info(f"Status Code: {response.status_code}")

            if response.status_code == 200:
                logging.info("Response Body:")
                print(response.text)
            else:
                logging.warning(f"Unexpected status code received: {response.status_code}")
                logging.warning(f"Response content: {response.text[:500]}")  # print first 500 chars

        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")

def main():
    # Ganti dengan URL target dan token autentikasi yang valid
    target_url = "https://example.com/protected-page"
    auth_token = "himg8yD59xpaHxfIY6W4FmG7K97Qq0Bz9EKFT2PO"

    fetch_protected_page(target_url, auth_token)

if __name__ == "__main__":
    main()
