#!/usr/bin/env python
from brain_games.core import game_generate
from brain_games.games import calc


def main():
    game_generate(calc)


if __name__ == '__main__':
    main()
