import pandas as pd

StateList = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho",
             "Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi",
             "Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio",
             "Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia",
             "Washington","West Virginia","Wisconsin","Wyoming","Canada"]

class School():
    def __init__(self,FullName,ShortName,Abbreviation,Nickname,State,City,PrimaryColor,SecondaryColor,StadiumName):
        ##User Inputted Values
        self.fullname = FullName
        self.shortname = ShortName
        self.abbreviation = Abbreviation
        self.nickname = Nickname
        self.state = State
        self.city = City
        self.primary_color = PrimaryColor
        self.secondary_color = SecondaryColor
        self.conference = "Independent"
        self.stadium_name = StadiumName
        self.stadium_capacity = 10000

        ##Generic Default Values
        self.wins_alltime = 0
        self.losses_alltime = 0
        self.conference_wins_alltime = 0
        self.conference_losses_alltime = 0
        self.playoff_wins = 0
        self.playoff_losses = 0
        self.conference_titles = 0
        self.national_titles = 0
        self.all_americans = 0
        self.player_awards = 0
        self.drafted_players = 0
        self.academics = 0
        self.crowd_noise = 0
        self.facilities = 0
        self.prestige = 0
        self.pro_prep = 0
        self.program_tradition = 0
        self.National_exposure = 0
        self.Regional_exposure = 0
        self.Alabama_exposure = 0
        self.Alaska_exposure = 0
        self.Arizona_exposure = 0
        self.Arkansas_exposure = 0
        self.California_exposure = 0
        self.Colorado_exposure = 0
        self.Connecticut_exposure = 0
        self.Delaware_exposure = 0
        self.Florida_exposure = 0
        self.Georgia_exposure = 0
        self.Hawaii_exposure = 0
        self.Idaho_exposure = 0
        self.Illinois_exposure = 0
        self.Indiana_exposure = 0
        self.Iowa_exposure = 0
        self.Kansas_exposure = 0
        self.Kentucky_exposure = 0
        self.Louisiana_exposure = 0
        self.Maine_exposure = 0
        self.Maryland_exposure = 0
        self.Massachusetts_exposure = 0
        self.Michigan_exposure = 0
        self.Minnesota_exposure = 0
        self.Mississippi_exposure = 0
        self.Missouri_exposure = 0
        self.Montana_exposure = 0
        self.Nebraska_exposure = 0
        self.Nevada_exposure = 0
        self.NewHampshire_exposure = 0
        self.NewJersey_exposure = 0
        self.NewMexico_exposure = 0
        self.NewYork_exposure = 0
        self.NorthCarolina_exposure = 0
        self.NorthDakota_exposure = 0
        self.Ohio_exposure = 0
        self.Oklahoma_exposure = 0
        self.Oregon_exposure = 0
        self.Pennsylvania_exposure = 0
        self.RhodeIsland_exposure = 0
        self.SouthCarolina_exposure = 0
        self.SouthDakota_exposure = 0
        self.Tennessee_exposure = 0
        self.Texas_exposure = 0
        self.Utah_exposure = 0
        self.Vermont_exposure = 0
        self.Virginia_exposure = 0
        self.Washington_exposure = 0
        self.WestVirginia_exposure = 0
        self.Wisconsin_exposure = 0
        self.Wyoming_exposure = 0
        self.Canada_exposure = 0
        self.International_exposure = 0

        state_conversion = State.replace(" ","")
        setattr(self,state_conversion+"_exposure",75)

old_schools = pd.read_csv('schools.csv')
loop = True
new_school_bucket = []
while loop == True:
    FullName = input("Full name of School?")
    ShortName = input("Short or Casual name of School?")
    Abbreviation = input("Abbreviation of School?")
    Nickname = input("Mascot of School?")
    state_control = True
    while state_control == True:
        State = input("What state/nation does the school reside in?")
        if State not in StateList:
            print("Sorry, I don't recognize that region. Please try again.")
        else:
            state_control = False
    City = input("What city does the school reside in?")
    PrimaryColor = input("What is the school's primary color?")
    SecondaryColor = input("What is the school's secondary color?")
    StadiumName = input("What is the name of the school's football stadium?")
    new_school_bucket.append(School(FullName,ShortName,Abbreviation,Nickname,State,City,PrimaryColor,SecondaryColor,StadiumName))
    again_question = True
    while again_question == True:
        another_school = input("Would you like to make another school?")
        if another_school in ["No","N","no","n","Stop","stop","S","s","False","false","f","false"]:
            print("Finishing.")
            loop = False
            again_question = False
        elif another_school in ["Yes","Y","yes","y","True","true","T","t","Go","G","go","g","another","Another","Again","again"]:
            again_question = False
        else:
            print("I didn't quite understand that. Please rememeber I'm a simple machine and answer in one word/letter responses.")

new_schools = pd.DataFrame([school.__dict__ for school in new_school_bucket])
combined_schools = pd.concat([old_schools,new_schools])
combined_schools.to_csv('schools.csv', index=False)