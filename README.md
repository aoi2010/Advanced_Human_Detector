# Advanced Human Detector
This is a human detector which uses HmmD Mmwave Sensor to detect humans.

![Sensor Case](CAD/Sensor_Case.png)

### Inspiration

I wanted to create a human detector using the Mmwave Sensor to detect humans and alert me when human is detected cuz some people always steals the flowers in my garden, and I want to catch them in the act.

### Challenges

Believe it or not, this was my second time using Fusion 360 and KiCad! I watched numerous tutorials and guides and did a kg of googling, but in the end, I'm pretty proud of the final product. I had the most struggle figuring out how to make sketches, and with the new mouse controls, it definitely took me a while to get the hang of it. Also in KiCad, I had a lot of trouble with footprints and making sure everything was aligned properly and the traces were correct(but it became a litle long traces).

### Specifications

BOM: 
1x Seeed Studio XIAO ESP32-C3 development board
1x Wavwshare HMMD 24 GHz mmWave human presence sensor
1x Passive piezo buzzer, 3 V, Ø12 mm
1x NPN transistor 2N2222, TO-92 package
1x Resistor 10 kΩ, ¼ W, through-hole
1x Resistor 1 kΩ, ¼ W, through-hole
1x Resistor 100–200 Ω, ¼ W, through-hole
1x Resistor 22–33 Ω, through-hole
1x Signal diode 1N4148
2x 0 Ω SMD resistor
1x 5-pin connector / header for HMMD sensor - Male
1x 5-pin connector / header for HMMD sensor - Female
1x LAN / multi-core cable for sensor connection
4x M3x16mm Screws
4x M3x4mm Heatset Inserts
1x PCB 


Others:
- Micropython Firmware
- PCB Gerber File(PCB/motionalr_mcu.zip)
- Top and Bottom of Sensor Case STL files for 3d Printing
- BOM.csv

Schematic            |  PCB         |   Sensor Case (Top)   |   Sensor Case (Bottom)
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
![image](PCB/Schematics.png)    |  ![image](PCB/PCB.png)  | ![image](CAD/Separate/sensor_top.png) | ![image](CAD/Separate/sensor_Bottom.png)


### Notes
The code is still basic in functionality because of lack of information on the sensor datasheet, but I will update it as soon as I get the sensor and debug it's output. The case for the mmwave sensor is measured with approx measurement available online, so I will also update the case design once I get the sensor and measure it myself. The PCB will be left bare as I like looking at PCBs.

<div align="center">

## Thanks For Reading! Also leave a star if you like the project! ⭐

</div>
