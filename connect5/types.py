import enum
from collections import namedtuple

BLACK = 1
WHITE = 2

class Player(enum.Enum):
  black = BLACK
  white = WHITE

  @property
  def other(self) -> self:
    return Player.black if self == Player.white else Player.white

class Point(namedtuple('Point', 'row col')):
  def neighbors(self) -> [Point] * 4:
    return [
      Point(self.row - 1, self.col),
      Point(self.row + 1, self.col),
      Point(self.row, self.col - 1),
      Point(self.row, self.col + 1),
    ]

class Direction(enum.Enum):
  right = 1
  down = 2
  right_down = 3
  left_down = 4
