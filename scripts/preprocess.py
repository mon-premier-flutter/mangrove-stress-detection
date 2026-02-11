import cv2
import numpy as np
import os

# --- CONFIGURATION DES CHEMINS AVEC REMONTÉE DE DOSSIER ---
# Le ".." permet de sortir de 'script' pour trouver 'data' à la racine du projet
BASE_DIR = '../data/datamangrove'
OUTPUT_DIR = '../data/processed'
TARGET_SIZE = (640, 640)


# La fonction clean_for_ai reste la même...
def clean_for_ai(img, target_size=TARGET_SIZE):
    h, w = img.shape[:2]
    scale = min(target_size[0] / h, target_size[1] / w)
    new_w, new_h = int(w * scale), int(h * scale)
    resized = cv2.resize(img, (new_w, new_h))

    canvas = np.zeros((target_size[1], target_size[0], 3), dtype=np.uint8)
    offset_y = (target_size[1] - new_h) // 2
    offset_x = (target_size[0] - new_w) // 2
    canvas[offset_y:offset_y + new_h, offset_x:offset_x + new_w] = resized

    # Amélioration du contraste (CLAHE)
    lab = cv2.cvtColor(canvas, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    final_img = cv2.cvtColor(cv2.merge((cl, a, b)), cv2.COLOR_LAB2BGR)
    return final_img


# --- VÉRIFICATION ET LANCEMENT ---
if not os.path.exists(BASE_DIR):
    print(f"ERREUR : Le dossier {os.path.abspath(BASE_DIR)} n'existe pas.")
    print("Vérifie que tu lances le script depuis le dossier 'script'.")
else:
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print("Début du traitement des 300 photos...")
    # ... la suite de la boucle reste identique
    for espece in os.listdir(BASE_DIR):
        espece_path = os.path.join(BASE_DIR, espece)
        if os.path.isdir(espece_path):
            save_path = os.path.join(OUTPUT_DIR, espece)
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            print(f"\nTraitement de l'espèce : {espece}")
            for img_name in os.listdir(espece_path):
                if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    img_path = os.path.join(espece_path, img_name)
                    raw_img = cv2.imread(img_path)
                    if raw_img is not None:
                        clean_img = clean_for_ai(raw_img)
                        cv2.imwrite(os.path.join(save_path, img_name), clean_img)
                        print(f" > {img_name} : OK", end='\r')
    print("\n\nSuccès ! Tes photos sont prêtes dans 'data/processed'.")