## Changelog : acceslibre (30 derniers jours, au 29 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment concernant la gestion des établissements relevant du Référentiel des Personnes en Situation de Handicap (RPA) et la simplification des processus de réclamation. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Amélioration de l'affichage et du rendu du texte du bouton de traduction. [#2726](https://github.com/MTES-MCT/acceslibre/issues/2726)
- Modification de la date de vérification de la mise à jour lors de la création, de l'édition ou de l'importation d'un ERP. [#2712](https://github.com/MTES-MCT/acceslibre/issues/2712)
- Les ERP relevant du RPA ne peuvent plus être modifiés. [#2698](https://github.com/MTES-MCT/acceslibre/issues/2698) et [#0f28f06](https://github.com/MTES-MCT/acceslibre/commit/0f28f06)
- Amélioration du processus de réclamation :
    - Mise à jour des règles de déclenchement de la modale de réclamation. [#2701](https://github.com/MTES-MCT/acceslibre/issues/2701)
    - Mise à jour de la page de succès et de la page de réclamation. [#2700](https://github.com/MTES-MCT/acceslibre/issues/2700) et [#a06c137](https://github.com/MTES-MCT/acceslibre/commit/a06c137)
    - Affichage conditionnel du badge RPA en fonction du type d'ERP. [#2715](https://github.com/MTES-MCT/acceslibre/issues/2715)
- Traduction du champ d'accessibilité à la demande. [#2692](https://github.com/MTES-MCT/acceslibre/issues/2692)

### Évolutions techniques
- Suppression de la bibliothèque `bleach` au profit de `nh3` pour une meilleure gestion de la sécurité. [#2744](https://github.com/MTES-MCT/acceslibre/issues/2744)
- Ajout de la surveillance du cache dans Sentry pour une meilleure détection des problèmes de performance. [#2727](https://github.com/MTES-MCT/acceslibre/issues/2727)
- Mise à jour de la configuration Docker pour mapper les ports 8000 et 7000. [#2728](https://github.com/MTES-MCT/acceslibre/issues/2728)
- Mise à jour de la version de Django. [#2716](https://github.com/MTES-MCT/acceslibre/issues/2716)

### Autres changements
- Documentation mise à jour.
- Diverses corrections de bugs et améliorations de la qualité du code.
- Mises à jour de dépendances (eslint, prettier, djlint, psycopg2-binary, django-debug-toolbar, django-reversion, setuptools, phonenumbers, ruff, pnpm, dompurify, scrapfly-sdk, sentry-sdk, actions/checkout).
