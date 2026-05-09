## Changelog : depenses-eclairees (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la qualité de l'extraction de données, notamment pour les fichiers Excel et les RIB, ainsi que sur l'ajout de nouvelles métriques pour évaluer la performance des modèles d'IA. Des optimisations ont été apportées pour gérer les fichiers volumineux et améliorer la robustesse du système. L'interface d'administration a également été améliorée.

### Évolutions fonctionnelles
- **OCR et Extraction de données :** Amélioration de la gestion des fichiers Excel volumineux (jusqu'à 3Mo) et optimisation du processus d'extraction pour éviter les erreurs de mémoire. [#115](https://github.com/betagouv/depenses-eclairees/issues/115)
- **RIB et IBAN :** Reconstitution de l'IBAN à partir d'autres codes présents sur les RIB. Validation du SIRET via l'algorithme Luhn, similaire à la validation des IBAN. [#103](https://github.com/betagouv/depenses-eclairees/issues/103), [#105](https://github.com/betagouv/depenses-eclairees/issues/105), [#107](https://github.com/betagouv/depenses-eclairees/issues/107)
- **Interface d'administration :** Amélioration de l'interface d'administration avec des filtres plus pertinents et une mise à jour de la liste des filtres pour les événements de suivi. [#112](https://github.com/betagouv/depenses-eclairees/issues/112)
- **Affichage des données :** Affichage des codes CCAP et AE pour les champs `ccp_simple` et `ccp_vae`. [#108](https://github.com/betagouv/depenses-eclairees/issues/108)
- **Permissions :** Amélioration du système de permissions avec la prise en charge de caractères génériques (wildcards). [#114](https://github.com/betagouv/depenses-eclairees/issues/114)

### Évolutions techniques
- **Métriques d'évaluation :** Ajout de métriques (précision, rappel, hallucinations) pour évaluer la qualité de la détection et de l'extraction des données par les modèles d'IA. [#110](https://github.com/betagouv/depenses-eclairees/issues/110)
- **Files d'attente :** Mise en place d'une file d'attente dédiée pour les tâches d'OCR afin d'améliorer la performance et la scalabilité.
- **Refactoring :** Refactorisation des tests de bout en bout pour simplifier la gestion des colonnes et améliorer la vérification des valeurs nulles.
- **Gestion des fichiers :** Ignorer les dossiers `__MACOSX` lors de la décompression des fichiers ZIP. [#119](https://github.com/betagouv/depenses-eclairees/issues/119)
- **Dépendances :** Ajout de la dépendance `pyxlsb` pour la gestion des fichiers Excel au format `.xlsb`.
- **Pipeline :** Les fichiers Excel volumineux sont maintenant marqués comme "skipped" dans le pipeline.

### Autres changements
- Suppression de la dépendance `jupyter`.
- Suppression de l'option `--force-analyze` dans le cron.
- Ajout de détails aux messages d'erreur de l'API OCR.
- Diminution de la limite de taille des fichiers Excel à 2Mo.
- Mise à jour des dépendances.
- Amélioration de la gestion des statuts de traitement.
- Normalisation de la gestion des payloads de durée.
- Amélioration des fonctions de comparaison.
- Suppression d'importations inutiles.
- Correction de bugs et nettoyage du code.
