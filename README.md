# Guvi-Project
Twitter Scraping(Streamlit web application)

What is Twitter Scraping?

      Scraping is a technique to get information from social network sites. Scraping Twitter can Yield many insights into sentiments,opinions and social media trends.Analysing tweets,shares,likes,URLs and interests is a powerful way to derive insight into public conversations.
      
      
How to scrape the Twitter Data?

    Scraping can be done with the help of many opensource libraries like
          1.Tweepy
          2.Twint
          3.Snscrape
          4.Getoldtweet3
     For my project I have used SNSCRAPE library.     
     
Libraries and Modules needed for the project
 
        1.snscrape.modules.twitter - (To Scrape the Data from Twitter)
        2.Pandas - (To Create a DataFrame with the scraped data)
        3.Pymongo - (To upload the dataframe to MongoDB database)
        4.Streamlit - (To Create Graphical user Interface)
        5.Datetime - (To get the current date)
        
Snscrape

         Snscrape allows you to scrape basic information such as a user's profile, tweet content, source, and so on. Snscrape is not limited to Twitter, but can also scrape content from other prominent social media networks like Facebook, Instagram, and others.
         
Streamlit


           Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc. Streamlit allows you to re-use any Python code you have already written. This can save considerable amounts of time compared to non-Python based tools where all code to create visualizations needs to be re-written.  In my project I've extensively used streamlit API Reference feature for creation of Titles, Images, Headers, Input boxes, Buttons, Checkbox, Download buttons.
To know more about Streamlit do visit the official site- https://docs.streamlit.io/library/api-reference

Workflow

     Lets us see the workflow of the twitter scraping project by breakingdown it step by step.

To view the demo video of my project checkout this link- 


Step 1
          
          Importing the libraries. As I have already mentioned above the list of libraries/modules needed for the project. First we have to import all those libraries. Before that check if the libraries are already installed or not by using the below piece of code.

                   !pip install ["Name of the library"]

If the libraries are already installed then we have to import those into our script by mentioning the below codes.

             import snscrape.modules.twitter as sntwitter
             import pandas as pd
             import pymongo
             import streamlit as st
             from datetime import date	
             
            
 Step 2
 
                    Getting inputs from the user. In the below code I have created the list of variables for getting user input. In the below codes st.sidebar denotes the streamlit user interface menu. With the help of streamlit I've also created the input boxes like text_input, number_input, date_input.

                    1.Keyword or Hashtag the user needed to search for (hashtag)
                    2.Number of tweets the user wants to scrape (tweets_count)
                    3.Tweets posted since date (start_date)
                    4.Tweets posted until date (end_date)
                    
Date when the user is scraping the tweets (today). Im getting this date with the help of datetime module


                    1.hashtag = st.sidebar.text_input("Enter the keyword or Hashtag you need to get : ")
                    2.tweets_count = st.sidebar.number_input("Enter the number of Tweets to Scrape : ", min_value= 1, max_value= 1000, step= 1)
                    3.start_date = st.sidebar.date_input("Start date (YYYY-MM-DD) : ")
                    4.end_date = st.sidebar.date_input("End date (YYYY-MM-DD) : ")
                    5.today = str(date.today())   
                    
Step 3
                     
                     After getting user inputs. In the next step I've created an empty list (tweets_list) so that we are going to append the scraped tweets from the twitter. Then with the streamlit library I've created the checkbox (Scrape Tweets).With the help of for loop and enumerate function im getting the variety of information from twitter. The method I've used is sntwitter.TwitterSearchScraper which helps in getting informations like date, id, rawContent, username, replyCount, retweetCount, likeCount, language, source and etc.I create function Scrapingdata(Hashtag,start_date,End_date,tweets_count) and this function call to get output.In my project search button, display button and download button available. If I touch the button code will ask to give input i give input and that input call function Scrapingdata(Hashtag,start_date,End_date,tweets_count) and function return value store variable.
                     
                     

                                    def Scrapingdata(Hashtag,start_date,End_date,tweets_count):
                                                tweets_list=[]
                                                for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{Hashtag} since:{start_date} until:{End_date}').get_items()):
                                                    if i>=tweets_count:
                                                             break
                                                     tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.url,tweet.retweetCount, tweet.source,tweet.likeCount, tweet.replyCount, tweet.lang]) 
                                                 return(tweets_list) 
           
          
          
           
      
      
