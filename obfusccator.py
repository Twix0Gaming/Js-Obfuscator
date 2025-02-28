import os
import subprocess

def obfuscate_js(input_file, output_file):
    """Führe den JavaScript-Obfuskator aus und speichere die obfuskierte Datei."""
    command = f"javascript-obfuscator {input_file} --output {output_file}"
    
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Die Datei wurde erfolgreich obfuskiziert und gespeichert in: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Obfuskieren der Datei: {e}")
def list_js_files(directory):
    """Gibt eine Liste von JavaScript-Dateien in einem Verzeichnis zurück."""
    js_files = []
    for file in os.listdir(directory):
        if file.endswith('.js'):
            js_files.append(file)
    return js_files

def main():
    directory = '.' 
    js_files = list_js_files(directory)
    if not js_files:
        print("Keine JavaScript-Dateien im aktuellen Verzeichnis gefunden.")
        return
    print("Verfügbare JavaScript-Dateien:")
    for i, file in enumerate(js_files, 1):
        print(f"{i}. {file}")
    print("\nGib die Nummern der Dateien ein, die du obfuskieren möchtest (durch Komma getrennt):")
    user_input = input("Eingabe: ").strip()
    selected_files = [js_files[int(num) - 1] for num in user_input.split(',') if num.isdigit() and 0 < int(num) <= len(js_files)]
    
    if not selected_files:
        print("Keine gültigen Dateien ausgewählt. Das Programm wird beendet.")
        return
    
    # Obfuskierung der ausgewählten Dateien
    for selected_file in selected_files:
        input_file = os.path.join(directory, selected_file)
        output_file = os.path.join(directory, f"obfuscated_{selected_file}")
        obfuscate_js(input_file, output_file)

if __name__ == "__main__":
    main()
