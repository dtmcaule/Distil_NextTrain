import httplib, urllib, base64, json

headers = {
   # Basic Authorization Sample
   # 'Authorization': 'Basic %s' % base64.encodestring('{username}:{password}'),
}

params = urllib.urlencode({
   # Specify your subscription key
   'api_key': 'kfgpmgvfgacx98de9q3xazww',
   # Specify Line code of Orange
   'LineCode': 'OR',
})

try:
   #connection to WMATA api
   conn = httplib.HTTPSConnection('api.wmata.com')
   #GET next train array from WMATA for Station code K04 which is Ballston, this station code was obtained from the api website
   conn.request("GET", "/StationPrediction.svc/json/GetPrediction/K04?%s" % params, "", headers)
   #store the response from WMATA
   response = conn.getresponse()
   #turn that response into a JSON object
   json_obj = json.load(response)
   #FOR loop to parse the object Trains.  Ballston station has Silver and Orange lines so must isolate Orange.
   for i in json_obj['Trains']:
    #If the Line is Orange then do a bunch of stuff
     if i ['Line'] == 'OR':
        #IF statement for BRD(Boarding) so we can change the language that's printed on screen for the Boarding status
        if i ['Min'] == 'BRD':
         print "The statuus of the next Orange line train arriving in Ballston is", i['Min'], "."
         break
        else:
            #IF statement for ARR(Arriving) so we can change the language that's printed on screen for the Boarding status
            if i ['Min'] == 'ARR':
             print "The status of the next Orange line train arriving in Ballston is", i['Min'], "."
             break
            else:
                #If the status isn't BRD or ARR tell the user how many minutes until the next Orange train arriving in Ballston
                print "The next Orange line train arriving in Ballston will be there in", i['Min'], "minutes."
                break
   conn.close()
except Exception as e:
   print("[Errno {0}] {1}".format(e.errno, e.strerror))
