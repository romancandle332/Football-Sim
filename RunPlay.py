import math
import random
import pandas as pd
import numpy as np
from SimLibrary import *

def RunPlay(offensive_team,defensive_team):
    ##offensive_team should be an object that holds both the strategy and depth chart of the offensive team
    ##defensive_team should be an object that holds both the strategy and depth chart of the defensive team

    ##calling the play
    offensive_play = 0 ##generic play holder
    offensive_personnel = 0 ##personnel holder

    if offensive_personnel == 98: ##place kick
        defensive_play = 98 ##generic play holder
    elif offensive_personnel == 99: #punt
        defensive_play = 99 ##generic play holder
    else:
        defensive_play = 0 ##generic play holder

    ##setting up the personnel
    if offensive_personnel == 98: ##place kick
        play_type = 2
        pass
    elif offensive_personnel == 99: #punt
        play_type = 3
        pass
    else:
        QB = offensive_team.QB1
        LT = offensive_team.LT1
        LG = offensive_team.LG1
        OC = offensive_team.OC1
        RG = offensive_team.RG1
        RT = offensive_team.RT1
        if offensive_personnel == 0: ##5 Wide
            WR1 = offensive_team.WR1
            WR2 = offensive_team.WR2
            WR3 = offensive_team.WR3
            WR4 = offensive_team.WR4
            WR5 = offensive_team.WR5
        elif offensive_personnel == 1: ##01 Personnel
            WR1 = offensive_team.WR1
            WR2 = offensive_team.WR2
            WR3 = offensive_team.WR3
            WR4 = offensive_team.WR4
            TE1 = offensive_team.TE1
        elif offensive_personnel == 2: ##02 Personnel
            WR1 = offensive_team.WR1
            WR2 = offensive_team.WR2
            WR3 = offensive_team.WR3
            TE1 = offensive_team.TE1
            TE2 = offensive_team.TE2
        elif offensive_personnel == 3: ##03 Personnel
            WR1 = offensive_team.WR1
            WR2 = offensive_team.WR2
            TE1 = offensive_team.TE1
            TE2 = offensive_team.TE2
            TE3 = offensive_team.TE3
        elif offensive_personnel == 4: ##10 Personnel
            WR1 = offensive_team.WR1
            WR2 = offensive_team.WR2
            WR3 = offensive_team.WR3
            WR4 = offensive_team.WR4
            RB1 = offensive_team.RB1
        elif offensive_personnel == 5: ##11 Personnel
            WR1 = offensive_team.WR1
            WR2 = offensive_team.WR2
            WR3 = offensive_team.WR3
            TE1 = offensive_team.TE1
            RB1 = offensive_team.RB1
        elif offensive_personnel == 6: ##12 Personnel
            WR1 = offensive_team.WR1
            WR2 = offensive_team.WR2
            TE1 = offensive_team.TE1
            TE2 = offensive_team.TE2
            RB1 = offensive_team.RB1
        elif offensive_personnel == 7: ##13 Personnel
            WR1 = offensive_team.WR1
            TE1 = offensive_team.TE1
            TE2 = offensive_team.TE2
            TE3 = offensive_team.TE3
            RB1 = offensive_team.RB1
        elif offensive_personnel == 8: ##20 Personnel, 2 HB
            WR1 = offensive_team.WR1
            WR2 = offensive_team.WR2
            WR3 = offensive_team.WR3
            RB1 = offensive_team.RB1
            RB2 = offensive_team.RB2
        elif offensive_personnel == 9: ##21 Personnel, 2 HB
            WR1 = offensive_team.WR1
            WR2 = offensive_team.WR2
            TE1 = offensive_team.TE1
            RB1 = offensive_team.RB1
            RB2 = offensive_team.RB2
        elif offensive_personnel == 10: ##22 Personnel, 2 HB
            WR1 = offensive_team.WR1
            TE1 = offensive_team.TE1
            TE2 = offensive_team.TE2
            RB1 = offensive_team.RB1
            RB2 = offensive_team.RB2
        elif offensive_personnel == 11: ##23 Personnel, 2 HB
            TE1 = offensive_team.TE1
            TE2 = offensive_team.TE2
            TE3 = offensive_team.TE3
            RB1 = offensive_team.RB1
            RB2 = offensive_team.RB2
        elif offensive_personnel == 12: ##20 Personnel, FB
            WR1 = offensive_team.WR1
            WR2 = offensive_team.WR2
            WR3 = offensive_team.WR3
            RB1 = offensive_team.RB1
            FB1 = offensive_team.FB1
        elif offensive_personnel == 13: ##21 Personnel, FB
            WR1 = offensive_team.WR1
            WR2 = offensive_team.WR2
            TE1 = offensive_team.TE1
            RB1 = offensive_team.RB1
            FB1 = offensive_team.FB1
        elif offensive_personnel == 14: ##22 Personnel, FB
            WR1 = offensive_team.WR1
            TE1 = offensive_team.TE1
            TE2 = offensive_team.TE2
            RB1 = offensive_team.RB1
            FB1 = offensive_team.FB1
        elif offensive_personnel == 15: ##23 Personnel, FB
            TE1 = offensive_team.TE1
            TE2 = offensive_team.TE2
            TE3 = offensive_team.TE3
            RB1 = offensive_team.RB1
            FB1 = offensive_team.FB1
        elif offensive_personnel == 16: ##30 Personnel
            WR1 = offensive_team.WR1
            WR2 = offensive_team.WR2
            RB1 = offensive_team.RB1
            RB2 = offensive_team.RB2
            FB1 = offensive_team.FB1
        elif offensive_personnel == 17: ##31 Personnel
            WR1 = offensive_team.WR1
            TE1 = offensive_team.TE1
            RB1 = offensive_team.RB1
            RB2 = offensive_team.RB2
            FB1 = offensive_team.FB1
        elif offensive_personnel == 18: ##32 Personnel
            TE1 = offensive_team.TE1
            TE2 = offensive_team.TE2
            RB1 = offensive_team.RB1
            RB2 = offensive_team.RB2
            FB1 = offensive_team.FB1

    if offensive_personnel == 98: ##place kick
        pass
    elif offensive_personnel == 99: #punt
        pass
    else:
        if defensive_team.def_base == "4-3":
            if offensive_personnel in [11,15,18]: ##against 0 WR sets
                pass
            elif offensive_personnel in [7,10,14,17]: ##against 1 WR sets
                pass
            elif offensive_personnel in [3,6,9,13,16]: ##against 2 WR sets
                LDE = defensive_team.LDE1
                LDT = defensive_team.LDT1
                RDT = defensive_team.RDT1
                RDE = defensive_team.RDE1
                LOLB = defensive_team.LOLB1
                MLB = defensive_team.MLB1
                ROLB = defensive_team.ROLB1
                CB1 = defensive_team.CB1
                CB2 = defensive_team.CB2
                FS = defensive_team.FS1
                SS = defensive_team.SS1
            elif offensive_personnel in [2,5,8,12]: ##against 3 WR sets
                pass
            elif offensive_personnel in [1,4]: ##against 4 WR sets
                pass
            elif offensive_personnel in [0]: ##against 5 WR sets
                pass
        elif defensive_team.def_base == "3-4":
            pass

    if play_type == 0: ##pass play
        ##determine blockers and rushers per gap

        ##snap the ball
        snap_adjustment = ConvertSkillToAdvantage(OC.Snapping)
        snap_roll = DiceRollHigh(snap_adjustment)
        if snap_roll != 1:
            pass
        else: ##fumbled snap
            pass

        ##determine blocking results

        ##determine if QB is blown up immediately by free rusher/poor blocking

        ##determine routes vs coverage

        ##determine how QB sees how open each read is

        ##determine which read QB throws to

        ##determine if pass rush gets to QB before then

        ##determine actual route vs coverage

        ##determine QB arm

        ##determine QB accuracy, adjusted by how open/covered the target is

        ##determine if catchable ball

        ##determine if caught

        ##determine if tackled immediately

        ##determine who can tackle receiver after catch

        ##determine if receiver makes it past the initial hits

        ##determine if anyone can catch up to receiver

        ##determine if receiver is tackled, pushed out of bounds, or TD

        ##if no open reads or pass rush gets home, determine if thrown away, scrambled, or sacked

        ##determine clock

    elif play_type == 1: ##run play
        ##determine blockers and rushers per gap

        ##snap the ball
        snap_adjustment = ConvertSkillToAdvantage(OC.Snapping)
        snap_roll = DiceRollHigh(snap_adjustment)
        if snap_roll != 1:
            pass
        else: ##fumbled snap
            pass

        ##determine blocking results

        ##is RB immediately blown up due to free rusher/poor blocking?

        ##determine how RB sees gaps

        ##determine which gap RB takes

        ##determine if RB makes it through gap

        ##determine who meets RB at second level

        ##determine if RB makes it through second level

        ##determine who meets RB at third level

        ##determine if RB makes it through third level

        ##determine if RB is fast enough to not get run down/pushed out or if they score

        ##determine amount of clock consumed
    elif play_type == 2: ##place kick
        pass
    elif play_type == 3: ##punt
        pass