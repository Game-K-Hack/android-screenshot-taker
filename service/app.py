import customtkinter as ctk
import subprocess
import threading
import os

emu = f"C:/Users/{os.getenv('USERNAME')}/AppData/Local/Android/Sdk/emulator/emulator.exe"

class AppScreenshotTool(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Screenshot Taker")
        self.geometry("500x400")

        # --- UI Layout ---
        self.label = ctk.CTkLabel(self, text="Émulateurs Disponibles", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        self.emulator_list = ctk.CTkComboBox(self, values=[], width=300)
        self.emulator_list.pack(pady=10)

        self.refresh_btn = ctk.CTkButton(self, text="Actualiser la liste", command=self.list_emulators)
        self.refresh_btn.pack(pady=5)

        self.launch_btn = ctk.CTkButton(self, text="Lancer l'Émulateur", fg_color="green", command=self.launch_emulator)
        self.launch_btn.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="Statut: En attente", text_color="gray")
        self.status_label.pack(pady=10)

        # Section Lancement App
        self.package_input = ctk.CTkEntry(self, placeholder_text="com.app.realprice", width=300)
        self.package_input.pack(pady=10)

        self.run_app_btn = ctk.CTkButton(self, text="~ Début ~", command=self.run_android_app)
        self.run_app_btn.pack(pady=5)

        self.process_thread = None

        # Initialisation
        self.list_emulators()

    def list_emulators(self):
        try:
            # Récupère la liste des AVDs
            result = subprocess.check_output(emu + " -list-avds", shell=True, text=True)
            avds = result.strip().split('\n')
            if avds[0] != '':
                self.emulator_list.configure(values=avds)
                self.emulator_list.set(avds[0])
            else:
                self.status_label.configure(text="Aucun émulateur trouvé.")
        except Exception as e:
            self.status_label.configure(text=f"Erreur: {e}")

    def launch_emulator(self):
        selected_avd = self.emulator_list.get()
        if not selected_avd:
            return

        def start():
            self.status_label.configure(text=f"Lancement de {selected_avd}...")
            # On lance l'émulateur dans un processus séparé
            subprocess.Popen(f"{emu} -avd {selected_avd}", shell=True)
        
        threading.Thread(target=start).start()

    def run_android_app(self) -> None:
        package_name = self.package_input.get()
        if package_name != "" and self.process_thread is None:
            self.process_thread = threading.Thread(target=self.process, args=(package_name, self.status_label))
            self.process_thread.start()
        return None

    def process(self, package_name:str=None, status=None) -> None:
        return None
