import arcade
import random
from app_objects import Tank, Enemy

# definicion de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Tank"

SPEED = 10


def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.rot_speed = 0.5
        self.speed = 10
        self.tanks = [
            Tank(200, 400, get_random_color()),
            Tank(400, 400, get_random_color())
        ]
        self.enemies = [
            Enemy(
                random.randrange(0, SCREEN_WIDTH),
                random.randrange(0, SCREEN_HEIGHT),
                random.randrange(10, 50)
            )
            for _ in range(10)
        ]

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.tanks[0].shoot(20)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.tanks[0].speed = SPEED
        if symbol == arcade.key.DOWN:
            self.tanks[0].speed = -SPEED

        if symbol == arcade.key.LEFT:
            self.tanks[0].angular_speed = 1.5
        if symbol == arcade.key.RIGHT:
            self.tanks[0].angular_speed = -1.5

        if symbol == arcade.key.W:
            self.tanks[1].speed = SPEED
        if symbol == arcade.key.S:
            self.tanks[1].speed = -SPEED

        if symbol == arcade.key.A:
            self.tanks[1].angular_speed = 1.5
        if symbol == arcade.key.D:
            self.tanks[1].angular_speed = -1.5

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.tanks[0].speed = 0

        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.tanks[0].angular_speed = 0

        if symbol in (arcade.key.W, arcade.key.S):
            self.tanks[1].speed = 0

        if symbol in (arcade.key.A, arcade.key.D):
            self.tanks[1].angular_speed = 0

        if symbol == arcade.key.SPACE:
            self.tanks[1].shoot(20)

    def on_update(self, delta_time: float):
        self.tanks[0].detect_collision(self.tanks[1])
        self.tanks[1].detect_collision(self.tanks[0])
        for t in self.tanks:
            t.update(delta_time)
        for e in self.enemies:
            e.detect_collision(self.tanks[0])
            e.detect_collision(self.tanks[1])

    def on_draw(self):
        arcade.start_render()
        i = 1
        for t in self.tanks:
            arcade.draw_text(f'Tank {i}: {t.life}', 0, 200 * i)
            t.draw()
            i += 1
        for e in self.enemies:
            e.draw()


if __name__ == "__main__":
    app = App()
    arcade.run()
