## Changelog : monstagedeseconde (30 derniers jours, au 5 juin 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, notamment la correction de failles XSS potentielles et la mise à jour de dépendances. Des corrections ont également été apportées à la gestion des conventions, des applications et des établissements, ainsi qu'à l'interface utilisateur pour une meilleure expérience. L'ajout d'un chatbot et l'amélioration des outils d'administration complètent ces évolutions.

### Évolutions fonctionnelles
- Correction d'un problème empêchant la mise à jour de la date de signature des conventions. [#827](https://github.com/betagouv/monstagedeseconde/issues/827)
- Amélioration de la gestion des applications :
    - Correction d'un bug permettant à un élève de postuler plusieurs fois pour la même offre.
    - Correction d'un problème d'affichage des applications dupliquées.
- Amélioration de la gestion des établissements :
    - Correction d'un bug empêchant les établissements de voir les conventions signées par l'employeur. [#891](https://github.com/betagouv/monstagedeseconde/issues/891)
    - Ajout de la possibilité d'importer des élèves depuis l'interface d'administration. [#880](https://github.com/betagouv/monstagedeseconde/issues/880)
- Ajout d'un chatbot pour l'assistance utilisateur. [#895](https://github.com/betagouv/monstagedeseconde/issues/895)
- Ajout de la gestion du niveau scolaire de l'élève. [#883](https://github.com/betagouv/monstagedeseconde/issues/883)
- Correction de l'affichage des URL des ressources. [#872](https://github.com/betagouv/monstagedeseconde/issues/872)
- Ajout du préfixe téléphonique de la Guadeloupe. [#859](https://github.com/betagouv/monstagedeseconde/issues/859)
- Correction du problème de nombre de places restantes à zéro.
- Correction du renvoi d'application. [#898](https://github.com/betagouv/monstagedeseconde/issues/898)
- Amélioration de la recherche des semaines. [#851](https://github.com/betagouv/monstagedeseconde/issues/851)
- Correction d'un problème de double convention. [#893](https://github.com/betagouv/monstagedeseconde/issues/893)

### Évolutions techniques
- Mise à jour de plusieurs dépendances : `qs`, `webpack-dev-server`, `view_component`, `devise`, `fast-uri`, `nokogiri`, `babel/plugin-transform-modules-systemjs`, `jwt`.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Amélioration de la gestion des erreurs Sygne.
- Correction de problèmes de typage.
- Amélioration des tests et correction de tests défaillants.
- Mise à jour de la version de Ruby à 3.4.9.
- Amélioration du geocoding et de la validation d'adresse pour les entreprises. [#817](https://github.com/betagouv/monstagedeseconde/issues/817)
- Amélioration de la gestion des jobs de reconstruction de la base de données.
- Correction de problèmes liés à l'authentification via token.

### Autres changements
- Suppression de fichiers inutiles.
- Nettoyage du code.
- Mise à jour de la documentation.
- Ajout de tests d'accessibilité (A11y).
- Correction de fautes de frappe et amélioration de la formulation.
- Suppression d'un add-on tiers inutile.
- Configuration du mode maintenance via un flag Flipper.
- Ajout de compétences pour l'IA Claude.
- Suppression de descriptions d'extensions commentées dans `structure.sql`.
- Correction de la configuration de l'environnement de test.
- Correction de l'importation des types dans les modèles.
- Correction de l'utilisation de `destroy_all` par `delete_all` pour améliorer les performances.
- Ajout de la gestion des statistiques pour les utilisateurs statisticiens.
- Correction de la signature des tokens.
- Correction de la configuration du CSP.
- Suppression d'un dump inutile.
- Correction de l'API opérateur.
- Correction de l'affichage des statistiques.
