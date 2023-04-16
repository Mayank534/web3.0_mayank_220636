import math
time_final=[0]
class Car:
    def __init__(self, make, model, year, speed_x,speed_y,speed_z, x, y,z):
        self.make = make
        self.model = model
        self.year = year
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_z = speed_z
        self.x = x
        self.y = y
        self.z = z

    def accelerate(self, speed_increment_x,speed_increment_y,speed_increment_z):
        self.speed_x += speed_increment_x
        self.speed_y += speed_increment_y
        self.speed_z += speed_increment_z

    # def brakes(self, speed_decrement_x,speed_decrement_y):
    #     self.speed_x -= speed_decrement_x
    #     self.speed_y -= speed_decrement_y
        


    def move(self):
        self.x += self.speed_x*time_final[0]
        self.y += self.speed_y*time_final[0]
        self.z += self.speed_z*time_final[0]
   
    flag=0
    def detect_collision(self, car2):
        x_frwd=x_bcwd=y_upwd=y_dnwd=v_x_bcwd=v_x_frwd=v_y_dnwd=v_y_upwd=z_upwd=z_dnwd=0
        x_speed_relative=(self.speed_x-car2.speed_x)
        y_speed_relative=(self.speed_y-car2.speed_y)
        z_speed_relative=(self.speed_z-car2.speed_z)
        x_distance=(self.x-car2.x)
        y_distance=(self.y-car2.y)
        z_distance=(self.z-car2.z)
        if self.x >= car2.x:
            x_frwd = self.x
            x_bcwd = car2.x
            v_x_frwd = self.speed_x
            v_x_bcwd = car2.speed_x
        else:
            x_frwd = car2.x
            x_bcwd = self.x
            v_x_frwd = car2.speed_x
            v_x_bcwd = self.speed_x 


        if self.y >= car2.y:
            y_dnwd = car2.y
            y_upwd = self.y
            v_y_upwd = self.speed_y
            v_y_dnwd = car2.speed_y
        else:
            y_dnwd = self.y
            y_upwd = car2.y
            v_y_upwd = car2.speed_y
            v_y_dnwd = self.speed_y 


        if self.z >= car2.z:
            z_dnwd = car2.z
            z_upwd = self.z
            v_z_upwd = self.speed_z
            v_z_dnwd = car2.speed_z
        else:
            z_dnwd = self.z
            z_upwd = car2.z
            v_z_upwd = car2.speed_z
            v_z_dnwd = self.speed_z
        

        if self.x == car2.x and self.y == car2.y and self.z == car2.z:
            flag=1
            time=0
            time_final[0]=0
            return True

        elif (x_speed_relative==0 and y_speed_relative==0 and z_speed_relative==0) :
            flag=0
            return False

        elif x_speed_relative == 0 and y_speed_relative==0:
            if x_distance == 0 and y_distance == 0:
                if v_z_dnwd > v_z_upwd:
                    time =abs((z_upwd-z_dnwd)/(v_z_upwd-v_z_dnwd))
                    time_final[0]=time
                    #print(time)
                    return True
                else:
                    return False 
            else:
                return False
        
        elif y_speed_relative == 0 and z_speed_relative == 0:
            if y_distance == 0 and z_distance == 0:
                if v_x_bcwd > v_x_frwd:
                    time =abs((x_frwd-x_bcwd)/(v_x_frwd-v_x_bcwd))
                    time_final[0]=time
                    #print(time) 
                    return True
                else:
                    return False 
            else:
                return False


        elif x_speed_relative == 0 and z_speed_relative==0:
            if x_distance == 0 and z_distance == 0:
                if v_y_dnwd > v_y_upwd:
                    time =abs((y_dnwd-y_upwd)/(v_y_dnwd-v_y_upwd))
                    time_final[0]=time
                    #print(time)
                    return True
                else:
                    return False 
            else:
                return False
        
        elif x_speed_relative == 0 :
            if x_distance == 0 :
                if v_y_dnwd > v_y_upwd:
                    time =abs((y_dnwd-y_upwd)/(v_y_dnwd-v_y_upwd))
                    if (z_dnwd+time*z_speed_relative==z_upwd):
                        time_final[0]=time
                    #print(time)
                        return True
                    else:
                        return False 
                else:
                    return False
            else:
                return False
        
        elif y_speed_relative == 0 :
            if y_distance == 0 :
                if v_z_dnwd > v_z_upwd:
                    time =abs((z_dnwd-z_upwd)/(v_z_dnwd-v_z_upwd))
                    if (x_bcwd+time*x_speed_relative==x_frwd):
                        time_final[0]=time
                    #print(time)
                        return True
                    else:
                        return False 
                else:
                    return False
            else:
                return False
            
        elif z_speed_relative == 0 :
            if z_distance == 0 :
                if v_y_dnwd > v_y_upwd:
                    time =abs((y_dnwd-y_upwd)/(v_y_dnwd-v_y_upwd))
                    if (x_bcwd+time*x_speed_relative==x_frwd):
                        time_final[0]=time
                    #print(time)
                        return True
                    else:
                        return False 
                else:
                    return False
            else:
                return False

        else:
            time = abs(x_speed_relative/x_distance)
            
            if (y_dnwd+time*y_speed_relative==y_upwd and z_dnwd+time*z_speed_relative==z_upwd):
                time_final[0]=time
                return True
            else:
                return False

    
# create two Car objects
car1 = Car("Hyundai", "Creta", 2022, 50,0,0,-100,0 ,0)
car2 = Car("Maruti", "Alto", 2021, 25,0,0,0,0,0)

# accelerate and decelarate car1 and car2
car1.accelerate(0,0,0)
car2.accelerate(0,0,0)



print("2 cars detected:")
print(car1.make+'\'s', car1.year, "produced", car1.model)
print(car2.make+'\'s', car2.year, "produced", car2.model)

if car1.detect_collision(car2):
    print("Collision detected!")
    print("The cars will collide in %.2f" % time_final[0] ,"hours (" , time_final[0]*60 , "mins.)")
    print("Hope you had your car insured :(")
else:
    print("No collision detected.")
    print("The cars will never collide.")
    print("Lucky!!")

#if want to move the car
car1.move()
car2.move()
