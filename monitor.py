import json
import urllib.request
import urllib.error

URLS = [
"https://explorer.nerva.one/",
]

def check_site(url):
print(f"\nПеревіряю: {url}")
try:
request = urllib.request.Request(
url,
headers={"User-Agent": "NERVA-Cloud-Monitor/1.0"}
)
with urllib.request.urlopen(request, timeout=15) as response:
print("Статус сайту:", response.status)
print("Підключення працює.")
except Exception as error:
print("Не вдалося отримати відповідь:", error)

def main():
print("=== NERVA Cloud Monitor ===")
print("Перевірка доступності оглядача блокчейна.")
for url in URLS:
check_site(url)
print("\nПеревірку завершено.")

if name == "main":
main()
