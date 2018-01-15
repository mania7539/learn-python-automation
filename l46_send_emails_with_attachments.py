import smtplib;
from os.path import basename;
from email.mime.application import MIMEApplication;
from email.mime.multipart import MIMEMultipart;
from email.mime.text import MIMEText;
from email.utils import COMMASPACE, formatdate;
import pyautogui;
import time;


def send_mail(send_from, send_to, subject, text, files=None,
              server="127.0.0.1"):
    #assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        print(f);
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)


    #smtp = smtplib.SMTP(server)
    smtp = smtplib.SMTP("smtp.gmail.com", 587);
    type(smtp);
    smtp.ehlo();
    smtp.starttls();
    smtp.login("sohardtyrrell@gmail.com", 'tfjtecytdkyzytyw');
    smtp.sendmail(send_from, send_to, msg.as_string());
    smtp.close();


pyautogui.screenshot("C:\\Users\\XDrz\\Desktop\\MinersLifeMatch.png");
time.sleep(4);
send_mail("sohardtyrrell@gmail.com",
          ["mania7539@gmail.com"],
          "[Miners-life] 你配對成功了喔!!",
          "Dear Ray, \n\nYou've got a match in miners-life\n\nBest, \nDavid",
          ["C:\\Users\\XDrz\\Desktop\\MinersLifeMatch.png"]
          );
