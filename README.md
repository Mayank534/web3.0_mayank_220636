# web3.0_mayank_220636

# Collison Detection in 3D Coordinates (Python)

The project consists of a class car where one enter the car's company,model, year of manufacture, x velocity, y velocity,z velocity, x position, y position,z positon.

It then tells where collison is possible, if yes then what time would be taken for collison.

### Explanation of code

#### Class car
#### FUNCTIONS AND THEIR USE :-
#### __ inti __
- It assigns the values passed in parameter to the self function.

#### accelerate function
- It adds the speed to the current speed in the given direction 

#### move function
- It adds the distance to the current current in the given direction 

#### detect_collison 
-  firstly I calculated the relative distance and relative speed in the x , y and z directions.
- then I calculatde which car was ahead(i.e it had greater coordinate in that direction) and assigned the value to new variable x_frwd,x_bcwd=y_upwd, y_dnwd, v_x_bcwd, v_x_frwd, v_y_dnwd, v_y_upwd, z_upwd, z_dnwd.
- I then made 8 cases  
    - if all the initial position is same then collisonwill occur before starting 
    - if the relative velocities are 0 but the initial position are not same then the cars will never collide
    - I made 3 cases, one when x,y relative velocies are 0 ; y,z relative velocities are 0; x, z relative velocites are 0; The other which is not equal I check whether they will meet or not and if they met i calculated the time there itself
    - I then made 3 cases when only one of x, y, z relative velocities are 0. for other 2 unequal velocites I checked that time for collison of both coordinates should be same. If it comes out to be same I calculated the time and stored in an global array.
    - The last case when all three relative velocities are unequal,  I calculated time for meeting of one coordinate and checked that it should be same for other 2 , if it comes out to be true i calculates the time using relative velocity and distance else I returned False
 #### Entering the value for cars
 The format for calling cars should be 

 name = Car("make","model","year of manufacture", x direction speed, y direction speed, z direction speed, x coordiante, y coordiante, z coordinate)

 eg:-

    car1 = Car("Hyundai", "Creta", 2022, 50,0,0,-100,0 ,0)

    car2 = Car("Maruti", "Alto", 2021, 25,0,0,0,0,0)
#### Output 
__If the cars collide:__ 

It will print:

    2 cars detected:
    Hyundai's 2022 produced Creta
    Maruti's 2021 produced Alto
    Collision detected!
    The cars will collide in 4.00 hours ( 240.0 mins.)
    Hope you had your car insured :(
__If the cars donnot collide:__

It will print:

    2 cars detected:
    Hyundai's 2022 produced Creta
    Maruti's 2021 produced Alto
    No collision detected.
    The cars will never collide.
    Lucky!!
