# ntu-automate-star-wars
ntu-automate-star-wars is to automate adding classes or modules. It removes the need for you to click repeatedly but rather just runs and you can see all the automation that are happening without clicking. It will also automatically log out and log back in when you are asked to log in again. It was built on 25/06/2020 during my course registration (updated stars). Please make sure that the cores you want to add (by clicking continuously) is already **saved as plan 1**. This is recommeneded after the initial few presses which results in 'no more vacancy' and you have to continue to press to get it when it gets release in the 3 hours. 

*This was done by my sudden impulse and it is not perfect at all. I am sure alot of people can do much better. I wanted to use selenium so that people can see what is happening and will still be within their control. I used selenium knowing it is not as fast as scaping becuase I was already familiar with it.*



## prerequisites
* python
* pip


## set up & run
1. Clone or Fork or download this github
2. Go to chrome settings and go to about chrome. Check chrome version
3. Go [here](https://chromedriver.chromium.org/downloads) and download chrome driver with correct version
4. Unzip the downloaded chromedriver and copy the directory it is saved in
5. In the `config.txt` file fill DRIVE directory, USERNAME and PASSWORD used for intu in the corresponding fields and save:
```
DRIVE = C:/Users/xxx/Downloads/chromedriver.exe
USERNAME = ET0001
PASSWORD = xxxx
```
*no quotation is required
6. Go to double click automateStars.bat

If this doesn't work use this method:
6. Open cmd and type in these:
```
pip install -r requirements.txt
python automateStars.py
```
and the script should be running
