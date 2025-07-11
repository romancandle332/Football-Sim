class DefensivePlay:
    def __init__(self,x):
        ##Defining the basics
        self.FullName = "Lengthy Play Name"
        self.Formation = x
        if x == 0:
            self.FormationName = "4-3"
            self.BaseLine = 4
            self.BaseBackers = 3
            self.BaseCorners = 2
            self.BaseSafeties = 2

            ##What Positions are used?
            self.UseNT = False
            self.UseLDT = True
            self.UseRDT = False
            self.UseLDE = True
            self.UseRDE = True
            self.UseSam = False
            self.UseLOLB = True
            self.UseMike = False
            self.UseMLB = True
            self.UseWill = False
            self.UseROLB = True
            self.UseJack = False
            self.UseBandit = False
            self.UseCB1 = True
            self.UseCB2 = True
            self.UseCB3 = False
            self.UseCB4 = False
            self.UseCB5 = False
            self.UseSS1 = True
            self.UseSS2 = False
            self.UseFS1 = True
            self.UseFS2 = False
        elif x == 1:
            elf.FormationName = "Base 4 Nickel"
            self.BaseLine = 4
            self.BaseBackers = 2
            self.BaseCorners = 3
            self.BaseSafeties = 2

            ##What Positions are used?
            self.UseNT = False
            self.UseLDT = True
            self.UseRDT = False
            self.UseLDE = True
            self.UseRDE = True
            self.UseSam = False
            self.UseLOLB = False
            self.UseMike = False
            self.UseMLB = True
            self.UseWill = False
            self.UseROLB = True
            self.UseJack = False
            self.UseBandit = False
            self.UseCB1 = True
            self.UseCB2 = True
            self.UseCB3 = True
            self.UseCB4 = False
            self.UseCB5 = False
            self.UseSS1 = True
            self.UseSS2 = False
            self.UseFS1 = True
            self.UseFS2 = False
            
        elif x == :
            self.FormationName = "3-4"
            self.BaseLine = 3
            self.BaseBackers = 4
            self.BaseCorners = 2
            self.BaseSafeties = 2

            ##What Positions are used?
            self.UseNT = True
            self.UseLDT = False
            self.UseRDT = False
            self.UseLDE = True
            self.UseRDE = True
            self.UseSam = True
            self.UseLOLB = False
            self.UseMike = True
            self.UseMLB = False
            self.UseWill = True
            self.UseROLB = False
            self.UseJack = True
            self.UseBandit = False
            self.UseCB1 = True
            self.UseCB2 = True
            self.UseCB3 = False
            self.UseCB4 = False
            self.UseCB5 = False
            self.UseSS1 = True
            self.UseSS2 = False
            self.UseFS1 = True
            self.UseFS2 = False
        elif x == :
            elf.FormationName = "Base"
            self.BaseLine = 0
            self.BaseBackers = 0
            self.BaseCorners = 0
            self.BaseSafeties = 0

            ##What Positions are used?
            self.UseNT = False
            self.UseLDT = False
            self.UseRDT = False
            self.UseLDE = False
            self.UseRDE = False
            self.UseSam = False
            self.UseLOLB = False
            self.UseMike = False
            self.UseMLB = False
            self.UseWill = False
            self.UseROLB = False
            self.UseJack = False
            self.UseBandit = False
            self.UseCB1 = True
            self.UseCB2 = False
            self.UseCB3 = False
            self.UseCB4 = False
            self.UseCB5 = False
            self.UseSS1 = False
            self.UseSS2 = False
            self.UseFS1 = False
            self.UseFS2 = False
        else:
            self.FormationName = "Base"
            self.BaseLine = 0
            self.BaseBackers = 0
            self.BaseCorners = 0
            self.BaseSafeties = 0

            ##What Positions are used?
            self.UseNT = False
            self.UseLDT = False
            self.UseRDT = False
            self.UseLDE = False
            self.UseRDE = False
            self.UseSam = False
            self.UseLOLB = False
            self.UseMike = False
            self.UseMLB = False
            self.UseWill = False
            self.UseROLB = False
            self.UseJack = False
            self.UseBandit = False
            self.UseCB1 = True
            self.UseCB2 = False
            self.UseCB3 = False
            self.UseCB4 = False
            self.UseCB5 = False
            self.UseSS1 = False
            self.UseSS2 = False
            self.UseFS1 = False
            self.UseFS2 = False


        ##What Roles do they have?
        self.RoleNT = "N/A"
        self.RoleLDT = "N/A"
        self.RoleRDT = "N/A"
        self.RoleLDE = "N/A"
        self.RoleRDE = "N/A"
        self.RoleSam = "N/A"
        self.RoleLOLB = "N/A"
        self.RoleMike = "N/A"
        self.RoleMLB = "N/A"
        self.RoleWill = "N/A"
        self.RoleROLB = "N/A"
        self.RoleJack = "N/A"
        self.RoleBandit = "N/A"
        self.RoleCB1 = "N/A"
        self.RoleCB2 = "N/A"
        self.RoleCB3 = "N/A"
        self.RoleCB4 = "N/A"
        self.RoleCB5 = "N/A"
        self.RoleSS1 = "N/A"
        self.RoleSS2 = "N/A"
        self.RoleFS1 = "N/A"
        self.RoleFS2 = "N/A"        
