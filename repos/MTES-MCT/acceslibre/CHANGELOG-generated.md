## Changelog : acceslibre (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la collecte et de l'importation de données (notamment via APIDAE), l'optimisation des performances (cache Redis, statistiques) et l'ajout de nouvelles questions pour affiner le signalement de l'accessibilité des établissements. Des corrections et améliorations ont également été apportées à l'interface utilisateur et à la gestion des PDF RPA.

### Évolutions fonctionnelles
- Ajout de questions signalétiques et ajustement des questions existantes pour les établissements scolaires et les lieux de santé. [#2620](https://github.com/MTES-MCT/acceslibre/issues/2620)
- Possibilité de contourner les vérifications de doublons lors de l'importation de données. [#2626](https://github.com/MTES-MCT/acceslibre/issues/2626)
- Amélioration de la recherche avec correction d'une erreur Sentry et support des combobox RGAa. [#2609](https://github.com/MTES-MCT/acceslibre/issues/2609)
- Utilisation de POST pour la génération des PDF RPA. [#2623](https://github.com/MTES-MCT/acceslibre/issues/2623)
- Import des données APIDAE. [#2641](https://github.com/MTES-MCT/acceslibre/issues/2641)

### Évolutions techniques
- Mise à jour de Django. [#2625](https://github.com/MTES-MCT/acceslibre/issues/2625)
- Implémentation d'un cache Redis pour stocker les événements des widgets et les vider dans la base de données toutes les heures, améliorant ainsi les performances. [#2624](https://github.com/MTES-MCT/acceslibre/issues/2624)
- Mise en cache du nombre d'éléments pour la pagination, améliorant les performances des requêtes. [#2621](https://github.com/MTES-MCT/acceslibre/issues/2621)
- Application de correctifs pour forcer les versions des packages. [#2635](https://github.com/MTES-MCT/acceslibre/issues/2635)
- Désactivation temporaire de l'acquisition via Scrapfly en attendant une réécriture. [#2640](https://github.com/MTES-MCT/acceslibre/issues/2640)

### Autres changements
- Suppression temporaire de la génération de PDF RPA et de son indexation. [#2622](https://github.com/MTES-MCT/acceslibre/issues/2622) et [#2611](https://github.com/MTES-MCT/acceslibre/issues/2611)
- Amélioration des statistiques de performance. [#2610](https://github.com/MTES-MCT/acceslibre/issues/2610)
- Correction d'un problème de login pour les contributeurs. [#2636](https://github.com/MTES-MCT/acceslibre/issues/2636)
- Diverses mises à jour de dépendances (Sentry, frictionless, gunicorn, ruff, django-modeltranslation, psycopg2, pnpm, eslint, prettier, dompurify, scrapfly-sdk, phonenumbers, faker) ont été appliquées.
