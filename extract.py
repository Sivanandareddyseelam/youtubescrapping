from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



def get_css_element(selector,driver):
    element = WebDriverWait(driver, 40).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,selector)))
    return element

def get_xpath_element(xpath,driver):
    element = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    return element



class Socila_scrapping():
    def __init__(self,channel_name):
        self.channel_name = channel_name
        youtube_videos_url = "https://www.youtube.com/"+self.channel_name+"/videos"
        
        service = Service(executable_path=r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe')
        driver = webdriver.Chrome(service=service,)
        driver.maximize_window()
        driver.get(youtube_videos_url)
        self.driver = driver
        
    
        
        
    def get_required_headerdata(self):
        header = ["#subscriber-count", "#videos-count > span:nth-child(1)", "#content"]
        for i in range(len(header)):
            #v_data = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,header[i])))
            v_data = get_css_element(header[i],self.driver)
            if i == 0:
                subscribers = v_data[0].text
            elif i==1:
                noof_videos = v_data[0].text
            elif i==2:
                bio = v_data[1].text
        return subscribers,noof_videos,bio



    def find_no_of_long_videos(self):
        before = 0
        while True:    
            body = WebDriverWait(self.driver, 1000).until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))
            body[0].send_keys(Keys.END)
            sleep(3)
            #thumbnails = WebDriverWait(driver, 40).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#video-title")))
            thumbnails = get_css_element("#video-title",self.driver)
            after = len(thumbnails)
            if before == after:
                break
            else:
                before = after
        return before

    
    
    def collect_data(self,no_of_videos):
        video_data = []
        for i in range(no_of_videos):
            dic = {} 
            thumbnails = get_css_element("#video-title",self.driver)
            #print(thumbnails[i].text)
            dic["thumbnail"] = thumbnails[i].text

            self.driver.execute_script("arguments[0].scrollIntoView();", thumbnails[i])
            actions = ActionChains(self.driver)

            self.driver.execute_script("arguments[0].click();", thumbnails[i])
            sleep(3)
            stop = get_xpath_element('//*[@id="movie_player"]//div[2]/div[1]/button',self.driver)
            self.driver.execute_script("arguments[0].click();", stop)
            
            duration = get_css_element("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span:nth-child(2) > span.ytp-time-duration",self.driver)
            dic["duration"] = duration[0].text

            data_open = get_xpath_element('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/tp-yt-paper-button[1]',self.driver)
            data_open.click()
            
            views = get_css_element("#info > span:nth-child(1)",self.driver)
            dic["views"] = views[0].text
            
            posted_on = get_css_element("#info > span:nth-child(3)",self.driver)
            dic["posted_on"] = posted_on[0].text
        
            likes = get_css_element("#segmented-like-button > ytd-toggle-button-renderer > yt-button-shape > button > div.cbox.yt-spec-button-shape-next__button-text-content > span",self.driver)
            dic["likes"] = likes[0].text

            video_data.append(dic)
            self.driver.back()
        self.driver.quit()
        return video_data


    