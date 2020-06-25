# ntu-automate-star-wars
This script is to automate adding classes rather than clicking. It was built on 25/06/2020 during my STARs (updated stars). Please make sure that the cores you want to add (by clicking continuously) is already saved as plan 1. This is recommeneded after the initial few presses which results in 'no more vacancy' and you have to continue to press to get it when it gets release in the 3 hours.

**This was done by my sudden impulse and not perfect at all. I wanted to use selenium so that people can see what is happening and will still be within their control. I know selenium is slower than scraping but since I already was familiar with it I just used it.**


## prerequisites
* python
* pip


## set up
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
