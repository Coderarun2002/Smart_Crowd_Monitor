import cv2
import smtplib
import datetime
n=int(input("Enter the limit"))

trainedmodel=cv2.CascadeClassifier("C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\data\\haarcascade_frontalface_default.xml")
webcam=cv2.VideoCapture(0)
i=0
j=0
while 1:
        i=0
        wc,v=webcam.read()#True or false along with the video of video running or not
        bnw=cv2.cvtColor(v,cv2.COLOR_BGR2GRAY)
        face=trainedmodel.detectMultiScale(bnw)#detect the face in cascade classifier
        for(x,y,w,h) in face:
            cv2.rectangle(v,(int (x),int (y)),(int (x+w),int(y+h)),(178,123,245),2)#(img,pt1,pt2,color,thickness)
            cv2.imshow("arunachalam",v)       
            key=cv2.waitKey(1)
            i=i+1
            if key==27:#escape key
                quit()
            if i>n:
                if(key==65):#CAPITAL A
                        n1=len(face)
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        print(f"person limit exceeded at the time of {strTime} and the count=",n1)                                        
            if(key==66):#capital B
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    n2=len(face)
                    print(f"time ={strTime} and number of persons=",n2)
        if(i>n and j!=(len(face))):
                l=len(face)
                r=str(l)
                import smtplib
                mymail="arunachalamgurusamy2002@gmail.com"
                mypass="czyydiywbwrgxnjo"
                con=smtplib.SMTP("smtp.gmail.com",587)
                con.starttls()
                con.login(user=mymail,password=mypass)
                con.sendmail(from_addr=mymail,to_addrs="arungurusamy2002@gmail.com",msg=f"Person has been exceeded beyond the limit and the count is{r}")
                con.close()
                j=len(face)

                
           
            
