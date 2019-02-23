##########################################
##              31.01.2019              ##
##            Black Jack                ##
##          Adam Palęga                 ##
##########################################

import random
import matplotlib.pyplot as plt
import os

##########################################
##                                      ##
## DWIE KLASY TWORZACE KARTE ORAZ TALIE ##
##                                      ##
##########################################

class Playing_Card():
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

class Deck():
    deck = []

    def __init__(self):
        self.create_deck()

    def create_deck(self):
        '''Funkcja tworzy talie
        
        Funkcja tworzy talie skladajaca sie z obiektow klasy Playing_Card.
        Obiekty sa dodawane do listy deck
        '''
        for s in ["Hearths", "Clubs","Diaomonds", "Spades"]:
            for v in ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]:
                self.deck.append(Playing_Card(v,s))
    def show_card(self,number):
        '''Pokazuje karte

        Funkcja pokazuje wartosc karty oraz jej kolor pod wskazanym numerem(0-51)
        '''
        return (self.deck[number].value + " of " + self.deck[number].suit)
    def shuffle_deck(self):
        #tasuje liste w ktorej znajduje sie talia
        random.shuffle(self.deck)

##################################################################################################
##  FUNKCJE ORAZ ZMIENNE DLA BLACK JACKA  ##
############################################
talia = Deck()
money = 0
points_d = 0
points_p = 0
bet = 0
current_card = 51
win_d = 0
win_p = 0


def value_for_black_jack(card):
    '''Podaje wartosci dla karty

    Funkcja podaje wartosc dla kazdej karty zgodnie z zasadami
    black jacka.
    dla kart:
    (2-10) - zgodnie z wartoscia 
    (J-K) - 10
    A - do wyboru 1 lub 11
    '''
    numbers = ["2","3","4","5","6","7","8","9","10"]
    faces = ["J","Q","K"]
    ace = "A"
    
    if card in numbers:
        return int(card)
    elif card in faces:
        return 10
    elif card == ace:
        wartosc = input("masz Asa wybierz 1 lub 11\n")
        return int(wartosc)


def value_for_black_jack_d(card,points):
    '''Podaje wartosci dla karty

    Funkcja podaje wartosc dla kazdej karty zgodnie z zasadami
    black jacka.
    dla kart:
    (2-10) - zgodnie z wartoscia 
    (J-K) - 10
    A - do wyboru 1 lub 11
    '''
    numbers = ["2","3","4","5","6","7","8","9","10"]
    faces = ["J","Q","K"]
    ace = "A"
    
    if card in numbers:
        return int(card)
    elif card in faces:
        return 10
    elif card == ace:
        if points <= 10:
            return 11
        else:
            return 1



def save_stats_to_file(plik,s_p,s_d,m):
    """zapisywanie statystyk do pliku

    funkcja ma za zadanie zapisania w dwoch kolmunach
    danej s_p oraz s_d 
    """
    s_p = str(s_p)
    s_d = str(s_d)
    m = str(m)
    with open(plik,"a") as f:
        f.write("{} {} {} \n".format(s_p,s_d,m))
#
     

#####################################################################################################
### WSTEP ###
#############




money = int(input("Witam w moim kasynie\n podaj sume pieniedzy za jaka chcesz zagrac\n"))
bet = int(input("podaj wysokosc zakladu o jaki chcesz zagrac \n"))





#####################################################################################################
### GRA ###
###########

