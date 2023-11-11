import requests
import argparse

def generate_urls(base_url, wordlist):
    with open(wordlist, 'r') as file:
        paths = file.read().splitlines()
    return [f"{base_url.replace('FUZZ', path)}" for path in paths]

def send_request(url):
    try:
        response = requests.get(url)
        return response
    except requests.RequestException as e:
        return f"Error: {e}"

def main():
    parser = argparse.ArgumentParser(description="Simple Python Fuzzer")
    parser.add_argument("url", help="Base URL for fuzzing (use 'FUZZ' as a placeholder)")
    parser.add_argument("-w", "--wordlist", help="Path to the wordlist file", required=True)
    args = parser.parse_args()

    base_url = args.url
    wordlist = args.wordlist

    urls_to_check = generate_urls(base_url, wordlist)

    for url in urls_to_check:
        response = send_request(url)
        if isinstance(response, requests.Response):
            print(f"URL: {url} | Status Code: {response.status_code} | Content Length: {len(response.content)}")

if __name__ == "__main__":
    main()
