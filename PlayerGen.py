import math
import random
import pandas as pd

class Player():
    def __init__(self,firstname,lastname,suffix,position,potential):
        self.FirstName = firstname
        self.LastName = lastname
        self.Suffix = suffix
        if self.Suffix == "":
            self.FullName = self.FirstName + " " + self.LastName
        else:
            self.FullName = self.FirstName + " " + self.LastName + " " + self.Suffix
        self.Age = 18
        self.HeightFt = 5
        self.HeightIn = 11
        self.Weight = 180
        self.Hometown = "Springfield"
        self.Homestate = "USA"
        self.Hand = "Right"
        self.Position = "ATH"
        self.PlayerStyle = ""
        self.Abilities = []
        self.Overall_Current = 1.0
        self.Overall_Potential = float(potential)
        self.Speed_Current = 1.0 ##Straight line speed
        self.Speed_Potential = 1.0
        self.Agility_Current = 1.0 ##Ability to change direction
        self.Agility_Potential = 1.0
        self.Jumping_Current = 1.0 ##Ability to high-point catches
        self.Jumping_Potential = 1.0
        self.ThrowStrength_Current = 1.0 ##Low underthrows deep passes and is more likely to be picked off, High causes more drops
        self.ThrowStrength_Potential = 1.0
        self.ThrowAccuracy_Current = 1.0 ##Ability to throw a catchable ball
        self.ThrowAccuracy_Potential = 1.0
        self.ThrowTouch_Current = 1.0 ##Ability to place the ball. Low lowers completion rate, yards after catch. High lowers drops and raises yards after catch.
        self.ThrowTouch_Potential = 1.0
        self.ThrowVision_Current = 1.0 ##Ability to determine if a player is open
        self.ThrowVision_Potential = 1.0
        self.PocketAwareness_Current = 1.0 ##Ability to feel the pass rush
        self.PocketAwareness_Potential = 1.0
        self.PlayAction_Current = 1.0 ##Ability to fool the defense
        self.PlayAction_Potential = 1.0
        self.Carrying_Current = 1.0 ##Ability to avoid fumbling
        self.Carrying_Potential = 1.0
        self.BreakTackle_Current = 1.0 ##Ability to break a tackle (any way)
        self.BreakTackle_Potential = 1.0
        self.RunVision_Current = 1.0 ##Also used as option ability for QBs
        self.RunVision_Potential = 1.0
        self.Catching_Current = 1.0 ##Ability to catch a pass
        self.Catching_Potential = 1.0
        self.ContestCatching_Current = 1.0 ##Ability to catch a pass in traffic or before being hit
        self.ContestCatching_Potential = 1.0
        self.RouteRunning_Current = 1.0 ##How well they run a route to create separation
        self.RouteRunning_Potential = 1.0
        self.Release_Current = 1.0 ##How well they start their route and beat press coverage
        self.Release_Potential = 1.0
        self.PassBlocking_Current = 1.0 ##Ability to prevent a defender from going past them
        self.PassBlocking_Potential = 1.0
        self.RunBlocking_Current = 1.0 ##Ability to push a defender backwards
        self.RunBlocking_Potential = 1.0
        self.Tackling_Current = 1.0 ##Ability to break the ballcarrier down
        self.Tackling_Potential = 1.0
        self.HitPower_Current = 1.0 ##Ability to cause fumbles and drops by hitting hard
        self.HitPower_Potential = 1.0
        self.SpeedRush_Current = 1.0 ##Ability to get around a blocker
        self.SpeedRush_Potential = 1.0
        self.PowerRush_Current = 1.0 ##Ability to push a blocker backwards or over
        self.PowerRush_Potential = 1.0
        self.BlockShedding_Current = 1.0 ##Ability to get off a block (to chase a carrier who ran past you)
        self.BlockShedding_Potential = 1.0
        self.PressCoverage_Current = 1.0 ##Ability to jam the receiver at the line
        self.PressCoverage_Potential = 1.0
        self.ManCoverage_Current = 1.0 ##Ability to follow a receiver across the field
        self.ManCoverage_Potential = 1.0
        self.ZoneCoverage_Current = 1.0 ##Ability to patrol a patch of field and cover who comes into it
        self.ZoneCoverage_Potential = 1.0
        self.PuntPower_Current = 1.0 ##Power behind a drop kick
        self.PuntPower_Potential = 1.0
        self.PuntAccuracy_Current = 1.0 ##Ability to aim a drop kick
        self.PuntAccuracy_Potential = 1.0
        self.KickPower_Current = 1.0 ##Power behind a place kick
        self.KickPower_Potential = 1.0
        self.KickAccuracy_Current = 1.0 ##Ability to aim a place kick
        self.KickAccuracy_Potential = 1.0
        self.Injury_Current = 1.0 ##How likely they are to be injured/How many "BIG HIT"s can they take before they retire at the end of the season? Pro Only
        self.Injury_Potential = 1.0

        Primary_Bucket = [] ##Skills that define how the player should play within the system. Max 2.
        Secondary_Bucket = [] ##Skills that support the position and archetype
        Tertiary_Bucket = [] ##Skills inherient to the position that are weaknesses of the archetype
        Quaternary_Bucket = [] ##Skills inherient to the position that are considered significant weaknesses.
        Support_Bucket = [] ##Skills that are generated differently
        archetype_roll = random.randint(0,59)
        if position == "QB":
            if archetype_roll % 6 == 0:
                self.PlayerStyle = "Gunslinger" ##Big Arm, Runs Around
                Primary_Bucket.extend(["Throw Strength","Agility"])
                Secondary_Bucket.extend(["Throw Vision","Pocket Awareness","Break Tackle"])
                Tertiary_Bucket.extend(["Throw Accuracy","Play Action","Speed","Run Vision"])
                Quaternary_Bucket.extend(["Throw Touch"])
                Support_Bucket.extend(["Injury","Carrying"])
            elif archetype_roll % 6 == 1:
                self.PlayerStyle = "Distributor" ##Gets the ball anywhere on the field
                Primary_Bucket.extend(["Throw Strength","Throw Accuracy"])
                Secondary_Bucket.extend(["Pocket Awareness","Throw Touch","Throw Vision"])
                Tertiary_Bucket.extend(["Play Action","Speed","Agility","Run Vision"])
                Quaternary_Bucket.extend(["Break Tackle"])
                Support_Bucket.extend(["Injury","Carrying"])
            elif archetype_roll % 6 == 2:
                self.PlayerStyle = "West Coast" ##Passers with lower arm strength , but better accuracy and touch
                Primary_Bucket.extend(["Throw Accuracy","Throw Touch"])
                Secondary_Bucket.extend(["Pocket Awareness","Play Action","Throw Vision"])
                Tertiary_Bucket.extend(["Agility","Speed","Break Tackle","Run Vision"])
                Quaternary_Bucket.extend(["Throw Strength"])
                Support_Bucket.extend(["Injury","Carrying"])
            elif archetype_roll % 6 == 3:
                self.PlayerStyle = "Hybrid" ##Try to be a mix of everything
                Primary_Bucket.extend(["Throw Accuracy","Agility"])
                Secondary_Bucket.extend(["Throw Strength","Throw Vision","Run Vision"])
                Tertiary_Bucket.extend(["Speed","Pocket Awareness","Play Action","Break Tackle"])
                Quaternary_Bucket.extend(["Throw Touch"])
                Support_Bucket.extend(["Injury","Carrying"])
            elif archetype_roll % 6 == 4:
                self.PlayerStyle = "Dual Threat" ##Can terrorize the defense with their arms and legs
                Primary_Bucket.extend(["Throw Strength","Speed"])
                Secondary_Bucket.extend(["Agility","Break Tackle","Run Vision"])
                Tertiary_Bucket.extend(["Throw Vision","Throw Touch","Play Action","Throw Accuracy"])
                Quaternary_Bucket.extend(["Pocket Awareness"])
                Support_Bucket.extend(["Injury","Carrying"])
            elif archetype_roll % 6 == 5:
                self.PlayerStyle = "Scrambler" ##A Quarterback who's primary threat is on the ground
                Primary_Bucket.extend(["Speed","Agility"])
                Secondary_Bucket.extend(["Break Tackle","Throw Strength","Run Vision"])
                Tertiary_Bucket.extend(["Throw Touch","Pocket Awareness","Play Action","Throw Vision"])
                Quaternary_Bucket.extend(["Throw Accuracy"])
                Support_Bucket.extend(["Injury","Carrying"])
        elif position == "HB":
            if archetype_roll % 4 == 0:
                self.PlayerStyle = "Receiving" ##Halfbacks who specialize in being a receiving option out of the backfield and pass blocking
                Primary_Bucket.extend(["Catching","Agility"])
                Secondary_Bucket.extend(["Speed","Pass Blocking","Route Running"])
                Tertiary_Bucket.extend(["Carrying","Break Tackle"])
                Quaternary_Bucket.extend(["Run Vision"])
                Support_Bucket.extend(["Injury"])
            elif archetype_roll % 4 == 1:
                self.PlayerStyle = "Downhill" ##Security and Power at the cost of speed
                Primary_Bucket.extend(["Carrying","Break Tackle"])
                Secondary_Bucket.extend(["Run Vision","Pass Blocking","Agility"])
                Tertiary_Bucket.extend(["Catching","Route Running"])
                Quaternary_Bucket.extend(["Speed"])
                Support_Bucket.extend(["Injury"])
            elif archetype_roll % 4 == 2:
                self.PlayerStyle = "Elusive" ##Halfbacks who focus on pure speed and athlecitism, at cost of strength
                Primary_Bucket.extend(["Speed","Agility"])
                Secondary_Bucket.extend(["Carrying","Run Vision","Break Tackle"])
                Tertiary_Bucket.extend(["Route Running","Catching"])
                Quaternary_Bucket.extend(["Pass Blocking"])
                Support_Bucket.extend(["Injury"])
            elif archetype_roll % 4 == 3:
                self.PlayerStyle = "Tailback" ##Halfbacks who line up deep, ready to attack any rushing lane
                Primary_Bucket.extend(["Run Vision","Carrying"])
                Secondary_Bucket.extend(["Speed","Agility","Break Tackle"])
                Tertiary_Bucket.extend(["Route Running","Catching"])
                Quaternary_Bucket.extend(["Catching"])
                Support_Bucket.extend(["Injury"])
        elif position == "FB":
            if archetype_roll % 3 == 0:
                self.PlayerStyle = "" 
                Primary_Bucket.extend([""])
                Secondary_Bucket.extend([""])
                Tertiary_Bucket.extend([""])
                Quaternary_Bucket.extend([""])
                Support_Bucket.extend(["Injury"])
        elif position == "WR":
            if archetype_roll % 5 == 0:
                self.PlayerStyle = "Deep Threat" ##Players who are great at running deep routes
                Primary_Bucket.extend(["Speed","Release"])
                Secondary_Bucket.extend(["Agility","Route Running","Jumping"])
                Tertiary_Bucket.extend(["Catching","Break Tackle","Carrying"])
                Quaternary_Bucket.extend(["Contested Catching"])
                Support_Bucket.extend(["Injury"])
            elif archetype_roll % 5 == 1:
                self.PlayerStyle = "Possession" ##Players who focus on running good routes and catching the ball.
                Primary_Bucket.extend(["Route Running","Catching"])
                Secondary_Bucket.extend(["Release","Contested Catching","Jumping"])
                Tertiary_Bucket.extend(["Break Tackle","Agility","Carrying"])
                Quaternary_Bucket.extend(["Speed"])
                Support_Bucket.extend(["Injury"])
            elif archetype_roll % 5 == 2:
                self.PlayerStyle = "Jump Ball" ##Players who are acceptable at highpointing catches and catching in traffic.
                Primary_Bucket.extend(["Jumping","Contested Catching"])
                Secondary_Bucket.extend(["Catching","Route Running","Agility"])
                Tertiary_Bucket.extend(["Speed","Carrying","Release"])
                Quaternary_Bucket.extend(["Break Tackle"])
                Support_Bucket.extend(["Injury"])
            elif archetype_roll % 5 == 3:
                self.PlayerStyle = "Route Runner" ##Players who focus on the fundamentals of route running while maintaining athleticism
                Primary_Bucket.extend(["Route Running","Speed"])
                Secondary_Bucket.extend(["Agility","Catching","Release"])
                Tertiary_Bucket.extend(["Jumping","Carrying","Contested Catching"])
                Quaternary_Bucket.extend(["Break Tackle"])
                Support_Bucket.extend(["Injury"])
            elif archetype_roll % 5 == 4:
                self.PlayerStyle = "Weapon" ##Players who are good with the balls in their hand
                Primary_Bucket.extend(["Speed","Agility"])
                Secondary_Bucket.extend(["Catching","Break Tackle","Carrying"])
                Tertiary_Bucket.extend(["Jumping","Contested Catching","Release"])
                Quaternary_Bucket.extend(["Route Running"])
                Support_Bucket.extend(["Injury"])
        self.Primary_Skills = Primary_Bucket
        self.Secondary_Skills = Secondary_Bucket
        self.Tertiary_Skills = Tertiary_Bucket
        self.Quaternary_Skills = Quaternary_Bucket
        self.Support_Skills = Support_Bucket