## Changelog : etape (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, le projet ETAPE a connu une avancée significative avec la mise en place d'une architecture monorepo, l'intégration de nouveaux outils de développement (ESLint, Prettier, Shadcn-UI) et le début du développement de l'application simulateur, ainsi que l'amélioration de la navigation et du design du site vitrine.

### Évolutions fonctionnelles
- Ajout d'un écran d'introduction pour le simulateur [#3](https://github.com/betagouv/etape/pulls/3).
- Implémentation d'une navigation complète avec un footer et des liens mis à jour [#8](https://github.com/betagouv/etape/pulls/8).
- Ajout de composants de navigation (site navigation) et intégration Figma [#2](https://github.com/betagouv/etape/pulls/2).
- Ajout des composants partagés `SkipLinks` et `Container` pour améliorer l'accessibilité et le respect du design system.

### Évolutions techniques
- Initialisation d'un monorepo avec Turborepo pour une meilleure gestion des projets et des dépendances [#1](https://github.com/betagouv/etape/pulls/1).
- Configuration centralisée de ESLint et Prettier pour garantir la qualité et la cohérence du code [#2](https://github.com/betagouv/etape/pulls/2).
- Intégration de la librairie de composants réutilisables Shadcn-UI [#1](https://github.com/betagouv/etape/pulls/1).
- Mise en place de déploiements de previews Vercel en mode prebuilt pour faciliter la revue de code et les tests [#9](https://github.com/betagouv/etape/pulls/9).
- Centralisation du découpage des chemins et renforcement de la sécurité de l'assemblage des routes.
- Branchement des liens d'évitement et de la cible de contenu pour améliorer l'accessibilité.

### Autres changements
- Ajout d'un template de pull request pour standardiser les contributions [#4](https://github.com/betagouv/etape/pulls/4).
- Mise à jour du titre du projet en "ETAPE" et correction de la terminologie dans le README (remplacement de "professionnel" par "salarié").
- Ajout de skills partagées (frontend-design, react-best-practices, web-design-guidelines).
- Mise à jour du fichier CSS global partagé avec de nouvelles familles de tokens.
- Mise à jour du fichier `.gitignore`.
