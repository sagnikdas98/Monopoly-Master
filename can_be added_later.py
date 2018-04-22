"""
double roll to get out of jail


            jailrollwhile = 0
            while jailrollwhile == 0:
                jailroll = input("do you wanna try and get out of jail")
                if jailroll == "N":
                    jailrollwhile = 1
                if jailroll == "Y":
                    die1x = random.randint(1, 6)
                    die2 = random.randint(1, 6)
                    # die1 + die2
                    if die1x == die2:
                        player.jailtime = 0
                        jailrollwhile = 1
                    else:
                        jailrollwhile = 1
                else:
"""