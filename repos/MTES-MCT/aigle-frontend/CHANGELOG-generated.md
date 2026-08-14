## Changelog : aigle-frontend (30 derniers jours, au 12/08/2026)

### Résumé
Cette période a été marquée par un enrichissement significatif des capacités d'analyse territoriale, notamment avec l'intégration du niveau EPCI et l'amélioration des tableaux de bord. Les outils d'administration ont également été affinés pour offrir une meilleure gestion des collectivités et des droits, tandis que la robustesse technique a été renforcée par une meilleure intégration des outils de suivi et de communication.

### Évolutions fonctionnelles
- **Analyse et visualisation de données** :
    - Amélioration des statistiques et du tableau de bord DDT.
    - Intégration du niveau territorial EPCI dans l'application.
    - Ajout de nouvelles vues pour le déploiement, incluant la gestion par lots et par zones d'activités économiques (ZAE).
- **Administration** :
    - Optimisation de la gestion des collectivités avec l'ajout de nouveaux filtres.
    - Amélioration de la gestion des dépassements de groupe (group override).
    - Nettoyage de l'interface d'administration (masquage des boutons Brevo et Sentry pour les administrateurs).
- **Corrections d'interface (UX)** :
    - Correction du placement des messages de feedback.
    - Résolution d'un problème lors de l'édition multiple.

### Évolutions techniques
- **Monitoring et Communication** :
    - Amélioration de l'intégration de Sentry pour le suivi des erreurs.
    - Optimisation de l'intégration de Brevo pour la gestion des communications.
- **Authentification et Architecture** :
    - Correction de la gestion du rafraîchissement des jetons (refresh token).
    - Optimisation des imports au sein du module d'administration.
