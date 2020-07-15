import requests

def main():
    text = requests.get("https://www.google.com")
    print(text.text)

if __name__=="__main__":
    main()
