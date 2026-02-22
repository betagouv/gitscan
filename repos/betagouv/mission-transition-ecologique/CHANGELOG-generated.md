## Changelog : mission-transition-ecologique (30 derniers jours)

### Résumé
Ce changelog résume les évolutions apportées à l'application au cours du dernier mois. Les principales améliorations concernent l'ajout de nouvelles sources de données pour les aides publiques (ADEME), la correction de bugs et l'amélioration de l'expérience utilisateur, notamment avec l'intégration d'un iframe pour la vérification du SIRET et des corrections sur la page d'accueil. Des mises à jour régulières des données des programmes et projets ont également été effectuées.

### Évolutions fonctionnelles
- Ajout des programmes bruts de l'ADEME, enrichissant ainsi l'offre d'aides disponibles. (#2438)
- Intégration d'un iframe permettant la vérification du SIRET directement dans l'application. (#2493)
- Correction d'un bug sur la page d'accueil concernant la vérification de la valeur du thème pour la limite de projets. (#2478)
- Amélioration de l'URL pour une meilleure accessibilité. (#2373)
- Publication de la release "agir" apportant des améliorations non spécifiées. (#2418)

### Évolutions techniques
- Correction de la gestion des valeurs nulles provenant des données PostHog dans la fonction `generate_company_id`. (#2469)
- Reconstruction de la page de détail pour les programmes archivés, avec des améliorations de logging. (#2467)
- Mise à jour des données statiques de l'application. (#2466)

### Autres changements
- Mises à jour régulières des données des programmes et des projets via les workflows automatisés. (Plusieurs commits, ex: #2510, #2509, #2506, #2496, #2501, #2494, #2495, #2491, #2479, #2480, #2475, #2470, #2472, #2471, #2465, #2460, #2449, #2448)
- Mise à jour des projets via les workflows automatisés. (Plusieurs commits, ex: #2503, #2501, #2494, #2491, #2479, #2470, #2464, #2460, #2448)
