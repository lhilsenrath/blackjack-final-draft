from flask_session import Session
import random
from flask import Flask, render_template, request, redirect

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4

@app.route("/", methods=["GET", "POST"])
def index():
    # go to playing page if play button is pushed
    if request.method == "POST":
        return redirect("/game")
    else:
        return render_template("index.html")

@app.route("/game", methods=["GET", "POST"])
def game():
    # if "deal" button is pushed
    if request.method == "POST":
        return redirect("/playing")
    else:
        return render_template("game.html")

@app.route("/playing", methods=["GET", "POST"])
def playing():
    # input blackjack stuff here?
    if request.method == "POST":
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4

        def player_deal(cards):
            playerhand = []
            for i in range(2):
                random.shuffle(cards)
                card = cards.pop()
                if card == 'J': 
                    card = 10
                if card == 'Q': 
                    card = 10
                if card == 'K': 
                    card = 10
                if card == 'A': 
                    card = 11
                playerhand.append(card)

        def dealer_deal(cards):
            dealerhand = []
            for i in range(2):
                random.shuffle(cards)
                card = cards.pop()
                if card == 'J': 
                    card = 10
                if card == 'Q': 
                    card = 10
                if card == 'K': 
                    card = 10
                if card == 'A': 
                    card = 11
                dealerhand.append(card)

        def hands(playerhand, dealerhand):
            if dealer_deal:
                print("Your cards: ", playerhand, " (total: )", sum(playerhand))
            if player_deal:
                print("Dealer's cards: X ", dealerhand[1], " (total: )", sum(dealerhand))

        def move(playerhand, dealerhand):
            while sum(playerhand) < 21:
                move = str(input("hit or stay? ").lower)
                if move == "hit":
                    newcard = cards.pop()
                    playerhand.append(newcard)
                    hands(playerhand, dealerhand)
                    if sum(dealerhand) >= 17:
                        print("Dealer stays.")
                        hands(dealerhand)
                    else:
                        print("Dealer hits!")
                        dealerhand.append(newcard)
                        hands(dealerhand)
                elif move == "stay":
                    hands(playerhand, dealerhand)
                    if sum(dealerhand) >= 17:
                        print("Dealer stays.")
                        hands(dealerhand)
                    else:
                        print("Dealer hits!")
                        dealerhand.append(newcard)
                        hands(dealerhand)

        def end(playerhand, dealerhand):
            while move == "stay" or "hit":
                if sum(playerhand) > sum(dealerhand):
                    print("You Win!")
                elif sum(dealerhand) > sum(playerhand):
                    print("Game Over. You Lose.")
                elif sum(dealerhand) == sum(playerhand):
                    print("It's a tie!")
                elif sum(dealerhand) > 21:
                    print("You Win! Dealer Busts!")
                elif sum(playerhand) > 21:
                    print("You Bust! You Lose.")
                elif sum(dealerhand) == 21 and sum(playerhand) < 21:
                    print("Game Over. You Lose.")
                return end == True
        if end == True:
            return redirect("/game")
        if request.form.get("Home"):
            return redirect("/")
    else: 
        return render_template("playing.html")