from os import environ as env
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sys
import time
from twilio.rest import Client

def get_twilio_creds():
    '''get Twilio credentials from environment variables'''
    try:
        twilio_sid = env['TWILIO_SID']
        twilio_token = env['TWILIO_TOKEN']
    except KeyError:
        print('Failed to get TWILIO_SID or TWILIO_TOKEN')
        print('    Make sure to set all Twilio environment variables')
        sys.exit(1)
    else:
        return (twilio_sid, twilio_token)


def get_phone_numbers():
    '''get Twilio source and destination phone numbers from environment variables'''
    try:
        src_num = env['TWILIO_SRC_NUM']
        dst_num = env['TWILIO_DST_NUM']
    except KeyError:
        print('Failed to get TWILIO_SRC_NUM or TWILIO_DST_NUM.')
        print('    Make sure to set all Twilio environment variables.')
        sys.exit(1)
    else:
        return (src_num, dst_num)


def send_alert(sms_text, src_phone, dst_phone, twilio_sid, twilio_token):
    '''send an SMS alert'''
    client = Client(twilio_sid, twilio_token)

    try:
        alert = client.messages.create(to=dst_phone,
                                       from_=src_phone,
                                       body=sms_text)
    except TwilioRestException as e:
        print(f'Error, failed to send Twilio SMS alert')
        print(f'    Error from Twilio:\n{e}')
    else:
        print('Successfully sent text message:')
        print(alert)


def registration_changed(message_text, url, xpath):
    hope_url = url
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(hope_url)

    try: xp = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
         )
    except TimeoutException:
        print('Request to site timed out')
        return False
    else:
        if 'text' in dir(xp):
            if  xp.text == message_text:
                print(f'the message is still "{xp.text}"')
                driver.close()
                return False
            else:
                print('the message changed!')
                print(f'    message: {xp.text}')
                driver.close()
                return True

        else:
            print('the important check is never being done')


def main():
    try:
        url = 'https://scheduler.hope.net/hope2020/talk/TRTLRT/'
        message_text = 'Workshop registration begins Friday.'
        xpath = '/html/body/div[3]/div/article/div/main/article/div/aside/div[2]/div'
        notify = 'HOPE Alert! Registration for OSINT class may be open!' + '\n\n' + url
        sleep_time = 5
        twilio_sid, twilio_token = get_twilio_creds()
        src_num, dst_num = get_phone_numbers()
        counter = 1

        while True:
            print(f'Attempt #{counter}: checking for registration')
            if registration_changed(message_text, url, xpath):
                send_alert(notify, src_num, dst_num, twilio_sid, twilio_token)
                print('CHANGED!')
                sys.exit(0)
            else:
                counter += 1
                print(f'sleeping for {int(sleep_time)} seconds')
                time.sleep(sleep_time)

    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()
