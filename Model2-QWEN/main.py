import tkinter as tk
import random

class RunnerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Endless Runner - Qwen Lab")
        self.canvas = tk.Canvas(root, width=600, height=300, bg="sky blue")
        self.canvas.pack()

        self.player_y = 220
        self.player_velocity = 0
        self.is_jumping = False
        self.score = 0
        self.game_over = False

        self.canvas.create_rectangle(0, 250, 600, 300, fill="dark green")
        self.player = self.canvas.create_rectangle(50, self.player_y, 80, 250, fill="red")
        
        self.obstacle_x = 600
        self.obstacle = self.canvas.create_rectangle(self.obstacle_x, 220, self.obstacle_x + 20, 250, fill="black")
        self.score_text = self.canvas.create_text(50, 30, text=f"Score: {self.score}", font=("Arial", 14), fill="black")

        self.root.bind("<space>", self.jump)
        self.update_game()

    def jump(self, event):
        if not self.is_jumping and not self.game_over:
            self.player_velocity = -12
            self.is_jumping = True

    def update_game(self):
        if self.game_over:
            return

        if self.is_jumping:
            self.player_y += self.player_velocity
            self.player_velocity += 0.8
            if self.player_y >= 220:
                self.player_y = 220
                self.is_jumping = False
            self.canvas.coords(self.player, 50, self.player_y, 80, 250)

        self.obstacle_x -= 7
        if self.obstacle_x < -20:
            self.obstacle_x = 600
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
        self.canvas.coords(self.obstacle, self.obstacle_x, 220, self.obstacle_x + 20, 250)

        p_coords = self.canvas.coords(self.player)
        o_coords = self.canvas.coords(self.obstacle)

        if p_coords[2] >= o_coords[0] and p_coords[0] <= o_coords[2]:
            if p_coords[3] >= o_coords[1]:
                self.game_over = True
                self.canvas.create_text(300, 150, text="GAME OVER", fill="red", font=("Arial", 24, "bold"))
                return

        self.root.after(20, self.update_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = RunnerGame(root)
    root.mainloop()
