from textblob import TextBlob
#('Ask User about how are they feeling')
print 'Welcome to Mood Analyzer 1.0'
print 'I rate your emotions on the scale of 1 to -1'
wiki = TextBlob(raw_input('How are you feeling now? '))
#('Perform Analysis')
print(wiki.sentiment.polarity)