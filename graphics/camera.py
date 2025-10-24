import math

from matrices.quaternion import matrix, multiply, normalize

class Camera:
    def __init__(self, x=0, y=0, z=0,focalLength = 289, speed = 0.1):
        self.x = x
        self.y = y
        self.z = z

        # Identity quaternion (no rotation)
        self.quat = [1, 0, 0, 0]  # [w, x, y, z]

        self.focalLength = focalLength
        self.speed = speed

    def set(self, position):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
    
    def move(self, movement, R):
        # Movement relative to camera orientation
        self.x += (R[0][0] * self.speed * movement[0]) + (R[0][1] * self.speed * movement[1]) + (R[0][2] * self.speed * movement[2])
        self.y += (R[1][0] * self.speed * movement[0]) + (R[1][1] * self.speed * movement[1]) + (R[1][2] * self.speed * movement[2])
        self.z += (R[2][0] * self.speed * movement[0]) + (R[2][1] * self.speed * movement[1]) + (R[2][2] * self.speed * movement[2])

    def rotate(self, deltaAngleDegrees, axis, R): # https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
        # Rotation relative to camera orientation

        # Transform world space axis to camera space axis by multiplying with the rotation matrix
        cameraAxis = [
            R[0][0] * axis[0] + R[0][1] * axis[1] + R[0][2] * axis[2],
            R[1][0] * axis[0] + R[1][1] * axis[1] + R[1][2] * axis[2],
            R[2][0] * axis[0] + R[2][1] * axis[1] + R[2][2] * axis[2]
        ]

        deltaAngle = math.radians(deltaAngleDegrees) / 2
        deltaQ = [
            math.cos(deltaAngle),
            cameraAxis[0] * math.sin(deltaAngle),
            cameraAxis[1] * math.sin(deltaAngle),
            cameraAxis[2] * math.sin(deltaAngle)]

        self.quat = normalize(multiply(self.quat, deltaQ))

    def matrix(self):
        return matrix(self.quat)