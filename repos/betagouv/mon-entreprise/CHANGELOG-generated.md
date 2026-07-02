## Changelog : mon-entreprise (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau du simulateur avec une refonte de l'interface du comparateur, des corrections d'accessibilité et des améliorations de la gestion des dates. Des corrections et mises à jour spécifiques ont également été apportées pour les cas particuliers de Mayotte et des artistes-auteurs. Enfin, une migration technique majeure vers React 19 et Turbopack a été entreprise pour améliorer les performances et la compatibilité.

### Évolutions fonctionnelles
- **Comparateur :** Nouvelle mise en page du comparateur avec regroupement des questions et ajout d'une navigation améliorée entre les sections. Possibilité de réinitialiser les valeurs par défaut.
- **Simulateur :** Amélioration de l'affichage des objectifs et des avertissements, notamment pour les outils en version bêta.
- **Cessation d'activité :** Ajout de la gestion de la date de cessation d'activité avec des messages d'erreur et un avertissement en cas de changement d'année de simulation.
- **Artiste-auteur :** Mise à jour des informations et du guide concernant l'IRCEC.
- **Mayotte :** Corrections et mises à jour des règles de calcul des cotisations sociales et des exonérations spécifiques à Mayotte, notamment pour les cotisations forfaitaires et les abattements.
- **Messages :** Les messages d'information sont désormais dismissibles (pouvant être fermés par l'utilisateur).

### Évolutions techniques
- **Migration React 19 & Turbopack :** Mise à jour de React en version 19 et adaptation pour l'utilisation de Turbopack, améliorant les performances et la compatibilité.
- **Refactorisation du code :** Simplification et amélioration de la structure du code, notamment au niveau des composants d'interface utilisateur et de la gestion des données.
- **Gestion des dépendances :** Mise à jour de plusieurs dépendances, incluant `recharts` et les plugins Vite.
- **Amélioration du build :** Configuration du build pour forcer l'environnement de production et correction de problèmes liés à la gestion des chemins d'alias TypeScript.
- **Tests :** Ajout de tests unitaires pour les exonérations à Mayotte et pour les composants de l'interface utilisateur.
- **Redux :** Intégration du provider Redux dans la structure Next.js.

### Autres changements
- Mise à jour du Smic.
- Correction de typos et amélioration des traductions.
- Amélioration des couleurs et du contraste des composants d'interface utilisateur.
- Ajout d'un role "status" pour améliorer l'accessibilité des avertissements.
- Mise à jour du lien vers le site QPV.
- Ajout de tracking pour le simulateur et le comparateur.
- Suppression de code inutile et de dépendances obsolètes.
