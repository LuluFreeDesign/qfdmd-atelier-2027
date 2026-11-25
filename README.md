# Que faire de mon équipe produit en 2027 ?

Outil d'atelier pour l'équipe Que faire de mes objets et déchets (séminaire du 30 novembre 2026).
Chacun lit les projets possibles et en propose jusqu'à 5, trie (garder ou retirer) sans notion de coût, puis répartit les jours de chaque métier (Dev, Design / PO, Contenu & SEO) sur les projets gardés, par demi-journée, dans la limite du temps et du budget de l'équipe. Enfin, chacun classe son top 5.

Tous les projets partent de zéro jour. Le temps incompressible est déjà compté. Le coût en euros = jours × coût d'une journée du métier.

## Pendant l'atelier

- **Participants** : https://lulufreedesign.github.io/qfdmd-atelier-2027/
  À la fin du parcours, « Obtenir mon code », puis coller le code dans le fil de l'atelier.
- **Animateur** : https://lulufreedesign.github.io/qfdmd-atelier-2027/?animateur
  Ouvre la Synthèse. Coller les codes reçus (plusieurs à la fois possible), le classement et le panier d'équipe se calculent.
  Pour revenir en vue participant sur le même navigateur : `?participant`.

Les choix restent dans le navigateur de chacun (localStorage) : aucune donnée n'est envoyée à un serveur.

## Modifier le contenu

- Liste des projets, rôles, jours disponibles et coût d'une journée (`tjm`) : `src/seed.json`
- Budget annuel : `budget` dans `src/seed.json` (laisser `null` pour jours × coût d'une journée)
- Interface : `src/template.html`
- Puis reconstruire la page : `python3 build.py` (génère `index.html`)

## Publication

GitHub Pages : Settings → Pages → Deploy from a branch → `main` / `(root)`.
