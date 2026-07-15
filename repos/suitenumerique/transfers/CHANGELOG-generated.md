## Changelog : transfers (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, le service de transfert de fichiers a bénéficié d'améliorations significatives en matière de sécurité, d'expérience utilisateur et d'architecture. L'ajout d'un scanner de fichiers renforce la sécurité des données, tandis que la migration vers une nouvelle infrastructure frontend améliore la performance et la maintenabilité du projet.

### Évolutions fonctionnelles
- Ajout d'un scanner de fichiers pour empêcher le stockage de fichiers dangereux. [#9](https://github.com/suitenumerique/transfers/issues/9)
- Amélioration de l'affichage des dates : affichage relatif intelligent avec date complète au survol.
- Renforcement de la sécurité du flux de téléchargement et correction des points soulevés lors de la revue de code. [#11](https://github.com/suitenumerique/transfers/issues/11)
- Implémentation d'un flux de connexion ProConnect simplifié. [#13](https://github.com/suitenumerique/transfers/issues/13)
- Correction d'un problème permettant l'utilisation d'une origine S3 dans la politique de sécurité du contenu (CSP) pour les uploads. [#7](https://github.com/suitenumerique/transfers/issues/7)

### Évolutions techniques
- Migration du frontend de Next.js vers Vite et TanStack Router pour une meilleure performance et une architecture plus moderne.
- Correction des remarques de CodeRabbit concernant la revue de code de la PR #10.
- Déplacement de TanStack dans les dépendances de développement.
- Amélioration de la robustesse du scanner antivirus en cas de scanner indisponible.
- Correction des points soulevés lors de la revue de code concernant le flux de rescan.

### Autres changements
- Aucune information supplémentaire à signaler.
