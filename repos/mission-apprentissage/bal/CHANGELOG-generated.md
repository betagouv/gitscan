## Changelog : bal (30 derniers jours, au 20 août 2026)

### Résumé
Ce mois-ci, BAL a bénéficié d'améliorations sur la gestion des listes de diffusion et d'une mise à jour majeure de ses outils de développement pour garantir une meilleure sécurité, une performance accrue et une maintenance simplifiée.

### Évolutions fonctionnelles
- Optimisation du processus de génération des listes de diffusion, incluant désormais l'envoi d'une notification par email une fois le traitement terminé ([#533](https://github.com/mission-apprentissage/bal/issues/533), [#534](https://github.com/mission-apprentissage/bal/issues/534)).

### Évolutions techniques
- Migration majeure de l'environnement de développement : passage à TypeScript 7, Next.js 16.3 et adoption de Biome pour remplacer ESLint et Prettier ([#4962](https://github.com/mission-apprentissage/bal/issues/4962), [#532](https://github.com/mission-apprentissage/bal/issues/532)).
- Mise à jour de l'infrastructure Docker pour l'image Metabase ([#531](https://github.com/mission-apprentissage/bal/issues/531)).
- Correction d'une vulnérabilité de sécurité critique (CVE) identifiée sur Vitest ([#530](https://github.com/mission-apprentissage/bal/issues/530)).
