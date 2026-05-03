## Changelog : OTP-DS-to-Grist (30 derniers jours, au 01 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse de la synchronisation automatique, l'amélioration de l'expérience utilisateur avec des messages d'erreur plus clairs et un meilleur suivi de la progression, ainsi que sur la correction de bugs affectant l'affichage des données et le comptage des dossiers synchronisés. De nouvelles fonctionnalités ont également été ajoutées, notamment un bandeau d'information pour la synchronisation automatique et une documentation plus complète.

### Évolutions fonctionnelles
- Amélioration des messages d'erreur pour la synchronisation automatique, les rendant plus précis et informatifs. [#304](https://github.com/betagouv/OTP-DS-to-Grist/issues/304)
- Ajout d'un bandeau d'information pour indiquer l'état de la synchronisation automatique. [#293](https://github.com/betagouv/OTP-DS-to-Grist/issues/293)
- Correction du comptage des dossiers synchronisés dans l'interface. [#295](https://github.com/betagouv/OTP-DS-to-Grist/issues/295)
- Correction de l'affichage du texte dans le pied de page. [#300](https://github.com/betagouv/OTP-DS-to-Grist/issues/300)
- Correction de la suppression d'une date de modification en fallback. [#292](https://github.com/betagouv/OTP-DS-to-Grist/issues/292)
- Amélioration de la gestion des dates lors de la conversion entre le format Démarches Simplifiées et Grist. [#283](https://github.com/betagouv/OTP-DS-to-Grist/issues/283)
- Ajout de la synchronisation de données de deux nouvelles tables. [#278](https://github.com/betagouv/OTP-DS-to-Grist/issues/278)
- Amélioration de la précision des erreurs lors de la synchronisation automatique. [#276](https://github.com/betagouv/OTP-DS-to-Grist/issues/276)
- Suppression des détails unitaires des temps d'appels dans la progression de la synchronisation. [#273](https://github.com/betagouv/OTP-DS-to-Grist/issues/273)
- Correction de la création de la table "avis". [#265](https://github.com/betagouv/OTP-DS-to-Grist/issues/265)

### Évolutions techniques
- Publication de la version 0.7.0 avec l'intégration de Docker et Codespaces. [#189](https://github.com/betagouv/OTP-DS-to-Grist/issues/189)
- Ajout d'une documentation pour le dossier de synchronisation. [#282](https://github.com/betagouv/OTP-DS-to-Grist/issues/282)
- Amélioration de la précision des messages d'erreur pour la synchronisation automatique. [#281](https://github.com/betagouv/OTP-DS-to-Grist/issues/281)

### Autres changements
- Mise à jour de la documentation et du README. [#280](https://github.com/betagouv/OTP-DS-to-Grist/issues/280)
- Mises à jour de dépendances (Ruff, pytest-cov, poethepoet, requests, cryptography, eslint, baseline-browser-mapping). Ces mises à jour sont de maintenance et n'affectent pas directement l'utilisateur.
