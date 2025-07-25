import math
import random
import pandas as pd

class Player():
    def __init__(self):
        self.FirstName = "Generic"
        self.LastName = "Player"
        self.FullName = self.FirstName + " " + self.LastName
        self.Age = 18
        self.HeightFt = 5
        self.HeightIn = 11
        self.Weight = 180
        self.Hometown = "Springfield"
        self.Homestate = "USA"
        self.Hand = "Right"
        self.Position = "ATH"
        self.CanQB = False
        self.CanHB = False
        self.CanFB = False
        self.CanWR = False
        self.CanTE = False
        self.CanOT = False
        self.CanOG = False
        self.CanC = False
        self.CanDE = False
        self.CanDT = False
        self.CanOLB = False
        self.CanILB = False
        self.CanCB = False
        self.CanS = False
        self.CanK = False
        self.CanP = False
        self.Overall = 1.0
        self.Speed_Current = 1.0
        self.Speed_Potential = 1.0
        self.Agility_Current = 1.0
        self.Agility_Potential = 1.0
        self.Acceleration_Current = 1.0
        self.Acceleration_Potential = 1.0
        self.Jumping_Current = 1.0
        self.Jumping_Potential = 1.0
        self.Injury_Current = 1.0
        self.Injury_Potential = 1.0
        self.ThrowStrength_Current = 1.0
        self.ThrowStrength_Potential = 1.0
        self.ThrowAccuracy_Current = 1.0
        self.ThrowAccuracy_Potential = 1.0
        self.ThrowTouch_Current = 1.0
        self.ThrowTouch_Potential = 1.0
        self.ThrowVision_Current = 1.0
        self.ThrowVision_Potential = 1.0
        self.PocketAwareness_Current = 1.0
        self.PocketAwareness_Potential = 1.0
        self.PlayAction_Current = 1.0
        self.PlayAction_Potential = 1.0
        self.Carrying_Current = 1.0
        self.Carrying_Potential = 1.0
        self.BreakTackle_Current = 1.0
        self.BreakTackle_Potential = 1.0
        self.RunVision_Current = 1.0
        self.RunVision_Potential = 1.0
        self.Catching_Current = 1.0
        self.Catching_Potential = 1.0
        self.ContestCatching_Current = 1.0
        self.ContestCatching_Potential = 1.0
        self.RouteRunning_Current = 1.0
        self.RouteRunning_Potential = 1.0
        self.Release_Current = 1.0
        self.Release_Potential = 1.0
        self.PassBlocking_Current = 1.0
        self.PassBlocking_Potential = 1.0
        self.RunBlocking_Current = 1.0
        self.RunBlocking_Potential = 1.0
        self.Tackling_Current = 1.0
        self.Tackling_Potential = 1.0
        self.SpeedRush_Current = 1.0
        self.SpeedRush_Potential = 1.0
        self.PowerRush_Current = 1.0
        self.PowerRush_Potential = 1.0
        self.BlockShedding_Current = 1.0
        self.BlockShedding_Potential = 1.0
        self.PressCoverage_Current = 1.0
        self.PressCoverage_Potential = 1.0
        self.ManCoverage_Current = 1.0
        self.ManCoverage_Potential = 1.0
        self.ZoneCoverage_Current = 1.0
        self.ZoneCoverage_Potential = 1.0
        self.PuntPower_Current = 1.0
        self.PuntPower_Potential = 1.0
        self.PuntAccuracy_Current = 1.0
        self.PuntAccuracy_Potential = 1.0
        self.KickPower_Current = 1.0
        self.KickPower_Potential = 1.0
        self.KickAccuracy_Current = 1.0
        self.KickAccuracy_Potential = 1.0

