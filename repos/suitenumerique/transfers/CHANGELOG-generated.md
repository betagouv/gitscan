## Changelog : transfers (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, le service de transfert de fichiers a bénéficié d'améliorations significatives en matière de sécurité, d'expérience utilisateur et d'architecture. L'ajout d'un scanner de fichiers renforce la sécurité des données stockées, tandis que la migration vers une nouvelle stack frontend (Vite + Tanstack Router) modernise l'application et améliore ses performances. Des corrections et améliorations ont également été apportées pour fluidifier le processus de téléchargement et d'affichage des dates.

### Évolutions fonctionnelles
- Ajout d'un scanner de fichiers pour empêcher le stockage de fichiers dangereux. [#9](https://github.com/suitenumerique/transfers/issues/9)
- Amélioration de l'affichage des dates : dates relatives intelligentes avec date complète au survol.
- Renforcement de la sécurité du flux de téléchargement et correction des points soulevés lors de la revue de code. [#11](https://github.com/suitenumerique/transfers/issues/11)
- Ajout d'un flux de connexion ProConnect simplifié. [#13](https://github.com/suitenumerique/transfers/issues/13)
- Correction d'un problème empêchant l'utilisation de S3 comme origine dans la politique de sécurité du contenu (CSP) pour les téléchargements.

### Évolutions techniques
- Migration du frontend de Next.js vers Vite + Tanstack Router pour une meilleure performance et une architecture plus moderne.
- Correction des remarques de CodeRabbit concernant la revue de code de la PR #10.
- Déplacement de Tanstack Router vers les dépendances de développement.
- Correction d'un problème identifié par CodeRabbit.
- Amélioration de la robustesse du scan antivirus, même en cas de scanner indisponible.
- Correction des points soulevés lors de la revue de code concernant le flux de rescan.

### Autres changements
- Aucun changement significatif à signaler.
