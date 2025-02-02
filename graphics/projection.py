from graphics.camera import Camera as Cam
from matrices.matrix import transpose

class Projection:
    def __init__(self):
        self.cam = Cam()
        self.R = [[1,0,0],[0,1,0],[0,0,1]]
        self.R_inv = transpose(self.R)
        self.updateR()

    def project(self, point):
        P1x = point[0] - self.cam.x
        P1y = point[1] - self.cam.y
        P1z = point[2] - self.cam.z
        #UpdateR()
        P2x = (self.R_inv[0][0]*P1x) + (self.R_inv[0][1]*P1y) + (self.R_inv[0][2]*P1z)
        P2y = (self.R_inv[1][0]*P1x) + (self.R_inv[1][1]*P1y) + (self.R_inv[1][2]*P1z)
        P2z = (self.R_inv[2][0]*P1x) + (self.R_inv[2][1]*P1y) + (self.R_inv[2][2]*P1z)
        if P2z > 0:
            return self.cam.focalLength * P2x / P2z, self.cam.focalLength * P2y / P2z
        else:
            return None

    def updateR(self):
        self.R = self.cam.matrix()
        self.R_inv = transpose(self.R)