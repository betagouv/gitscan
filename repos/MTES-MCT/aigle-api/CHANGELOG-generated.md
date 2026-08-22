## Changelog : aigle-api (30 derniers jours, au 20/08/2026)

### Résumé
Les dernières mises à jour (incluant les PR [#82](https://github.com/MTES-MCT/aigle-api/pull/82) à [#85](https://github.com/MTES-MCT/aigle-api/pull/85)) enrichissent les capacités d'analyse géospatiale de la plateforme, notamment avec l'intégration du niveau EPCI et des descriptions de zones personnalisées. L'expérience de pilotage est également améliorée grâce à l'optimisation du tableau de bord DDT et de l'interface d'administration.

### Évolutions fonctionnelles
- Intégration du niveau EPCI dans l'application.
- Amélioration du tableau de bord DDT.
- Ajout de descriptions pour les zones géographiques personnalisées.
- Amélioration de l'interface d'administration :
    - Ajout de nouveaux filtres pour les collectivités.
    - Meilleure gestion de l'écrasement des groupes.

### Évolutions techniques
- Implémentation de "feature flags" pour le contrôle des fonctionnalités.
- Ajout de vues "batches" et "zae" dans le processus de déploiement.
- Optimisation des imports dans l'interface d'administration.
- Correction d'une commande permettant de forcer la mise à jour des zones géographiques personnalisées (`geocustomzone`).
