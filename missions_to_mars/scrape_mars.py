#!/usr/bin/env python
# coding: utf-8




# Dependencies
from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


# *NASA Mars News*
# 


def scrape_info():

    #splinter exercise
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    mars= {}





    #scrape website
    url= 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(browser.html, 'html.parser')

    #pulling title
    news_title= soup.find_all('div', class_='content_title')
    news_title= news_title[1].a.text
    #print(news_title)

    mars["news_title"]=news_title

    news_p= soup.find_all('div', class_='article_teaser_body')
    news_p= news_p[0].text
    mars["news_p"]= news_p











    soup


    # *Splinter*




    url= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)
    browser.find_by_id("full_image").click()
    time.sleep(2)
    browser.find_link_by_partial_text("more info").click()
    time.sleep(2)
    soup= BeautifulSoup(browser.html, 'html.parser')
    result= soup.find("figure", class_= "lede")
    result= result.a.img["src"]
    result
    featured_image_link= "https://www.jpl.nasa.gov" + result
    mars["featured_image_link"]= featured_image_link


    # FEATURED IMAGE

    # MARS FACTS




    url= 'https://space-facts.com/mars/'
    table= pd.read_html(url)
    table[0]
    df= table[0]
    df.columns= ["Description", "Values"]
    df.set_index("Description", inplace= True)
    df
    html_table= df.to_html()
    html_table= html_table.replace('\n', '')
    mars["Facts"]= html_table





    mars


    # Mars Hemispheres




    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    hemisphere_image_url= []

    for i in range (4):
        hemispheres= {}
        time.sleep(2)
        browser.find_by_css("a.product-item h3")[i].click()
        soup= BeautifulSoup(browser.html, 'html.parser')
        title= soup.find("h2", class_= "title").get_text()
        image= soup.find("a", text= "Sample").get("href")
        hemispheres["title"]= title
        hemispheres["img_url"]= image
        hemisphere_image_url.append(hemispheres)
        browser.back()
        
    mars["hemispheres"]= hemisphere_image_url





    return mars

if __name__ == "__main__":
    print(scrape_info())







