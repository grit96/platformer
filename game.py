from graphics import *
import time

def main():
    FPS = 30

    screen = Canvas(size = (40, 40))

    ball = Sprite(
        shapes.Circle(5),
        position = (14, 10)
    )

    screen.sprites.append(ball)

    with NonBlockingInput() as nbi:
        while True:

            if not 0 in ball.edge(screen):
                ball.move(0)

            ch = nbi.char()

            if ch == '.':
                if not 3 in ball.edge(screen):
                    ball.move(3)
            if ch == ',':
                if not 1 in ball.edge(screen):
                    ball.move(1)
            if ch == ' ':
                ball.position[1] = 10

            print(screen)

            time.sleep(1/FPS)

if __name__ == '__main__':
    main()