## Changelog : acceslibre (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer la plateforme acceslibre en se concentrant sur l'expérience utilisateur, la performance et la qualité du code. Des améliorations ont été apportées à l'interface d'administration, à la gestion des contributions et à l'import de données. Des corrections de bugs et des optimisations ont également été réalisées pour améliorer la stabilité et la réactivité de la plateforme. Une migration vers des composants d'interface utilisateur plus modernes (DSFR) est en cours.

### Évolutions fonctionnelles
- Possibilité d'ajouter une image depuis la page de détails d'un ERP. (#2463)
- Amélioration de l'affichage des contributions reçues (tri). (#2467)
- Correction d'un bug lié à la pagination. (#2466)
- Prise en charge du format XML pour l'import de données. (#2505)
- Amélioration du formulaire de réclamation avec des corrections de wording et d'accessibilité. (#2501, #2503)
- Possibilité de revendiquer un ERP (#2490)
- Correction de l'affichage des valeurs booléennes lors de l'import des cinémas. (#2478)
- Correction d'un bug lié à l'affichage du lien "Pas de photo". (#2481)

### Évolutions techniques
- Migration progressive vers l'utilisation de composants d'interface utilisateur du Design System Français (DSFR) pour remplacer Bootstrap. (#2440, #2489)
- Optimisation des requêtes pour éviter les problèmes de performance liés aux requêtes N+1. (#2449, #2452)
- Mise à jour de Django en version 6.0.2. (#2464)
- Refactoring du code pour améliorer la lisibilité et la maintenabilité. (#2484, #2488)
- Suppression de RGAA et de la librairie crispy_forms. (#2488)
- Suppression de `package-lock.json`.
- Suppression de Bootstrap. (#2439, #2479, #2480)

### Autres changements
- Correction de bugs mineurs et améliorations de l'interface utilisateur. (#2500, #2502, #2504, #2506, #2507, #2508, #2509)
- Corrections de typos. (#2502)
- Amélioration de la gestion des erreurs (email, site web). (#2508)
- Diverses mises à jour de dépendances (voir commits dependabot). (#2455, #2456, #2457, #2458, #2459, #2460, #2461, #2470, #2471, #2472, #2473, #2474, #2492, #2493, #2494, #2495, #2497, #2498)
- Ajout de tests pour l'import des cinémas. (#2476)
- Suppression d'index inutiles. (#2448)
- Amélioration de la configuration pour l'environnement Docker. (#2450)
- Ajout de la possibilité de changer le type d'utilisateur et d'enregistrer un log lors d'une réclamation. (#2501)
