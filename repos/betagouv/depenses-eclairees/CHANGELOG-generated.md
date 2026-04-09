## Changelog : depenses-eclairees (30 derniers jours, au 2026-04-02)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la synchronisation des données, la qualité de l'extraction d'informations (notamment pour les devis et les CCAP), et la stabilisation des tests automatisés. Des optimisations ont également été apportées à la gestion des fichiers et au traitement des erreurs lors de la synchronisation. L'utilisation du modèle de langage Mistral Medium a été étendue pour améliorer la performance.

### Évolutions fonctionnelles
- Amélioration de la synchronisation des engagements et des ordres d'achat/demandes de garantie avec une meilleure gestion des mises à jour et des conflits de dates [#88](https://github.com/betagouv/depenses-eclairees/issues/88), [#89](https://github.com/betagouv/depenses-eclairees/issues/89).
- L'OCR est maintenant exécuté sur tous les fichiers PDF [#102](https://github.com/betagouv/depenses-eclairees/issues/102).
- Amélioration de l'extraction d'informations pour les devis, incluant la gestion de l'objet et des raisons associées, ainsi que des améliorations de la qualité générale [#78](https://github.com/betagouv/depenses-eclairees/issues/78), [#96](https://github.com/betagouv/depenses-eclairees/issues/96).
- Gestion améliorée des documents de sous-traitance, avec des modifications des vues et des modèles correspondants.
- Ajout de la fonctionnalité `included_columns` pour la comparaison des tests de qualité [#99](https://github.com/betagouv/depenses-eclairees/issues/99).
- Stabilisation des tests de qualité E2E avec l'ajout de `best_comparison` et `included_column` [#100](https://github.com/betagouv/depenses-eclairees/issues/100).

### Évolutions techniques
- Passage au modèle de langage Mistral Medium pour améliorer la performance et la qualité de l'extraction d'informations [#91](https://github.com/betagouv/depenses-eclairees/issues/91), [#78](https://github.com/betagouv/depenses-eclairees/issues/78).
- Refactoring des imports dans `views.py` pour améliorer l'organisation du code.
- Amélioration de la logique de déduplication pour gérer les synchronisations importantes [#84](https://github.com/betagouv/depenses-eclairees/issues/84), [#85](https://github.com/betagouv/depenses-eclairees/issues/85).
- Mise à jour des dépendances [#92](https://github.com/betagouv/depenses-eclairees/issues/92).
- Amélioration de la gestion des erreurs lors du téléchargement des fichiers, avec un nouveau seuil de retentative.
- Suppression de la section "Durée du Marché" redondante dans les CCAP [#101](https://github.com/betagouv/depenses-eclairees/issues/101).
- Ajout de post-processing pour les noms d'entités juridiques.
- Amélioration de la gestion des valeurs nulles dans les schémas CCAP.

### Autres changements
- Documentation améliorée pour l'extraction du SIREN.
- Suppression de sections et de champs du front-end pour les types de documents AE et CCAP, en fonction des évaluations de qualité [#98](https://github.com/betagouv/depenses-eclairees/issues/98).
- Correction de logs et de descriptions de classifications.
- Suppression temporaire d'une tâche cron pour maintenance.
- Ajustement de la fréquence des tâches cron.
- Ajout de tests unitaires pour la fonction de post-processing CCAP.
- Suppression de tests obsolètes.
- Amélioration de la comparaison des JSON complexes dans les tests de qualité.
