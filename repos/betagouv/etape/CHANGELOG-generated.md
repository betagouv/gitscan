## Changelog : etape (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, le projet ETAPE a connu une avancée significative avec la mise en place d'une infrastructure moderne basée sur Turborepo et l'intégration de Shadcn UI.  Un premier jet du simulateur de transition professionnelle a été implémenté, ainsi que des améliorations de l'accessibilité et de la qualité du code.

### Évolutions fonctionnelles
- **Simulateur de transition professionnelle :** Ajout d'une première version du simulateur, incluant l'écran d'introduction aligné sur le design system. [#3](https://github.com/betagouv/etape/pull/3)
- **Accessibilité :** Implémentation des liens d'évitement (SkipLinks) et branchement des cibles de contenu pour améliorer l'accessibilité de l'application.
- **Skills partagées :** Ajout de skills partagées pour le développement frontend (design, React). [#4](https://github.com/betagouv/etape/pull/4)

### Évolutions techniques
- **Infrastructure :** Initialisation d'un monorepo avec Turborepo pour une meilleure gestion des projets et des dépendances.
- **Shadcn UI :** Intégration de la librairie de composants Shadcn UI pour accélérer le développement et assurer une cohérence visuelle. [#1](https://github.com/betagouv/etape/pull/1)
- **Qualité du code :** Configuration centralisée d'ESLint et Prettier pour garantir un style de code uniforme et détecter les erreurs potentielles. [#2](https://github.com/betagouv/etape/pull/2)
- **Design System :** Ajout des composants partagés `SkipLinks` et `Container` au design system.
- **CSS Global :** Mise à jour des tokens CSS globaux.

### Autres changements
- Ajout d'un template de pull request pour faciliter les contributions. [#29d0585](https://github.com/betagouv/etape/commit/29d0585)
- Modification du titre du projet en "ETAPE".
- Mise à jour de la description dans le README pour utiliser le terme "salarié" au lieu de "professionnel".
- Initialisation du dépôt.
