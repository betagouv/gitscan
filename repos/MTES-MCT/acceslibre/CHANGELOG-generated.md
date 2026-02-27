## Changelog : acceslibre (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer la plateforme acceslibre, avec un focus sur l'optimisation des performances, la correction de bugs et l'amélioration de l'expérience utilisateur, notamment au niveau de l'import de données et de la gestion des contributions. Des efforts importants ont également été déployés pour moderniser la base de code et les dépendances du projet.

### Évolutions fonctionnelles
- Possibilité de joindre une image lors de la modification des détails d'un ERP. (#2463)
- Amélioration de la gestion des contributions : ordre d'affichage et pagination corrigés. (#2466, #2467)
- Support du format XML pour l'import de données. (#2505)
- Mise en place d'un système de révision et de journalisation lors de la prise en charge d'un ERP. (#2501)
- Ajout d'une fonctionnalité permettant de revendiquer un ERP. (#2490)
- Correction de bugs liés à l'affichage et au fonctionnement des formulaires. (#2491, #2500)
- Amélioration de l'import des données pour les cinémas. (#2476)

### Évolutions techniques
- Mise à jour de Django en version 6.0.2. (#2464)
- Refactorisation du code pour supprimer l'utilisation de Bootstrap et adopter le DSFR (Design System for French Administration). (#2440, #2479, #2480)
- Optimisation des requêtes SQL pour éviter les problèmes de performance (N+1 queries). (#2449)
- Suppression de RGAA et de la librairie crispy_forms, et refactoring du code associé. (#2488)
- Amélioration de l'optimisation de Panoramax et corrections d'accessibilité. (#2451, #2486)
- Remplacement de `@import` par `@use` dans les fichiers Sass. (#2522)
- Suppression de npm. (#2521)

### Autres changements
- Mise à jour de nombreuses dépendances (eslint, faker, @panoramax/web-viewer, phonenumbers, pnpm, markdown, redis, sentry-sdk, ipython, deepl, outscraper, parsel, @sentry/browser, gunicorn, django-debug-toolbar, django-import-export, frictionless, prettier, ruff).
- Correction de problèmes liés aux permissions d'administration. (#2488, #2509, #2520)
- Amélioration de la gestion des erreurs et des messages d'information. (#2485, #2508)
- Corrections de typos et améliorations de la lisibilité du code. (#2502, #2503)
- Suppression de `package-lock.json`.
- Suppression d'index inutiles sur la base de données. (#2448)
- Amélioration de la gestion des couleurs et du style visuel. (#2477, #2481, #2489)
- Ajout de tests pour l'import des données cinéma. (#2476)
- Correction de l'affichage des valeurs booléennes lors de l'import des données cinéma. (#2478)
