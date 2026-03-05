## Changelog : document-ia (30 derniers jours)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'extraction d'informations à partir de documents, notamment avec une meilleure gestion des schémas complexes et l'ajout de la prise en charge de l'OCR Mistral avec des images. Des corrections de bugs ont également été apportées pour améliorer la fiabilité du système.

### Évolutions fonctionnelles
- Ajout du modèle de certificat Visale [#50](https://github.com/betagouv/document-ia/issues/50).
- Amélioration de la gestion des schémas complexes pour les prompts d'extraction et les résultats de l'API [#49](https://github.com/betagouv/document-ia/issues/49).
- L'OCR Mistral peut désormais utiliser des images au lieu de PDF [#45](https://github.com/betagouv/document-ia/issues/45).
- Ajout de la date d'émission lors de l'extraction d'informations à partir de documents 2Ddoc [#46](https://github.com/betagouv/document-ia/issues/46).

### Évolutions techniques
- Mise à jour de la version du parser 2Ddoc dans les workers [#47](https://github.com/betagouv/document-ia/issues/47).
- Correction d'un bug empêchant la re-tentative des erreurs récupérables [#43](https://github.com/betagouv/document-ia/issues/43).
