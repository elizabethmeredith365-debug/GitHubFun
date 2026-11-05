class Player:
  
    def __init__(self, name, hand = None):
            self.name = name
            self.hand = [] if hand is None else hand

    def draw_card(self):
        if self.hand:
            return self.hand.pop(0)
        return None

    def  add_cards(self, cards):
        self.hand.extend(cards)

    def count_cards(self): 
          return len (self.hand) 

    def has_cards(self):
          return self.count_cards() > 0 
    
                
 
    
    