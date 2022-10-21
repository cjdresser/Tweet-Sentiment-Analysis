import sentiment_analysis
# Name: Christian Dresser
# Date: November 17th, 2020
# Description: Prompts user for two text file names, computes the text files
#              and outputs the necessary data
# Dependencies: sentiment_analysis.py

sentiment = sentiment_analysis

txt_file = input("Please input the name of the tweet file: ").lower()
key_file = input("Please input the name of the keyword file: ").lower()

tuple_list = sentiment.compute_tweets(txt_file, key_file)
print("-----------------Average Happiness Score------Total Tweets with Keywords------Total Tweets-----------------\n")
print("Eastern Timezone:       {:.2f}                             {}                        {}\n".format(tuple_list[0][0], tuple_list[0][1], tuple_list[0][2]))
print("Central Timezone:       {:.2f}                             {}                        {}\n".format(tuple_list[1][0], tuple_list[1][1], tuple_list[1][2]))
print("Mountain Timezone:      {:.2f}                             {}                         {}\n".format(tuple_list[2][0], tuple_list[2][1], tuple_list[2][2]))
print("Pacific Timezone:       {:.2f}                             {}                        {}\n".format(tuple_list[3][0], tuple_list[3][1], tuple_list[3][2]))

#keywords.txt
#tweets.txt
