import model
import controller
import view

def main():
    controller.init()
    #controller.game_loop()
    view.main_menu()
    print("Now playing ASTEROID DEFENSE")

if __name__ == "__main__":
    main()