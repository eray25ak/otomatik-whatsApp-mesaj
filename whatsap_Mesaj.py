import pywhatkit as kit
from datetime import datetime
import time

number = '+90'  # Hedef telefon numarası
while True:
    current_time = datetime.now()
    hours = current_time.hour
    minutes = current_time.minute + 1  # 2 dakika sonra göndermek istiyorsanız

    kit.sendwhatmsg(number, 'Merhaba, bu bir test mesajıdır.', hours, minutes)

    

    # 2 saniye bekleyin
    time.sleep(3)
