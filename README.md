# ipsender
Get current ip and send it via email

crontab -e
# check ip and send it via email
30 7 * * * /usr/bin/python /home/pi/mokkula/ipsender.py >/dev/null 2>&1
