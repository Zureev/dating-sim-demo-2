init -9 python:

    class Toriel(Monster):
        def __init__(self):
            Monster.__init__(self)
            self.default_event = Event("Toriel_manager_default",True,0,self)
            self.default_room = "Toriel's Room"
            self.name = "Toriel"
            self.FP = 0
            self.seed_default_schedule()
            self.default_sprite = "toriel normal"
            self.d_1 = {"Decided to Stay" : False, "Day past 3": False}
            self.d_2 = {"FP > 20": False}
            self.d_3 = {"Plant watered 3 times" : False}
            self.d_4 = {"Mastered Flirting" : False}
            self.dating_requirements = {}
            self.cell_phone_pic = "UI/toriel_cell_face.png"
            self.talk_day = 0
        

        def handle_relationship_requirements(self):

            self.d_1 = {}
            self.d_2 = {}
            self.d_3 = {}
            self.d_4 = {}
            self.dating_requirements = {}

            yellow = "#ffff00"
            red = "#f00"
            green = "#00ff00"

            if 'Toriel_Friendship_1_Complete' in player.variables:
                self.d_1["Complete!"] = True
            elif world.day > 3 and 'accepted_toriel' in player.variables and player.variables['accepted_toriel']:
                self.d_1["Find Toriel!"] = False
            else:
                self.d_1["Accepted Your Bedroom"] = 'accepted_toriel' in player.variables and player.variables['accepted_toriel']
                self.d_1["Day > 3"] = world.day > 3

            if 'Toriel_Friendship_Hangout1' in player.variables:
                self.d_2 = {"Complete!" : True}
            elif get_toriel().FP > 20:
                self.d_2 = {"Find Toriel!" : False}
            else:
                self.d_2 = {"FP > 20": get_toriel().FP > 20}


            if 'Toriel_Friendship_Hangout1' in player.variables:
                self.d_3 = {"Complete!" : True}
            elif 'toriel_plant_watered_count' in player.variables and  player.variables['toriel_plant_watered_count'] >= 3:
                self.d_3 = {"Find Toriel!" : False}
            else:
                self.d_3 = {"Plant watered 3 times": 'toriel_plant_watered_count' in player.variables and  player.variables['toriel_plant_watered_count'] >= 3}
            
            if 'Toriel_Friendship_Hangout1' in player.variables:
                self.d_4 = {"Complete!" : True}
            elif 'Toriel_Flirts_Complete' in player.variables:
                self.d_4 = {"Find Toriel!" : False}
            else:
                self.d_4 = {"All Flirts Complete": 'Toriel_Flirts_Complete' in player.variables}


            if 'Toriel_Friendship_1_Complete' not in player.variables:
                self.dating_requirements["{color=%s}Sleep well?{/color}" % red] = self.d_1
            else:
                self.dating_requirements["{color=%s}Sleep well?{/color}" % green] = self.d_1

            if 'Toriel_Friendship_Hangout1' not in player.variables:
                self.dating_requirements["{color=%s}Doing Just Piene{/color}" % red] = self.d_2
            else:
                self.dating_requirements["{color=%s}Doing Just Piene{/color}" % green] = self.d_2

            if 'Toriel_Friendship_2_Complete' not in player.variables:
                self.dating_requirements["{color=%s}The Stunted Flower{/color}" % red] = self.d_3
            else:
                self.dating_requirements["{color=%s}The Stunted Flower{/color}" % green] = self.d_3

            if 'Toriel_TL_Date_1_Complete' not in player.variables:
                self.dating_requirements["{color=%s}If You Were A Fruit...{/color}" % red] = self.d_4
            else:
                self.dating_requirements["{color=%s}If You Were A Fruit...{/color}" % green] = self.d_4

            return


           
        def handle_special_events(self):

            #Friendship Event 1
                # Staying with Toriel
                # 3 nights have passed
            if 'Toriel_Friendship_1_Complete' not in player.variables:
                if 'accepted_toriel' in player.variables and player.variables['accepted_toriel'] and world.day > 3:
                    self.special_event = Event('toriel_friendship_event_1',False,0,self)
            #FP Hangout 1, time for pie
                #Friendship 1 done,
                #20 FP
                #Staying with Toriel
            elif 'Toriel_Friendship_1_Complete' in player.variables:
                if get_toriel().FP > 20 and 'accepted_toriel' in player.variables and player.variables['accepted_toriel'] and 'Toriel_Friendship_Hangout1' not in player.variables:
                    self.special_event = Event('toriel_friendship_hangout_1',False,0,self)
                    self.move_to_room("Kitchen")

        

            #Friendship Event 2
                #flower has bloomed
                #staying with Toriel
            elif 'Toriel_Friendship_2_Complete' not in player.variables and 'Toriel_Friendship_1_Complete' in player.variables:
                if 'toriel_plant_watered_count' in player.variables:
                    if player.variables['toriel_plant_watered_count'] >= 3 and world.day > player.variables['toriel_plant_watered_day']:
                        self.special_event = Event('toriel_friendship_event_2',False,0,self)

            #Date 1
                #Friendship 1 done
                #used up all flirts 
            elif 'Toriel_Friendship_1_Complete' in player.variables and 'Toriel_TL_Date_1_Complete' not in player.variables:
                if 'Toriel_Flirts_Complete' in player.variables:
                    self.special_event = Event('toriel_tl_date_1',False,0,self)
            else:
                self.remove_event()
            return
            

        def seed_default_schedule(self):
            self.reset_schedule() 
            #night
            self.update_schedule("Sunday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Monday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Tuesday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Wednesday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Thursday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Friday","Night","Toriel's Room",self.default_event)
            self.update_schedule("Saturday","Night","Toriel's Room",self.default_event)
            #morning
            self.update_schedule("Sunday","Morning","Kitchen",self.default_event)
            self.update_schedule("Monday","Morning","Kitchen",self.default_event)
            #self.update_schedule("Monday","Morning","Basement Door",self.default_event)
            self.update_schedule("Tuesday","Morning","Kitchen",self.default_event)
            self.update_schedule("Wednesday","Morning","Kitchen",self.default_event)
            self.update_schedule("Thursday","Morning","Kitchen",self.default_event)
            self.update_schedule("Friday","Morning","Kitchen",self.default_event)
            self.update_schedule("Saturday","Morning","Kitchen",self.default_event)
            #day
            self.update_schedule("Sunday","Day","Cave Room",self.default_event)
            #self.update_schedule("Monday","Day","",self.default_event)
            self.update_schedule("Tuesday","Day","Cave Room",self.default_event)
            #self.update_schedule("Wednesday","Day","",self.default_event)
            self.update_schedule("Thursday","Day","Cave Room",self.default_event)
            #self.update_schedule("Friday","Day","",self.default_event)
            self.update_schedule("Saturday","Day","Cave Room",self.default_event)
            #afternoon
            self.update_schedule("Sunday","Afternoon","Spider Bakery",self.default_event)
            self.update_schedule("Monday","Afternoon","Dummy Room",self.default_event)
            self.update_schedule("Tuesday","Afternoon","Sassy Rock Room",self.default_event)
            self.update_schedule("Wednesday","Afternoon","Dummy Room",self.default_event)
            self.update_schedule("Thursday","Afternoon","Sassy Rock Room",self.default_event)
            self.update_schedule("Friday","Afternoon","Dummy Room",self.default_event)
            self.update_schedule("Saturday","Afternoon","Sassy Rock Room",self.default_event)
            #evening
            self.update_schedule("Sunday","Evening","Toriel's Room",self.default_event)
            self.update_schedule("Monday","Evening","Living Room",self.default_event)
            self.update_schedule("Tuesday","Evening","Living Room",self.default_event)
            self.update_schedule("Wednesday","Evening","Toriel's Room",self.default_event)
            self.update_schedule("Thursday","Evening","Living Room",self.default_event)
            self.update_schedule("Friday","Evening","Toriel's Room",self.default_event)
            self.update_schedule("Saturday","Evening","Living Room",self.default_event)
            


