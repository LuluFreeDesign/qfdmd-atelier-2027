# Que faire de mon équipe produit en 2027 ?

Outil d'atelier pour l'équipe Que faire de mes objets et déchets (séminaire du 30 novembre 2026).
Chacun lit les projets possibles, en propose jusqu'à 5, trie (garder ou retirer) en respectant le temps de l'équipe, puis classe son top 5.

## Pendant l'atelier

- **Participants** : https://lulufreedesign.github.io/qfdmd-atelier-2027/
  À la fin du parcours, « Obtenir mon code », puis coller le code dans le fil de l'atelier.
- **Animateur** : https://lulufreedesign.github.io/qfdmd-atelier-2027/?animateur
  Ouvre la Synthèse. Coller les codes reçus (plusieurs à la fois possible), le classement et le panier d'équipe se calculent.
  Pour revenir en vue participant sur le même navigateur : `?participant`.

Les choix restent dans le navigateur de chacun (localStorage) : aucune donnée n'est envoyée à un serveur.

## Modifier le contenu

- Liste des projets, rôles et capacités : `src/seed.json`
- Interface : `src/template.html`
- Puis reconstruire la page : `python3 build.py` (génère `index.html`)

## Publication

GitHub Pages : Settings → Pages → Deploy from a branch → `main` / `(root)`.