Step 4
            
            The first function is used to create the Pandas DataFrame using the datas that was appended to tweets_list = []. Column names were provided as per my need.
Second function is to convert the DataFrame object into a CSV file using to_csv() function.
The last function is to convert the DataFrame object into a JSON file using to_json() function.

# Creating DataFrame with the scraped tweets
                                      
                                      def data_frame(data):
                                             return pd.DataFrame(data, columns= ['datetime', 'user_id', 'url', 'tweet_content', 'user_name','reply_count', 'retweet_count', 'like_count', 'language', 'source'])

# Converting DataFrame to CSV file
                                    
                                    def convert_to_csv(c):
                                              return c.to_csv().encode('utf-8')

# Converting DataFrame to JSON file
                                   
                                   def convert_to_json(j):
                                        return j.to_json(orient='index')    
    
    
Here is the object creation with different variable names of all the above three functions. This will act as the driver code for function execution.

# Creating objects for dataframe and file conversion

                              df = data_frame(tweets_list)
                              csv = convert_to_csv(df)
                              json = convert_to_json(df)


Step 5
                 Bridging the connection between MongoDB and Python. For this we would need the pymongo library and the .MongoClient attribute. After successful connection I've created the database named twitterscraping and collection named scraped_data. We are going to store all the scraped datas in this collection.

The scr_data is going to hold the basic informations like Scraped word, date scraped and scraped data. Then these details are uploded into the MongoDB collection.

                           client = pymongo.MongoClient("mongodb+srv://rahamaththullah:11111@cluster0.wxicfev.mongodb.net/?retryWrites=true&w=majority")
                                         db = client.Twitter
                                         records=db.scrapping
                                         scr_data={"Scraped_word":Hashtag,"Scraped_date":today,"Scraped_data":df.to_dict("list")}
             
 Step 6
               
               Here comes the importance of streamlit in my project. I have created many buttons overall for this project.
                
                In my project search button, display button and download button available. If I touch the button code will ask to give input i give input and that input call function Scrapingdata(Hashtag,start_date,End_date,tweets_count) and function return value store variable.
                
                                               def Scrapingdata(Hashtag,start_date,End_date,tweets_count):
                                                tweets_list=[]
                                                for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{Hashtag} since:{start_date} until:{End_date}').get_items()):
                                                    if i>=tweets_count:
                                                             break
                                                     tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.url,tweet.retweetCount, tweet.source,tweet.likeCount, tweet.replyCount, tweet.lang]) 
                                                 return(tweets_list) 
                
                
                                 Hashtag=st.sidebar.text_input("Enter Hashtag or Keyword")
                                 start_date=st.sidebar.date_input("Enter starting date:(YYYY-MM-DD)")
                                 End_date=st.sidebar.date_input("Enter end date:(YYYY-MM-DD)")
                                 tweets_count=st.sidebar.number_input("Enter Tweet count",min_value=1,max_value=1500,step=2)
                                 list_tweet=Scrapingdata(Hashtag,start_date,End_date,tweets_count)
    
Step 6
    
         These below two buttons are used to generate CSV or JSON files as per the user wish. In the backend the conver_to_csv or conver_to_json is called and executed. User will get the CSV file or JSON file downloaded to their downloads.

 BUTTON 
   
    st.download_button(label="Download csv",data=csv,file_name="file.csv",mime="text/csv") 
    st.download_button(label="Download json",data=json,file_name="file.json",mime="text/json")
    
    
    To run this script go to the Terminal and type the below command, you will get a new window opened in your browser there we can interact with the streamlit user interface.

	    streamlit run streamlitapp.py


    
                    
             
             

         
        
