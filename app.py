from instapy_cli import client
import os
import time, shutil, configpass
from google_images_download import google_images_download  

username = 'in_jail_out_soon5'
password = '9256142896'
image = 'posts/'
text = """#love #instagood #nibba #nibbi #jcb #bbkivines #backbench #joker #iphone11 #dankmeme #memes #girl #beautiful #instadaily #summer #instagramhub #iphoneonly #follow #igdaily #bestoftheday #happy #picstitch #tagblender #jj #sky #nofilter #meme #followme #fun #sun
"""
response = google_images_download.googleimagesdownload()  

rajju = os.listdir("posts/")

queryyyy = raw_input("Search the images: ")

search_queries = [ queryyyy ] 

def downloadimages(query): 
    # keywords is the search query 
    # format is the image file format 
    # limit is the number of images to be downloaded 
    # print urs is to print the image file url 
    # size is the image size which can 
    # be specified manually ("large, medium, icon") 
    # aspect ratio denotes the height width ratio 
    # of images to download. ("tall, square, wide, panoramic") 
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit":100, 
                 "print_urls":True, 
                 "size": "medium", 
                 "aspect_ratio": "square"} 
    try: 
        response.download(arguments) 
      
    # Handling File NotFound Error     
    except FileNotFoundError:  
        arguments = {"keywords": query, 
                     "format": "jpg", 
                     "limit":4, 
                     "print_urls":True,  
                     "size": "medium"} 
                       
        # Providing arguments for the searched query 
        try: 
            # Downloading the photos based 
            # on the given arguments 
            response.download(arguments)  
        except: 
            pass
  
# Driver Code 
for query in search_queries: 
    downloadimages(query)  
    print() 
    
images = os.listdir("downloads/"+query)

for names in images:   
    shutil.copyfile("downloads/"+query+"/"+names, "posts/"+names )    
    
rajju = os.listdir("posts/")

with client(username, password) as cli:
    for x in rajju:
        try:
            print(image+x)
            cli.upload(image+x, text)
            os.remove(image+x)
            time.sleep (60)
        except:
            os.remove(image+x)
            time.sleep (60)