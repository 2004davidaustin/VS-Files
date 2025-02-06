


code = ""
print("\n\n")



def cool(id, script, a="none", b="none", c="none"):
    global code
    if id == code and a != "none" :
            response = input("\n" + script + "\n").lower()
            if a in response : code += "a"
            elif b in response : code += "b"
            elif c in response : code += "c"
            else : print("\nYou spontaneously combusted")
    elif id == code and a == "none" : print(script)



cool("", '''
You are in your room and you are bored.
     
Do you CALL your not best but very appricated friend, or WAIT for something amazing to happen?
''', "call", "wait")


cool("a", '''
You call your not best but very appricated friend. He tells you he just got abducted by aliens
and he needs you to save him.

Do you steal a private jet and FLY to the mothership to save him, or do you CALL the police?
''', "fly", "call")

cool("aa", '''
You fly towards the mothership. This is just like space invaders. You dodge enemy ships and
break into the giant mother ship. You hop out of your plane and begin searching. You find three
doors, one says "FRIEND of human being containment cell", another says "definietly an EXIT and
totally not the real containment cell", and the last says "free FOOD."

Which do you go through?
''', "friend", "exit", "food")

cool("aaa", '''
You walk in to find your friend strapped to a table. The tall lanky aliens are doing strange experiments
to him. You fight them off with your amazing 7th grade judo skills. You break out, and fly off into the
sunset while your not best but very appricated friend uses the new superpowers the aliens accidentally
gave him to blow up the mothership. 
''')

cool("aab", '''
You walk through the door only to find that it was in fact and exit. You are now plummeting thousands
of feet to your death.
''')

cool("aac", '''
You decide to not help your friend and treat yourself to a wonderful meal. Behind the door is an all
you can eat 5 star chinese restraunt. Afterwards you went back home. You had a very pleasing afternoon.
''')



cool("ab", '''
You call the police. They say they can help. The police has a special alien defense division just for
these kinds of situations. However, you have to pay 1,000,000 U.S. dollars plus tax upfront before they
do anything.

Do you go into life altering DEBT to save your friend, or do you forgo saving your friend in order to
SUE the government for enacting such a stupid law?
''', "debt", "sue")

cool("aba", '''
The S.A.D. (special alien defense) division springs into action. They capture the alien space ship
and save your not best but very appricated friend. You now find yourself in crippling debt.
You have won. But at what cost?
''')

cool("abb", '''
You sue the governemnt and win billions of dollars in damages (it was a very stupid law.) You are now
one of the richest people on the planet, but at the expense of letting your friend go missing forever.
You have won. But at what cost?
''')







cool("b", '''
You wait in your room. Nothing happened. It got dark outside.

Do you RUN outside in a random direction for fun, or do you BARRICADE yourself inside your home from the 
imaginary demons?
''', "run", "barricade")

cool("ba", '''
You run outside for several hours until you run into homeless man Sam. He offers you a RED pill and a BLUE pill.
Which do you take?
''', "red", "blue")

cool("baa", '''
You take the pill and realize you're playing a weird choose your own adventure game made by a college student. Wow.
''')

cool("bab", '''
You take the pill. Suddenly the police show up out of nowhere and arrest you for taking illegal drugs from homeless
man Sam. You immediately regret your desicion, and wish you had followed the counsels of modern prophets to obey
the word of wisdom.
''')




cool("bb", '''
You barricade every window and door in your house. It was a good decision considering that it turns out that 
the demons are real. Now there's a horrifying lanky humanoid entity outside that's trying to break in. It's been
hours, but the figure is still clawing at the and door offering an extremely low intrest auto loan deal. It sounds
amazing, but you're sure it's just lying to convince you to come out.

Do you ACCEPT the entity's offer to buy the lamborghini you've always wanted, or do you CALL your mom?
''', "accept", "call")

cool("bba", '''
You accept the offer. It turns out he wasn't lying. You purchase a very tasteful hot pink lambo and drive it
into a lake because why not.
''')

cool("bbb", '''
You call your mom. She comforts you and gives you very good advice. The creature still breaks in and harvests your soul,
but at least you've finally spent some quality time talking to your mother after all of these years.
''')

print("\nTHE END\n\n")













'''

def wonk(id, script, a="none", b="none", c="none"):
    global code

    #print("\n*new wonk read") #TESTLINE
    #print("*id=" + id) #TESTLINE
    #print("*code=" + code) #TESTLINE

    if id == code and a == "none" : print(script)
    if id == code and a != "none" :
        #print("*Correct wonk found") #TESTLINE
        response = input("\n" + script + "\n").lower()
        if a in response : code += "a"
        if b in response : code += "b"
        if c in response : code += "c"
    #else : print("*wonk determined incorrect / end\n") #TESTLINE

'''