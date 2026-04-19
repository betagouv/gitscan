## Changelog : OTP-DS-to-Grist (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse de la synchronisation des données, l'amélioration de l'expérience utilisateur avec des messages d'erreur plus précis et une meilleure indication de la progression, ainsi que sur l'ajout de données pour deux nouvelles tables. Des efforts ont également été faits pour améliorer la documentation et la configuration du projet.

### Évolutions fonctionnelles
- Ajout de la synchronisation des données pour deux nouvelles tables. [#278](https://github.com/betagouv/OTP-DS-to-Grist/issues/278)
- Amélioration des messages d'erreur pour une meilleure compréhension des problèmes de synchronisation. [#281](https://github.com/betagouv/OTP-DS-to-Grist/issues/281) et [#276](https://github.com/betagouv/OTP-DS-to-Grist/issues/276)
- Amélioration de l'affichage de la progression de la synchronisation, en supprimant les détails unitaires des temps d'appels pour une vue plus claire. [#273](https://github.com/betagouv/OTP-DS-to-Grist/issues/273)
- Correction de la création de la table "avis". [#265](https://github.com/betagouv/OTP-DS-to-Grist/issues/265)
- Amélioration de la précision du "loader" (indicateur de chargement). [#270](https://github.com/betagouv/OTP-DS-to-Grist/issues/270) et [#249](https://github.com/betagouv/OTP-DS-to-Grist/issues/249)
- Ajout de la récupération et de la création de la table "expert". [#247](https://github.com/betagouv/OTP-DS-to-Grist/issues/247) et [#248](https://github.com/betagouv/OTP-DS-to-Grist/issues/248)

### Évolutions techniques
- Optimisation des performances : mise en cache globale, utilisation d'instructeurs uniques, traitement par lots des champs et ajout de champs de requêtes d'extraction. [#224](https://github.com/betagouv/OTP-DS-to-Grist/issues/224)
- Suppression de code mort et ajout de "fallbacks" (solutions de repli) pour améliorer la robustesse. [#257](https://github.com/betagouv/OTP-DS-to-Grist/issues/257)
- Suppression des crochets et guillemets dans les données JSON pour éviter les erreurs de parsing. [#256](https://github.com/betagouv/OTP-DS-to-Grist/issues/256)

### Autres changements
- Ajout d'un nouveau README pour le dossier de synchronisation, améliorant la documentation du projet. [#282](https://github.com/betagouv/OTP-DS-to-Grist/issues/282) et [#280](https://github.com/betagouv/OTP-DS-to-Grist/issues/280)
- Publication de la version 0.7.0. [#189](https://github.com/betagouv/OTP-DS-to-Grist/issues/189)
