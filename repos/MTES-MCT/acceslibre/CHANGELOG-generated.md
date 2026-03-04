## Changelog : acceslibre (30 derniers jours)

### Résumé
Le projet a connu une période d'amélioration continue, avec des corrections de bugs, des optimisations de performance et une migration vers des composants d'interface utilisateur plus modernes et conformes aux standards du gouvernement français (DSFR). Des améliorations ont également été apportées à l'import de données, notamment pour les cinémas, et à la gestion des contributions.

### Évolutions fonctionnelles

- Ajout de la possibilité d'ajouter une image depuis la page de détails d'un ERP. [#2463](https://github.com/MTES-MCT/acceslibre/pull/2463)
- Amélioration de l'import des données pour les cinémas, avec ajout de tests. [#2476](https://github.com/MTES-MCT/acceslibre/pull/2476)
- Prise en charge du format XML pour l'import de données. [#2505](https://github.com/MTES-MCT/acceslibre/pull/2505)
- Mise en place d'un système de révision, de changement de type d'utilisateur et d'enregistrement des actions lors de la prise en charge d'un ERP. [#2501](https://github.com/MTES-MCT/acceslibre/pull/2501)
- Correction de l'ordre d'affichage des contributions reçues. [#2467](https://github.com/MTES-MCT/acceslibre/pull/2467)
- Correction d'un bug lié à la pagination. [#2466](https://github.com/MTES-MCT/acceslibre/pull/2466)
- Correction de l'affichage des valeurs booléennes lors de l'import. [#2478](https://github.com/MTES-MCT/acceslibre/pull/2478)
- Correction d'un problème avec le lien "pas de photo". [#2481](https://github.com/MTES-MCT/acceslibre/pull/2481)
- Mise en place d'un bouton pour prendre en charge un ERP. [#2490](https://github.com/MTES-MCT/acceslibre/pull/2490)
- Correction de l'affichage du texte dans le widget. [#2477](https://github.com/MTES-MCT/acceslibre/pull/2477)
- Correction de l'affichage des erreurs dans les champs de saisie. [#2491](https://github.com/MTES-MCT/acceslibre/pull/2491) et [#2520](https://github.com/MTES-MCT/acceslibre/pull/2520)
- Correction de fautes de frappe dans les messages liés aux prises en charge. [#2502](https://github.com/MTES-MCT/acceslibre/pull/2502)
- Amélioration du wording du modal de prise en charge et correction des attributs ARIA. [#2503](https://github.com/MTES-MCT/acceslibre/pull/2503)

### Évolutions techniques

- Mise à jour de Django en version 6.0.2. [#2464](https://github.com/MTES-MCT/acceslibre/pull/2464)
- Suppression de Bootstrap et remplacement par des composants DSFR (Design System for French Administration). [#2440](https://github.com/MTES-MCT/acceslibre/pull/2440) et [#2479](https://github.com/MTES-MCT/acceslibre/pull/2479)
- Refactoring du code pour supprimer RGAA et la librairie crispy_forms. [#2488](https://github.com/MTES-MCT/acceslibre/pull/2488)
- Refactoring du widget. [#2484](https://github.com/MTES-MCT/acceslibre/pull/2484)
- Tentative d'optimisation des performances. [#2453](https://github.com/MTES-MCT/acceslibre/pull/2453)
- Remplacement de `@import` par `@use` dans les feuilles de style. [#2522](https://github.com/MTES-MCT/acceslibre/pull/2522)
- Suppression de npm. [#2521](https://github.com/MTES-MCT/acceslibre/pull/2521)

### Autres changements

- Correction de problèmes liés à l'affichage des photos et des liens. [#2485](https://github.com/MTES-MCT/acceslibre/pull/2485)
- Ajustements CSS pour améliorer l'apparence de l'interface. [#2486](https://github.com/MTES-MCT/acceslibre/pull/2486) et [#2487](https://github.com/MTES-MCT/acceslibre/pull/2487)
- Suppression du fichier `package-lock.json`.
- Plusieurs mises à jour de dépendances (eslint, faker, @panoramax/web-viewer, phonenumbers, pnpm, markdown, redis, ipython, deepl, outscraper, sentry-sdk, npm, pandas, gunicorn, django-debug-toolbar, parsel, @sentry/browser, prettier, ruff).
