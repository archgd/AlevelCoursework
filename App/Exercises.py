import random
#make into CSV file
exercises_legs = []
exercises_arms = []
exercises_biceps = ["Bicep Curl", "Hammer Curl", "Barbell Curl", "Incline Dumbbell Curl"]
exercises_triceps = []
exercises_back = []
exercises_shoulders = []
exercises_chest = []

exercises_arms.append(exercises_triceps)
exercises_arms.append(exercises_biceps)

random_even_number = random.randrange(6, 17, 2)

exercises_arms = [item for row in exercises_arms for item in row]
for item in exercises_arms:
    print(item)
    print(random_even_number)
    #print(' '.join(map(str, exercises_arms)))