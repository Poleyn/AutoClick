import pyautogui as pi
pi.sleep(2) 

for i in range(1,1000):
    pi.click(button="left")#(button="right") for right click
    #pi.sleep() <= delay example: pi.sleep(5)
    i+=1

#for contact: discord: Poleyn#3199