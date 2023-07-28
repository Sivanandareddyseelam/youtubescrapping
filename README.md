# Scrapping Youtube channel Videos Data

All about this project is to extract data from Youtube, with the help of "channel id" using Flask and Selenium webdriver. 
where we can provide channel id from HTML page as an input.
After confirming  channel id with the submit button, code will start extracting data from that channel in sequence.

Step 1: Header data collection from channle which is available at channel's home page.


Step 2: Count the no of long Videos available under Videos section by Scolling down till the end.


Header data contains:
Channnel id
Subscribers
Number of Videos Uploaded
Bio of YouTube Channel
Number of Long Videos Available



Step 3:Then cursor go to each video and collect info like
thumbnail, views, likes, video posted date,duration.

Step 4:After collecting all videos info, it stores into csv file.
and HTML page with header data will display. where we have an option to download the csv file.

Step 5: By clicking on the Download file button csv file going to be downloaded to local system.



![image](https://github.com/Sivanandareddyseelam/DSA_PPT_assignments/assets/113836018/67d3dc44-b62f-481a-afcf-e1ef65ee1136)


![image](https://github.com/Sivanandareddyseelam/DSA_PPT_assignments/assets/113836018/71a24769-e391-4709-a5d6-1a4ea20a1fe9)