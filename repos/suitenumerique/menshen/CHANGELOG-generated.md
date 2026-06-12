## Changelog : menshen (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la simplification de la configuration et l'optimisation du code backend de Menshen. La fonctionnalité d'échange de jetons est désormais activée par défaut, et des efforts ont été faits pour moderniser le code en utilisant des structures de données plus performantes et en supprimant du code obsolète.

### Évolutions fonctionnelles
- La fonctionnalité d'échange de jetons est maintenant activée par défaut, simplifiant ainsi son utilisation. [#64f8163](https://github.com/suitenumerique/menshen/commit/64f8163)

### Évolutions techniques
- Les sérialiseurs ont été migrés vers des structures `msgspec` pour améliorer les performances. [#dac2ee9](https://github.com/suitenumerique/menshen/commit/dac2ee9)
- Suppression des arguments inutilisés de la méthode `TokenGenerator.generate_jwt`, allégeant le code et améliorant sa lisibilité. [#851d5b5](https://github.com/suitenumerique/menshen/commit/851d5b5)
- Ajout du support des types pour une meilleure maintenance et détection d'erreurs. [#a4a120f](https://github.com/suitenumerique/menshen/commit/a4a120f)
- Automatisation de la génération des variables d'environnement pour les environnements de développement et CI, facilitant la configuration et la reproductibilité. [#449a218](https://github.com/suitenumerique/menshen/commit/449a218)
