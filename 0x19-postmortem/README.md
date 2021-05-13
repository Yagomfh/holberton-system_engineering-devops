## Postmortem for web stack debugging #3
### Sumary
September 11th, 2018 server began to spit out 500 error on the web. By checking the server status on the docker container there was an Apache server configuration file that has a typo.

### Timeline
* 08:15 - 500 error showing in server
* 08:17 - Check status of server and shows its OK
* 08:20 - Used strace to find issue by connecting Child process for Apache
* 08:30 - Found issue in the wp-settings.php showing that file missing
* 08:32 - Found file being misspelled in the settings file .phpp
* 08:34 - Fixed file by changing the typo to .php
* 08:35 - Restarte Apache
* 08:36 - Server now running normally

### Root Cause and Resolution
The issue was found by trying to access the server by curl into it but the response was shooting out 500 error. By checking the server using strace and connecting the PID that is associated with the child process of the Apache service, the main cause of the server issue was the misspelling in the wp-setting file. In the file there was a call to /class-wp-locale.phpp witch is misspelled because the file it was trying to call is the /class-wp-locale.php file and due to this misspelling the strace shows that the file doesn’t exist when it is trying to call it. Than I changed the .phpp to .php by using puppet to replace any files that are named .phpp to be replaced to .php to fix all the other possible misspelling issues that might have occurred in the file/. After restarting the Apache service the server started to operate normally. 

### Corrective and Preventative Measures
* To make thing better in the future the server should be tested before deploying. Because of this small misspelling issue, the service went down, and customers cannot access the service.
* Another way to prevent from this happening, we should enable error logging to find issues quicker by looking at error logs in the assigned server there where no error logs enabled so to find the issue we needed to enable the error log to find issue. 
