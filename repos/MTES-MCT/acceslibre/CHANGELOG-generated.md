## Changelog : acceslibre (30 derniers jours)

### Résumé
Ce changelog couvre les 30 derniers jours d'évolution de la plateforme acceslibre. Les améliorations portent principalement sur l'interface utilisateur, la gestion des contributions, l'import de données et la correction de bugs. Des efforts importants ont également été faits pour moderniser les dépendances et améliorer la performance de l'application.

### Évolutions fonctionnelles
- Possibilité d'ajouter une image depuis la page de détails d'un ERP. (#2463)
- Amélioration de l'interface utilisateur pour la recherche et l'information administrative. (#2441)
- Correction de l'affichage des erreurs dans les champs de saisie des contributions. (#2438)
- Amélioration de l'interface pour la réclamation d'un ERP, incluant des corrections de typographie et d'accessibilité. (#2503, #2502)
- Ajout de la prise en charge du format XML pour l'import de données. (#2505)
- Correction de bugs liés à l'affichage des informations de contact (email, site web). (#2508)
- Amélioration de l'affichage des liens sociaux des ERP. (#2504, #2506)
- Correction de l'affichage des espaces dans les détails des ERP. (#2507)
- Correction de l'import des données cinéma et ajout de tests associés. (#2476)
- Correction de l'import des valeurs booléennes pour les cinémas. (#2478)
- Correction de l'affichage des données sur la page d'accueil pour les personnels. (#2483)

### Évolutions techniques
- Mise à jour de Django en version 6.0.1. (#2425)
- Refactoring du code pour supprimer l'utilisation de Bootstrap et adopter le DSFR (Design System des Finances Publiques). (#2440, #2479, #2480, #2439)
- Optimisation des requêtes pour éviter les problèmes de performance liés à N+1. (#2449)
- Suppression de code inutile. (#2437)
- Amélioration de l'optimisation et de l'accessibilité de la page Panoramax. (#2451)
- Mise à jour de nombreuses dépendances (pandas, gunicorn, sentry-sdk, redis, etc.).
- Suppression de l'index sur reversion. (#2448)
- Utilisation de geopf au lieu de api-adresse.data.gouv.fr. (#2427)

### Autres changements
- Correction d'un problème de permissions d'administration. (#2509)
- Mise à jour de la documentation et de la configuration.
- Suppression du fichier `package-lock.json`.
- Ajout de tests unitaires.
- Amélioration de la configuration pour l'environnement Docker.
- Correction de la pagination. (#2466)
- Amélioration de la gestion des notifications de contributions. (#2467)
- Mise à jour des dépendances de développement (prettier, ruff, faker, django-debug-toolbar).
