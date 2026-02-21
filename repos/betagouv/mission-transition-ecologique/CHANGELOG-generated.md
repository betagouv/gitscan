## Changelog : mission-transition-ecologique (30 derniers jours)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives, notamment l'ajout de données ADEME brutes, la correction de bugs liés à l'affichage des programmes archivés et à la gestion des données PostHog, ainsi que l'intégration d'un iframe pour la vérification du SIRET. Des mises à jour régulières des données des programmes et projets ont également été effectuées.

### Évolutions fonctionnelles
- Ajout des données brutes des programmes ADEME (#2438)
- Intégration d'un iframe pour la vérification du numéro SIRET (#2493)
- Correction de l'affichage des pages de détail des programmes archivés (#2467)
- Amélioration de l'URL de l'application (#2373)
- Mise à jour de la page "À propos" avec un lien externe corrigé et une structure de carte améliorée (#2440)
- Correction d'un bug lié à la vérification de la valeur du thème pour la limite de projets sur la page d'accueil (#2478)
- Publication de la release "agir" (#2418)

### Évolutions techniques
- Gestion des valeurs nulles provenant des données PostHog dans la fonction `generate_company_id` (#2469)
- Mise à jour régulière des données des programmes et des projets (plusieurs commits, ex: #2510, #2496, #2480, #2475, #2472, #2471, #2465, #2449, #2448)

### Autres changements
- Mise à jour des données statiques (#2466)
