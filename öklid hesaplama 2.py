import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaların listesi
points = [(1, 2), (4, 6), (7, 1), (3, 3), (5, 5)]

# Mesafelerin saklanacağı liste
distances = []

# Tüm nokta çiftleri arasındaki mesafeleri hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bul
min_distance = min(distances)

print("Tüm nokta çiftleri arasındaki mesafeler:", distances)
print("Minimum mesafe:", min_distance)
