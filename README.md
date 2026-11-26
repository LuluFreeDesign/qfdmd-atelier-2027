# Que faire de mon équipe produit en 2027 ?

Outil d'atelier pour l'équipe Que faire de mes objets et déchets (séminaire du 30 novembre 2026).
Chacun lit les projets possibles et en propose jusqu'à 5, trie (garder ou retirer) sans notion de coût, puis répartit les jours de chaque métier (Dev, Design / PO, Contenu & SEO) sur les projets gardés, par demi-journée, dans la limite du temps et du budget de l'équipe. Enfin, chacun classe son top 5.

Tous les projets partent de zéro jour. Le temps incompressible est déjà compté. Le coût = jours × coût d'une journée du métier, affiché en trimaniak, la monnaie de l'atelier (1 000 € = 100 trimaniak).

Ressources 2027 : Dev 118 j à 941 € (94,1 trimaniak), Design / PO 59 j à 739 € (73,9 trimaniak), Contenu & SEO 70 j à 739 € (73,9 trimaniak). Budget : 206 369 € = 20 637 trimaniak.

Dans chaque projet, une durée estimée en semaines : le métier le plus chargé, à son rythme (Dev 2,5 j/sem, Design / PO 1 j puis 1,5 j une semaine sur deux, Contenu & SEO 1,5 j/sem). Rythmes modifiables via `parSemaine` dans `src/seed.json`.

La poubelle Que faire présente l'atelier en pleine page après le prénom, puis présente les trimaniak avant « Répartir les jours » (une seule fois par navigateur). Textes dans `STORIES`, dans `src/template.html`.

## Pendant l'atelier

- **Participants** : https://lulufreedesign.github.io/qfdmd-atelier-2027/
  À la fin du parcours, « Obtenir mon code », puis coller le code dans le fil de l'atelier.
- **Animateur** : https://lulufreedesign.github.io/qfdmd-atelier-2027/?animateur
  Ouvre la Synthèse. Coller les codes reçus (plusieurs à la fois possible), le classement et le panier d'équipe se calculent.
  Pour revenir en vue participant sur le même navigateur : `?participant`.

Les choix restent dans le navigateur de chacun (localStorage) : aucune donnée n'est envoyée à un serveur.

## Modifier le contenu

- Liste des projets, rôles, jours disponibles et coût d'une journée (`tjm`) : `src/seed.json`
- Budget annuel en euros : `budget` dans `src/seed.json` (`null` = jours × coût d'une journée)
- Monnaie de l'atelier : `monnaie` et `taux` (trimaniak par euro) dans `src/seed.json`
- Son des boutons : `src/halo-space.mp3`, extrait du son « halo-space » de [Button Sounds](https://buttons.joshwcomeau.com) de Josh Comeau (licence MIT). Chacun peut couper le son avec « Son activé » en haut à droite.
- Interface : `src/template.html`
- Puis reconstruire la page : `python3 build.py` (génère `index.html`)

## Publication

GitHub Pages : Settings → Pages → Deploy from a branch → `main` / `(root)`.
