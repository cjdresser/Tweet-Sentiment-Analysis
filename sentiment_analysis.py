# Name: Christian Dresser
# Date: November 17th, 2020
# Description: Reads in a text file containing tweets, and another text file containing keywords
#              along with their respective values. Analyzes tweets to determine happiness score and
#              outputs average happiness score, total number of tweets containing keywords and total number of
#              tweets for each region (Easter, Central, Mountain, Pacific)
# Dependencies: N/A

# reads a textfile
def readIn(file_name):
    try:
        f = open(file_name, "r", encoding="utf-8")
        return f
    except IOError:
        print(IOError)
        return []


# removes extra spaces, sends all characters to lowercase
def formatInput(textLine):
    newList = []
    PUNC = '!\"#$%&\'()*+,-./:;<=>?@[]^_`{|}~'
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    for word in wordList:
        word = word.strip(PUNC)
        newList.append(word)
    textLine = " ".join(newList)
    return textLine


# determines the timezone from which a tweet was posted
def determine_timezone(lat, long):
    lat = float(lat)
    long = float(long)
    timezone = ""
    # Timezones
    p1 = (49.189787, -67.444574)
    p2 = (24.660845, -67.444574)
    p3 = (49.189787, -87.518395)
    p4 = (24.660845, -87.518395)
    p5 = (49.189787, -101.998892)
    p6 = (24.660845, -101.998892)
    p7 = (49.189787, -115.236428)
    p8 = (24.660845, -115.236428)
    p9 = (49.189787, -125.242264)
    p10 = (24.660845, -125.242264)

    if p1[0] >= lat >= p2[0]:
        if p3[1] <= long < p1[1]:
            timezone = "eastern"
        elif p5[1] <= long < p3[1]:
            timezone = "central"
        elif p7[1] <= long < p5[1]:
            timezone = "mountain"
        elif p9[1] <= long < p7[1]:
            timezone = "pacific"
        else:
            timezone = ""
    else:
        timezone = ""
    return timezone


# determines the average happiness score for a region and counts # of keyword tweets
# as well as the number of total tweets for that region
def happiness_score(tweetlist, keylist):
    tweet_score_list = []
    happiness = 0
    tweet_count = 0
    keywordcount = 0
    keytweetcount = 0
    tweet_score = 0
    # for every tweet
    for tweets in tweetlist:
        tweet_count += 1
        tweet_score = 0
        keywordcount = 0
        tweetstr = tweets[2]
        wordlist = tweetstr.split()
        # for every word in every tweet
        for tweetword in wordlist:
            # for each word in the keyword file
            for keywords in keylist:

                if keywords[0] == tweetword:
                    happiness += keywords[1]
                    tweet_score += keywords[1]
                    keywordcount += 1
                else:
                    continue
        if keywordcount > 0:
            keytweetcount += 1
            tweet_score = tweet_score/keywordcount
            tweet_score_list.append(tweet_score)

    if keytweetcount != 0:
        average_happy = sum(tweet_score_list) / keytweetcount
    else:
        average_happy = 0

    region_data = (average_happy, keytweetcount, tweet_count)
    return region_data


# puts all necessary data into a list and controls the order of functions
def compute_tweets(tweet_file, key_file):
    tweet_list = []
    tuple_list = []
    eastern = []
    central = []
    mountain = []
    pacific = []
    keywords_list = []
    final_list = []

    tweets = readIn(tweet_file)
    i = 0
    for line in tweets:
        tweet_list.append(line)
        tweet_list[i].split()
        i += 1

    for tweet in tweet_list:
        if tweet != "":
            lst = tweet.split()
            latitude = lst[0].strip("[,")
            longitude = lst[1].strip("]")
            tweet = " ".join(lst[5:])
            tweet = formatInput(tweet)
            tuple = (latitude, longitude, tweet)
            tuple_list.append(tuple)

    for tuple in tuple_list:
        if determine_timezone(tuple[0], tuple[1]) == "eastern":
            eastern.append(tuple)
        elif determine_timezone(tuple[0], tuple[1]) == "central":
            central.append(tuple)
        elif determine_timezone(tuple[0], tuple[1]) == "mountain":
            mountain.append(tuple)
        elif determine_timezone(tuple[0], tuple[1]) == "pacific":
            pacific.append(tuple)
        else:
            continue

    keywords = readIn(key_file)
    temp = []

    i = 0
    for line in keywords:
        temp.append(line.strip("\n"))

        temp2 = temp[i].split(",")

        if temp2[0] != "":
            key_tuple = (temp2[0], int(temp2[1]))
            keywords_list.append(key_tuple)
        i += 1

    final_list = [happiness_score(eastern, keywords_list), happiness_score(central, keywords_list),
                  happiness_score(mountain, keywords_list), happiness_score(pacific, keywords_list)]

    return final_list
