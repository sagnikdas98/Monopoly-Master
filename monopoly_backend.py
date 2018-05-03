from return_utterance import *




class SPACE:
    def __init__(self , space):
        self.type = space


class Property (SPACE):
    def __init__(self , name , spacetype , position , cost , housecost , mortgage , rent , h1 , h2 , h3 , h4 , h5 ,
                 owner , color, houses):
        super (Property , self).__init__ (spacetype)
        self.name = name
        self.sType = spacetype
        self.position = position
        self.owner = owner

        self.color = color
        self.cost = int (cost)
        self.housecost = int (housecost)
        self.mortgage = int (mortgage)
        self.rent = int (rent)
        self.h1 = int (h1)
        self.h2 = int (h2)
        self.h3 = int (h3)
        self.h4 = int (h4)
        self.h5 = int (h5)
        self.houses = int (houses)


class Railroad (SPACE):
    def __init__(self , name , spacetype , position , owner):
        super (Railroad , self).__init__ (spacetype)
        self.name = name
        self.sType = spacetype
        self.position = position
        self.owner = owner

        self.cost = float (200)
        self.rr1 = float (25)
        self.rr2 = float (50)
        self.rr3 = float (100)
        self.rr4 = float (200)
        self.mortgage = float (100)


class Utility (SPACE):
    def __init__(self , name , spacetype , position , owner):
        super (Utility , self).__init__ (spacetype)
        self.name = name
        self.sType = spacetype
        self.position = position
        self.owner = owner

        self.cost = float (150)
        self.u1 = float (4)
        self.u2 = float (10)
        self.mortgage = float (75)


class Taxspace (SPACE):
    def __init__(self , name , spacetype , position , tax):
        super (Taxspace , self).__init__ (spacetype)
        self.name = name
        self.sType = spacetype
        self.position = position

        self.tax = tax


class Freespace (SPACE):
    def __init__(self , name , spacetype , position):
        super (Freespace , self).__init__ (spacetype)
        self.name = name
        self.sType = spacetype
        self.position = position
        # jail, freeparking, go


class Gotojailspace (SPACE):
    def __init__(self , name , spacetype , position):
        super (Gotojailspace , self).__init__ (spacetype)
        self.name = name
        self.sType = spacetype
        self.position = position


class Communitychestspace (SPACE):
    def __init__(self , name , spacetype , position):
        super (Communitychestspace , self).__init__ (spacetype)
        self.name = name
        self.sType = spacetype
        self.position = position


class Chancespace (SPACE):
    def __init__(self , name , spacetype , position):
        super (Chancespace , self).__init__ (spacetype)
        self.name = name
        self.sType = spacetype
        self.position = position


class CommunityChestCard:
    def __init__(self , description , move , collect , pay , payperhouse , getoutofjailfree , gotojail , collect50):
        self.description = description
        self.move = int (move)
        self.collect = int (collect)
        self.pay = int (pay)
        self.payperhouse = int (payperhouse)
        self.getoutofjailfree = getoutofjailfree
        self.gotojail = gotojail
        self.collect50 = collect50


class ChanceCard:
    def __init__(self , description , move , collect , pay , payperhouse , getoutofjailfree , gotojail , moveback):
        self.description = description
        self.move = int (move)
        self.collect = int (collect)
        self.pay = int (pay)
        self.payperhouse = int (payperhouse)
        self.getoutofjailfree = getoutofjailfree
        self.gotojail = gotojail
        self.moveback = moveback


