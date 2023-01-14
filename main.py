import random
import time


def dealer_hand():

    hand = random.randint(2, 11)
    return hand


def user_hand():

    hand = random.randint(11, 21)
    return hand


def hit_or_stand(feedback, user):

    if feedback == 'H':
        user += random.randint(2, 11)

    elif feedback == 'S':
        user += 0

    return user


def display_hands(user, dealer):

    print("\nDealer's hand: " + str(dealer))
    print("Your hand: " + str(user))


def main():

    play_again = 'y'
    while play_again == 'y':

        dealer = dealer_hand()
        user = user_hand()

        end = False
        while not end:

            display_hands(user, dealer)

            if user == 21:
                end = True
                print("\nYOU WIN!")

            else:
                feedback = input("\nEnter 'H' to hit and 'S' to stand: ").upper()
                user = hit_or_stand(feedback, user)
                time.sleep(0.5)

                if feedback == 'S':

                    while dealer < 21 and dealer <= user:
                        dealer += random.randint(2, 11)
                        display_hands(user, dealer)
                        time.sleep(2)

                    if user > dealer or dealer > 21:
                        end = True
                        print("\nYOU WIN!")

                    elif dealer > user:
                        end = True
                        print("\nYOU LOSE!")

                if user > 21:
                    display_hands(user, dealer)
                    end = True
                    print("\nBUST! YOU LOSE!")

        time.sleep(2)
        play_again = input("\nEnter 'y' to play again: ").lower()


if __name__ == "__main__":
    main()
