# balloon_manager.py

# BalloonMgr class

from pygame.locals import *
from balloon import *


# BalloonMgr manages a list of Balloon objects
class BalloonMgr:

    def __init__(self, window: pygame.Surface, max_width: int, max_height: int) -> None:
        self.window: pygame.Surface = window
        self.max_width: int = max_width
        self.max_height: int = max_height
        self.balloon_list: list = []
        self.n_popped: int = 0
        self.n_missed: int = 0
        self.score: int = 0


    def start(self) -> None:
        self.balloon_list = []
        self.n_popped = 0
        self.n_missed = 0
        self.score = 0

        for balloon_num in range(N_BALLOONS):
            random_balloon_class = random.choice((BalloonSmall, BalloonMedium, BalloonLarge, MegaBalloon))

            o_balloon = random_balloon_class(self.window, self.max_width, self.max_height, balloon_num)

            self.balloon_list.append(o_balloon)

    def handle_event(self, event) -> None:
        if event.type == MOUSEBUTTONDOWN:
            # Go "reversed" so top-most balloon gets popped
            for o_balloon in reversed(self.balloon_list):
                was_hit: bool
                n_points: int
                was_hit, n_points = o_balloon.clicked_inside(event.pos)

                if was_hit:
                    if n_points > 0:    # remove this balloon
                        self.balloon_list.remove(o_balloon)
                        self.n_popped += 1
                        self.score += n_points

                    return

    def update(self) -> None:
        for o_balloon in self.balloon_list:
            status: str = o_balloon.update()

            if status == BALLOON_MISSED:
                # Balloon went off the top, remove it
                self.balloon_list.remove(o_balloon)
                self.n_missed += 1

    def get_score(self) -> int:
        return self.score

    def get_count_popped(self) -> int:
        return self.n_popped

    def get_count_missed(self) -> int:
        return self.n_missed

    def draw(self):
        for o_balloon in self.balloon_list:
            o_balloon.draw()