class Player:
    def __init__(self , number , money , boardpos , jailcards , jailtime):
        self.number = int (number)
        self.boardpos = int (boardpos)
        self.money = int (money)
        self.proplist = [ [ ] , [ ] , [ ] , [ ] , [ ] , [ ] , [ ] , [ ] ]
        self.raillist = [ ]
        self.utlist = [ ]
        self.jailcards = int (jailcards)
        self.jailtime = int (jailtime)

    def addproperty(self , newprop):
        newprop.owner = self.number
        self.money -= newprop.cost
        gotprop = 0
        while gotprop == 0:
            if isinstance (newprop , Property):
                switch_color = {"darkblue": 0 , "green": 1 ,
                                "yellow": 2 , "red": 3 ,
                                "orange": 4 , "pink": 5 ,
                                "lightblue": 6 , "purple": 7}
                addindex = switch_color[ newprop.color ]
                self.proplist[ addindex ].append (newprop)
                gotprop = 1

            if isinstance (newprop , Railroad):
                self.raillist.append (newprop)
                gotprop = 1
            if isinstance (newprop , Utility):
                self.utlist.append (newprop)
                gotprop = 1

    def mortgageprop(self , modprop):
        self.money += modprop.mortgage
        modprop.owner = "bank"
        for colorlist in self.proplist:
            for prop in colorlist:
                if modprop.name == prop.name:
                    colorlist.remove(prop)

        for rail in self.raillist:
            if modprop.name == rail.name:
                self.raillist.remove (rail)
        for ut in self.utlist:
            if modprop.name == ut.name:
                self.utlist.remove (ut)


