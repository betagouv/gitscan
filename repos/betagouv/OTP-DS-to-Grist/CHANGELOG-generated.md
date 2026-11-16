## Changelog : OTP-DS-to-Grist (30 derniers jours, au 15 novembre 2026)

### Résumé
Ce mois-ci, le connecteur a gagné en précision et en fiabilité. Les utilisateurs bénéficient d'une synchronisation plus riche (notamment pour les données OCR des pièces justificatives) et d'un meilleur suivi des processus. En parallèle, l'infrastructure technique a été stabilisée par l'introduction d'un système de gestion de base de données plus robuste et de nouveaux outils de test.

### Évolutions fonctionnelles
- **Synchronisation enrichie :** Prise en charge de la synchronisation des sous-colonnes OCR des pièces justificatives [#594](https://github.com/betagouv/OTP-DS-to-Grist/issues/594).
- **Flexibilité de synchronisation :** Possibilité de lancer des synchronisations multiples [#617](https://github.com/betagouv/OTP-DS-to-Grist/issues/617) et découplage des identifiants de colonnes pour une meilleure adaptabilité [#608](https://github.com/betagouv/OTP-DS-to-Grist/issues/608).
- **Amélioration du suivi :** Meilleure gestion de la progression des tâches de synchronisation [#622](https://github.com/betagouv/OTP-DS-to-Grist/issues/622).
- **Fiabilité des données :** Correction de la suppression des lignes de blocs dans Grist [#582](https://github.com/betagouv/OTP-DS-to-Grist/issues/582) et optimisation de la séquence de synchronisation automatique [#587](https://github.com/betagouv/OTP-DS-to-Grist/issues/587) (incluant la correction d'un décalage de synchronisation [#589](https://github.com/betagouv/OTP-DS-to-Grist/issues/589)).
- **Correction de configuration :** Prévention de la perte de données (token DN et numéro) si la clé Grist est manquante [#584](https://github.com/betagouv/OTP-DS-to-Grist/issues/584).

### Évolutions techniques
- **Gestion de données :** Mise en place d'un système de migrations pour la base de données [#618](https://github.com/betagouv/OTP-DS-to-Grist/issues/618) et stockage de la durée des synchronisations en base [#581](https://github.com/betagouv/OTP-DS-to-Grist/issues/581).
- **Optimisation et Qualité :** Amélioration des performances des filtres serveur [#561](https://github.com/betagouv/OTP-DS-to-Grist/issues/561), ajout de tests pour la base de données [#606](https://github.com/betagouv/OTP-DS-to-Grist/issues/606) et intégration d'un outil d'audit [#619](https://github.com/betagouv/OTP-DS-to-Grist/issues/619).
- **Refactorisation :** Nettoyage du code (suppression de code mort [#578](https://github.com/betagouv/OTP-DS-to-Grist/issues/578)) et normalisation des noms de colonnes [#579](https://github.com/betagouv/OTP-DS-to-Grist/issues/579).

### Autres changements
- **Documentation :** Mise à jour de la documentation technique, incluant le schéma des tables Grist [#632](https://github.com/betagouv/OTP-DS-to-Grist/issues/632).
- **Interface utilisateur :** Corrections de texte et mise à jour des titres du service dans l'interface principale.
