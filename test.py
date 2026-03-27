import Geometrie

v1 = Geometrie.Punkt("v1", 0, 0)
v2 = Geometrie.Punkt("v2", 4, 5)
v3 = Geometrie.Punkt("v3", 6, 8)
v4 = Geometrie.Punkt("v4", 10, 10)
v5 = Geometrie.Punkt("v5", 12, 15)
v6 = Geometrie.Punkt("v6", 15, 20)
print(v1.abstand(v2))
print(v2.abstand(v3))
print(v3.abstand(v4))
print(v4.abstand(v5))
print(v5.abstand(v6))
print(v6.abstand(v1))

polygon1 = Geometrie.Polygon("Polygon1", [v1, v2, v3, v4, v5, v6])

print(polygon1.umfang())
print(polygon1)
