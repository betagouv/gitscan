## Changelog : OTP-DS-to-Grist (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la synchronisation des données, la gestion des erreurs et l'amélioration de l'expérience utilisateur. Des tables de données supplémentaires sont désormais synchronisées et la précision des messages d'erreur a été accrue. Des corrections ont également été apportées pour améliorer la robustesse de l'application et la gestion des dates.

### Évolutions fonctionnelles
- Ajout de la synchronisation de données pour deux nouvelles tables [#278](https://github.com/betagouv/OTP-DS-to-Grist/pull/278).
- Amélioration de la gestion des dates lors de la conversion vers le format Grist, notamment pour la colonne `date_modif` [#283](https://github.com/betagouv/OTP-DS-to-Grist/pull/283).
- Suppression d'un fallback inutile pour la date de modification [#292](https://github.com/betagouv/OTP-DS-to-Grist/pull/292).
- Correction du libellé dans le pied de page [#300](https://github.com/betagouv/OTP-DS-to-Grist/pull/300).
- Amélioration de la précision des messages d'erreur pour les synchronisations automatiques [#276](https://github.com/betagouv/OTP-DS-to-Grist/pull/276) et pour les erreurs générales [#281](https://github.com/betagouv/OTP-DS-to-Grist/pull/281).
- Ajout d'un README pour le dossier de synchronisation [#282](https://github.com/betagouv/OTP-DS-to-Grist/pull/282).
- Correction de la création de la table "avis" [#265](https://github.com/betagouv/OTP-DS-to-Grist/pull/265).
- Ajout de la récupération et de la création de la table "expert" [#248](https://github.com/betagouv/OTP-DS-to-Grist/pull/248).

### Évolutions techniques
- Suppression du code mort et ajout de fallbacks pour une meilleure robustesse [#257](https://github.com/betagouv/OTP-DS-to-Grist/pull/257).
- Suppression des crochets et guillemets JSON pour éviter les erreurs de parsing [#256](https://github.com/betagouv/OTP-DS-to-Grist/pull/256).
- Suppression des détails unitaires des temps d'appels dans les logs de progression [#273](https://github.com/betagouv/OTP-DS-to-Grist/pull/273).
- Amélioration de la gestion du loader pour une meilleure indication de l'état d'avancement [#249](https://github.com/betagouv/OTP-DS-to-Grist/pull/249) et [#270](https://github.com/betagouv/OTP-DS-to-Grist/pull/270).

### Autres changements
- Publication de la version 0.7.0 [#189](https://github.com/betagouv/OTP-DS-to-Grist/pull/189).
- Mise à jour de plusieurs dépendances de développement (pytest-cov, ruff, poethepoet, baseline-browser-mapping, eslint, requests, cryptography).
