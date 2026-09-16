## Changelog : st-deploycenter (30 derniers jours, au 14 septembre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'introduction de nouveaux services liés à ProConnect et à la gestion des domaines. Parallèlement, la sécurité et la fiabilité du processus de déploiement ont été considérablement renforcées.

### Évolutions fonctionnelles
- Introduction d'une nouvelle API ProConnect et d'un service dédié à la gestion des domaines [#60](https://github.com/suitenumerique/st-deploycenter/pull/60).
- Correction de plusieurs problèmes d'affichage de l'interface utilisateur (UI) sur les blocs ProConnect.

### Évolutions techniques
- Optimisation majeure du processus de déploiement incluant l'utilisation de Caddy, de builds "distroless", le filtrage par adresse IP et le support de la double authentification (2FA) [#61](https://github.com/suitenumerique/st-deploycenter/pull/61).
- Amélioration des scripts de gestion des listes d'autorisation (allowlist) pour ProConnect.

### Autres changements
- Mise en conformité du formatage du code (Prettier) pour les fichiers de listes d'autorisation.
