# MasterBait

Jeu de pêche en 2D développé en **Python** avec **Pygame**.

Pêchez des poissons, revendez-les, améliorez votre canne à pêche (6 niveaux)… et méfiez-vous de Cthulhu.

## Lancer le jeu

### Version Python

Prérequis : Python 3.9+ et pygame 2.3+.

```bash
pip install pygame
```

```bash
python MasterBait.py
```

Lancez la commande depuis le dossier du projet : le jeu charge `Assets/` et `save.txt` en chemin relatif.

### Version Windows (.exe)

Téléchargez `MasterBaitEXE.zip` dans l'onglet **Releases** du dépôt, décompressez-le et lancez `MasterBait.exe`.

## Sauvegarde

La progression est enregistrée dans `save.txt` (lignes : argent, niveau de canne, compteur d'anchois). Fermez le jeu avant de modifier ce fichier.

## Structure

```
.
├── MasterBait.py                            # code du jeu
├── save.txt                                 # sauvegarde (état initial)
├── requirements.txt                         # versions Python / pygame
├── Assets/
│   ├── Audio/   (Musiques, SFX)
│   ├── Font/
│   ├── Sprites/ (Cannes, Poissons, UI)
│   └── icone.png
├── Cahier_des_Charges_projet_MasterBait.pdf # cahier des charges
└── Doc.pdf                                  # documentation
```
