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

        status.configure(text=f"Screenshot d'accueil...")
        bot.tap_id("currency_input_money_amount")
        bot.clear_text()
        bot.add_text("10")
        bot.take_screenshot("01_home")

        status.configure(text=f"Screenshot des paramètres...")
        bot.tap_id("settings")
        bot.take_screenshot("02_setting")

        status.configure(text=f"Screenshot du calcul...")
        bot.tap_id("settings_back_button")

        bot.tap_id("currency_input_money_amount", 2)
        bot.clear_text()
        bot.add_text("1000")
        bot.take_screenshot("03_sum")

        status.configure(text=f"Screenshot fenêtre de recherche...")
        bot.tap_id("currency_input_button_change_currency", 2)

        bot.tap_id("dialog_choose_currency_search")
        bot.take_screenshot("04_search")

        status.configure(text=f"Screenshot de recherche...")
        bot.add_text("won")
        bot.take_screenshot("05_won")

        status.configure(text=f"Screenshot de calcul...")
        bot.tap_id("item_choose_currency_symbol")
        bot.take_screenshot("06_choice")

    status.configure(text=f"Script terminé")

if __name__ == "__main__":
    app = AppScreenshotTool()
    app.process = run_full_marketing_sequence
    app.mainloop()
