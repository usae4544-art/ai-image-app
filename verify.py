import requests

def verify():
    response = requests.get('http://localhost:8000/index.html')
    content = response.text

    assert '<meta http-equiv="Content-Security-Policy"' in content
    assert 'window.open(result.url, "_blank", "noopener,noreferrer")' in content

    print("Verification successful!")

if __name__ == "__main__":
    verify()
