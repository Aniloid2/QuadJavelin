# QuadJavelin

Embedded program for the QuadLink Quadcopter telemetry system. 

Load every file in a directory on a Raspery pi that is connected by serial to an arduino. Connect a 2G,3G, 4G or wifi dongle and setup connectivity to the raspbery pi.

Run Bash script to initialise data posting to server. parameters { Username Password Number_of_posting_threads} Recomended  Number_of_posting_threads = 10; for 10Hz refresh rate at 100ms latenct. 

to connect to the server reciving asyncronous data go to https://quadlink.herokuapp.com and Enjoy!


