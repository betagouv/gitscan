## Changelog : mon-entreprise (30 derniers jours, au 27 avril 2026)

### Résumé
Cette période a été marquée par une refonte importante de l'architecture du projet, notamment au niveau des workflows CI/CD, de la gestion des règles Publicodes et de l'organisation du code. Des corrections et améliorations ont également été apportées aux simulateurs, en particulier pour les travailleurs indépendants (TI) et les sociétés par actions simplifiées unipersonnelles (SASU), avec une mise à jour des règles de cotisation et une simplification de l'expérience utilisateur.

### Évolutions fonctionnelles
- **Décommissionnement du simulateur RGCP :** Le simulateur RGCP n'est plus disponible.
- **Amélioration de l'affichage des informations d'entreprise :** Correction d'un bug empêchant l'affichage correct des informations de l'entreprise sélectionnée.
- **Prise en charge des dividendes :** Ajout de la gestion des dividendes dans les simulateurs pour indépendants et SASU, avec des questions et des informations pertinentes.
- **Amélioration de l'expérience utilisateur :** Correction de bugs d'affichage et de navigation dans les simulateurs, notamment en iframe.
- **Nouvelles règles et mises à jour de cotisations :** Mise à jour des règles de cotisation pour les travailleurs indépendants (régime micro-social) et les professions libérales (PLR), incluant la réforme des barèmes.
- **Ajout de liens utiles :** Ajout de liens vers des services pertinents pour les utilisateurs, tels que le service employeur.
- **Amélioration de la gestion des professions :** Correction et clarification des règles liées aux professions libérales et aux activités indépendantes.

### Évolutions techniques
- **Refonte des workflows CI/CD :** Refonte complète des workflows GitHub Actions pour améliorer la fiabilité, la performance et la maintenabilité. Renommage des workflows pour plus de clarté.
- **Gestion des règles Publicodes :** Refactorisation de la gestion des règles Publicodes pour une meilleure organisation et une plus grande flexibilité. Création de paquets de règles communes.
- **Amélioration de l'architecture :** Refactorisation du code pour une meilleure séparation des préoccupations, notamment au niveau de la gestion de l'état, des composants d'interface utilisateur et des appels à l'API.
- **Mise à jour des dépendances :** Mise à jour des dépendances du projet, notamment Node.js et les actions GitHub.
- **Correction de bugs et amélioration de la qualité du code :** Correction de nombreux bugs et amélioration de la qualité du code grâce à des tests unitaires et des revues de code.
- **Amélioration des performances :** Optimisation de la performance de certains composants et fonctions.

### Autres changements
- **Documentation :** Amélioration de la documentation du projet et ajout de documentation pour les nouveaux paquets de règles.
- **Traduction :** Mise à jour des traductions.
- **Nettoyage du code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Mise à jour des plafonds de CA :** Mise à jour des plafonds de chiffre d'affaires pour les calculs de cotisations.
- **Corrections de tests :** Correction de plusieurs tests unitaires et d'intégration.
