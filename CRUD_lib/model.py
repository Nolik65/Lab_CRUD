import requests
from bs4 import BeautifulSoup
import re


users: list = []


class User:
    def __init__(self, imie: str, nazwisko: str, posty: int, lokalizacja: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.posty = posty
        self.lokalizacja = lokalizacja
        self.coordinates = self.get_coordinates()
        self.marker = None

    def convert_coordinate(self, coordinate: str) -> float:
        coordinate = coordinate.strip().replace(",", ".")

        try:
            return float(coordinate)
        except ValueError:
            pass

        pattern = r"(\d+(?:\.\d+)?)°\s*(\d+(?:\.\d+)?)?[′']?\s*(\d+(?:\.\d+)?)?[″\"]?\s*([NSEW])"
        match = re.match(pattern, coordinate)

        if not match:
            raise ValueError(f"Nie można odczytać współrzędnej: {coordinate}")

        degrees = float(match.group(1))
        minutes = float(match.group(2) or 0)
        seconds = float(match.group(3) or 0)
        direction = match.group(4)

        decimal = degrees + minutes / 60 + seconds / 3600

        if direction in ["S", "W"]:
            decimal = -decimal

        return decimal

    def get_coordinates(self) -> list:
        url = f"https://pl.wikipedia.org/wiki/{self.lokalizacja}"

        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        response_html = BeautifulSoup(response.text, "html.parser")

        latitude_text = response_html.select(".latitude")[0].text
        longitude_text = response_html.select(".longitude")[0].text

        latitude = self.convert_coordinate(latitude_text)
        longitude = self.convert_coordinate(longitude_text)

        return [latitude, longitude]
