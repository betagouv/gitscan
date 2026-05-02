## Changelog : depenses-eclairees (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la robustesse du traitement des fichiers (en particulier les fichiers Excel volumineux), l'optimisation de l'OCR, et l'amélioration de la qualité de l'extraction d'informations, notamment concernant les RIB et les CCAP/AE. Des améliorations de l'interface d'administration et de la gestion des permissions ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de l'affichage des CCAP et AE dans l'interface utilisateur, en affichant `ccp_simple` et `ccp_vae` comme CCAP et AE. [#108](https://github.com/betagouv/depenses-eclairees/issues/108)
- Amélioration de la reconstitution de l'IBAN à partir des codes présents sur les RIB. [#105](https://github.com/betagouv/depenses-eclairees/issues/105)
- Ajout de la validation Luhn du SIRET, similaire à la validation IBAN. [#103](https://github.com/betagouv/depenses-eclairees/issues/103)
- Réutilisation des prompts existants pour l'extraction d'informations sur différents types de documents (CCAP, AE, avenant, devis). [#104](https://github.com/betagouv/depenses-eclairees/issues/104)
- Amélioration de l'interface d'administration avec des mises à jour de filtres et une meilleure organisation. [#112](https://github.com/betagouv/depenses-eclairees/issues/112)
- Amélioration du système de permissions avec la prise en charge de caractères joker (wildcard) pour les scopes. [#114](https://github.com/betagouv/depenses-eclairees/issues/114)

### Évolutions techniques
- Optimisation du traitement des fichiers Excel pour éviter les erreurs de mémoire (OOM) lors de l'extraction de données. [#115](https://github.com/betagouv/depenses-eclairees/issues/115)
- Mise en place d'une file d'attente dédiée pour les tâches d'OCR afin d'améliorer la performance et la réactivité du système.
- Limitation de la taille des fichiers Excel à 2Mo pour éviter les problèmes de performance.
- Ajout de la dépendance `pyxlsb` pour la gestion des fichiers Excel au format .xlsb.
- Amélioration de la robustesse de la synchronisation des engagements en gérant les cas où `external_updated_at` est nul.
- Lancement de l'OCR sur tous les fichiers PDF. [#102](https://github.com/betagouv/depenses-eclairees/issues/102)
- Correction de bugs liés au traitement des fichiers xlsx. [#109](https://github.com/betagouv/depenses-eclairees/issues/109) et [#116](https://github.com/betagouv/depenses-eclairees/issues/116)
- Correction d'erreurs introduites par la reconstruction de l'IBAN. [#107](https://github.com/betagouv/depenses-eclairees/issues/107)

### Autres changements
- Nettoyage du code. [#118](https://github.com/betagouv/depenses-eclairees/issues/118)
- Suppression de la section "Durée du Marché" redondante dans les CCAP. [#101](https://github.com/betagouv/depenses-eclairees/issues/101)
- Stabilisation des tests qualité e2e. [#100](https://github.com/betagouv/depenses-eclairees/issues/100)
- Mise à jour des dépendances. [#113](https://github.com/betagouv/depenses-eclairees/issues/113)
- Correction du filtre `filter_stuck_batches`. [#111](https://github.com/betagouv/depenses-eclairees/issues/111)
- Les fichiers Excel de plus de 3Mo sont maintenant ignorés pendant le traitement.
- Suppression de l'option `--force-analyze` dans le cron.
- Ajout de détails aux messages d'erreur de l'API OCR.
- Les fichiers Excel volumineux sont maintenant marqués comme ignorés dans le pipeline.
