## Changelog : mission-transition-ecologique (30 derniers jours)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives, notamment l'ajout de données de programmes ADEME, des corrections de bugs pour une meilleure stabilité et l'implémentation d'une fonctionnalité d'intégration via iframe avec la possibilité de pré-remplir le SIRET. Des mises à jour régulières des données des programmes et projets ont également été effectuées.

### Évolutions fonctionnelles
- Ajout des données brutes des programmes ADEME, enrichissant ainsi l'offre d'aides disponibles. (#2438)
- Implémentation d'un iframe permettant d'intégrer l'application et de pré-remplir le SIRET de l'entreprise. (#2493, #2515)
- Correction d'un bug concernant la vérification de la valeur du thème pour la limite de projets sur la page d'accueil. (#2478)
- Amélioration de la gestion des programmes archivés, permettant de retrouver la page de détail. (#2467)
- Correction de la gestion des valeurs nulles provenant des données PostHog dans la fonction `generate_company_id`. (#2469)

### Évolutions techniques
- Mise à jour des paquets Sentry à la version 10.27.0. (#2331)
- Mises à jour régulières des données des programmes et projets via les workflows automatisés. (#2449, #2465, #2471, #2472, #2475, #2480, #2491, #2494, #2495, #2496, #2501, #2503, #2506, #2509, #2510)

### Autres changements
- Mise à jour des données statiques. (#2466)
- Publication de la release "agir". (#2418)
