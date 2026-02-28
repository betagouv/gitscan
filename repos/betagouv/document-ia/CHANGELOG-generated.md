## Changelog : document-ia (30 derniers jours)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'extraction d'informations à partir de documents, notamment via l'ajout de la date d'émission sur les documents 2ddoc et la correction de problèmes liés à l'OCR avec Mistral. Une correction a également été apportée pour assurer la re-tentative automatique des erreurs temporaires.

### Évolutions fonctionnelles
- Amélioration de l'extraction d'informations des documents 2ddoc : la date d'émission est maintenant extraite et disponible. (#46)
- Correction d'un bug empêchant l'utilisation d'images au lieu de PDF avec l'OCR Mistral. (#45)
- Correction d'un problème de re-tentative des erreurs : les erreurs temporaires sont maintenant automatiquement re-tentées. (#43)

### Évolutions techniques
- Mise à jour de la version du parser 2ddoc dans le worker. (#47)
