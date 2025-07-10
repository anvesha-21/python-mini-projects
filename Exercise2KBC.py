# Create a program capable of diaplaying questions to user like KBC.


print("**********************************************************************DEVIYO aur SAJJANO SWAGAT HAI AAPKA *******************************************************")
print("***************************************************************************KON BANEGA CROREPATI MAI**************************************************************")
string = input("  Aapka Subh Naam :- ")
print("Hello.." , string)
print("Welcome to Kaun Banega Crorepati – where every answer brings you closer to your crore-dream!\n\n")

print("""Aapke paas 4 vikalp hain...
Option 1 se leke Option 4 tak.
Apna uttar chuniye — aur agar aap khel chhodna chahein, toh 0 dabaiye:- \n""")




questions =[

["Q1. Which language was used to create Facebook?" , "Python" , "French" , "Hindi" , "Php" , "None" , 4],

["Q2. Who was the first Indian to win an individual Olympic gold medal? " , "Leander Paes" ,"Abhinav Bindra" ,  "Rajyavardhan Singh Rathore" , "Karnam Malleswari" , 2 ] , 

["Q3. In which year did the Battle of Buxar take place?" , "1757" , "1761" ,  "1764" , "1775" , 3],

["Q4.Who is credited with the discovery of the neutron" , "James Chadwick" ,  "Ernest Rutherford" , "JJ.Thomson" ,  "Niels Bohr" , 1],

["Q5. Which Indian classical musician was awarded Bharat Ratna in 1999 posthumously?" , "Bismillah Khan" ,  "M.S Subbulakshmi" , "Pandit Ravi Shankar" , "Amjad Ali Khan" , 3],

["Q6.Who was the first Prime Minister of independent India?" , ". Subhas Chandra Bose" , " Jawaharlal Nehru" , ". Mahatma Gandhi" , "Dr. Rajendra Prasad" , 2 ],

["Q7.What movement did Mahatma Gandhi launch in 1942?", "Non-Cooperation Movement" , "Salt March" , "Quit India Movement" , "Swadeshi Movement" , 3],

["Q8.Which Article of the Indian Constitution grants special status to Jammu and Kashmir (before 2019)?", ". Article 356" , "Article 360" , ". Article 370" , ". Article 42" , 3 ],

["Q9.Who was the first woman Prime Minister of India?" , "Sarojini Naidu" , " Indira Gandhi" , ". Pratibha Patil" , " Sushma Swaraj" , 2],

["Q10.Which Indian freedom fighter formed the Indian National Army (INA)?", "Bhagat Singh" , ". Subhas Chandra Bose" , "Sardar Vallabhbhai Patel" , " Jawaharlal Nehru" , 2],

["Q11.Who was the President of India during the Emergency (1975-77)?", " V.V. Giri" , ". Dr. Rajendra Prasad" , "Fakhruddin Ali Ahmed" , "R. Venkataraman" ,3 ],

["Q12.Which Indian Act first gave a limited franchise to Indians in British India?", "Regulating Act, 1773" , "Charter Act, 1833" , "Government of India Act, 1919" , ". Government of India Act, 1935" ,3 ],

["Q13.The Simon Commission was boycotted by Indians because:", " It had too many Indians" , " It was appointed during war" , " It had no Indian member" , " It was headed by a viceroy" ,3 ],

["Q14.The first Indian Governor-General of independent India was:", " Lord Mountbatten" , "Dr. B.R. Ambedkar" , " C. Rajagopalachari" , "S. Radhakrishnan" , 3],

["Q15.Q: Which of the following leaders was not present in the Constituent Assembly of India on 26th November 1949, the day the Constitution was adopted?", " Dr. B.R. Ambedkar" , "Jawaharlal Nehru" , ". Mahatma Gandhi" , "Dr. Rajendra Prasad" , 3],


] 

levels = [1000 , 2000 , 3000 , 5000 , 10000 , 20000 , 40000 , 80000 , 160000 , 320000 , 640000 , 1250000 , 2500000 , 5000000 , 10000000]
money = 0


for i  in range (0 , len (questions)):
    question = questions[i]
    print("")
    print(f"Question for Rs.{levels[i]}")
    print(question[0])
    print(f"a.{question[1]}")                
    print(f"b.{question[2]}")   
    print(f"c.{question[3]} ")         
    print(f"d.{question[4]}\n")   
    reply = int(input("Answer Your Question:-"))
    
    if(reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(f"Correct answer , you have won Rs.{levels[i]}\n")
        if (i==4):
            money = 10000
        elif(i==9):
            money = 320000
        elif(i==14):
            money = 10000000

    else:
        print("Wrong Answer!")
        break


print(f"AAPNE JITTE HAI {money}")
