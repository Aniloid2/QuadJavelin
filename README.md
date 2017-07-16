# QuadJavelin

Embedded program for the QuadLink Quadcopter telemetry system. 

Load every file in a directory on a Raspberry Pi that is connected by serial to an Arduino. Connect a 2G,3G, 4G or wifi dongle and setup connectivity to the Raspberry Pi.

Run Bash script to initialise data posting to server. parameters { Username Password Number_of_posting_threads} Recomended  Number_of_posting_threads = 10; for 10Hz refresh rate at 100ms latenct. 

Tested with a 4G Vodafone GSM dongle, app in Italy, server in London and quadcopter in Italy achieving 10Hz and 170ms latency.

to connect to the server receiving asynchronous data go to https://quadlink.herokuapp.com and Enjoy!
