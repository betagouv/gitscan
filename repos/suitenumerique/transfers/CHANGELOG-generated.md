## Changelog : transfers (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, le service de transfert de fichiers a bénéficié d'améliorations significatives en termes de sécurité, d'expérience utilisateur et d'architecture. Une nouvelle fonctionnalité de scan de fichiers a été ajoutée pour prévenir le stockage de fichiers dangereux, et l'interface utilisateur a été modernisée avec une migration vers Vite et TanStack Router, améliorant ainsi la performance et la maintenabilité.

### Évolutions fonctionnelles
- Ajout d'un scan de fichiers pour bloquer le stockage de fichiers potentiellement dangereux. [#9](https://github.com/suitenumerique/transfers/issues/9)
- Amélioration de l'affichage des dates : affichage relatif intelligent (ex: "il y a 2 jours") avec date complète au survol.
- Renforcement de la sécurité du flux de téléchargement et correction des points soulevés lors de la revue de code. [#11](https://github.com/suitenumerique/transfers/issues/11)
- Implémentation d'un flux de connexion ProConnect simplifié. [#13](https://github.com/suitenumerique/transfers/issues/13)
- Autorisation de l'origine S3 dans la directive `connect-src` du CSP pour les uploads.

### Évolutions techniques
- Migration de Next.js vers Vite et TanStack Router pour une meilleure performance et une architecture plus moderne.
- Correction des retours de CodeRabbit sur la PR #10.
- Déplacement de TanStack Router dans les dépendances de développement.
- Correction d'un point soulevé par CodeRabbit.

### Autres changements
- Aucun changement significatif à signaler.