label initialize_toriel:
        
    image toriel placeholder = "characters/Toriel/toriel_ph.png"
    image toriel angry = "characters/Toriel/Toriel_Angry.png"
    image toriel annoyed = "characters/Toriel/Toriel_Annoyed.png"
    image toriel awkward = "characters/Toriel/Toriel_Awkward.png"
    image toriel blushing = "characters/Toriel/Toriel_Blushing.png"
    image toriel laughing = "characters/Toriel/Toriel_Laughing.png"
    image toriel normal = "characters/Toriel/Toriel_Neutral.png"
    image toriel reallysad = "characters/Toriel/Toriel_ReallySad.png"
    image toriel sad = "characters/Toriel/Toriel_Sad.png"
    image toriel smallsmile = "characters/Toriel/Toriel_Small_Smile.png"
    image toriel smile = "characters/Toriel/Toriel_Smile.png"
    image toriel surprised = "characters/Toriel/Toriel_Surprised.png"


    define toriel = ('Toriel')
    define torielChar = Character('Toriel', color="#FFFFFF")
    python:
        def toriel(text, *args, **kwargs):
               torielChar(text, *args, **kwargs)
    return

#this is Toriels default scene
label Toriel_manager_default(owner = False,pause = True):
    
    call show_buttons from _call_show_buttons
    if renpy.music.get_playing() != "audio/ruins/toriel.mp3":
        play music "audio/ruins/toriel.mp3" fadein 5
    show toriel normal with Dissolve(.25)
    # if owner.FP < 20:
    #     show toriel reallysad with Dissolve(.25)
    # elif owner.FP < 40:
    #     show toriel awkward with Dissolve(.25)
    # elif owner.FP < 60:
    #     show toriel normal with Dissolve(.25)
    # elif owner.FP < 80:
    #     show toriel laughing with Dissolve(.25)
    # else:
    #     show toriel blushing with Dissolve(.25)

    if pause:
        $renpy.pause()
    
    if owner.talk_day != world.day:
        $ owner.chat_count = 0
        $ owner.flirt_count = 0
        $ owner.talk_day = world.day

    toriel "Hello, dear. Can I help you?"

    if 'has_toriel_cell' not in player.variables:
        toriel "Oh! Is that a CELL?"
        toriel "Can I see it for a second?"
        "* Toriel fumbles around with the buttons for a little longer than is comfortable."
        toriel "There!"
        play sound "audio/sfx/use_item.wav"
        "You got Toriel's Number!"
        $ player.variables['has_toriel_cell'] = True
        toriel "Do not hesitate to call me if you need me!"
    
    menu:
        
        "Hello, dear. Can I help you?"
        '"I brought you some snails!"' if player.current_snails > 0:
            call Toriel_Manager_Give_Snails
            $ world.add_to_ac(2)

        "Chat" if owner.chat_count < 4:
            call Toriel_Manager_Chat(owner)
            $ world.add_to_ac(2)

        "Ask":
            call Toriel_Manager_Ask
            $ world.add_to_ac(2)

        "Flirt" if owner.flirt_count < 4:
            call Toriel_Manager_Flirt
            $ world.add_to_ac(2)

        "Gift" if len(inventory.items) > 0:
            show screen gift_item_menu(owner)
            "What should you give them?"
            $ world.add_to_ac(10)
            
        # "Testing":
        #     menu:
        #         "Hurt her heart":
        #             $world.get_monster('Toriel').update_HP(-10)
        #             show toriel angry with hpunch
        #             show toriel normal
        #         "Increase Friendship Points":
        #             $world.get_monster('Toriel').update_FP(10)
        #         "Decrease Friendship Points":
        #             $world.get_monster('Toriel').update_FP(-10)
        #         "True Love Date 1":
        #             call toriel_tl_date_1
        #         "Friendship Event 1":
        #             call toriel_friendship_event_1
        #         "Friendship Event 2":
        #             call toriel_friendship_event_2
        #         "Friendship Hangout":
        #             call toriel_friendship_hangout_1
        #         "Back":
        #             return

        "Leave":
            toriel "Take care, dear."

    
    return



