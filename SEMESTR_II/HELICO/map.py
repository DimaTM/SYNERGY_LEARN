import random
from utils import randbool

# Базовые тайлы игрового мира
# 0 - трава (🟩), 1 - дерево (🌲), 2 - река (🟦), 3 - госпиталь (🏥), 4 - магазин (🏪), 5 - огонь (🔥)
CELL_TYPES = ["🟩", "🌲", "🌊", "🏥", "🏪", "🔥"]

TREE_BONUS = 100
UPGRADE_COST = 5000
LIFE_COST = 10000

class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
        self.generate_forest(5, 10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_upgrade_shop()
        self.generate_hospital()
        
    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True
        
    def print_map(self, helico, clouds):
        # Верхняя рамка из черных квадратов
        output = "⬛" * (self.w + 2) + "\n"
        
        for ri in range(self.h):
            output += "⬛" # Левая черная граница
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                sign = CELL_TYPES[cell]
                
                # Погодные условия
                if clouds.cells[ri][ci] == 1:
                    sign = "☁️ "
                elif clouds.cells[ri][ci] == 2:
                    sign = "⚡"
                    
                # Игрок на вертолёте
                if (helico.x == ri and helico.y == ci):
                    sign = "🛸"
                    
                output += sign
            output += "⬛\n" # Правая черная граница
            
        # Нижняя рамка из черных квадратов
        output += "⬛" * (self.w + 2) + "\n"
        print(output, end="")

    def generate_river(self, l):
        rcx = random.randint(0, self.h - 1)
        rcy = random.randint(0, self.w - 1)
        self.cells[rcx][rcy] = 2
        while l > 0:
            drx, dry = random.choice([(-1, 0), (0, 1), (1, 0), (0, -1)])
            if self.check_bounds(rcx + drx, rcy + dry):
                rcx += drx
                rcy += dry
                self.cells[rcx][rcy] = 2
                l -= 1

    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def generate_tree(self):
        c = random.randint(0, self.w - 1)
        r = random.randint(0, self.h - 1)
        if self.cells[r][c] == 0:
            self.cells[r][c] = 1

    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
                elif cell == 1:
                    if randbool(1, 10):
                        self.cells[ri][ci] = 5

    def generate_hospital(self):
        c = random.randint(0, self.w - 1)
        r = random.randint(0, self.h - 1)
        if self.cells[r][c] != 2:
            self.cells[r][c] = 3
        else:
            self.generate_hospital()

    def generate_upgrade_shop(self):
        c = random.randint(0, self.w - 1)
        r = random.randint(0, self.h - 1)
        if self.cells[r][c] != 2 and self.cells[r][c] != 3:
            self.cells[r][c] = 4
        else:
            self.generate_upgrade_shop()

    def process_helicopter(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        if c == 2:
            helico.tank = helico.mxtank
        if c == 5 and helico.tank > 0:
            helico.tank -= 1
            helico.score += TREE_BONUS
            self.cells[helico.x][helico.y] = 1
        if c == 4 and helico.score >= UPGRADE_COST:
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
        if c == 3 and helico.score >= LIFE_COST:
            helico.lives += 10
            helico.score -= LIFE_COST
        if clouds.cells[helico.x][helico.y] == 2:
            helico.lives -= 1
            if helico.lives == 0:
                helico.game_over()

    def export_data(self):
        return {"cells": self.cells}
        
    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]