from bs4 import BeautifulSoup
import requests

valor = input("insira o codigo ICAO")
print(valor.strip().upper())
html = requests.get("https://www.aisweb.aer.mil.br/?i=aerodromos&codigo=" + valor.strip().upper())
soup = BeautifulSoup(html.content, "html.parser")
sunrise = soup.find('sunrise')
sunset = soup.find('sunset')
metar = soup.find('h5',{"class":"mb-0 heading-primary"}).findNext("p")
taf = soup.find('h5',{"class":"mb-0 heading-primary"}).findNext("p").findNext("p")
cartas = soup.find_all('ul',{"class":"list list-icons list-primary list-icons-style-2"})

print("Cartas disponíveis:")
for link in cartas:
	print(link.findPrevious("h4").text)
	print(link.findNext("a")["href"])
print("---------------------------")

print("nascer do sol:",sunrise.text)
print("por do sol:",sunset.text)
print("---------------------------")

print("Metar:",metar.text)
print("Taf:",taf.text)
