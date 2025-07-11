class DefensiveFormation():
    def __init__(self):
        self.ShortName = "Blank"
        self.LongName = "The Blank Blank"

        ##Setting the Position Groups
        self.DefensiveLine = []
        self.Linebackers = []
        self.Cornerbacks = []
        self.Safeties = []
        
        ##Setting the Run/Blitz Gap Assignments. Gaps are immediate bodies, second wave are folks who should be attacking the ball unless they misread the play
        self.AGapStrong = []
        self.AGapWeak = []
        self.BGapStrong = []
        self.BGapWeal = []
        self.CGapStrong = []
        self.CGapWeal = []
        self.DGapStrong = []
        self.DGapWeak = []
        self.EGapStrong = []
        self.EGapWeak = []
        self.SecondWaveMiddle = []
        self.SecondWaveStrong = []
        self.SecondWaveRight = []

        ##Defining Zone Assignments with a 6-wide grid.
        self.ZoneAvailable = []
        self.ZoneDeepStrong = [] 
        self.ZoneDeepMid = []
        self.ZoneDeepWeak = []
        self.ZoneMidStrong = []
        self.ZoneMidMid = []
        self.ZoneMidWeak = []
        self.ZoneShortStrong = []
        self.ZoneShortMid = []
        self.ZoneShortWeak = []

        ##Defining Man Assignments. 1v1, 2v2, 3v3, etc. Goes through  Plays will modify this.
        self.ManAvailable = []
        self.QBSpy = []

FourThree = DefensiveFormation()
FourThree.DefensiveLine = ["SDE","SDT","WDT","WDE"]
FourThree.Linebackers = ["SOLB","MLB","WOLB"]
FourThree.Cornerbacks = ["CB1","CB2"]
FourThree.Safeties = ["FS","SS"]