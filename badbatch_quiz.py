#badbatch quiz from only the show
print('Welcome to this fun quiz! There will be 20 questions in total.')
ask_play = input('Do you want to play this quiz? ')

if ask_play.lower() != 'yes':
    quit()

ask_starwars = input('Do you know anything about Star Wars: The Bad Batch? Answer with yes, no, a little. ')

if ask_starwars == 'yes':
    print('You may do very well!')
    print("Yay! Let's continue!")
if ask_starwars == 'no':
    print('You will struggle on this quiz.')
    print("But that's okay, let's continue!")
if ask_starwars == 'a little':
    print('You might need some luck.')
    print("There is no harm in trying, let's continue!")

count = 0

answer = input("1) What are the clone's home world called?" )
if answer.lower() == 'kamino' or answer.lower() == 'tipoca' or answer.lower() == 'tipoca city':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('2) What does Echo complain about when they arrive back to their barracks? ')
if answer.lower() == 'the smell' or answer.lower() ==  'smell' or answer.lower() == 'the fragrance' or answer.lower() == 'fragrance' or answer.lower() == 'the odor' or answer.lower() == 'odor':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('3) Who does the batch meet in the corridor? ')
if answer.lower() == 'omega':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input("4) What is the padawan that Hunter let escape? ")
if answer.lower() == 'caleb' or answer.lower() == 'caleb dume' or answer.lower() == 'kanan' or answer.lower() == 'kanan jarrus' or answer.lower() == 'jarrus':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('5) Which bad batch member sided with the Empire?')
if answer.lower() == 'crosshair':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('6) Who does the batch turn to in episode 2 for help with desertion? That is a big hint ')
if answer.lower() == 'cut' or answer.lower() == 'sue' or answer.lower() == 'cut and sue' or answer.lower() == 'cut lawquane':
    print('Correct')
    count += 1
else:
    print('Incorrect!')

answer = input("7) On Ord Mantell, who does the batch turn to for credits and missions? ")
if answer.lower() == 'cid':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input("8) What type of species is Muchi? ")
if answer.lower() == 'a rancor' or answer.lower() == 'rancor':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input("9) Which bad batch member aside from Crosshair executes order 66? ")
if answer.lower() == 'wrecker':
    print('Correct!')
    count += 1
else:
    print('Incorrect')

answer = input("10) What is the name of the criminal who took over Cid's parlor? ")
if answer.lower() == 'roland durand' or answer.lower() == 'roland' or answer.lower() == 'durand':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('11) What bounty hunter from The Mandalorian makes an appearance? ')
if answer.lower() == 'fennec shand' or answer.lower() == 'fennec' or answer.lower() == 'shand':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('12) Which Kaminoan is killed by Fennec Shand? ')
if answer.lower() == 'taun we':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('13) What question does Trace ask after Rafa repeats her statement? ')
if answer.lower() == 'is there an echo in here':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input("14) What is the name of the droid that assist the batch in escaping Kamino? ")
if answer.lower() == 'azi' or answer.lower() == 'azi-3' or answer.lower() == 'azi 3' or answer.lower() == 'azi-345211896246498721347':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input("15) What animal does Tech discover that lives under Cid's parlor? ")
if answer.lower() == 'irling' or answer.lower() == 'irlings':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('16) What is the name of the clone trooper that the batch rescue on Daro? ')
if answer.lower() == 'gregor':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('17) What food does Wrecker and Omega eat after every mission as their tradition? ')
if answer.lower() == 'mantell mix':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('18) What planet does the batch go to in order to save a Separatist? ')
if answer.lower() == 'raxus':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input("19) What clone decided to tell his brothers to lay down their weapons and disobey the Empire? ")
if answer.lower() == 'howzer':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

answer = input('20) Who appears on Ryloth as a child? Hint: They appeared in Rebels. ')
if answer.lower() == 'hera' or answer.lower() =='hera syndulla':
    print('Correct!')
    count += 1
else:
    print('Incorrect!')

print('')
print(count)
print('')
print('You scored', count, 'out of 20!')
if count >= 15:
    print("Not bad, for a reg. You know what your stuff. You might as well join the squad...if you're not a reg.")
elif 14 >= count >= 6:
    print('Eh, Wrecker would be disappointed. Go watch the show then try again.')
else:
    print('Why did you even bother taking this quiz? Tech might even call you unintelligent.')
print('')
print('Thanks for playing!')


