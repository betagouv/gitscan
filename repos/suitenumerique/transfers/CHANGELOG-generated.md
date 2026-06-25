## Changelog : transfers (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, le service de transfert de fichiers a bénéficié d'améliorations significatives en matière de sécurité, d'expérience utilisateur et de refonte technique. L'ajout d'un scanner de fichiers dangereux renforce la sécurité, tandis que la migration vers Vite et Tanstack Router modernise l'architecture frontend et améliore les performances. De nouvelles options d'authentification et des améliorations de l'affichage des dates contribuent à une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'un scanner de fichiers pour empêcher le stockage de fichiers dangereux. [#9](https://github.com/suitenumerique/transfers/issues/9)
- Amélioration de l'affichage des dates : affichage relatif intelligent avec date complète au survol.
- Ajout d'un flux de connexion ProConnect sans authentification préalable. [#13](https://github.com/suitenumerique/transfers/issues/13)
- Implémentation de liens uniques à usage unique qui s'auto-désactivent après le premier téléchargement complet. [#5](https://github.com/suitenumerique/transfers/issues/5)
- Autorisation de l'origine S3 dans la directive `connect-src` du CSP pour les uploads.

### Évolutions techniques
- Refonte complète du frontend : migration de Next.js vers Vite et Tanstack Router.
- Renforcement du flux de téléchargement et correction des points soulevés lors de la revue de code. [#11](https://github.com/suitenumerique/transfers/issues/11)
- Déplacement de Tanstack Router dans les dépendances de développement.
- Correction d'un problème identifié par CodeRabbit.

### Autres changements
- Ajout de documentation. [#246148d](https://github.com/suitenumerique/transfers/commit/246148d)
