sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')
sets = set(sequence_0)
if sets == sequence_1 or sets == sequence_2 or sets == 
sequence_2 or sets == sequence_3:
    print("Set has unique symbols only")
else:
    print("Set doesn't have unique symbols")
