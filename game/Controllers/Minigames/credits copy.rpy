#Please ignore this file.  It shouldnt exist.  Why did I spend time making this.  Its a bad joke.


init python:
    title_text = "Credits!"
    credit_text = ["Voice Actor\n","Writers\n","Artists\n"]
    coders_text = ["AnnAisu\n","Chloekat1things (Cece)\n","lzuehsow\n","PayneGray\n","SesuRescue\n"]
    leadership_text = ["Al\n","Blue\n","Becca\n","Louie\n","Nekomayata\n","Sky\n","Wilson\n"]
    audio_text = ["Mitsuko\n","Anna Mangette\n","X2H\n"]
    artist_text = ["LMaruchartista\n","Marci Nehlsen\n","Agenthisui\n","BloodyDragon117\n","Bielek\n","JRO\n","Mint\n","Betraeyal\n"]
    writers_text = ["CelestialSushi\n","Felix\n","Jeffrey\n","Kate\n","Nevran\n","Quinn\n","Riza\n","Ronnie\n","Rose\n","Sage\n","Sam\n","Vunde\n"]
    voice_text = ["Oolay-Tiger\n","Deathykloak\n","Zen\n","Anti-Hero\n"]
    testers_text = ["Markus The Xeno\n","sophisticatedmarten\n","Oxius\n","Kello\n","Richarad\n","Elis\n","ChaosTheLegend\n","InsanelyADD\n","Kurosidad\n","Sakura\n","Stone\n","Auntie Diluvian\n","Foxgloves\n","ChaosAirlines\n","GoldenScale\n","Ayahne\n"]
    credit_speed = 25
    credit_gap = 10
    movecenter = Move((.5,2),(0.5,0.0), credit_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    moveleft = Move((.33,1),(0.33,0.0), credit_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    moveright = Move((.66,1),(0.66,0.0), credit_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    titlecenter = Move((.5,1),(.5,0.0), credit_speed, repeate =False, bounce = False, xanchor="center",yanchor="bottom")

init:
    image sans_cred = Text(["{size=30}Sans\n"] + credit_text, text_align=0.5)
    image coder_cred = Text(["{size=50}Coders\n{/size}{size=30}"] + coders_text, text_align=0.5)
    image writer_cred = Text(["{size=50}Writers\n{/size}{size=30}"] + writers_text, text_align=0.5)
    image audio_cred = Text(["{size=50}Audio\n{/size}{size=30}"] + audio_text, text_align=0.5)
    image artist_cred = Text(["{size=50}Artists\n{/size}{size=30}"] + artist_text, text_align=0.5)
    image leader_cred = Text(["{size=50}Leadership\n{/size}{size=30}"] + leadership_text, text_align=0.5)
    image tester_cred = Text(["{size=50}Testers\n{/size}{size=30}"] + testers_text, text_align=0.5)
    image begin = Text("{size=80}Project UDS \n {size=40} inLove : An Undertale Dating Simulator\n", text_align =0.5)
    image end = Text("Thanks for Playing!",text_align = .5)



label scrolling_credits:
    
    #play music "audio/music/megalovania.mp3"
    scene black
    

    show begin at titlecenter
    with Pause(credit_gap)

    show coder_cred at movecenter
    with Pause(credit_gap*1.1)
    show writer_cred at movecenter
    with Pause(credit_gap)
    show audio_cred at movecenter
    with Pause(credit_gap)
    show artist_cred at movecenter
    with Pause(credit_gap*1.5)
    show tester_cred at movecenter
    with Pause(credit_gap)
    show leader_cred at movecenter
    with Pause(credit_gap*1.3)
    #show sans_credit at moveright
    
    
    # show toriel_cred at moveright
    # show toriel_credit at moveleft
    # with Pause(credit_gap)

    


    show end at Move((.5,1),(0.5,0.5), credit_speed*.7, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credit_gap*10)

    return