import math

class Vector2:
    def __init__(self, x: float | int = 0.0, y: float | int = 0.0) -> None:
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        return Vector2(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        return Vector2(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, Vector2):  # element-wise multiplication
            return Vector2(self.x * other.x, self.y * other.y)
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        return Vector2(self.x / other, self.y / other)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __iadd__(self, other):
        self.x += other.x if isinstance(other, Vector2) else other
        self.y += other.y if isinstance(other, Vector2) else other
        return self

    def __isub__(self, other):
        self.x -= other.x if isinstance(other, Vector2) else other
        self.y -= other.y if isinstance(other, Vector2) else other
        return self

    def __imul__(self, other):
        self.x *= other.x if isinstance(other, Vector2) else other
        self.y *= other.y if isinstance(other, Vector2) else other
        return self

    def __itruediv__(self, other):
        self.x /= other.x if isinstance(other, Vector2) else other
        self.y /= other.y if isinstance(other, Vector2) else other
        return self

    def __eq__(self, other):
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def magnitude(self) -> float:
        return math.hypot(self.x, self.y)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2(0, 0)
        return self / mag

    def distance_to(self, other) -> float:
        return (self - other).magnitude()
    
    def fast_distance_to(self, other) -> float:
        """
        Removing sqrt() based functions make calculations much faster!
        Returns square distance instead...
        """
        return ((self.x*other.x)**2) - ((self.y-other.y)**2)

    def angle_to(self, other) -> float:
        dot = self.dot(other)
        mag = self.magnitude() * other.magnitude()
        if mag == 0:
            return 0.0
        return math.degrees(math.acos(dot / mag))

    def perpendicular(self):
        """Return a vector perpendicular to this one (rotated 90 degrees CCW)."""
        return Vector2(-self.y, self.x)

    def tuple(self) -> tuple:
        return (self.x, self.y)
    
    def get(self):
        return Vector2(self.x, self.y)
    
    def set(self, x: float | int, y: float | int) -> None:
        self.x = x
        self.y = y

    def get_x(self) -> float | int:
        return self.x
    
    def get_y(self) -> float | int:
        return self.y
    
    def set_x(self, value: float | int) -> None:
        self.x = value
    
    def set_y(self, value: float | int) -> None:
        self.y = value

    def round(self, decimals: int | None = None):
        return Vector2(round(self.x, decimals), round(self.y, decimals))

def lerp(a, b, t):
    return a + t * (b - a)