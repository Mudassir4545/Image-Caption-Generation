from flask import Flask,render_template,redirect,request,url_for
import Caption_it
from gtts import gTTS
import os

# __name__ == __main__
app = Flask(__name__)


## for GET request
@app.route('/')
def hello():
	return render_template("index.html")


## for POST request
@app.route('/',methods = ['POST'])
def marks():

	if request.method == 'POST':

		files = request.files.getlist('userfile[]')
		file_names=[]
		paths_image=[]
		captions=''
		gallery = ''
		
		for f in files:
			file_names.append(f.filename)
			
			path="./static/{}".format(f.filename)
			
			paths_image.append(f.filename) 
			
			f.save(path)
			caption=''
			caption = Caption_it.caption_this_image(path)
			captions=captions+"."+caption
			path=''
		for i in paths_image:
    	# html for image gallery
			gallery += '<div class="col-lg-4 col-sm-6"><div class="thumbnail"><img src="'+i+'"></div></div>'

		# captions="group of people are standing around the table.a man is sitting on the bench.a car is stuck on the mountain.dogs are playing in the water."

		path2 = "./static/{}".format("final_caption") + ".mp3"

		

		output = gTTS(text = captions, lang = 'en',slow = False)
		output.save(path2)

		result_dic = {
		'images' : paths_image,
		'caption' : captions,
		'sound' : path2
		}

	return render_template("index.html",your_result = result_dic)


@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename=filename), code=301)


if __name__ == '__main__':
	app.run(debug = True)

