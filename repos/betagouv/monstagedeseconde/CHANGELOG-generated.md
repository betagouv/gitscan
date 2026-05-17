## Changelog : monstagedeseconde (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de la plateforme, notamment au niveau de la gestion des conventions et des adresses, ainsi que sur la correction de plusieurs erreurs signalées en production via Sentry. Des optimisations ont également été apportées à la gestion des offres de stage et des candidatures, et des mises à jour de dépendances ont été effectuées.

### Évolutions fonctionnelles
- Amélioration de la validation des candidatures pour les élèves de seconde, avec un message spécifique lors de la soumission sur plusieurs semaines. [#819](https://github.com/betagouv/monstagedeseconde/pull/819)
- Possibilité pour un élève d'avoir deux stages validés simultanément. [#836](https://github.com/betagouv/monstagedeseconde/pull/836)
- Correction de l'affichage du nom et de l'email du responsable d'établissement lors de l'édition des conventions. [#808](https://github.com/betagouv/monstagedeseconde/pull/808) et [#814](https://github.com/betagouv/monstagedeseconde/pull/814)
- Amélioration de la géolocalisation et de la validation des adresses des entreprises. [#817](https://github.com/betagouv/monstagedeseconde/pull/817)
- Correction de l'affichage des offres dans le tableau de bord employeur.
- Correction de l'affichage des semaines sur la recherche pour les étudiants.
- Correction de l'export des candidatures qui provoquait une erreur 500. [#833](https://github.com/betagouv/monstagedeseconde/pull/833)
- Correction d'un bug empêchant la validation d'une candidature retenue. [#762](https://github.com/betagouv/monstagedeseconde/pull/762)

### Évolutions techniques
- Mise à jour de la version de Rails en 8.1. [#765](https://github.com/betagouv/monstagedeseconde/pull/765)
- Optimisation de la reconstruction de l'index des offres de stage pour améliorer les performances.
- Amélioration de la gestion des autorisations (abilities) pour les notifications.
- Refactorisation du code lié à la validation des adresses et des champs associés.
- Utilisation de `delete_all` au lieu de `destroy_all` pour accélérer certaines opérations de suppression en base de données.
- Amélioration de la gestion des erreurs Sentry, avec ajout de cache et correction de plusieurs incidents. [#826](https://github.com/betagouv/monstagedeseconde/pull/826), [#828](https://github.com/betagouv/monstagedeseconde/pull/828), [#829](https://github.com/betagouv/monstagedeseconde/pull/829)
- Mise à jour de plusieurs dépendances : `fast-uri`, `nokogiri`, `@babel/plugin-transform-modules-systemjs`, `view_component`, `devise`, `ip-address`.

### Autres changements
- Correction de typos et amélioration de la lisibilité du code.
- Mise à jour de la documentation.
- Suppression de fonctionnalités obsolètes.
- Amélioration des tests unitaires et d'intégration.
- Correction de plusieurs problèmes signalés par les outils d'analyse statique du code.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
- Correction de plusieurs erreurs d'affichage et de comportement dans l'interface utilisateur.
- Suppression de code inutile et nettoyage général du code.
- Mise à jour des scripts de connexion SSH pour utiliser Clever Tools et les variables d'environnement.
