## Changelog : mobilic-api (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec l'introduction des demandes de détachement d'employés et des fonctionnalités de contestation. Les rapports d'activité (PDF/Excel) ont été nettement améliorés pour offrir une lecture plus précise des temps de pause et des activités scindées, tandis que les outils d'administration ont été renforcés par un mode impersonnalisation plus complet et une meilleure gestion des droits.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités métier** :
    - Mise en place du processus de demande de détachement d'employés, incluant l'envoi automatique d'emails [#731](https://github.com/MTES-MCT/mobilic-api/pull/731).
    - Introduction de la possibilité pour les employés de formuler des contestations [#722](https://github.com/MTES-MCT/mobilic-api/pull/722).
- **Amélioration des exports et rapports (PDF/Excel)** :
    - Meilleure lisibilité des activités scindées (mention "scindé") et intégration des motifs d'activité dans l'historique des missions.
    - Optimisation des colonnes de temps de pause et calcul des totaux dans les exports de jours travaillés.
    - Correction des doublons de motifs de litige et meilleure gestion des fuseaux horaires pour les dates de contrôle.
- **Administration et support** :
    - Renforcement du mode impersonnalisation : possibilité de créer des missions et de tracer les actions de support dans les exports [#732](https://github.com/MTES-MCT/mobilic-api/pull/732), [#749](https://github.com/MTES-MCT/mobilic-api/pull/749).
    - Amélioration du contenu, du formatage et de la fiabilité des emails de détachement.
    - Sécurisation des calculs de réglementation en exigeant les droits d'administrateur entreprise [#741](https://github.com/MTES-MCT/mobilic-api/pull/741).

### Évolutions techniques
- **Performance et Base de données** :
    - Optimisation des performances via la gestion des index (ajout d'index sur les calculs de réglementation et suppression des index redondants) [#740](https://github.com/MTES-MCT/mobilic-api/pull/740).
    - Amélioration de la rapidité du tableau de bord pour le suivi des validations en attente.
- **Infrastructure et CI/CD** :
    - Intégration des "Scalingo Review Apps" pour permettre des environnements de test temporaires par fonctionnalité [#737](https://github.com/MTES-MCT/mobilic-api/pull/737).
- **Fiabilité et Maintenance** :
    - Mise en place d'un système de cache pour les webinaires Livestorm afin d'optimiser les appels.
    - Réduction du bruit d'alertes dans Sentry pour une meilleure surveillance des erreurs réelles [#724](https://github.com/MTES-MCT/mobilic-api/pull/724).
    - Refactorisation du code de gestion de l'historique pour limiter la duplication de logique.

### Autres changements
- Consolidation et nettoyage des branches de migration de la base de données.
- Ajout de tests de sécurité (scope guards) pour le mode impersonnalisation.
