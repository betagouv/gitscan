## Changelog : acceslibre (30 derniers jours, au 06 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des performances, la correction de bugs et l'ajout de fonctionnalités liées à la génération de rapports d'accessibilité (RPA). Des améliorations ont également été apportées à la recherche et à la gestion des permissions utilisateurs. Enfin, plusieurs dépendances ont été mises à jour pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Amélioration de la recherche avec correction d'une erreur Sentry et support des combobox RGAAA. [#2609](https://github.com/MTES-MCT/acceslibre/issues/2609)
- Possibilité de demander l'API du widget par `asp_id`. [#2580](https://github.com/MTES-MCT/acceslibre/issues/2580)
- Correction d'un bug lié à l'édition du type d'utilisateur, limitant l'accès à cette fonctionnalité aux propriétaires des ERP. [#2576](https://github.com/MTES-MCT/acceslibre/issues/2576)
- Correction d'un bug concernant l'affichage des informations d'un ERP. [#2599](https://github.com/MTES-MCT/acceslibre/issues/2599)
- Correction d'un bug lié à la question "Pente" dans le formulaire. [#2600](https://github.com/MTES-MCT/acceslibre/issues/2600)
- Amélioration de la gestion des erreurs lors de la génération de l'URL RPA. [#2583](https://github.com/MTES-MCT/acceslibre/issues/2583)
- Correction d'un bug lié à la section "À propos". [#2577](https://github.com/MTES-MCT/acceslibre/issues/2577)

### Évolutions techniques
- Optimisation des performances lors de la récupération du nombre d'éléments pour la pagination, en utilisant un cache par requête. [#2621](https://github.com/MTES-MCT/acceslibre/issues/2621)
- Utilisation de la méthode POST pour la génération du PDF RPA. [#2623](https://github.com/MTES-MCT/acceslibre/issues/2623)
- Mise en place d'un switch Django-waffle pour activer/désactiver la fonctionnalité RPA. [#2578](https://github.com/MTES-MCT/acceslibre/issues/2578)
- Amélioration de la gestion des connexions à la base de données. [#2579](https://github.com/MTES-MCT/acceslibre/issues/2579)
- Optimisation des statistiques de performance. [#2610](https://github.com/MTES-MCT/acceslibre/issues/2610)

### Autres changements
- Mise à jour de Django. [#2625](https://github.com/MTES-MCT/acceslibre/issues/2625)
- Suppression temporaire de la génération de PDF RPA. [#2622](https://github.com/MTES-MCT/acceslibre/issues/2622)
- Suppression de l'indexation du PDF RPA. [#2611](https://github.com/MTES-MCT/acceslibre/issues/2611)
- Plusieurs mises à jour de dépendances (ruff, sentry-sdk, django-modeltranslation, @sentry/browser, prettier, dompurify, scrapfly-sdk, phonenumbers, faker, requests, psycopg2, redis, eslint, django-debug-toolbar, pandas). Ces mises à jour visent à améliorer la sécurité, la stabilité et les performances de la plateforme.
