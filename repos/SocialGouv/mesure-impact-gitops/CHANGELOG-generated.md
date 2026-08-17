## Changelog : mesure-impact-gitops (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois a été marqué par l'initialisation du dépôt et l'optimisation du pipeline de déploiement. Les évolutions visent à sécuriser la récupération des composants et à renforcer la stabilité et la reproductibilité des environnements de développement et de production.

### Évolutions techniques
- **Sécurité et automatisation** : Amélioration du processus de récupération des versions de charts Helm via GHCR, permettant désormais de s'affranchir de l'utilisation de secrets partagés.
- **Fiabilité du déploiement** : Correction du mécanisme de rendu des manifests pour garantir que le namespace cible est systématiquement associé aux fichiers générés.
- **Stabilité des environnements** : Verrouillage des versions (pinning) pour les environnements de développement et de production afin d'assurer des déploiements prévisibles.

### Autres changements
- Initialisation (bootstrap) de la structure du dépôt GitOps.
