## Changelog : hubee (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la modernisation de l'infrastructure et de l'architecture du projet. Cela inclut l'adoption de nouvelles pratiques de CI/CD avec GitHub Actions, la refactorisation du code pour une meilleure modularité et la mise à jour des dépendances pour bénéficier des dernières améliorations de sécurité et de performance. Des mesures de sécurité supplémentaires ont également été mises en place concernant la documentation.

### Évolutions techniques
- **Architecture :** Refactorisation majeure de l'architecture en namespaces `::API`, `::Portail`, et `::Hubee` pour une meilleure organisation et modularité du code [#69](https://github.com/datagouv/hubee/pull/69).
- **CI/CD :** Intégration de GitHub Actions pour la CI et ajout d'un hook pre-commit pour améliorer la qualité du code [#70](https://github.com/datagouv/hubee/pull/70).
- **Dépendances :** Mise à jour des gems et suppression des contraintes de version pour faciliter les mises à jour futures [#66](https://github.com/datagouv/hubee/pull/66).
- **Environnement :** Gel de l'API V2, passage à PostgreSQL 18 et Ruby 4.0.5 pour bénéficier des dernières versions stables [#65](https://github.com/datagouv/hubee/pull/65).
- **Automatisation :** Mise en place de Renovate pour la gestion automatisée des dépendances [#72](https://github.com/datagouv/hubee/pull/72).
- **Docker:** Mise à jour de l'image Docker Ruby [#74](https://github.com/datagouv/hubee/pull/74).
- **Actions:** Mise à jour de l'action GitHub Checkout vers la version 7 [#76](https://github.com/datagouv/hubee/pull/76).

### Autres changements
- **Documentation :** Interdiction des références confidentielles dans le dépôt public pour renforcer la sécurité des informations sensibles [#68](https://github.com/datagouv/hubee/pull/68).
- **IA :** Adoption du plugin `hubee-claude-plugin` comme source de vérité pour les aspects liés à l'intelligence artificielle [#67](https://github.com/datagouv/hubee/pull/67).
