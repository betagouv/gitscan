## Changelog : acceslibre (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation des performances, notamment au niveau des requêtes et de la génération de PDF, ainsi que sur la correction de bugs liés à la recherche et à l'affichage des informations. Des mises à jour de sécurité et de dépendances ont également été effectuées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Correction d'un bug lié à la recherche "où" qui provoquait des erreurs Sentry et affectait la compatibilité RGAA. [#2609](https://github.com/MTES-MCT/acceslibre/issues/2609)
- Ajout d'une option permettant de contourner les vérifications de doublons. [#2626](https://github.com/MTES-MCT/acceslibre/issues/2626)
- Amélioration des performances de l'affichage des statistiques. [#2610](https://github.com/MTES-MCT/acceslibre/issues/2610)
- Correction d'un problème lié à la génération des PDF RPA, qui a été temporairement retirée puis réintégrée avec une méthode POST. [#2622](https://github.com/MTES-MCT/acceslibre/issues/2622) et [#2623](https://github.com/MTES-MCT/acceslibre/issues/2623)
- Correction de bugs mineurs liés à l'affichage des détails des ERP. [#2600](https://github.com/MTES-MCT/acceslibre/issues/2600) et [#2599](https://github.com/MTES-MCT/acceslibre/issues/2599)

### Évolutions techniques
- Mise à jour de Django. [#2625](https://github.com/MTES-MCT/acceslibre/issues/2625)
- Optimisation du cache pour la pagination afin d'améliorer les performances des requêtes. [#2621](https://github.com/MTES-MCT/acceslibre/issues/2621)
- Utilisation de la méthode POST pour la génération des PDF RPA, améliorant potentiellement la sécurité et la fiabilité.

### Autres changements
- Mises à jour régulières des dépendances (ruff, sentry-sdk, django-modeltranslation, @sentry/browser, psycopg2, pnpm, eslint, dompurify, scrapfly-sdk, phonenumbers, faker, requests, redis, django-debug-toolbar, pandas) pour maintenir la sécurité et la stabilité du projet. Ces mises à jour sont gérées par Dependabot.
