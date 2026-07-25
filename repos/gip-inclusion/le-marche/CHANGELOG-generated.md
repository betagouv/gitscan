## Changelog : le-marche (30 derniers jours, au 11 juillet 2026)

### Résumé
Les dernières mises à jour de "Le Marché de l'Inclusion" se concentrent sur l'amélioration de l'expérience utilisateur pour les acheteurs, notamment avec l'ajout d'une page dédiée aux "besoins inspirants" et l'affichage des coordonnées des structures pour les acheteurs connectés. Des améliorations de sécurité ont également été apportées, notamment en rendant le téléchargement de listes de recherche accessible uniquement aux utilisateurs authentifiés. Enfin, plusieurs mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'une page "besoins inspirants" pour les acheteurs, accessible au public, avec des secteurs d'activité tronqués et un tri chronologique. [#2151](https://github.com/gip-inclusion/le-marche/issues/2151)
- Corrections d'affichage sur la page "besoins inspirants" (carte CTA et pagination). [#2150](https://github.com/gip-inclusion/le-marche/issues/2150)
- Affichage des coordonnées de la structure pour les acheteurs connectés sur la page SIAE. [#2140](https://github.com/gip-inclusion/le-marche/issues/2140)
- Le téléchargement de la liste de recherche est désormais réservé aux utilisateurs authentifiés. [#2139](https://github.com/gip-inclusion/le-marche/issues/2139)
- Ajout d'une bannière promotionnelle pour "Les Traiteurs Engagés" sur la page SIAE. [#2137](https://github.com/gip-inclusion/le-marche/issues/2137)

### Évolutions techniques
- Génération du téléchargement de la liste SIAE à la volée pour optimiser les performances. [#2146](https://github.com/gip-inclusion/le-marche/issues/2146)

### Autres changements
- Mises à jour de plusieurs dépendances : astral-sh/setup-uv, coverage, sentry-sdk, huey, boto3, nh3, django-simple-history, redis, ruff, actions/setup-python, django-debug-toolbar, django-environ, pytest.
