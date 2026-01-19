from service.app import AppScreenshotTool
from service.taker import AndroidAutoTaker

def run_full_marketing_sequence(package, status):
    bot = AndroidAutoTaker(package)

    langs = ["fr-FR", "en-GB", "ko-KR", "ja-JP", "zh-CN", "it-IT", "es-ES", "ru-RU", "de-DE"]

    for lang in langs:
        status.configure(text=f"Initailisation pour \"{lang}\"...")
        bot.change_lang_and_restart(lang)
        bot.tap_id("currency_input_button_change_currency", 2)
        bot.tap_id("dialog_choose_currency_search")
        bot.add_text("jpy")
        bot.tap_id("item_choose_currency_symbol")

        status.configure(text="Screenshot d'accueil...")
        bot.tap_id("currency_input_money_amount")
        bot.clear_text()
        bot.add_text("10")
        bot.dark_mode(False)
        bot.take_screenshot("01_light_home")
        bot.dark_mode(True)
        bot.take_screenshot("01_dark_home")

        status.configure(text="Screenshot des paramètres...")
        bot.tap_id("settings")
        bot.dark_mode(False)
        bot.take_screenshot("02_light_setting")
        bot.dark_mode(True)
        bot.take_screenshot("02_dark_setting")

        status.configure(text="Screenshot du calcul...")
        bot.tap_id("settings_back_button")

        bot.tap_id("currency_input_money_amount", 2)
        bot.clear_text()
        bot.add_text("1000")
        bot.dark_mode(False)
        bot.take_screenshot("03_light_sum")
        bot.dark_mode(True)
        bot.take_screenshot("03_dark_sum")

        status.configure(text="Screenshot fenêtre de recherche...")
        bot.dark_mode(False)
        bot.tap_id("currency_input_button_change_currency", 2)
        bot.tap_id("dialog_choose_currency_search")
        bot.take_screenshot("04_light_search")
        status.configure(text="Screenshot de recherche...")
        bot.add_text("won")
        bot.take_screenshot("05_light_won")

        bot.dark_mode(True)
        bot.tap_id("currency_input_button_change_currency", 2)
        bot.tap_id("dialog_choose_currency_search")
        bot.take_screenshot("04_dark_search")
        status.configure(text="Screenshot de recherche...")
        bot.add_text("won")
        bot.take_screenshot("05_dark_won")

        status.configure(text="Screenshot de calcul...")
        bot.tap_id("item_choose_currency_symbol")
        bot.tap_id("currency_input_money_amount", 2)
        bot.clear_text()
        bot.add_text("1000")
        bot.dark_mode(False)
        bot.take_screenshot("06_light_choice")
        bot.dark_mode(True)
        bot.take_screenshot("06_dark_choice")

    status.configure(text="Script terminé")

if __name__ == "__main__":
    app = AppScreenshotTool()
    app.process = run_full_marketing_sequence
    app.mainloop()
