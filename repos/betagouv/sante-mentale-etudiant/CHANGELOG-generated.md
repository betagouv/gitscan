## Changelog : sante-mentale-etudiant (30 derniers jours, au 13 juillet 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la mise en place de l'intégration continue avec GitHub Actions et la migration vers le gestionnaire de paquets pnpm. Une première bannière a été ajoutée à la page d'accueil.

### Évolutions fonctionnelles
- Ajout d'une première bannière sur la page d'accueil. [#1](https://github.com/betagouv/sante-mentale-etudiant/issues/1)

### Évolutions techniques
- Mise en place initiale des jobs GitHub Actions pour l'intégration continue. [#5](https://github.com/betagouv/sante-mentale-etudiant/pull/5)
- Migration du gestionnaire de paquets vers pnpm version 11.
- Configuration de pnpm pour autoriser les scripts de build pour le déploiement.
- Correction de la configuration de pnpm pour les overrides.
- Correction d'une vulnérabilité de sécurité dans la dépendance `postcss` via pnpm audit.

### Autres changements
- Initialisation du dépôt avec un premier commit.
