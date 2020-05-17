


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def mars_news(browser):

   # Visit the mars nasa news site
   url = 'https://mars.nasa.gov/news/'
   browser.visit(url)

   # Optional delay for loading the page
   browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

   # Convert the browser html to a soup object and then quit the browser
   html = browser.html
   news_soup = soup(html, 'html.parser')

   slide_elem = news_soup.select_one('ul.item_list li.slide')
   slide_elem.find("div", class_='content_title')

   # Use the parent element to find the first <a> tag and save it as  `news_title`
   news_title = slide_elem.find("div", class_='content_title').get_text()
   news_title

   # Use the parent element to find the paragraph text
   news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
   news_p
   
    
   return news_title, news_p


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)


url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')
slide_elem.find("div", class_='content_title')

news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.find_link_by_partial_text('more info')
more_info_elem.click()


html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')


img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


df.to_html

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None
    
    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)
    
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

def scrape_all():
   # Initiate headless driver for deployment
   browser = Browser("chrome", executable_path="chromedriver", headless=True)

data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now()
}

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())

browser.quit()






