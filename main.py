import os
import simplematrixbotlib as botlib


def prepare_bot() -> botlib.Bot:
    homeserver = os.environ.get('BOT_HOMESERVER')
    username = os.environ.get('BOT_USERNAME')
    password = os.environ.get('BOT_PASSWORD')
    access_token = os.environ.get('BOT_TOKEN')

    creds = botlib.Creds(
            homeserver=homeserver,
            username=username,
            password=password,
            access_token=access_token
            )

    bot = botlib.Bot(creds)
    return bot


def main() -> None:
    bot = prepare_bot()

    @bot.listener.on_message_event
    async def donation_link(room, message) -> None: 
        match = botlib.MessageMatch(room, message, bot)
        if not match.is_not_from_this_bot():
            return
        if not (match.contains('ukraine') or match.contains('Ukraine')):
            return

        if not (
                match.contains('aid') or
                match.contains('donat') or
                match.contains('help')
                ):
            return

        response = "matrix-ukraine-donation-bot\n" \
                "You can aid Ukraine through the following:\n" \
                "\n" \
                "Army:\n" \
                "https://ukraine.ua/news/support-the-armed-forces-of-ukraine/ \n" \
                "https://savelife.in.ua/en/donate/ \n" \
                "https://armysos.com.ua/en/ \n" \
                "http://wings-phoenix.org.ua/en/about-fund/ \n" \
                "https://vostok-sos.org/en/make-a-donation/ \n" \
                "\n" \
                "Medical:\n" \
                "https://www.facebook.com/RazomForUkraine/fundraisers \n" \
                "https://www.facebook.com/donate/337101825010055/ \n" \
                "https://www.facebook.com/donate/507886070680475/ \n" \
                "https://www.rsukraine.org/ \n" \
                "https://www.facebook.com/hospitallers/posts/2953630548255167 \n" \
                "\n" \
                "Misc:\n" \
                "https://redcross.org.ua/en/2022/02/donate-to-support-the-ukrainian-red-cross-to-help-civilians-in-this-difficult-time-for-ukraine/ \n" \
                "https://www.uwvm.org.ua/ \n" \
                "https://voices.org.ua/en/ \n" \
                "\n" \
                "More information can be found here:\n" \
                "https://en.wikipedia.org/wiki/2022_Russian_invasion_of_Ukraine"

        await bot.api.send_text_message(room.room_id, response)

    bot.run()

if __name__ == '__main__':
    main()
