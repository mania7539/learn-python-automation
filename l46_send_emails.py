

# sending emails with smtplib

import smtplib;

connection = smtplib.SMTP("smtp.gmail.com", 587);   # 587 is gmail's port
type(connection);   # ??

connection.ehlo();      # el hello - lots of history: connect to the server
                        # output:
                        # (250, b'smtp.gmail.com at your service, [106.1.233.84]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
                        # 250 is the response code, everything with '2'xx means OK

connection.starttls();  # start with tls which makes the connection encypted
                        # output: (220, b'2.0.0 Ready to start TLS'), means OK

connection.login('sohardtyrrell@gmail.com', 'tfjtecytdkyzytyw');    # [] use app specific password to avoid dis-functioning when you changing your gmail password
                                                                    # https://support.google.com/accounts/answer/185833?hl=en 

fromAddress = 'sohardtyrrell@gmail.com';
toAddress = "mania7539@gmail.com";
emailContent = "Subject: [Miners-life] You've got a matched! \n This Is Header!\nDear Me, \n\nYou've got a match in miners-life\n\nBest, \nDavid\nContent-Disposition:attachment; filename=C:\\Users\\XDrz\\Desktop\\MinersLifeMatch.png";
# Subject ends with \n;
# Header ends with \n; (We won't use it)
# Body is next to Header

connection.sendmail(fromAddress, toAddress, emailContent);
# sendmail will return the email address lists which are failed to send
