## Changelog : hubee (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, l'équipe hubee a réalisé des travaux importants pour moderniser l'infrastructure et l'architecture du projet. L'introduction de Renovate pour la gestion des dépendances, l'adoption de GitHub Actions pour l'intégration continue et le refactoring de l'architecture vers un modèle modulaire sont les points forts de cette période. Ces améliorations visent à renforcer la sécurité, la maintenabilité et la scalabilité de la plateforme.

### Évolutions techniques
- **Architecture :** Refactoring majeur de l'architecture vers un modèle modulaire avec des namespaces dédiés pour l'API, le Portail et le cœur de Hubee. [#69](https://github.com/datagouv/hubee/pull/69)
- **CI/CD :** Mise en place de GitHub Actions pour l'intégration continue et ajout d'un hook pre-commit. [#70](https://github.com/datagouv/hubee/pull/70)
- **Gestion des dépendances :** Intégration de Renovate pour automatiser les mises à jour des dépendances. [#72](https://github.com/datagouv/hubee/pull/72)
- **Environnement de développement :** Gel de l'API V2, passage à PostgreSQL 18 et Ruby 4.0.5. [#65](https://github.com/datagouv/hubee/pull/65)
- **Mise à jour des gems :** Mise à jour des gems et suppression des contraintes de version. [#66](https://github.com/datagouv/hubee/pull/66)
- **Image Docker :** Mise à jour de l'image Docker Ruby. [#74](https://github.com/datagouv/hubee/pull/74)
- **Actions GitHub :** Mise à jour de l'action `actions/checkout` vers la version 7. [#76](https://github.com/datagouv/hubee/pull/76)

### Autres changements
- **Documentation :** Interdiction des références confidentielles dans le dépôt public. [#68](https://github.com/datagouv/hubee/pull/68)
- **Intelligence Artificielle :** Adoption de `hubee-claude-plugin` comme source de vérité pour les aspects liés à l'IA. [#67](https://github.com/datagouv/hubee/pull/67)
