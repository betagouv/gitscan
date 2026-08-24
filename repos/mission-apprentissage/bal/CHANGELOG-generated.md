## Changelog : bal (30 derniers jours, au 22 août 2026)

### Résumé
Ce mois-ci, BAL a amélioré l'expérience de gestion des listes de diffusion en offrant un meilleur suivi de l'avancement et des notifications automatiques par email. Le projet a également bénéficié d'une modernisation majeure de ses outils de développement et d'un renforcement de sa sécurité.

### Évolutions fonctionnelles
- **Gestion des listes de diffusion** : ajout d'un indicateur d'avancement sur la page de gestion [#535](https://github.com/mission-apprentissage/bal/pull/535) et mise en place de notifications par email à la fin du traitement des listes [#533](https://github.com/mission-apprentissage/bal/pull/533).

### Évolutions techniques
- **Modernisation de la stack technique** : montée de version vers TypeScript 7 et Next.js 16.3, et migration de l'outillage de linting/formatage vers Biome [#4962](https://github.com/mission-apprentissage/bal/pull/4962).
- **Sécurité et maintenance** : correction d'une vulnérabilité critique (CVE) sur Vitest [#530](https://github.com/mission-apprentissage/bal/pull/530) et mise à jour de l'image Docker Metabase [#531](https://github.com/mission-apprentissage/bal/pull/531).
- **CI/CD et déploiement** : correction du processus de publication de l'image UI de production lors des releases [#537](https://github.com/mission-apprentissage/bal/pull/537).
