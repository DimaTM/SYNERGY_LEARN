class Helicopter:
    def __init__(self, w, h):
        self.x = 0
        self.y = 0
        self.h = h
        self.w = w
        self.mxtank = 1
        self.tank = 0
        self.score = 0
        self.lives = 20
        
    def move(self, dx, dy):
        nx, ny = self.x + dx, self.y + dy
        if (nx >= 0 and nx < self.h and ny >= 0 and ny < self.w):
            self.x = nx
            self.y = ny
            
    def print_stats(self):
        print("💧 ", self.tank, "/", self.mxtank, sep="", end=" | ")
        print("🏆 ", self.score, sep="", end=" | ")
        print("❤️ ", self.lives, sep="")
        
    def game_over(self):
        print("\033[H\033[J", end="")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                            X")
        print("X  GAME OVER, YOU LOSE! 😭  X")
        print("X                            X")
        print("X  YOUR SCORE:", self.score, " " * (13 - len(str(self.score))), "X")
        print("X                            X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        exit()
        
    def export_data(self):
        return {
            "score": self.score,
            "lives": self.lives,
            "x": self.x, "y": self.y,
            "tank": self.tank, "mxtank": self.mxtank
        }
        
    def import_data(self, data):
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank = data["tank"] or 0
        self.mxtank = data["mxtank"] or 1
        self.lives = data["lives"] or 20
        self.score = data["score"] or 0