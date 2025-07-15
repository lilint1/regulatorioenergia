import requests
import re

class BaseRegex():
    def __init__(self, html: str):
        self.html = html

    @abstractmethod
    def extrair(self) -> list[dict]:
        """
        Deve retornar uma lista de dicionários,
        cada um com 'titulo', 'tema', 'link', 'fonte'
        """

    def extrair_titulo(self, pattern: str, tema: str, fonte: str) -> list[dict]:
        resultado = []
        match = re.findall(pattern)


class Aneel(BaseRegex):
    def extract(self) -> list[dict]:
        pattern = r'<(h[1-2])[^>]*>(.*?)<\/(h[1-2])>'
        return self.extrair_titulo(pattern, tema = 'Energia Elétrica', fonte = 'ANEEL')
    

class Aneel(BaseRegex):
    def extract(self) -> list[dict]:
        pattern = r'<(h[1-2])[^>]*>(.*?)<\/(h[1-2])>'
        return self.extrair_titulo(pattern, tema = 'Energia Elétrica', fonte = 'EPE')