label Toriel_Manager_Chat(owner=False):

    if owner.chat_count == 0:
        '"How are you doing?"'
        call toriel_gd_howdoing

    if owner.chat_count == 1:
        '"What’s crackin’?"'
        show toriel awkward with Dissolve(.25)
        toriel "... I don’t believe anything is cracking... Did you hear something breaking? Oh dear, is it that rock again?"

    if owner.chat_count == 2:
        '"\'Sup?"'
        call toriel_gd_sup

    if owner.chat_count == 3:
        '"What have you been doing lately?"'
        show toriel smallsmile with Dissolve(.25)
        toriel "Not much, just the usual. Watching over Frisk, baking, the occasional snail hunting. Although I have also been having a wonderful time with you."

    $ owner.chat_count += 1
    return

label toriel_gd_howdoing:
    show toriel smile with Dissolve(.25)
    toriel "I am doing well! Thank you for asking. How are you doing, dear?"
    menu:
         "I'm good, thanks.":
             show toriel smile with Dissolve(.25)
             toriel "That is good to hear."
         "Better now that I'm talking to you.":
             show toriel blushing with Dissolve(.25)
             toriel "Oh! Well, I am glad I could brighten your day!"
    return

label toriel_gd_sup:
    show toriel awkward with Dissolve(.25)
    toriel "... ‘Sup’? Is... Is that a surface word? I am sorry, but I am not familiar with it."
    menu:       #Once you've explained it, should she give a different dialogue?
        "Oh! Sorry. It stands for ‘What is up’, which is a commonly used greeting on the surface.":
            show toriel smile with Dissolve(.25)
            toriel "Ah, I see! Thank you for explaining so well."
            show toriel smallsmile with Dissolve(.25)
            toriel "Well, I suppose I shall also ask you, ‘sup’?"
        "It means ‘what’s up’.":
            show toriel awkward with Dissolve(.25)
            toriel "Oh... Ah... The ceiling, I suppose... Although I think I might see a spider up there."
        "You seriously don’t know what ‘sup’ means?!":
            show toriel awkward with Dissolve(.25)
            toriel "Oh... Should I know? I am... I am sorry dear, but I do not..."
    return

