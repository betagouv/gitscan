## Changelog : depenses-eclairees (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse de la synchronisation des données, l'amélioration de la qualité de l'extraction d'informations (notamment pour les RIB, SIRET et devis), et la correction de bugs liés au traitement de certains documents. Des optimisations ont également été apportées à la gestion des fichiers et à l'utilisation des modèles de langage.

### Évolutions fonctionnelles
- Amélioration de la reconstitution de l'IBAN à partir des codes bancaires présents sur les RIB. [#107](https://github.com/betagouv/depenses-eclairees/issues/107)
- Ajout de la validation du SIRET via l'algorithme Luhn, similaire à la validation des IBAN. [#103](https://github.com/betagouv/depenses-eclairees/issues/103)
- Amélioration de l'extraction d'informations des devis, notamment pour l'objet du devis. [#78](https://github.com/betagouv/depenses-eclairees/issues/78)
- Prise en charge des documents de sous-traitance avec des améliorations de l'interface et des tests. [#83](https://github.com/betagouv/depenses-eclairees/issues/83)
- Amélioration de la gestion des fichiers volumineux lors de l'OCR. [#109](https://github.com/betagouv/depenses-eclairees/issues/109)
- Correction de bugs liés à la synchronisation des engagements et à la gestion des dates. [#88](https://github.com/betagouv/depenses-eclairees/issues/88), [#95](https://github.com/betagouv/depenses-eclairees/issues/95), [#97](https://github.com/betagouv/depenses-eclairees/issues/97)

### Évolutions techniques
- Passage au modèle de langage Mistral Medium pour certaines tâches d'extraction. [#91](https://github.com/betagouv/depenses-eclairees/issues/91)
- Refactorisation du code pour améliorer l'organisation et la lisibilité, notamment dans les vues et les tests.
- Amélioration de la gestion des erreurs lors du traitement des fichiers Excel. [#87](https://github.com/betagouv/depenses-eclairees/issues/87)
- Optimisation de la logique de déduplication des données lors de la synchronisation.
- Amélioration de la robustesse de la synchronisation en cas d'erreurs 401. [#99](https://github.com/betagouv/depenses-eclairees/issues/99)
- Stabilisation des tests qualité end-to-end avec de nouvelles métriques de comparaison. [#100](https://github.com/betagouv/depenses-eclairees/issues/100)

### Autres changements
- Mise à jour des dépendances. [#92](https://github.com/betagouv/depenses-eclairees/issues/92)
- Suppression temporaire d'une tâche cron pour maintenance.
- Amélioration de la documentation et des tests unitaires.
- Nettoyage du code et suppression de sections/champs obsolètes dans l'interface utilisateur.
- Ajout de tests pour la fonction de post-processing des documents CCAP.
- Suppression de champs inutiles dans l'interface utilisateur pour les documents AE et CCAP.
- Correction de problèmes de formatage et de ponctuation dans les descriptions de classification.
- Ajout de la possibilité de comparer des JSON complexes dans les tests qualité.
- Amélioration de la gestion des valeurs nulles dans les tests.
- Suppression de la correction automatique des SIRET incorrects.
- Réutilisation des prompts existants pour différents types de documents. [#104](https://github.com/betagouv/depenses-eclairees/issues/104)
- Ajout de la fonction `included_columns` pour la comparaison des tests qualité. [#96](https://github.com/betagouv/depenses-eclairees/issues/96)
- Amélioration de la gestion des noms d'entités légales.
