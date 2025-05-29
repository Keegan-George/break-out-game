from game_manager import GameManager


screen, paddle, ball, brick_factory, scoreboard = GameManager.initialize_game()
GameManager.start_game(screen, paddle, ball, brick_factory, scoreboard)
