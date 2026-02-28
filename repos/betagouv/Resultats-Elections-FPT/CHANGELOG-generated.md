## Changelog : Resultats-Elections-FPT (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au projet Resultats-Elections-FPT au cours des 30 derniers jours. Les évolutions se concentrent sur l'amélioration de l'interface utilisateur, l'ajout de nouvelles fonctionnalités pour la manipulation et l'affichage des données, et des corrections de bugs pour une meilleure expérience utilisateur. Une version "staging" a également été mise en place pour faciliter les phases de recette.

### Évolutions fonctionnelles
- Ajout d'un type d'affichage "badge" pour les cellules du tableau de résultats (#37).
- Possibilité de masquer le formulaire de validation de scrutin (#34).
- La colonne "badge" est désormais optionnelle dans la recherche de scrutin (#33).
- Réduction de la taille de la modale du tableau (#32).
- Ajout de filtres au tableau de résultats (#30).
- La recherche est désormais insensible à la casse et aux accents, et affiche automatiquement la liste complète si elle est vide (#29).
- Suppression d'une icône non nécessaire (#28).
- Diverses améliorations de l'expérience utilisateur et de l'interface (#26).
- Ajout d'une nouvelle vue pour la cartographie des collectivités (#24).
- Ajout d'un bouton de téléchargement optionnel sur la fiche de scrutin (#18).

### Évolutions techniques
- Création d'une version figée des custom widgets à la version v0.12 (#38).
- Mise en place d'un build "staging" pour faciliter la recette (#25).
- Migration vers Vue.js pour remplacer les custom widgets HTML (#15).
- Correction des URLs générées au build pour utiliser des chemins relatifs (#17).
- Première version de la vue tableau utilisant les composants DSFR (#16).

### Autres changements
- Mise à jour du Changelog (#21).
- Création d'une CI/CD pour automatiser le build de l'application (#20).
- Correction de valeurs en dur dans le code (#13).
