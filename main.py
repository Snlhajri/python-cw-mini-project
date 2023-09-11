# write your code here
def padel_court_cost(court_tybe):
    if court_tybe == "indoor":
        return 30
    elif court_tybe == "outdoor":
       return 20

def rackets_cost (racket_brand) :
    if racket_brand == "bullpadel":
        return 100
    elif racket_brand == "nox":
        return 140
    elif racket_brand == "siux":
        return 200
    

def padel_balls_cost(ball_boxes):
    if  ball_boxes == 1 :
        return 2
    elif ball_boxes  ==2 :
        return 3.5
    if ball_boxes == 3 :
        return 5
    
def padel_game_cost():
    court_tybe = input("enter court tybe: ") 
    racket_brand = input("enter racket brand: ")
    ball_boxes = int(input("enter number of ball boxes: "))
    total= padel_court_cost(court_tybe)+rackets_cost(racket_brand) +padel_balls_cost(ball_boxes)
    return total
print(f"total cost {padel_game_cost()}")



