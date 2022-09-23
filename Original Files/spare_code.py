
f = open("file1.csv", "w")
f.truncate()
f.close()
  
  
  with open ("file1.csv","w",encoding='UTF8') as file:    
      writer = csv.writer(file)
        writer.writerow(['command'])
        writer.writerow([text])
        
        
try:
        r = sr.Recognizer()
        text1 = r.recognize_google(audio1)
        print ("you said: " + text1)
        return text1
    except:
        print('I didnt hear anything')
        return 'done'