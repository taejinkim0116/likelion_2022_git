# chapter4 번역하기
from googletrans import Translator

translator = Translator()

sentence = input("번역할 문장을 입력해주세요 : ")
dest = input("어떤 언어로 번역을 원하시나요?")

result = translator.translate(sentence,dest)
detected = translator.detect(sentence)

print("======출 력 결 과=======")
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
print("========================")

#chapter 5 

import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
message.set_content("본문입니다")

message["Subject"] = "제목입니다."
message["From"] = "gootaejin0116@gmail.com"
message["To"] = "gootaejin0116@gmail.com"

with open("codelion.png","rb") as image:
    image_file = image.read()

image_type = imghdr.what('codelion',image_file)
message.add_attachment(image_file,maintype='image',subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("gootaejin0116@gmail.com","비밀번호")

sendEmail("gootaejin0116@gmailcom")
smtp.quit()