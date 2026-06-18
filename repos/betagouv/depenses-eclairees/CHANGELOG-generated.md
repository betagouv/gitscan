## Changelog : depenses-eclairees (30 derniers jours, au 15 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'analyse des documents, notamment les RIB et les avenants, avec des améliorations de l'extraction d'informations et du post-traitement. Des optimisations ont également été apportées à la synchronisation des données et au suivi des traitements par l'IA. L'interface utilisateur a été enrichie pour la gestion des avenants.

### Évolutions fonctionnelles
- Amélioration de l'affichage des numéros RIB et ajout d'un tri. [#141](https://github.com/betagouv/depenses-eclairees/issues/141)
- Ajout de champs pour les fiches navette, incluant un montant maximum. [#140](https://github.com/betagouv/depenses-eclairees/issues/140)
- Prise en charge des IBAN étrangers lors du post-traitement des RIB. [#139](https://github.com/betagouv/depenses-eclairees/issues/139)
- Ajout d'un front-end pour la gestion des avenants, incluant l'affichage et la normalisation des données. [#132](https://github.com/betagouv/depenses-eclairees/issues/132) et [#131](https://github.com/betagouv/depenses-eclairees/issues/131)
- Extraction enrichie et post-traitements pour les avenants, avec tests qualité via Grist.
- Synthèse des engagements à partir des pièces jointes, accessible via un lancement manuel. [#106](https://github.com/betagouv/depenses-eclairees/issues/106)
- Ajout de la date de création externe aux engagements et mise à jour de la logique de synchronisation. [#133](https://github.com/betagouv/depenses-eclairees/issues/133)
- Augmentation de la longueur maximale des champs de formulaire. [#135](https://github.com/betagouv/depenses-eclairees/issues/135)

### Évolutions techniques
- Ajout du suivi des modèles utilisés pour l'OCR, la classification et l'analyse de contenu. [#134](https://github.com/betagouv/depenses-eclairees/issues/134)
- Amélioration de la gestion des erreurs de connexion lors de la synchronisation.
- Mise à jour des crons pour une meilleure gestion des tâches planifiées.
- Optimisation des requêtes à la base de données pour la synthèse des engagements, réduisant le nombre de requêtes.
- Simplification du code pour le process unitaire par engagement, sans utilisation de Pandas.
- Ajout d'en-têtes forwarded et de paramètres de sécurité pour le déploiement.
- Refactoring des prompts pour les champs communs afin d'améliorer la cohérence.
- Ajout de métriques pour le comptage des tokens et la date de traitement. [#128](https://github.com/betagouv/depenses-eclairees/issues/128)
- Ajout de post-processing pour le titulaire du compte et ajout de regex pour EI/SCOP/SELAS. [#137](https://github.com/betagouv/depenses-eclairees/issues/137)
- Conservation du numéro de compte (AE, DC4) et mise à jour de la logique de post-traitement des RIB. [#129](https://github.com/betagouv/depenses-eclairees/issues/129)

### Autres changements
- Correction d'un test instable.
- Correction de l'affichage de la date lorsque celle-ci est vide.
- Tri des documents non traités.
- Correction de la banque seule dans le post-traitement des RIB.
- Retrait de tests redondants.
- Rebase de la table Engagement.
- Normalisation du booléen `avenant-incidence_bpu` dans les vues.
- Ajout de fonctions de test.
- Suppression de la page web privée.
