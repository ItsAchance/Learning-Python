# Detta är en madlib som jag skapade 17-01-2022

print("Nu ska ni få åka på en resa genom ett helt fantastiskt program skapad av yours truly\n\nFyll i det som promptas så får vi se ifall det händer något skoj")

svar0 = input("Ett namn: ")
svar1 = input("En mening: ")
svar2 = input("Ett namn igen: ")
svar3 = input("Ett föremål(Ett): ")
svar4 = input("Ett föremål till(En): ")
svar5 = input("Ett annorlunda föremål(En): ")
svar6 = input("Ett annorlunda föremål till(Ett): ")
svar7 = input("Ett häftigt föremål(En): ")
svar8 = input("En hemsida: ")
svar9 = input("Ett verb: ")

linebreak = "\n\n"

madlib0 = f"Det var en helt vanlig dag, Morgan började dagen med att gå ut med Hector, till sin förvåning fick han se {svar0}. {svar0} tyckte Morgan såg konstig ut och sa {svar1}!."

madlib1 = f"Detsamma {svar0} svarade Morgan. Plöstligt ringde det i telefonen, det var {svar2} som ringde. Fuck, inte igen tänkte Morgan. Vad vill han denna gången?"

madlib2 = f"{svar2} höll på i vanlig ordning och ville ha ett {svar3} av Morgan. Det kan du ta och fixa själv sa Morgan och la på luren. Som en blixt från ovan blev Morgan akut \
skitnödig och han kunde inte hålla sig längre, han var tvungen att skita i en {svar4}."

madlib3 = f"Hoppas ingen ser mig nu sa Morgan samtidigt som Hector tittade snett på sin skitande husse. Utan toapapper hade Morgan inte mycket till val, \
han fick antingen ta en {svar5} eller ett {svar6}."

madlib4 = f"Med sina McGuyver skills så kombinerade han sin {svar5} och sitt {svar6} och fick en {svar7}. Nyskiten och glad så traskade Morgan och Hector vidare hemmåt."

madlib5 = f"När Morgan skulle starta sin jobbdator så fick han upp ett virusprogram efter att han varit inne på hemsidan {svar8} dagen innan, \
och innehållet låste hans dator. Det enda Morgan kunde göra nu var att {svar9} resten av dagen."


totallib = linebreak + madlib0 + linebreak + madlib1 + linebreak + madlib2 + linebreak + madlib3 + linebreak + madlib4 + linebreak + madlib5

print(totallib)
