from textblob import TextBlob
my_file = 'xapo.csv'
while True: 
    try:
        f = open(my_file,'r',encoding='UTF-8-SIG')
    except:
        print('Error！Please reenter the path')
        my_file = input("input the path of the file:")
        continue
    else: 
        break

header_var = f.readline()
header_var = header_var.rstrip()
header_var = header_var+','+'sentiment_score'

# form the special list of header
new_header_list = header_var.split(',')
#read the rest of file
rest_lines = f.readlines() 

new_rest_list = []
for tweet in rest_lines:
    tweet = tweet.rstrip()
    try:  
        t_text = tweet.split(',')[2]
    except:
        t_text = ' '
    t_sentiment = TextBlob(t_text).polarity
    new_tweet = tweet+','+str(t_sentiment)+'\n'
    new_rest_list.append(new_tweet)
f.close()

# write
out_file = open('xapo-S.csv','w',encoding='UTF-8-SIG')
new_header_str = ''
# write header
for i in new_header_list:
    new_header_str = new_header_str+i+','
new_header_str =  new_header_str[:-1]+'\n'
out_file.write(new_header_str)

# write rest data
new_rest_str = ''
for s in new_rest_list:
    out_file.write(s)
    
print("writing successfully!")

out_file.close() 

