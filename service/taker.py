import subprocess
import time
import re
import xml.etree.ElementTree as ET
import os

class AndroidAutoTaker:
    def __init__(self, package_name):
        self.package = package_name
        self.current_lang = None

    def get_element_coords(self, resource_id:str, index: int = 1) -> tuple[int, int] | None:
        """Trouve les coordonnées X,Y du n-ième élément correspondant à l'ID"""
        target_occurrence = index  # On veut la n-ième occurrence
        current_occurrence = 0

        # 1. Dump de l'écran actuel
        subprocess.run("adb shell uiautomator dump /sdcard/view.xml", shell=True, capture_output=True)
        subprocess.run("adb pull /sdcard/view.xml .", shell=True, capture_output=True)

        if not os.path.exists('view.xml'):
            return None

        # 2. Analyse du XML
        tree = ET.parse('view.xml')
        root = tree.getroot()
        
        full_id = f"{self.package}:id/{resource_id}"

        for node in root.iter('node'):
            if node.get('resource-id') == full_id:
                current_occurrence += 1
                
                # Si on a atteint l'occurrence souhaitée
                if current_occurrence == target_occurrence:
                    bounds = node.get('bounds') 
                    nums = list(map(int, re.findall(r'\d+', bounds)))
                    x = (nums[0] + nums[2]) // 2
                    y = (nums[1] + nums[3]) // 2
                    return x, y
                    
        return None

    def tap_id(self, resource_id:str, index:int=1) -> bool:
        coords = self.get_element_coords(resource_id, index)
        if coords:
            subprocess.run(f"adb shell input tap {coords[0]} {coords[1]}", shell=True)
            time.sleep(0.5)
            return True
        return False

    def take_screenshot(self, name:str) -> None:
        if self.current_lang is not None:
            os.makedirs(f"images/{self.current_lang}", exist_ok=True)
            fullname = self.current_lang + "/" + name
        else:
            os.makedirs("images", exist_ok=True)
        time.sleep(1)
        subprocess.run(f"adb exec-out screencap -p > images/{fullname}.png", shell=True)
        print(f"📸 Capture enregistrée : {name}.png")

    def change_lang_and_restart(self, lang:str) -> None:
        self.current_lang = lang
        subprocess.run(f"adb shell cmd locale set-app-locales {self.package} --user current --locales \"{lang}\"", shell=True)
        time.sleep(0.5)
        subprocess.run("adb shell am force-stop com.app.realprice", shell=True)
        time.sleep(0.5)
        subprocess.run(f"adb shell monkey -p {self.package} -c android.intent.category.LAUNCHER 1", shell=True)
        time.sleep(1)

    def clear_text(self, n:int=10) -> None:
        subprocess.run("adb shell input keyevent KEYCODE_MOVE_END", shell=True)
        time.sleep(0.5)
        for _ in range(n):
            subprocess.run("adb shell input keyevent $(printf 'KEYCODE_DEL %.0s' {1..250})", shell=True)
            time.sleep(0.1)

    def add_text(self, text:str) -> None:
        subprocess.run(f"adb shell input text '{text}'", shell=True)
        time.sleep(0.5)

    def dark_mode(self, mode:bool=True) -> None:
        subprocess.run(f'adb shell "cmd uimode night {"yes" if mode else "no"}"', shell=True)
        time.sleep(0.5)
