## Changelog : depenses-eclairees (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse de la synchronisation des données, l'amélioration de la qualité de l'extraction d'informations (OCR et LLM), et l'affinage de la validation des données, notamment pour les RIB et les SIRET. Des corrections ont également été apportées pour améliorer la gestion des fichiers volumineux et des erreurs lors du traitement des documents. Enfin, des ajustements ont été faits à l'interface utilisateur pour simplifier l'affichage et la pertinence des informations.

### Évolutions fonctionnelles
- Amélioration de la gestion des fichiers volumineux lors de l'OCR (#109).
- Affichage des codes CCAP et AE pour les champs `ccp_simple` et `ccp_vae` (#108, #104).
- Amélioration de la validation et de la reconstitution des numéros IBAN à partir des codes RIB (#105, #107).
- Validation du numéro SIRET via l'algorithme Luhn, similaire à la validation IBAN (#103, #71c1c75).
- Amélioration de la déduplication des données lors de la synchronisation des engagements (#89, #88).
- Correction de l'affichage des noms de fichiers lors de la synchronisation (#86).

### Évolutions techniques
- Passage au modèle de langage Mistral Medium pour améliorer la performance et la qualité de l'extraction d'informations (#91, #86).
- Amélioration de la gestion des erreurs lors du traitement des fichiers Excel, avec une conversion des `AssertionError` en `ValueError` pour une meilleure gestion des exceptions (#87).
- Stabilisation des tests d'intégration (e2e) avec l'ajout de `best_comparison` et `included_column` (#100).
- Ajout de fonctions de post-processing pour les noms d'entités légales (#94).
- Amélioration de la logique de synchronisation pour préserver les dates de mise à jour les plus récentes (#89).
- Correction de la gestion des erreurs 401 lors de la synchronisation (#99).
- Ajout de la gestion des fichiers PDF lors de l'OCR (#102).
- Correction d'un bug dans le traitement des fichiers XLSX (#6d2c671).

### Autres changements
- Suppression de sections et de champs obsolètes ou non évalués dans l'interface utilisateur pour les types de documents AE et CCAP.
- Ajustement de la définition du champ "prestations" pour une meilleure concision et simplification du schéma.
- Interdiction des valeurs nulles pour les champs de liste de lots dans le schéma CCAP, avec ajout de post-processing défensif (#85).
- Amélioration de la classification des documents avec mise à jour du dictionnaire et des tests associés (#96).
- Suppression d'une tâche cron de maintenance (#d9f4869).
- Ajout de tests unitaires pour les fonctions de post-processing CCAP.
- Correction de la définition des champs pour les tests unitaires.
- Mise à jour des dépendances (#92).
