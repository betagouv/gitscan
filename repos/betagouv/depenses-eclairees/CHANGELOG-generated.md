## Changelog : depenses-eclairees (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la synchronisation des données, le traitement des fichiers RIB (Relevé d'Identité Bancaire) et l'ajout de fonctionnalités pour la gestion des engagements et des navettes. Des optimisations ont également été apportées pour améliorer la performance et la robustesse de l'application.

### Évolutions fonctionnelles
- Amélioration de la gestion des synchronisations, notamment pour les données sur plusieurs mois [#142](https://github.com/betagouv/depenses-eclairees/issues/142).
- Prise en charge des IBAN étrangers dans le post-traitement des fichiers RIB [#139](https://github.com/betagouv/depenses-eclairees/issues/139).
- Ajout de champs spécifiques pour les fiches navette [#140](https://github.com/betagouv/depenses-eclairees/issues/140) et [#137](https://github.com/betagouv/depenses-eclairees/issues/137).
- Ajout d'un affichage amélioré des noms de fichiers RIB avec possibilité de tri [#141](https://github.com/betagouv/depenses-eclairees/issues/141).
- Implémentation d'un front-end pour la gestion des avenants [#132](https://github.com/betagouv/depenses-eclairees/issues/132).
- Synthèse des engagements à partir des pièces jointes, avec lancement manuel [#106](https://github.com/betagouv/depenses-eclairees/issues/106).

### Évolutions techniques
- Ajout du suivi des modèles pour l'OCR, la classification et l'analyse du contenu [#134](https://github.com/betagouv/depenses-eclairees/issues/134).
- Amélioration de la gestion des erreurs de connexion lors de la synchronisation.
- Mise à jour des crons pour une meilleure planification des tâches.
- Propagation de la date depuis les sources externes vers le modèle Document [#136](https://github.com/betagouv/depenses-eclairees/issues/136).
- Augmentation de la longueur maximale des champs de formulaire [#135](https://github.com/betagouv/depenses-eclairees/issues/135).
- Optimisation des requêtes à la base de données pour la synthèse des engagements.
- Simplification du code de synthèse des engagements pour un traitement unitaire par engagement.
- Ajout de headers forwarded et configuration de paramètres de sécurité.
- Ajout du champ `external_created_at` aux engagements et mise à jour de la logique de synchronisation [#133](https://github.com/betagouv/depenses-eclairees/issues/133).

### Autres changements
- Correction d'un test instable.
- Retrait de tests redondants.
- Normalisation du champ booléen `avenant-incidence_bpu` dans les vues.
- Ajout de tests unitaires et de fonctions de test pour la synthèse des engagements.
- Rebase de la table Engagement.
