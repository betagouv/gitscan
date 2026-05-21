## Changelog : api-engagement (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en termes de gestion des accès, de performance et de robustesse. Des correctifs ont été apportés pour améliorer la stabilité de l'infrastructure et des nouvelles fonctionnalités ont été ajoutées pour faciliter l'intégration et l'utilisation de l'API, notamment pour les missions SDIS et les scripts d'auto-hébergement.

### Évolutions fonctionnelles
- Ajout de la gestion des journaux d'audit pour une meilleure traçabilité des actions sur l'API. [#1019](https://github.com/betagouv/api-engagement/issues/1019)
- Possibilité d'ajouter des scripts d'auto-hébergement pour l'API et l'application. [#1039](https://github.com/betagouv/api-engagement/issues/1039)
- Intégration des missions Service Civique dans le job Grimpio. [#977](https://github.com/betagouv/api-engagement/issues/977)
- Ajout d'une tabulation pour les clés API des annonceurs dans les paramètres de l'application. [#1015](https://github.com/betagouv/api-engagement/issues/1015)
- Amélioration de l'accessibilité des graphiques Metabase dans l'application. [#1025](https://github.com/betagouv/api-engagement/issues/1025)
- Possibilité de refuser des missions avec un commentaire obligatoire. [#1037](https://github.com/betagouv/api-engagement/issues/1037)
- Ajout de scripts pour les missions SDIS. [#942](https://github.com/betagouv/api-engagement/issues/942)
- Affichage de l'URL sandbox de l'API dans l'exemple curl de l'application. [#1012](https://github.com/betagouv/api-engagement/issues/1012)

### Évolutions techniques
- Refonte de la gestion des permissions et des contrôles d'accès avec des tests unitaires. [#1013](https://github.com/betagouv/api-engagement/issues/1013)
- Amélioration de la performance des recherches d'organisations en utilisant `tsvector`. [#950](https://github.com/betagouv/api-engagement/issues/950)
- Refactorisation de la gestion des webhooks Brevo pour une meilleure sécurité. [#1026](https://github.com/betagouv/api-engagement/issues/1026)
- Suppression de la validation des adresses IP Brevo. [#1027](https://github.com/betagouv/api-engagement/issues/1027)
- Mise en place d'une exécution séquentielle des agrégations du widget pour éviter les problèmes de concurrence. [#966](https://github.com/betagouv/api-engagement/issues/966)
- Suppression du magasin partagé de limitation de débit. [#959](https://github.com/betagouv/api-engagement/issues/959)
- Ajout de jobs de sauvegarde de la base de données. [#955](https://github.com/betagouv/api-engagement/issues/955)
- Ajout de limitation de débit pour les requêtes API (publisher et IP). [#932](https://github.com/betagouv/api-engagement/issues/932)
- Correction de l'URL de la plateforme dans la construction. [#1049](https://github.com/betagouv/api-engagement/issues/1049)
- Activation de la passerelle publique sur le staging. [#1048](https://github.com/betagouv/api-engagement/issues/1048)
- Déclaration Scaleway MNQ SQS. [#1047](https://github.com/betagouv/api-engagement/issues/1047)

### Autres changements
- Mise à jour de la documentation et du changelog.
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Publication des versions v1.5.0, v1.5.1, v1.6.0 et v1.7.0.
- Mise à jour des dépendances (actions/checkout, orhun/git-cliff-action, scaleway/action-scw, etc.).
