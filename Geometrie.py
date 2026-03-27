class Figur:
    def __init__(self):
        self.name = "Figur"

    def umfang(self):
        return 0

    def __str__(self):
        return self.name


class Punkt:
    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y

    def abstand(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

    def __str__(self):
        return f"{self.name}: ({self.x}, {self.y})"


class Kreis(Figur):
    def __init__(self, name: str, mittelpunkt: Punkt, radius: float):
        super().__init__()
        self.name = name
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def umfang(self):
        return 2 * 3.14159 * self.radius

    def __str__(self):
        return f"{self.name}: Mittelpunkt {self.mittelpunkt}, Radius {self.radius}"


class Dreieck(Figur):
    def __init__(self, name: str, p1: Punkt, p2: Punkt, p3: Punkt):
        super().__init__()
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):
        return f"{self.name}: {self.p1}, {self.p2}, {self.p3}"

    def umfang(self):
        return (
            self.p1.abstand(self.p2)
            + self.p2.abstand(self.p3)
            + self.p3.abstand(self.p1)
        )


class Rechteck(
    Figur
):  # Diese Klasse behandelt gemäss Aufgabenstellung Rechtecke dessen Seiten parallel zu den Koordinatenachsen sind. Für andere Vierecke ist die Klasse Polygon zu verwenden.
    def __init__(self, name: str, stützpunkt: Punkt, länge: float, breite: float):
        super().__init__()
        self.name = name
        self.stützpunkt = stützpunkt
        self.länge = länge
        self.breite = breite

    def umfang(self):
        return 2 * (self.länge + self.breite)

    def __str__(self):
        return f"{self.name}: Stützpunkt {self.stützpunkt}, Länge {self.länge}, Breite {self.breite}"


class Polygon(Figur):
    def __init__(self, name: str, punkte: list):
        super().__init__()
        self.name = name
        self.punkte = punkte

    def __str__(self):
        return f"{self.name}: {[str(p) for p in self.punkte]}"

    def umfang(self):

        abstandsliste = []

        for i in range(len(self.punkte)):
            if i == len(self.punkte) - 1:
                abstandsliste.append(self.punkte[-1].abstand(self.punkte[0]))

            else:
                abstandsliste.append(self.punkte[i].abstand(self.punkte[i + 1]))

        return (abstandsliste, sum(abstandsliste))
