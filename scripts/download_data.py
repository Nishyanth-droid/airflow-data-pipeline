import urllib.request

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
output_path = "/tmp/raw_data.csv"

print("Downloading Iris dataset...")
urllib.request.urlretrieve(url, output_path)
print(f"Downloaded successfully to {output_path}")
