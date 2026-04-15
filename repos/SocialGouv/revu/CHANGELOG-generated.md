## Changelog : revu (30 derniers jours, au 14 avril 2026)

### Résumé
Cette version apporte principalement des corrections de bugs et des améliorations techniques pour stabiliser et sécuriser l'application. Les utilisateurs ne constateront pas de nouvelles fonctionnalités majeures, mais bénéficieront d'une meilleure fiabilité et d'une préparation pour les déploiements en environnement de pré-production.

### Évolutions fonctionnelles
Aucune évolution fonctionnelle majeure n'a été introduite dans cette version.

### Évolutions techniques
- Mise à jour de la configuration `sealed-secrets` pour l'environnement de pré-production ([#277](https://github.com/SocialGouv/revu/issues/277)).
- Migration vers l'outil de gestion de paquets `pnpm` ([#268](https://github.com/SocialGouv/revu/issues/268)).
- Ajout d'une étape de compilation TypeScript (`tsc`) dans le pre-commit hook pour garantir la qualité du code ([#269](https://github.com/SocialGouv/revu/issues/269)).
- Amélioration de la gestion des erreurs lors des interactions avec GitHub et ajout de logs de débogage ([5e9b43b](https://github.com/SocialGouv/revu/commit/5e9b43b4f63051d5a23ee85fd1294ee46ca93ef9)).
- Correction d'un problème de divergence entre les numéros de ligne de début et de fin dans les suggestions.
- Suppression des blocs de suggestions redondants ([#274](https://github.com/SocialGouv/revu/issues/274), [#271](https://github.com/SocialGouv/revu/issues/271)).
- Correction d'une erreur qui provoquait des fuites d'erreurs dans les pull requests ([#276](https://github.com/SocialGouv/revu/issues/276)).
- Correction d'un problème lié au volume temporaire.
- Mise à jour de la version du modèle ANTHROPIC dans la configuration.

### Autres changements
Aucun autre changement significatif à signaler.
