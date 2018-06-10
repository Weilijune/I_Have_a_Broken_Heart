# -*- coding: utf-8 -*-
from agent import Agent
from card import ALL_CARDS


class MyAgent(Agent):
    '''
    You have to decide which card to play in this round.
    cards_you_have: list of cards in your hand
    cards_played: cards that has been played this round
    heart_broken: heart is broken or not
    info: score information and cards played in previous rounds
    '''
    def play(self, cards_you_have, cards_played, heart_broken, info):
                self.cards_you_have = cards_you_have
        self.cards_played = cards_played
        self.heart_broken = heart_broken
        self.info = info
        legal = get_legal_moves(cards_you_have, cards_played, heart_broken)

        if cards_played:
            suit = cards_played[0].suit
            other = {card.suit: card.number for card in cards_played if card.suit == suit}
            #mycard = {card.suit: card.number for card in cards_you_have if card.suit == suit}
            mycard = [card.number for card in cards_you_have if card.suit == suit]
            havesuit = []
            blacktwelve = ['♠12']
            blackthirteen = ['♠13']


            for card in cards_you_have:
                if card.suit == suit:
                    havesuit.append(card)

            if not havesuit:
                cards_heart = [card for card in cards_you_have if card.suit == "♥"]
                for card in cards_you_have:
                    if card.suit == '♠' and card.number == 12:
                        return blacktwelve
                    else:
                        return ('♥',max(cards_heart))
            #for othercard in cards_played:if othercard.suit == suit:num = int(othercard[1:])played_num.append(num)
            else:      
                if suit == '♠':
                    for num in mycard:
                        if num > 12:
                            littleblack = mycard.remove(num)
                for card in legal:
                    if card.suit == suit:
                    #mynum = [mycard.values()]不知道可不可以這樣用
                        for othercard in cards_played:
                            if othercard.point > 0:
                                for num in mycard:
                                    if num > max(played_num):
                                        mycard.remove(num)
                                        return (suit, max(mycard))
                            else:
                                if len(cards_played) == 3:
                                    return (suit, max(mycard))
                                else:
                                    for card in cards_played:
                                        if card == '♠13':
                                            for num in mycard:
                                                if suit == '♠' and num == 12:
                                                    return blacktwelve
                                                else:
                                                    return (suit, max(mycard))
                                        elif card == '♠1':
                                            for num in mycard:
                                                if suit == '♠' and num == 12:
                                                    return blacktwelve
                                                elif suit == '♠' and num == 13:
                                                    return blackthirteen
                                                else:
                                                    return (suit, max(mycard))
                                        else:
                                            if littleblack:
                                                return (suit, max(littleblack))
                                            else:
                                                return (suit, max(mycard))
        else:
            mycard = [card.number for card in cards_you_have]
            cards_noheart = [card for card in cards_you_have if card.suit != "♥" and card.suit != '♠']
            for card in cards_you_have:
                if card.suit == '♥':
                    for num in mycard:
                        if num > 5:
                            littleheart = mycard.remove(num)
            for card in cards_you_have:
                if card.suit != '♥':
                    for num in mycard:
                        if num >= 5:
                            littlecard = mycard.remove(num)
            for card in cards_you_have and num in mycard:
                if heart_broken:
                    if card.suit == '♥' and num < 5:
                        return ('♥',min(littleheart))
                    else:
                        if card.suit != '♥':

                            #don't know how to write
                            #出小牌，不管花色是什麼
                            return ...
                else:
                    if not card.suit == '♠' and not card.suit == '♥':
                        #出大牌，菱形梅花都可以
                        #疑慮:如果有一張菱形大排，一張黑桃大牌會不會同時被出出去
                    elif card.suit == '♠' and card.number < 12:
                        return max(card)

    '''
    decide cards you want to pass to the player next to you
    0->1, 1->2, 2->3, 3->0

    cards: list of cards in your hand
    '''
    def pass_cards(self, cards):
        return ...
