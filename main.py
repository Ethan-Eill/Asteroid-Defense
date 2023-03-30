import model
import controller
from view import main_menu_view

def main():
    controller.init()
    controller.game_loop()
    #main_menu_view.main_menu()
    print("Now playing ASTEROID DEFENSE")

if __name__ == "__main__":
    main()