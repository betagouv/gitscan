## Changelog : menshen (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la simplification du code, l'amélioration des performances et l'ajout de tests pour les modèles d'échange de jetons. La fonctionnalité d'échange de jetons est désormais activée par défaut et le projet bénéficie d'une meilleure gestion des variables d'environnement pour le développement et l'intégration continue.

### Évolutions fonctionnelles
- Les tests pour les modèles d'échange de jetons ont été ajoutés, améliorant la robustesse du système. [#ca2fb77](https://github.com/suitenumerique/menshen/commit/ca2fb77)

### Évolutions techniques
- La fonctionnalité d'échange de jetons est maintenant activée par défaut, simplifiant la configuration. [#64f8163](https://github.com/suitenumerique/menshen/commit/64f8163)
- Les sérialiseurs ont été migrés vers des structures `msgspec`, améliorant potentiellement les performances. [#dac2ee9](https://github.com/suitenumerique/menshen/commit/dac2ee9)
- Suppression d'arguments inutilisés de la méthode `generate_jwt` de `TokenGenerator`, allégeant le code. [#851d5b5](https://github.com/suitenumerique/menshen/commit/851d5b5)
- Ajout de la gestion des types (type hints) pour une meilleure lisibilité et maintenance du code. [#a4a120f](https://github.com/suitenumerique/menshen/commit/a4a120f)
- Automatisation de la génération des variables d'environnement pour les environnements de développement et d'intégration continue. [#449a218](https://github.com/suitenumerique/menshen/commit/449a218)
