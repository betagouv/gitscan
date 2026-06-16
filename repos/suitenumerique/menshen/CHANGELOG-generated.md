## Changelog : menshen (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance et la simplification du code de Menshen. La suppression d'un indicateur de fonctionnalité (feature flag) et l'utilisation de structures de données plus efficaces (msgspec) contribuent à une meilleure efficacité. Des tests unitaires ont été ajoutés pour renforcer la fiabilité des modèles d'échange de jetons.

### Évolutions fonctionnelles
- Ajout de tests unitaires pour les modèles d'échange de jetons, améliorant ainsi la robustesse du système. [#ca2fb77](https://github.com/suitenumerique/menshen/commit/ca2fb77)

### Évolutions techniques
- Migration des sérialiseurs vers des structures `msgspec`, optimisant la performance de la sérialisation et désérialisation des données. [#dac2ee9](https://github.com/suitenumerique/menshen/commit/dac2ee9)
- Suppression de l'indicateur de fonctionnalité `TOKEN_EXCHANGE_ENABLED`, simplifiant la configuration et le code. [#64f8163](https://github.com/suitenumerique/menshen/commit/64f8163)
- Suppression d'arguments inutilisés de la méthode `generate_jwt` dans `TokenGenerator`, améliorant la lisibilité et la maintenance du code. [#851d5b5](https://github.com/suitenumerique/menshen/commit/851d5b5)
- Ajout de la prise en charge des types (type hints) pour améliorer la lisibilité et la maintenabilité du code. [#a4a120f](https://github.com/suitenumerique/menshen/commit/a4a120f)
- Automatisation de la génération des variables d'environnement pour les environnements de développement et CI. [#449a218](https://github.com/suitenumerique/menshen/commit/449a218)