while True:
    if money > 0:
        print("Jezeli:\n -chcesz zagrac  wcisnij 1\n-chcesz zmienic zaklad wcisnij 2\n-jeżeli chcesz sprawdzic statystyki wcisnij 3\n-jezelichcesz wyjsc  wcisnij 4")
        
        decision = int(input())
        choice = 0

        if decision == 1: #wlasciwa gra

            
            talia.shuffle_deck()
            current_card = 51
            print("posiadasz {} $ \n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$".format(money))


            points_d = points_d + value_for_black_jack_d(talia.deck[current_card].value,points_d)
            print("karta dealera to: \n {} pkt: {}: \n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$".format(talia.show_card(current_card),points_d))
            current_card = current_card - 1
            
            

            points_p = value_for_black_jack(talia.deck[current_card].value) + value_for_black_jack(talia.deck[current_card -1].value)
            print("twoje karty to:\n {}\n {} \n pkt: {}\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$".format(talia.show_card(current_card),talia.show_card(current_card -1),points_p))
            current_card = current_card - 2
            
            double = int(input("DOUBLE TAK-1/NIE-2"))
            
            if double == 1:
                bet = bet * 2

            if points_p == 21:
                print("BLACK JACK!!!")
                win_p = 1
                money = money + 2*bet
                save_stats_to_file("stat.txt",win_p,win_d,money)
                points_d = 0
                points_p = 0
                win_d = 0
                win_p = 0 
            else:
                while points_p <= 21:
                    choice = 0
                    print("dobierz-1/stop-2")
                    choice = int(input())
                    
                    if choice == 1:
                        points_p = points_p + value_for_black_jack(talia.deck[current_card].value)
                        print("dobrana karta to:\n{}\n pkt:{}\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$".format(talia.show_card(current_card),points_p))
                        current_card = current_card - 1
                    if choice == 2:
                        break
                
                if points_p > 21:
                    print("niestety przegrales ( ͡° ʖ̯ ͡°)")
                    win_d = 1
                    money = money - bet
                    save_stats_to_file("stat.txt",win_p,win_d,money)
                    points_d = 0
                    points_p = 0
                    win_d = 0
                    win_p = 0
                    
                elif points_p <= 21:
                    while points_d < 17:
                        points_d = points_d + value_for_black_jack_d(talia.deck[current_card].value,points_d)
                        print("karta dealera to:\n{}\n pkt:{}\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$".format(talia.show_card(current_card),points_d))
                        current_card = current_card - 1
                    if points_d > 21:
                        print("WYGRALES ( ͡° ͜ʖ ͡°)")
                        win_p = 1
                        money = money + bet
                        save_stats_to_file("stat.txt",win_p,win_d,money)
                        points_d = 0
                        points_p = 0
                        win_d = 0
                        win_p = 0
                        
                    elif points_d < points_p:
                        print("WYGRALES ( ͡° ͜ʖ ͡°)")
                        win_p = 1
                        money = money + bet
                        save_stats_to_file("stat.txt",win_p,win_d,money)
                        points_d = 0
                        points_p = 0
                        win_d = 0
                        win_p = 0
                        
                    elif points_d > points_p:
                        print("niestety przegrales ( ͡° ʖ̯ ͡°)")
                        win_d = 1
                        money = money - bet
                        save_stats_to_file("stat.txt",win_p,win_d,money)
                        points_d = 0
                        points_p = 0
                        win_d = 0
                        win_p = 0
                        
                    elif points_p == points_d:
                        print("nikt nie wygral")
                        points_d = 0
                        points_p = 0
                        win_d = 0
                        win_p = 0
                        money = money
                        save_stats_to_file("stat.txt",win_p,win_d,money)
    
            print("posiadasz {} $ \n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$".format(money))
                        
        if decision == 2:
            wprowadzony_bet = int(input("podaj stawke:"))
            if wprowadzony_bet > 0 and wprowadzony_bet <= money:
                bet = wprowadzony_bet
            else:
                print("Stawka musi być większa od 0 oraz mniejszy lub rowny od twojego stanu konta ")
        if decision == 3:
            print(" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ \n Twoj stan konta to:{} \n Aktualna stawka to:{}\n $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$".format(money,bet))
            with open("stat.txt","r") as staty:
                player_stat = []
                dealer_stat = []
                player_money = []
                for i in staty:
                    stata = i.split()
                    player_stat.append(int(stata[0]))
                    dealer_stat.append(int(stata[1]))
                    player_money.append(int(stata[2]))
            
            player_money_times = range(len(player_money))
            
            player_won = [x for x in player_stat if x > 0]
            dealer_won = [y for y in dealer_stat if y > 0]
            
            times = []
            
            times.append(len(player_won))
            times.append(len(dealer_won))
            plt.subplot(2,2,1)
            plt.bar(range(2),times)
            plt.ylabel("wgranych razy")
            plt.title("ilosc wygranych")
            plt.subplot(2,2,2)
            plt.title("zagranych razy/ilosci pieniedzy")
            plt.xlabel("zagranych razy")
            plt.ylabel("pieniadze")
            plt.plot(player_money_times,player_money)
            
            plt.show()
        if decision == 4:
            os.remove("stat.txt")
            break
    else:
        print("nie masz pieniedzy \n KONIEC GRY")
        os.remove("stat.txt")
        break
    


            
#####################################################################################################
#talia = Deck()

#talia.shuffle_deck()

#print(talia.show_card(51))

#print(talia.deck[51].value,talia.deck[51].suit)

#print(value_for_black_jack(talia.deck[51].value))

#print(player.money)

####################################################################################################

