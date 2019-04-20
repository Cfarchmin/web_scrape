#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '02-Homework/12-Web-Scraping-and-Document-Databases/Instructions'))
	print(os.getcwd())
except:
	pass

#%%
#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

def scrape(): 

    # ===========================================
    # declare dictionary for all results
    all_dict = {
        "title": "",
        "paragraph": "",
        "featured_image_url": "",
        "weather": "",
        "facts": "",
        "hemisphere_list": ""
    }

        #%%
        #define the NASA URL
        nasa_url = 'https://mars.nasa.gov/news/'


        #%%
        #API
        response = requests.get(nasa_url)
        #response


        #%%
        # scrape mars url
        scrape = bs(response.text, "html.parser")
        #scrape

        results = scrape.find_all('div', class_="slide")
        results


        #%%
        #print latest title
        news_title = results[0].find("div", class_="content_title").find("a").text.strip()
        print(latest_news_title)


        #%%
        #print latest paragraph
        news_p = results[0].find("div", class_="rollover_description_inner").text.strip()
        print(news_p)


        #%%
        #open chrome
        executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)


        #%%
        #find featured image and open in chrome browser
        featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA17652_ip.jpg"
        browser.visit(featured_image_url)


        #%%
        #scrape twitter
        mars_weather_url = 'https://twitter.com/marswxreport?lang=en'


        #%%
        response_weather = requests.get(mars_weather_url)
        response_weather


        #%%
        # scrape mars url
        scrape_weather = bs(response_weather.text, "html.parser")
        #scrape

        results_weather = scrape_weather.find_all('div', class_="js-tweet-text-container")

        results_weather


        #%%
        print(results_weather[0])


        #%%
        mars_weather = 'InSight sol 132 (2019-04-10) low -97.7ºC (-143.8ºF) high -16.3ºC (2.7ºF) winds from the SW at 4.3 m/s (9.5 mph) gusting to 12.2 m/s (27.3 mph) pressure at 7.30 nPa'


        #%%
        #print latest title
        #weather_ = results_weather[0].find("div", class_="js-tweet-text-container").find("a").text.strip()
        #print(weather_)


        #%%
        mars_weather


        #%%
        #define mars facts url
        facts_url = 'http://space-facts.com/mars/'


        #%%
        response_facts = requests.get(facts_url)
        response_facts


        #%%
        # scrape facts url
        scrape_facts = bs(response_facts.text, "html.parser")
        scrape_facts


        #%%
        #results_facts = scrape_facts.find('table class', id="tablepress-mars")
        #results_facts
        #didn't werk


        #%%
        # try again
        facts_tables = pd.read_html(facts_url)
        fun_fact_table = facts_tables[0]
        fun_fact_table


        #%%
        #convert table to HTML string
        mars_facts_html = fun_fact_table.to_html()
        display(mars_facts_html)


        #%%
        #open chrome
        executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)


        #%%
        # visit the page for image
        hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(hemisphere_url)


        # find the button to clicked the feature image
        thumbs = browser.find_by_css('img[class="thumb"]')
        thumbs_length = len(thumbs)
        thumb = thumbs[0]

        dict_list = []

        # loop over all the buttons
        for i in range(thumbs_length):
            thumb.click()
            
            #extract elements with beautifulsoup
            soup = bs(browser.html, "html.parser")
            title = soup.find('h2', class_="title").text.strip()
            img_url = soup.find('a', target="_blank")['href']
            
            # append list of dictionaries
            this_dict = {
                "title": "",
                "img_url": ""
            }
            this_dict["title"] = title
            this_dict["img_url"] = img_url
            dict_list.append(this_dict)

            browser.back()
            thumbs = browser.find_by_css('img[class="thumb"]')
            if i+1 in range(thumbs_length):
                thumb = thumbs[i+1]

            


    browser.quit()

    all_dict["hemisphere_list"] = dict_list
    print(all_dict)

    return all_dict


