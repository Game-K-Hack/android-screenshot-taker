<div align="right">
    <a href="./README.fr.md">:fr: Français</a> | <b>:uk: English</b>
</div>

# Screenshot Taker
Python application that automatically takes screenshots of an application. It is currently calibrated for the **RealPrice** application ([`com.app.realprice`](https://play.google.com/store/apps/details?id=com.app.realprice)), but if you want to adapt it to your own application, you only need to modify the `main.py` file.

## Usage
You must have **Android Studio** installed and at least one **AVD** (Android Virtual Device) configured. Additionally, make sure that all required Python libraries are properly installed. Then simply run the `main.py` application.

## Customization
If you want to adapt this application to your own app, you can create your own commands using the **adb** tool by modifying the `service/taker.py` file.

Here are the features used for my application:

| Function | Description |
| -------- | ----------- |
| `change_lang_and_restart` | Changes the application language, then restarts it |
| `tap_id` | Simulates a click on an element using its ID, which can be found in the application layouts. Example: `android:id="@+id/currency_input_money_amount"`, the ID is therefore `currency_input_money_amount` |
| `clear_text` | Clears a text field by pressing the `backspace` key `n` times |
| `add_text` | Adds text to a text field |
| `take_screenshot` | Takes a screenshot of the Android emulator |
