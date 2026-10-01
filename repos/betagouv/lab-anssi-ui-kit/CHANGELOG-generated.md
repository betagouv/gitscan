## Changelog : lab-anssi-ui-kit (30 derniers jours, au 30/09/2026)

### Résumé
Ce mois-ci, le projet a bénéficié d'une montée en maturité importante, axée sur la robustesse et la qualité du code. Outre l'ajout de nouveaux composants et l'amélioration de l'accessibilité, un travail conséquent a été réalisé pour renforcer la fiabilité des tests et la précision du typage TypeScript, garantissant ainsi une base plus stable pour les développeurs.

### Évolutions fonctionnelles
- **Nouveautés** : Ajout du composant `DsfrShare`.
- **Accessibilité** : Amélioration de la visibilité du focus et correction d'un problème de boucle de focus dans les modales contenant des boutons imbriqués.
- **Composants Lab** : Ajustements responsives pour le Bandeau de page (affichage mobile) et le Centre d'aide (positionnement des icônes).
- **Composants DSFR** : Rendu de la propriété `disabled` réactive et correction du comportement du menu déroulant (`DsfrDropdown`).
- **Icônes** : Ajout de l'icône "gamepad", compatibilité avec les styles DSFR et possibilité de personnaliser la taille des icônes.
- **Interface** : Optimisation des espacements et des paddings dans le bloc fonctionnalité.

### Évolutions techniques
- **Qualité et Typage** : Refonte majeure de la gestion des types (TypeScript) pour éliminer les `any` et corriger les erreurs `null/undefined`, ainsi qu'une optimisation de la configuration ESLint.
- **Tests et Storybook** : Optimisation du workflow de test des stories, exclusion des exemples des tests et amélioration de la conformité des stories aux standards DSFR.
- **CI/CD et Outillage** : Intégration de `svelte-check` pour la validation des types, mise en place de `lint-staged` et uniformisation des scripts de formatage (Prettier).
- **Sécurité** : Correction d'une violation de la politique de sécurité de contenu (CSP) dans la navigation du header.

### Autres changements
- Mise à jour de la documentation concernant le processus de release.
- Plusieurs montées de version publiées (passage de la version 1.60.10 à 1.61.3).
