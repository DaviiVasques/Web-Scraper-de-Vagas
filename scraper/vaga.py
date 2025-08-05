class Vaga:
    def __init__(self, titulo, empresa, localizacao, link):
        self.titulo = titulo
        self.empresa = empresa
        self.localizacao = localizacao
        self.link = link

    def to_list(self):
        return [self.titulo, self.empresa, self.localizacao, self.link]

    def __str__(self):
        return f"{self.titulo} | {self.empresa} | {self.localizacao} | {self.link}"