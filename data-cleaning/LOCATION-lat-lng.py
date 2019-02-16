import requests
import json

input_list=['binance-loca.csv','bitcoincom-loca.csv','bitmain-loca.csv','bitpay-loca.csv','bitstamp-loca.csv','blockchain-loca.csv','coinbase-loca.csv','kraken-loca.csv','purse.io-loca.csv','shapeshift-loca.csv','xapo-loca.csv']
output_list=['binance-lc.csv','bitcoincom-lc.csv','bitmain-lc.csv','bitpay-lc.csv','bitstamp-lc.csv','blockchain-lc.csv','coinbase-lc.csv','kraken-lc.csv','purse.io-lc.csv','shapeshift-lc.csv','xapo-lc.csv']
count = 0
n=len(input_list)
while count<n:
    my_file = 'E://'+input_list[count]
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
    rest_lines = f.readlines()

    new_rest_list = []
    for tweet in rest_lines:
        tweet = tweet.rstrip()
        tweet = tweet.split(',')
        try:  
            t_loca = tweet[4]
        except:
            continue
        try:
            test = tweet[9]
        except:
            try:
                tweet.append('9')
                tweet.append('10')
                tweet[10]=tweet[8]
                tweet[9]=tweet[7]
                tweet[8]=tweet[6]
                tweet[7]=tweet[5]
                tweet[6]=tweet[4]
                tweet[5]=tweet[3]
                tweet[4]=tweet[2]
                tweet[3]=tweet[1]
                tweet[2]=tweet[0]
                tweet[0]='1050000000000000000'
                tweet[1]='887524' 
            except:
                continue
        api = 'https://maps.googleapis.com/maps/api/geocode/json?address='+t_loca+'your_key'
        r = requests.get(api)
        json_var = json.loads(r.text)
        if json_var['results']:
            lat = str(json_var['results'][0]['geometry']['location']['lat'])
            long =str(json_var['results'][0]['geometry']['location']['lng'])
        else:
            lat = '24'
            long= '-40'
        loc = lat+' '+long
        tweet[4] = loc      
        new_tweet = ''
        for i in tweet:
            new_tweet = new_tweet + i +','
        new_tweet=new_tweet[:-1]+'\n'
        new_rest_list.append(new_tweet)
    f.close()

    # write
    outname = 'E://'+output_list[count]
    out_file = open(outname,'w',encoding='UTF-8-SIG')
    # write header
    out_file.write(header_var)
    # write rest data
    for s in new_rest_list:
        out_file.write(s)

    print(output_list[count]+" writing successfully!")
    out_file.close()
    count = count+1
