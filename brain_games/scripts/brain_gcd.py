#!/usr/bin/env python
from brain_games.core import game_generate
from brain_games.games import gcd


def main():
    game_generate(gcd)


if __name__ == '__main__':
    main()
