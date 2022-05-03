

def ballEnergyCalc(number_of_legos,height_of_legos):
    
    number_of_legos=int(input("number of legos: "))
    if(number_of_legos<0 or number_of_legos>10**5):
        raise Exception("inputs not in the specified range")
    
    height_of_legos=[]
    
    for i in range(number_of_legos):
        
        legos=(int(input("height_of_legos: ")))
        height_of_legos.append(legos)
        
    
    min_ball_energy=1
    while(1):
        
        ball_energy=min_ball_energy
        
        for i in range(number_of_legos):
            
            if(ball_energy<height_of_legos[i]):
                new_energy=ball_energy-(height_of_legos[i]-ball_energy)
                ball_energy=new_energy
                #print("ball energy",ball_energy)
                    
                     
            elif(ball_energy>=height_of_legos[i]):
                new_energy=ball_energy+(ball_energy-height_of_legos[i])
                ball_energy=new_energy
                #print("ball energy",ball_energy)
                
             
        if(ball_energy<0):
            min_ball_energy+=1
            continue
        
        if(ball_energy>0):
            break
    
    return min_ball_energy
        

print(ballEnergyCalc(number_of_legos=0,height_of_legos=[]))
    