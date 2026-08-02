## Changelog : api-apprentissage (30 derniers jours, au 1er août 2026)

### Résumé
Cette mise à jour apporte des corrections de sécurité importantes, améliore la gestion des erreurs lors de la communication avec le service LBA et met à jour la documentation du dépôt d'offres. Une rotation du secret principal SOPS a également été effectuée pour renforcer la sécurité.

### Évolutions fonctionnelles
- Correction d'un problème où l'API renvoyait une erreur 500 en cas de timeout lors de la communication avec le service LBA. Elle renvoie maintenant une erreur 504 plus appropriée. [#499](https://github.com/mission-apprentissage/api-apprentissage/issues/499)
- Mise à jour de la documentation `depot-offre.doc.ts`. [#497](https://github.com/mission-apprentissage/api-apprentissage/issues/497)

### Évolutions techniques
- Correction de deux vulnérabilités de sécurité critiques (CVE) dans les dépendances Vitest et Tar. [#498](https://github.com/mission-apprentissage/api-apprentissage/issues/498)
- Rotation du secret principal SOPS pour une meilleure sécurité. [#496](https://github.com/mission-apprentissage/api-apprentissage/issues/496)
