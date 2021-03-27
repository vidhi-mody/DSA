#Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower. 
# The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one).You have the following constraints:
#(1) Only one disk can be moved at a time.
#(2) A disk is slid off the top of one tower onto another tower.
#(3) A disk cannot be placed on top of a smaller disk.
#Write a program to move the disks from the first tower to the last using stacks.
 
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         
# Driver code
n = 5
TowerOfHanoi(n, '1', '2', '3')
