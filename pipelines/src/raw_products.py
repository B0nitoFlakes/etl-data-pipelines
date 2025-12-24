import requests  # pyright: ignore[reportMissingModuleSource]

def task():
    url = "https://fake-store-api.mock.beeceptor.com/api/products"
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        print("✅ Successfully fetched comments")
        return response.json()
    
    except requests.exceptions.Timeout:
        print("Request timed out")
        return None
    
    except requests.exceptions.ConnectionError:
        print("Connection Error")
        return None
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return None
    
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None