class Board:



    def __init__(self , n):
        self.number = n
        self.started = False
        self.question_id = None
        self.cclist = None
        self.current_player = None
        self.current_player_index = 0
        self.playerlist = [ ]
        self.currspace = None

        for i in range (self.number):
            self.playerlist.append (Player (i + 1 , 1500 , 0 , 0 , 0))

        self.boardlist = [ ]

        gospace = Freespace ("PASS GO" , "freespace" , 1)
        self.boardlist.append (gospace)
        medit = Property ("Mediterranean Avenue" , "property" , 2 , 60 , 50 , 30 , 2 , 10 , 30 , 90 , 160 , 250 , "bank" ,
                          "purple" , 0)
        self.boardlist.append (medit)
        cc1 = Communitychestspace ("Community Chest" , "communitychestspace" , 3)
        self.boardlist.append (cc1)
        baltic = Property ("Baltic Avenue" , "property" , 4 , 60 , 50 , 30 , 4 , 20 , 60 , 180 , 320 , 450 , "bank" ,
                           "purple" , 0)
        self.boardlist.append (baltic)
        inctax = Taxspace ("Income Tax" , "taxspace" , 5 , 200)
        self.boardlist.append (inctax)
        r1 = Railroad ("Reading Railroad" , "railroad" , 6 , "bank")
        self.boardlist.append (r1)
        oriental = Property ("Oriental Avenue" , "property" , 7 , 100 , 50 , 50 , 6 , 30 , 90 , 270 , 400 , 550 , "bank" ,
                             "lightblue" ,
                             0)
        self.boardlist.append (oriental)
        chance1 = Chancespace ("Chance" , "chancespace" , 8)
        self.boardlist.append (chance1)
        vermont = Property ("Vermont Avenue" , "property" , 9 , 100 , 50 , 50 , 6 , 30 , 90 , 270 , 400 , 550 , "bank" ,
                            "lightblue" , 0)
        self.boardlist.append (vermont)
        connave = Property ("Connecticut Avenue" , "property" , 10 , 120 , 50 , 60 , 8 , 40 , 100 , 300 , 450 , 600 ,
                            "bank" ,
                            "lightblue" , 0)
        self.boardlist.append (connave)
        jailspace = Freespace ("Jail" , "freespace" , 11)
        self.boardlist.append (jailspace)
        stchar = Property ("St. Charles Place" , "property" , 12 , 140 , 100 , 70 , 10 , 50 , 150 , 450 , 625 , 750 ,
                           "bank" , "pink" ,
                           0)
        self.boardlist.append (stchar)
        ut1 = Utility ("Electric Company" , "utility" , 13 , "bank")
        self.boardlist.append (ut1)
        states = Property ("States Avenue" , "property" , 14 , 140 , 100 , 70 , 10 , 50 , 150 , 450 , 625 , 750 , "bank" ,
                           "pink" , 0)
        self.boardlist.append (states)
        virginia = Property ("Virginia Avenue" , "property" , 15 , 160 , 100 , 80 , 12 , 60 , 180 , 500 , 700 , 900 ,
                             "bank" , "pink" ,
                             0)
        self.boardlist.append (virginia)
        r2 = Railroad ("Pennsylvania Railroad" , "railroad" , 16 , "bank")
        self.boardlist.append (r2)
        stjames = Property ("St. James Place" , "property" , 17 , 180 , 100 , 90 , 14 , 70 , 200 , 550 , 750 , 950 ,
                            "bank" ,
                            "orange" , 0)
        self.boardlist.append (stjames)
        cc2 = Communitychestspace ("Community Chest" , "communitychestspace" , 18)
        self.boardlist.append (cc2)
        tennessee = Property ("Tennessee Avenue" , "property" , 19 , 180 , 100 , 90 , 14 , 70 , 200 , 550 , 750 , 950 ,
                              "bank" ,
                              "orange" , 0)
        self.boardlist.append (tennessee)
        newyork = Property ("New York Avenue" , "property" , 20 , 200 , 100 , 100 , 16 , 80 , 200 , 600 , 800 , 1000 ,
                            "bank" ,
                            "orange" , 0)
        self.boardlist.append (newyork)
        freepark = Freespace ("Free Parking" , "freespace" , 21)
        self.boardlist.append (freepark)
        kentucky = Property ("Kentucky Avenue" , "property" , 22 , 220 , 150 , 110 , 18 , 90 , 250 , 700 , 875 , 1050 ,
                             "bank" , "red" ,
                             0)
        self.boardlist.append (kentucky)
        chance2 = Chancespace ("Chance" , "chancespace" , 23)
        self.boardlist.append (chance2)
        indiana = Property ("Indiana Avenue" , "property" , 24 , 220 , 150 , 110 , 18 , 90 , 250 , 700 , 875 , 1050 ,
                            "bank" , "red" , 0)
        self.boardlist.append (indiana)
        illinois = Property ("Illinois Avenue" , "property" , 25 , 240 , 150 , 120 , 20 , 100 , 300 , 750 , 925 , 1100 ,
                             "bank" , "red" ,
                             0)
        self.boardlist.append (illinois)
        r3 = Railroad ("B&O Railroad" , "railroad" , 26 , "bank")
        self.boardlist.append (r3)
        atlantic = Property ("Atlantic Avenue" , "property" , 27 , 260 , 150 , 130 , 22 , 110 , 330 , 800 , 975 , 1150 ,
                             "bank" ,
                             "yellow" , 0)
        self.boardlist.append (atlantic)
        ventnor = Property ("Ventnor Avenue" , "property" , 28 , 260 , 150 , 130 , 22 , 110 , 330 , 800 , 975 , 1150 ,
                            "bank" ,
                            "yellow" , 0)
        self.boardlist.append (ventnor)
        ut2 = Utility ("Water Works" , "utility" , 29 , "bank")
        self.boardlist.append (ut2)
        marvin = Property ("Marvin Gardens" , "property" , 30 , 280 , 150 , 140 , 24 , 120 , 360 , 850 , 1025 , 1200 ,
                           "bank" ,
                           "yellow" , 0)
        self.boardlist.append (marvin)
        gojail = Gotojailspace ("Go To Jail" , "gotojailspace" , 31)
        self.boardlist.append (gojail)
        pacific = Property ("Pacific Avenue" , "property" , 32 , 300 , 200 , 150 , 26 , 130 , 390 , 900 , 1100 , 1275 ,
                            "bank" ,
                            "green" , 0)
        self.boardlist.append (pacific)
        ncarol = Property ("North Carolina Avenue" , "property" , 33 , 300 , 200 , 150 , 26 , 130 , 390 , 900 , 1100 ,
                           1275 , "bank" ,
                           "green" , 0)
        self.boardlist.append (ncarol)
        cc3 = Communitychestspace ("Community Chest" , "communitychestspace" , 34)
        self.boardlist.append (cc3)
        pennave = Property ("Pennsylvania Avenue" , "property" , 35 , 320 , 200 , 160 , 28 , 150 , 450 , 1000 , 1200 ,
                            1400 , "bank" ,
                            "green" , 0)
        self.boardlist.append (pennave)
        r4 = Railroad ("Short Line" , "railroad" , 36 , "bank")
        self.boardlist.append (r4)
        chance3 = Chancespace ("Chance" , "chancespace" , 37)
        self.boardlist.append (chance3)
        parkplace = Property ("Park Place" , "property" , 38 , 350 , 200 , 175 , 35 , 175 , 500 , 1100 , 1300 , 1500 ,
                              "bank" ,
                              "darkblue" , 0)
        self.boardlist.append (parkplace)
        luxtax = Taxspace ("Luxury Tax" , "taxspace" , 39 , 75)
        self.boardlist.append (luxtax)
        boardwalk = Property ("Boardwalk" , "property" , 40 , 400 , 200 , 200 , 50 , 200 , 600 , 1400 , 1700 , 2000 ,
                              "bank" ,
                              "darkblue" , 0)
        self.boardlist.append (boardwalk)

        self.cclist = [ ]

        ccdesc1 = "GRAND OPERA OPENING. COLLECT $50 FROM EVERY PLAYER."
        c1 = CommunityChestCard (ccdesc1 , 0 , 0 , 0 , 0 , 0 , 0 , 50)
        self.cclist.append (c1)
        ccdesc2 = "RECEIVE FOR SERVICES $25."
        c2 = CommunityChestCard (ccdesc2 , 0 , 10 , 0 , 0 , 0 , 0 , 0)
        self.cclist.append (c2)
        ccdesc3 = "ADVANCE TO GO (COLLECT $200)."
        c3 = CommunityChestCard (ccdesc3 , 1 , 0 , 0 , 0 , 0 , 0 , 0)
        self.cclist.append (c3)
        ccdesc4 = "PAY HOSPITAL $100. "
        c4 = CommunityChestCard (ccdesc3 , 0 , 0 , 100 , 0 , 0 , 0 , 0)
        self.cclist.append (c4)
        ccdesc5 = "DOCTOR'S FEE. PAY $50. "
        c5 = CommunityChestCard (ccdesc5 , 0 , 0 , 50 , 0 , 0 , 0 , 0)
        self.cclist.append (c5)
        ccdesc6 = "GET OUT OF JAIL FREE CARD."
        c6 = CommunityChestCard (ccdesc6 , 0 , 0 , 0 , 0 , 1 , 0 , 0)
        self.cclist.append (c6)
        ccdesc7 = "FROM SALE OF STOCK YOU GET $45."
        c7 = CommunityChestCard (ccdesc7 , 0 , 45 , 0 , 0 , 0 , 0 , 0)
        self.cclist.append (c7)
        ccdesc8 = "YOU INHERIT $100."
        c8 = CommunityChestCard (ccdesc8 , 0 , 100 , 0 , 0 , 0 , 0 , 0)
        self.cclist.append (c8)
        ccdesc9 = "GO TO JAIL. GO DIRECTLY TO JAIL. DO NOT PASS GO. DO NOT COLLECT $200."
        c9 = CommunityChestCard (ccdesc9 , 0 , 0 , 0 , 0 , 0 , 1 , 0)
        self.cclist.append (c9)
        ccdesc10 = "LIFE INSURANCE MATURES. COLLECT $100."
        c10 = CommunityChestCard (ccdesc10 , 0 , 100 , 0 , 0 , 0 , 0 , 0)
        self.cclist.append (c10)
        ccdesc11 = "YOU HAVE WON SECOND PRIZE IN A BEAUTY CONTEST. COLLECT $10."
        c11 = CommunityChestCard (ccdesc11 , 0 , 10 , 0 , 0 , 0 , 0 , 0)
        self.cclist.append (c11)
        ccdesc12 = "XMAS FUND MATURES. COLLECT $100."
        c12 = CommunityChestCard (ccdesc12 , 0 , 100 , 0 , 0 , 0 , 0 , 0)
        self.cclist.append (c12)
        ccdesc13 = "YOU ARE ASSESSED FOR STREET REPAIRS. $40 PER HOUSE."
        c13 = CommunityChestCard (ccdesc13 , 0 , 0 , 0 , 40 , 0 , 0 , 0)
        self.cclist.append (c13)
        ccdesc14 = "BANK ERROR IN YOUR FAVOR. COLLECT $200."
        c14 = CommunityChestCard (ccdesc14 , 0 , 200 , 0 , 0 , 0 , 0 , 0)
        self.cclist.append (c14)
        ccdesc15 = "INCOME TAX REFUND. COLLECT $20."
        c15 = CommunityChestCard (ccdesc15 , 0 , 20 , 0 , 0 , 0 , 0 , 0)
        self.cclist.append (c15)

        self.chancelist = [ ]

        cdesc1 = "ADVANCE TO ILLINOIS AVE. IF YOU PASS GO, COLLECT $200."
        c1 = ChanceCard (cdesc1 , 25 , 0 , 0 , 0 , 0 , 0 , 0)
        self.chancelist.append (c1)
        cdesc2 = "YOU ARE ASSESSED FOR STREET REPAIRS. $40.00 PER HOUSE."
        c2 = ChanceCard (cdesc2 , 0 , 0 , 0 , 40 , 0 , 0 , 0)
        self.chancelist.append (c2)
        cdesc3 = "GET OUT OF JAIL FREE CARD."
        c3 = ChanceCard (cdesc3 , 0 , 0 , 0 , 0 , 1 , 0 , 0)
        self.chancelist.append (c3)
        cdesc4 = "ADVANCE TO GO."
        c4 = ChanceCard (cdesc4 , 1 , 0 , 0 , 0 , 0 , 0 , 0)
        self.chancelist.append (c4)
        cdesc5 = "ADVANCE TO ST.CHARLES PLACE. IF YOU PASS GO, COLLECT $200."
        c5 = ChanceCard (cdesc5 , 12 , 0 , 0 , 0 , 0 , 0 , 0)
        self.chancelist.append (c5)
        cdesc6 = "PARKING FINE $15."
        c6 = ChanceCard (cdesc6 , 0 , 0 , 15 , 0 , 0 , 0 , 0)
        self.chancelist.append (c6)
        cdesc7 = "BANK PAYS YOU DIVIDEND OF $50."
        c7 = ChanceCard (cdesc7 , 0 , 50 , 0 , 0 , 0 , 0 , 0)
        self.chancelist.append (c7)
        cdesc8 = "YOUR XMAS FUND MATURES. COLLECT $100."
        c8 = ChanceCard (cdesc8 , 0 , 100 , 0 , 0 , 0 , 0 , 0)
        self.chancelist.append (c8)
        cdesc9 = "TAKE A WALK ON THE BOARDWALK."
        c9 = ChanceCard (cdesc9 , 40 , 0 , 0 , 0 , 0 , 0 , 0)
        self.chancelist.append (c9)
        cdesc10 = "PAY POOR TAX OF $12."
        c10 = ChanceCard (cdesc10 , 0 , 0 , 12 , 0 , 0 , 0 , 0)
        self.chancelist.append (c10)
        cdesc11 = "TAKE A RIDE ON THE READING. ADVANCE TOKEN AND IF YOU PASS GO COLLECT $200."
        c11 = ChanceCard (cdesc11 , 6 , 0 , 0 , 0 , 0 , 0 , 0)
        self.chancelist.append (c11)
        cdesc12 = "GO BACK THREE SPACES."
        c12 = ChanceCard (cdesc12 , 0 , 0 , 0 , 0 , 0 , 0 , 3)
        self.chancelist.append (c12)
        cdesc13 = "YOUR BUILDING AND LOAN MATURES - RECIEVE $150."
        c13 = ChanceCard (cdesc13 , 0 , 150 , 0 , 0 , 0 , 0 , 0)
        self.chancelist.append (c13)
        cdesc14 = "MAKE GENERAL REPAIRS ON ALL OF YOUR HOUSES. FOR EACH HOUSE PAY $25"
        c14 = ChanceCard (cdesc14 , 0 , 0 , 0 , 25 , 0 , 0 , 0)
        self.chancelist.append (c14)
        cdesc15 = "GO TO JAIL. GO DIRECTLY TO JAIL. DO NOT PASS GO. DO NOT COLLECT $200."
        c15 = ChanceCard (cdesc15 , 0 , 0 , 0 , 0 , 0 , 1 , 0)
        self.chancelist.append (c15)

        # random.shuffle(self.playerlist)
        random.shuffle (self.cclist)
        random.shuffle (self.chancelist)

    def returnNumberOfPlayers(self):
        return len (self.playerlist)

    def playerlose(self , player):
        for item in self.boardlist:
            if isinstance (item , Property):
                if item.owner == player.number:
                    item.owner = "bank"
                    item.houses = 0
                if isinstance (item , Railroad):
                    if item.owner == player.number:
                        item.owner = "bank"
                        item.houses = 0
                if isinstance (item , Utility):
                    if item.owner == player.number:
                        item.owner = "bank"
                        item.houses = 0

    def playermove(self , player , movenum , warp=0):


        say_it = [ ]


        newspot = int (movenum) + player.boardpos
        if warp == 1:
            # doubt
            newspot = int(movenum)
            if player.boardpos > newspot:
                player.money += int(200)
                # passed go
            player.boardpos = newspot
        if newspot > 39:
            newspot += -40
            player.money += int(200)
            # passed go
        player.boardpos = newspot
        for space in self.boardlist:
            if self.boardlist.index (space) == player.boardpos:

                self.currspace = space

                break

        say_it.append(format_statement (random_statement(property_landed) , self.currspace.name))

        if isinstance (self.currspace , Property):
            if self.currspace.owner == "bank":
                if player.money >= self.currspace.cost:
                    say_it.append(random_statement(want_to_buy_prop))
                    self.question_id = "want_to_buy_prop"
                    return say_it

            elif self.currspace.owner == player.number:
                say_it.append (random_statement(already_owned_by_you))
            else:
                say_it.append (self.prop_owner(player))
                return say_it

        if isinstance(self.currspace , Railroad):
            if self.currspace.owner == "bank":  # if can buy
                if player.money >= self.currspace.cost:
                    say_it.append (random_statement(want_to_buy_railroad))
                    self.question_id = "want_to_buy_railroad"
                    return say_it
            elif self.currspace.owner == player.number:
                say_it.append (random_statement(already_owned_by_you_railroad))
            else:
                say_it.append(self.railroad_owner(player))
                return say_it

        if isinstance (self.currspace , Utility):
            if self.currspace.owner == "bank":  # if can buy
                if player.money >= self.currspace.cost:
                    say_it.append (random_statement(want_to_buy_utility))
                    self.question_id = "want_to_buy_utility"
                    return say_it

            elif self.currspace.owner == player.number:
                say_it.append (random_statement(already_owned_by_you_utility))
            else:
                say_it.append (self.utility_owner (player))
                return say_it

        if isinstance (self.currspace , Taxspace):
            paytax = self.currspace.tax
            self.question_id = "tax_payment"
            if player.money < paytax:
                self.playerlose(player)
                say_it.append(random_statement(tax_fail))

                self.current_player_index += 1
                self.current_player = self.playerlist[ self.current_player_index % len (self.playerlist) ]
                say_curr_player = format_statement (random_statement (next_player_turn) , self.current_player.number)
                say_it.append (say_curr_player)
                if self.current_player.jailtime > 0:
                    ret_sat = self.jail_check (self.current_player)
                    say_it.append (ret_sat)
                return say_it

            else:
                player.money += -paytax
                say_it.append(format_statement(random_statement(tax_pass),paytax))
                self.current_player_index += 1
                self.current_player = self.playerlist[ self.current_player_index % len (self.playerlist) ]
                say_curr_player = format_statement (random_statement (next_player_turn) , self.current_player.number)
                say_it.append (say_curr_player)
                if self.current_player.jailtime > 0:
                    ret_sat = self.jail_check (self.current_player)
                    say_it.append (ret_sat)
                return say_it

        if isinstance(self.currspace, Freespace):
            self.question_id = "free_space"
            # say_it.append (format_statement(random_statement (),))
            self.current_player_index += 1
            self.current_player = self.playerlist[ self.current_player_index % len (self.playerlist)]
            say_curr_player = format_statement (random_statement (next_player_turn) , self.current_player.number)
            say_it.append (say_curr_player)
            if self.current_player.jailtime > 0:
                ret_sat = self.jail_check (self.current_player)
                say_it.append (ret_sat)
            return say_it

        if isinstance (self.currspace , Gotojailspace):
            player.boardpos = 11
            player.jailtime = 3

            self.current_player_index += 1
            self.current_player = self.playerlist[self.current_player_index % len (self.playerlist)]
            say_curr_player = format_statement (random_statement (next_player_turn) , self.current_player.number)
            say_it.append (say_curr_player)
            if self.current_player.jailtime > 0:
                ret_sat = self.jail_check (self.current_player)
                say_it.append (ret_sat)
            return say_it

        if isinstance (self.currspace , Communitychestspace):

            self.cclist.append (self.cclist.pop (0))
            card = self.cclist[ -1 ]
            say_it.append( card.description)
            # print stuff
            if card.move > 0:
                self.playermove (player , card.move , 1)
            if card.collect > 0:
                player.money += card.collect
            if card.pay > 0:
                player.money += card.collect
            if card.payperhouse > 0:
                player.money += -card.payperhouse
            if card.getoutofjailfree > 0:
                player.jailcards += 1
            if card.gotojail > 0:
                player.board = 11
                player.jailtime = 3
                # print stuff
            if card.collect50 > 0:
                for i in self.playerlist:
                    if i != player:
                        if i.money > 50:
                            i.money += -50
                            player.money += 50
                        else:
                            player.money += i.money
                            self.playerlose (i)
                            say_it.append (random_statement(insufficient_balance))

            self.current_player_index += 1
            self.current_player = self.playerlist[ self.current_player_index % len (self.playerlist) ]
            say_curr_player = format_statement (random_statement (next_player_turn) , self.current_player.number)
            say_it.append (say_curr_player)
            if self.current_player.jailtime > 0:
                ret_sat = self.jail_check (self.current_player)
                say_it.append (ret_sat)
            return say_it

        if isinstance (self.currspace , Chancespace):
            self.chancelist.append (self.chancelist.pop (0))
            card = self.chancelist[ -1 ]
            say_it.append (card.description)
            if card.move > 0:
                self.playermove (player , card.move , 1)
            if card.collect > 0:
                player.money += card.collect
            if card.pay > 0:
                player.money += -card.pay
            if card.payperhouse > 0:
                player.money += -card.payperhouse
            if card.getoutofjailfree > 0:
                player.jailcards += 1
            if card.gotojail > 0:
                player.boardpos = 11
                player.jailtime = 3
                # print -someone- goes to jail
            if card.moveback > 0:
                self.playermove (player , 1 , 0)
            self.current_player_index += 1
            self.current_player = self.playerlist[ self.current_player_index % len (self.playerlist) ]
            say_curr_player = format_statement (random_statement (next_player_turn) , self.current_player.number)
            say_it.append (say_curr_player)
            if self.current_player.jailtime > 0:
                ret_sat = self.jail_check (self.current_player)
                say_it.append (ret_sat)
            return say_it
        else:
            self.current_player_index += 1
            self.current_player = self.playerlist[ self.current_player_index % len (self.playerlist) ]
            say_curr_player = format_statement (random_statement (next_player_turn) , self.current_player.number)
            say_it.append (say_curr_player)
            if self.current_player.jailtime > 0:
                ret_sat = self.jail_check (self.current_player)
                say_it.append (ret_sat)
            return say_it

    def bought_prop(self , player):
        player.addproperty (self.currspace)
        return random_statement(owned_property)

    def prop_owner(self, player):
        propowner = None
        for person in self.playerlist:
            if person.number == self.currspace.owner:
                propowner = person
        hasmonopoly = 0
        for colorlist in propowner.proplist:
            if colorlist:
                for prop in colorlist:
                    if prop.color == self.currspace.color:
                        if "monopoly" in colorlist:
                            hasmonopoly = 1
                            break

        if hasmonopoly == 1:
            if self.currspace.houses == 0:
                payout = 2 * int (self.currspace.rent)
            elif self.currspace.houses == 1:
                payout = int (self.currspace.h1)
            elif self.currspace.houses == 2:
                payout = int (self.currspace.h2)
            elif self.currspace.houses == 3:
                payout = int (self.currspace.h3)
            elif self.currspace.houses == 4:
                payout = int (self.currspace.h4)
            else:  # self.currspace.houses == 5:
                payout = int (self.currspace.h5)

            if player.money <= payout:
                propowner.money += player.money
                self.playerlose (player)
                return random_statement (insufficient_balance_rent)

            else:
                player.money += -payout
                propowner.money += payout
                return format_statement_2(random_statement(you_have_paid_rent_to), payout, propowner.number)
        else:
            payout = int (self.currspace.rent)
            if player.money <= payout:
                propowner.money += player.money
                self.playerlose (player)
                return random_statement (insufficient_balance_rent)
            else:
                player.money += - payout
                propowner.money += payout
                return format_statement_2(random_statement(you_have_paid_rent_to) , payout, propowner.number)

                # railroad start

    def bought_railroad(self, player):
        player.addproperty(self.currspace)
        return random_statement(owned_property)

    def railroad_owner(self, player):
        propowner = None
        for person in self.playerlist:
            if self.currspace.owner == person:
                propowner = person
        if 1 == len (propowner.raillist):
            payout = int (self.currspace.rr1)
        elif 2 == len (propowner.raillist):
            payout = int (self.currspace.rr2)
        elif 3 == len (propowner.raillist):
            payout = int (self.currspace.rr3)
        else:  # 4 == len(propowner.raillist):
            payout = int (self.currspace.rr4)
        if player.money <= payout:
            propowner.money += player.money
            self.playerlose (player)
            return random_statement (insufficient_balance_rent)
        else:
            player.money += -payout
            propowner.money += payout
            return format_statement_2 (random_statement (you_have_paid_rent_to) , payout , propowner.number)

    # utility start

    def bought_utility(self , player):
        player.addproperty (self.currspace)
        return random_statement(owned_property)

    def utility_owner(self , player):
        propowner = None

        for person in self.playerlist:  # determine property owner
            if self.currspace.owner == person:
                propowner = person

            if len (propowner.utlist) == 1:
                payout = int (self.currspace.u1)
            else:  # len(propowner.utlist) == 2:
                payout = int (self.currspace.u2)

            if player.money <= payout:
                propowner.money += player.money
                self.playerlose (player)
                return random_statement (insufficient_balance_rent)
            else:
                player.money += -payout
                propowner.money += payout
                return format_statement_2 (random_statement (you_have_paid_rent_to) , payout , propowner.number)

    def jail_check(self , player):
        # if player.jailtime > 0:

        if player.jailcards > 0 and player.money > 50:
            self.question_id = "jail_card_or_money"
            return random_statement(jail_card_or_money)
        elif player.jailcards > 0:
            self.question_id = "jail_card"
            return random_statement(jail_card)
        elif player.money >= 50:
            self.question_id = "jail_money"
            return random_statement(jail_money)
        else:
            self.question_id = "you_have_to_pass"
            return random_statement(have_to_pass)

    def get_out_card(self , player):
        player.jailcards += -1
        player.jailtime = 0
        return random_statement (out_of_jail_now)

    def get_out_money(self , player):
        player.money += -50
        player.jailtime = 0
        return random_statement (out_of_jail_now)

    def buy_house(self , player):
        for COLORLIST in player.proplist:
            if "monopoly" in COLORLIST:
                for property in COLORLIST:
                    if property.houses <= 5 and player.money >= property.housecost:
                        self.question_id = "buy_house"
                        return random_statement (want_to_buy_house)
                    else:
                        return random_statement (cant_buy_house)

            else:
                return random_statement (cant_buy_house)

    def bought_house(self, player):
        for COLORLIST in player.proplist:
            for property in COLORLIST:
                player.money += -property.housecost
                property.houses += 1

    def mortgage(self , player):
        ownsprop = [ ]
        for COLORLIST in player.proplist:
            if COLORLIST:
                ownsprop = [ "yes" ]
        if ownsprop or player.raillist or player.utlist:
            self.question_id = "which_prop_to_mortgage"
            return random_statement(which_prop_to_mortgage)
        else:
            return random_statement(not_owned_property)

    # list of property names

    def mortage_this(self , player , mortthis):
        for COLORLIST in player.proplist:
            for PROP in COLORLIST:
                if PROP.name == mortthis:
                    COLORLIST.remove (PROP)
        for SPACE in self.boardlist:
            if SPACE.name == mortthis:
                if SPACE.owner == player.number:
                    SPACE.owner = "bank"
                    SPACE.houses = 0
                    player.money += SPACE.mortgage
        return random_statement(mortgage_done)