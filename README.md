# Upper-computer-sampling-program
An upper computer program created for sampling. It accept HEX 8 digit number through Ethernet and also include band filter.

The program is a 8 channels upper computer program recieveing HEX 8 digit number through Ethernet. The first digit is n-th channel and the second digit is nothing. The rest 6 digits is data represented in 2's complement number binary system. The local Ethernet IP address is 192.168.1.102. 

The quick sender block was customized for a lower machine.

Recieving Data through Ethernet is done in JVM packaged inside, and UI and calculation are done thourgh pyQT and Python.
