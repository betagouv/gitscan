## Changelog : api-apprentissage (30 derniers jours, au 22 mai 2026)

### Résumé
Cette mise à jour apporte une amélioration de la robustesse de l'API en ajoutant un délai d'attente pour les requêtes transmises au service LBA. Cela permet d'éviter les blocages en cas de réponse tardive de LBA et d'améliorer la stabilité globale de l'application.

### Évolutions techniques
- Ajout d'un timeout sur les requêtes forwardées vers LBA pour éviter les blocages.  Cette correction est liée à l'issue [#485](https://github.com/mission-apprentissage/api-apprentissage/issues/485).
