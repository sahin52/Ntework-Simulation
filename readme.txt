2264562 Sahin KASAP
2171296- Mustafa Badilli

What is that project for?
This is a project to understand the network connection between devices, setting UDP protocol using python and see the effects of delaying. 

First Part - Connecting and sharing packets

In the first part, first of all you need to connect the devices in the Geni environment. Click on add slices and then click on add resources. Add the xml file and click on "site", in the left part of screen you will see universities under site. Choose one and wait, it will be approved. Click on reserve resources. After that, the devices will go green. You can start connecting to devices. Use ssh to connect on devices. Upload python files. You must add scriptD.py to d, scriptR1.py to r1 and so on. After uploading, run them in the order of D-S-R2-R1-R3. You will have measurement files. By using vi or nano command you can look into them and find out the times they take. Socket library is used to have a UDP connection. In this experiment, S stands for source, D stands for destination. By looking at the files "measure" we can see shortest path from S to D is S-R3-D.

Second Part - Delaying Experiments

For this part, we must find the best route from S to D. It is S-r3-D. Now we can conduct our experiment on them. For the experiment part, we need to use the python files which are ending with -exp.py . scriptS-exp.py is for source. You can send your files via ssh or copy their content into a file you created via "touch" command. After sending the files, write "tc qdisc add dev eth0 root netem delay 20ms 5ms distribution normal" for the first experiment. Here 20 and 5 means 20+-5 ms and dstribution normal tells it is a normal distribution. Run this command on the terminals of the devices.And run python files in the order D-S-R3. After the ending of execution, you will find the measurements in "measure.txt". 
After conducting first experiment, change the "20ms 5ms" to "40ms 5ms" to have a 40+-5 delay. Run the command again and run the python files again. Do the same things with "50ms 5ms".