label Toriel_Manager_Give_Snails:
    show toriel smile with Dissolve(.25)
    toriel "Thank you so much dear."
    if player.current_snails == 1:
        "* Toriel takes the lone snail from your inventory."
    else:
        "* Toriel takes the [player.current_snails] snails from your inventory."

    toriel "Here, please take this as a thank you."
    "* Toriel hands you [player.current_snails] gold."
    $ player.gold += player.current_snails
    $ player.current_snails = 0
    return

label Toriel_Manager_Flirt:
    $ Toriel = get_monster("Toriel")
    if Toriel.flirt_count == 0:
        '"Do you have a compass? Because I keep getting lost in your eyes."'
        show toriel surprised with Dissolve(.25)
        toriel "Oh!"
        show toriel laughing with Dissolve(.25)
        toriel "Ahahahaha!"
        show toriel blushing with Dissolve(.25)
        toriel "My, you caught me off guard with that! I honestly do not know what to say... Perhaps... I could {i}map{/i} out a way for you?"
        show toriel laughing with Dissolve(.25)
        toriel "Hehehehe!"

    elif Toriel.flirt_count == 1:
        '"I love the way your fur looks in the ruins light."'
        show toriel blushing
        toriel "Oh! Ah... Thank you! Thank you very much, dear. That was very... Very kind of you to say! ...You are looking nice yourself! Hehehe!"
    elif Toriel.flirt_count == 2:
        '"Butterscotch Pie has got nothing on you in sweetness"'
        show toriel blushing
        toriel "Oh my... I am... I am at quite a loss for words... Th-thank you dear. That was very... Well... Sweet of you!"
    elif Toriel.flirt_count == 3:
        '"Are you using fire magic right now? Because you’re warming my heart."'
        show toriel blushing
        toriel "Oh dear... You’re making me so flustered... Thank... Thank you dear! I am... So glad I could make you feel happy!"
        $ player.variables['Toriel_Flirts_Complete'] = True
    #else have a default flirt that keeps repeating?
    $ Toriel.flirt_count += 1
    return
    

