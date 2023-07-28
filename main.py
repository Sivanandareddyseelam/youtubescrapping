''' This program is used to collect long videos info of given youtube channel'''
import pandas as pd
from flask import Flask,request,render_template,send_file
from extract import Socila_scrapping


app = Flask(__name__)

@app.route("/", methods = ['GET'])
def homepage():
    ''' Function to display home page where we can provide channel id as input'''
    return render_template("index.html")


@app.route("/getdata",methods = ['POST','GET'])
def extract_data():
    '''Function to extract header information'''
    if request.method == "POST":
        channel_id = request.form['channel_id']
        obj = Socila_scrapping(channel_id)                       #object initialization
        sub,videos,bio = obj.get_required_headerdata()
        no_of_videos = obj.find_no_of_long_videos()
        video_data = obj.collect_data(no_of_videos)
        
        temp_file_path = "temp_data.csv"
        data =  pd.DataFrame(video_data)
        data.to_csv(temp_file_path, index=False, encoding='utf-8-sig')  
        
        sample_data = {
        'Channel_id' : channel_id,
        'subscribers': sub,
        'videos_uploaded': videos,
        'channel_bio': bio,
        'long_videos': no_of_videos}
    
    return render_template('result.html', **sample_data)     # displays header info


@app.route('/download_file')
def download_file():
    ''' Function to download the file'''
    temp_file_path = "temp_data.csv"
    return send_file(temp_file_path)

@app.route('/back')
def back():
    ''' Function to download the file'''
    return homepage()


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8000)
    app.run(debug=True)