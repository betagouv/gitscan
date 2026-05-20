## Changelog : acceslibre (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance de la plateforme, notamment au niveau de la gestion des statistiques et de la pagination. Des corrections ont été apportées à la recherche et à la génération de PDF, et des optimisations ont été réalisées pour la gestion des événements de l'interface utilisateur. Plusieurs mises à jour de dépendances ont également été intégrées pour assurer la sécurité et la stabilité du système.

### Évolutions fonctionnelles
- Amélioration de la recherche "où" avec correction d'une erreur Sentry et support des combobox RGAAs. [#2609](https://github.com/MTES-MCT/acceslibre/issues/2609)
- Possibilité de contourner les vérifications de doublons. [#2626](https://github.com/MTES-MCT/acceslibre/issues/2626)
- Utilisation de POST pour la génération des PDF RPA. [#2623](https://github.com/MTES-MCT/acceslibre/issues/2623)
- Correction d'un problème lié à l'indexation des PDF RPA. [#2611](https://github.com/MTES-MCT/acceslibre/issues/2611)
- Correction pour la question Pente. [#2600](https://github.com/MTES-MCT/acceslibre/issues/2600)
- Correction pour les détails ERP. [#2599](https://github.com/MTES-MCT/acceslibre/issues/2599)

### Évolutions techniques
- Utilisation de Redis pour stocker les événements des widgets, avec vidange vers la base de données toutes les heures, améliorant ainsi la performance. [#2624](https://github.com/MTES-MCT/acceslibre/issues/2624)
- Mise à jour de Django. [#2625](https://github.com/MTES-MCT/acceslibre/issues/2625)
- Mise en cache du nombre d'éléments pour la pagination, améliorant la performance des requêtes. [#2621](https://github.com/MTES-MCT/acceslibre/issues/2621)
- Optimisation des performances des statistiques. [#2610](https://github.com/MTES-MCT/acceslibre/issues/2610)
- Application de versions fixes pour les packages. [#2635](https://github.com/MTES-MCT/acceslibre/issues/2635)

### Autres changements
- Mises à jour de diverses dépendances (ruff, sentry-sdk, django-modeltranslation, @sentry/browser, psycopg2, pnpm, eslint, dompurify, scrapfly-sdk, phonenumbers, faker, requests, redis).
- Nettoyage et refactoring du code.
- Préparation et déploiement en production.
