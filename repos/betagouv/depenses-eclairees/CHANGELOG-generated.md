## Changelog : depenses-eclairees (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la robustesse du traitement des documents, notamment des fichiers Excel et PDF volumineux, ainsi que sur l'amélioration de la qualité de l'extraction d'informations, en particulier pour les RIB et les documents financiers. Des corrections et des optimisations ont également été apportées à la synchronisation des données et à l'interface utilisateur.

### Évolutions fonctionnelles
- Amélioration de l'affichage des données CCAP et AE dans l'interface utilisateur, en affichant `ccp_simple` et `ccp_vae` comme CCAP et AE. [#108](https://github.com/betagouv/depenses-eclairees/issues/108)
- Reconstitution de l'IBAN à partir des autres codes présents sur les RIB, avec validation Luhn. [#105](https://github.com/betagouv/depenses-eclairees/issues/105)
- Amélioration de la qualité des tests E2E avec l'ajout de `best_comparison` et `included_column`. [#100](https://github.com/betagouv/depenses-eclairees/issues/100)
- Suppression de sections et champs non évalués dans l'interface utilisateur pour les documents AE et CCAP, simplifiant l'affichage.
- Amélioration de la gestion des erreurs lors de la synchronisation des données avec un mécanisme de nouvelle tentative en cas de code 401. [#99](https://github.com/betagouv/depenses-eclairees/issues/99)
- Prise en charge de l'OCR sur tous les fichiers PDF. [#102](https://github.com/betagouv/depenses-eclairees/issues/102)
- Amélioration du dictionnaire de classification et mise à jour des tests associés. [#96](https://github.com/betagouv/depenses-eclairees/issues/96)

### Évolutions techniques
- Optimisation du traitement des fichiers Excel pour éviter les erreurs de mémoire (OOM) lors de l'extraction des données. [#115](https://github.com/betagouv/depenses-eclairees/issues/115) et [#116](https://github.com/betagouv/depenses-eclairees/issues/116)
- Limitation de la taille des fichiers Excel acceptés à 2Mo pour améliorer la performance.
- Mise en place d'une file d'attente dédiée pour les tâches d'OCR afin d'améliorer la réactivité du système.
- Amélioration de la gestion des fichiers volumineux lors de l'OCR. [#109](https://github.com/betagouv/depenses-eclairees/issues/109)
- Amélioration du système de permissions avec support des wildcards. [#114](https://github.com/betagouv/depenses-eclairees/issues/114)
- Correction de bugs et amélioration de la robustesse du code de synchronisation.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Amélioration de l'interface admin avec des filtres plus pertinents. [#112](https://github.com/betagouv/depenses-eclairees/issues/112) et [#111](https://github.com/betagouv/depenses-eclairees/issues/111)

### Autres changements
- Mise à jour des dépendances. [#113](https://github.com/betagouv/depenses-eclairees/issues/113)
- Nettoyage du code et corrections mineures. [#118](https://github.com/betagouv/depenses-eclairees/issues/118)
- Suppression de la variable `num_ej` des noms de fichiers.
- Correction d'erreurs introduites par la reconstruction de l'IBAN. [#107](https://github.com/betagouv/depenses-eclairees/issues/107)
- Suppression de `try_correct_false_siret`.
- Suppression de la section "Durée du Marché" en double dans les CCAP. [#101](https://github.com/betagouv/depenses-eclairees/issues/101)
