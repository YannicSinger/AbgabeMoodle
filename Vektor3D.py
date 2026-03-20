class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"x:{self.x}, y:{self.y}, z:{self.z}"

    def __add__(self, weiterer):
        if type(weiterer) == Vector3:
            return Vector3(
                self.x + weiterer.x, self.y + weiterer.y, self.z + weiterer.z
            )
        if type(weiterer) == float or type(weiterer) == int:
            return Vector3(self.x + weiterer, self.y + weiterer, self.z + weiterer)
        else:
            return TypeError

    def __radd__(self, weiterer):
        return Vector3(self.x + weiterer, self.y + weiterer, self.z + weiterer)

    def __sub__(self, weiterer):
        if type(weiterer) == Vector3:
            return Vector3(
                self.x - weiterer.x, self.y - weiterer.y, self.z - weiterer.z
            )
        if type(weiterer) == float or type(weiterer) == int:
            return Vector3(self.x - weiterer, self.y - weiterer, self.z - weiterer)
        else:
            return TypeError

    def __rsub__(self, weiterer):
        return Vector3(self.x - weiterer, self.y - weiterer, self.z - weiterer)

    def __mul__(self, weiterer):
        if type(weiterer) == Vector3:
            return Vector3(
                self.x * weiterer.x, self.y * weiterer.y, self.z * weiterer.z
            )
        if type(weiterer) == float or type(weiterer) == int:
            return Vector3(self.x * weiterer, self.y * weiterer, self.z * weiterer)
        else:
            return TypeError

    def __rmul__(self, weiterer):
        return Vector3(self.x * weiterer, self.y * weiterer, self.z * weiterer)

    def cross(self, weiterer):
        return Vector3(
            self.y * weiterer.z - self.z * weiterer.y,
            self.z * weiterer.x - self.x * weiterer.z,
            self.x * weiterer.y - self.y * weiterer.x,
        )

    def dot(self, weiterer):
        return float(self.x * weiterer.x + self.y * weiterer.y + self.z * weiterer.z)

    def normalize(self):
        a = (self.x**2 + self.y**2 + self.z**2) ** -0.5
        return a * self
