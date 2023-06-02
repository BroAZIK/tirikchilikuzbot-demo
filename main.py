import time
from handlers import (
    get_last_update,
    start,
    product,
    info,
    savat
)


def main():
    # get last update
    last_update = get_last_update()
    # get last update_id
    last_update_id = last_update['update_id']

    # infinite loop
    while True:
        # get new update
        new_update = get_last_update()

        # get new update_id
        new_update_id = new_update['update_id']

        # check if new update_id is not equal to last update_id
        if new_update_id != last_update_id:
            # get new message
            new_message = new_update['message']
            
            # get user chat_id
            chat_id = new_message['chat']['id']
            
            # check if new message has text
            if 'text' in new_message.keys():
                # get new message text
                text = new_message['text']
                print(text)

                # check if new message text is equal to '/start'
                if text == '/start' or '🏠 Bosh menyu':

                    # get new message first_name
                    first_name = new_message['chat']['first_name']

                    # send start message
                    start(chat_id, first_name)
                if text == '🔥 Mahsulotlar':

                    product(chat_id)

                if text == "ℹ️ Ma'lumot":

                    info(chat_id)
                if text == "📥Savat":
                    savat(chat_id)
            # set last update_id to new update_id
            last_update_id = new_update_id

        # sleep for 1 second
        time.sleep(1)
main()
