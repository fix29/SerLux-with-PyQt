# SerLux-with-PyQt
Simple writing and reading data from arduino through PC via PyQt.

![screenshoot.png](https://github.com/fix29/SerLux-with-PyQt/blob/master/Images/screenshoot.png)

# What data?
* Writing : write angle value (in degree) to servo
* Reading : read raw sensor data from A0 and convert it to "Lux". 

There you have it, a simple servo control and poor man's Lux meter.

# Wiring diagram
* Servo wiring:
  
  I used JR style servo with **BROWN=GND, RED=5V** and **ORANGE=SIGNAL**. Other servo types can be seen [here](https://www.rcgroups.com/forums/showpost.php?p=31975310&postcount=9).

![sweep_bb.png](https://github.com/fix29/SerLux-with-PyQt/blob/master/Images/sweep_bb.png)

* Photoresistor/LDR wiring:

  Actually, this wiring is pretty much voltage divider which actively change its value depends on the amount of light that shines on it.     The overlapped connection between LDR and resistor are fed to arduino's analog pin (A0). 

  **[EDIT]**
  
  I used 4K7 ohm resistor in my setup. Ideally you want 5K ohm resistor, since the code were designed to use that value.
  
  ![LDR1-1-620x436.png](https://github.com/fix29/SerLux-with-PyQt/blob/master/Images/LDR1-1-620x436.png)

* My setup:
  
  Apologize for my messy setup.
  
  ![DSC_4643.jpg](https://github.com/fix29/SerLux-with-PyQt/blob/master/Images/DSC_4643.jpg)