label Toriel_Manager_Ask:
    #Friendship level neutral options:
    menu:
        "What do you do for fun?":
            show toriel smile with Dissolve(.25)
            toriel "Usually, I like to read, bake, and hunt for bugs. I know it does not sound like much, but it’s just perfect for me."

        "Do you have a job?":
            show toriel smallsmile with Dissolve(.25)
            toriel "Not at the moment... Unless you count taking care of Frisk."
            show toriel surprised with Dissolve(.25)
            toriel "Not in a bad way, I hope you understand!"
            show toriel smallsmile with Dissolve(.25)
            toriel "Frisk is wonderful, but they are still a teenager. Hehehe!"

        "How long have you lived in the Ruins?":
            jump toriel_gd_askLivedRuins

        "What's your favorite thing to bake?":
            show toriel smallsmile with Dissolve(.25)
            toriel "Well, I do very much enjoy making Butterscotch Pie. However, if I manage to find enough snails, Snail Pie is something I love to make as well." 
            toriel "Frisk seems to like Butterscotch more than Snail, however. So I try not to make Snail Pie too often."
            toriel "I have also been known to make the occasional cake."

        "How’s Frisk treating you?":
            show toriel smallsmile with Dissolve(.25)
            toriel "Ah, Frisk's arrival has been a true blessing. They are a very conscientious child."
            toriel "They help me with cooking, do chores without complaining, and they are kind to the other residents of the ruins."
            toriel "Really, I have nothing to complain about. They are the most wonderful child I could ever ask for."

        "What do you think of Napstablook?":
            show toriel normal with Dissolve(.25)
            toriel "I think that they are... Well, I can not have a real opinion of them because they never talk to me."
            toriel "They are particularly shy, so I try not to bother them. But I hope one day I can join them in a real conversation. Maybe even invite them over!"

        #"What kind of snails to you want today?":
            #Mondays and  Tuesdays
            #toriel “If you could, I would really like the green snails that carry around a house on their back.”
            #Wednesdays and Thursdays
            #toriel “If it is no trouble, could you please gather as many rocket snails as you can?”
            #Fridays
            #toriel “If it is possible, I would really like for you to catch the blue snails with glasses, or perhaps the red ones that like coffee too much?”
            #Saturday and Sunday
            #toriel “I am afraid I do not need any specific kind of snail today, dear. Any will do just fine.”


    return
    
label toriel_gd_askLivedRuins:
    show toriel awkward with Dissolve(.25)
    toriel "... A while."
    menu:
        "Oh, okay.":
            show toriel awkward with Dissolve(.25)
            toriel "..."
            show toriel normal with Dissolve(.25)
            toriel "I do hope you’re enjoying your stay here!"
        "What’s wrong?":
            show toriel awkward with Dissolve(.25)
            toriel "... It is nothing, dear. But thank you for your concern."
        "How long is ‘a while’?":
            show toriel awkward with Dissolve(.25)
            toriel "... I do not remember. It is not important, anyway."
    return
