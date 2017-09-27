 #! python3
#!/usr/bin/env python

import random


capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
    'New York': 'Albany', 'North Carolina': 'Raleigh',                                                  
  	'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
 



for i in range(25):
	quizquestions=open('quiz%s.txt' % (i+1) ,'w' )
	answerslist=open('quiz_answers%s.txt' % (i+1) ,'w')

	quizquestions.write('Name:\n\nDate:\n\nRoll:\n\n')

	quizquestions.write((' '*21) + 'quizpaper%s\n\n' % (i+1))

	states=list(capitals.keys())
	random.shuffle(states)

	for j in range(50):
		correctanswer=capitals[states[j]]

		wronganswers=list(capitals.values())

		del wronganswers[wronganswers.index(correctanswer)]

		wronganswers=random.sample(wronganswers,3)

		answersforthisquestion=wronganswers + [correctanswer]

		random.shuffle(answersforthisquestion)

		
		quizquestions.write('%s. what is the capital of %s?\n' % (j+1, states[j] ))

		for k in range(4):

				quizquestions.write('%s. %s\n' % ( 'ABCD'[k], answersforthisquestion[k]))

		quizquestions.write('\n')

		answerslist.write('%s. %s\n' % ( j+1,'ABCD'[answersforthisquestion.index(correctanswer)]))

	quizquestions.close();

	answerslist.close();


     








