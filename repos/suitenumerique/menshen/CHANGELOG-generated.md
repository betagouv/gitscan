## Changelog : menshen (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la simplification du code, l'ajout de tests et la préparation du projet pour une utilisation plus large. La fonctionnalité d'échange de jetons est désormais activée par défaut et le code a été modernisé avec l'utilisation de `msgspec` pour les sérialiseurs et l'ajout de support de typage.

### Évolutions fonctionnelles
- La fonctionnalité d'échange de jetons est maintenant activée par défaut, simplifiant ainsi son utilisation. [#64f8163](https://github.com/suitenumerique/menshen/commit/64f8163)
- Ajout de tests pour les modèles d'échange de jetons, améliorant la robustesse du système. [#ca2fb77](https://github.com/suitenumerique/menshen/commit/ca2fb77)

### Évolutions techniques
- Refactorisation des sérialiseurs pour utiliser les structures `msgspec`, améliorant potentiellement les performances et la lisibilité. [#dac2ee9](https://github.com/suitenumerique/menshen/commit/dac2ee9)
- Suppression d'arguments inutilisés de la méthode `generate_jwt` de `TokenGenerator`, simplifiant le code. [#851d5b5](https://github.com/suitenumerique/menshen/commit/851d5b5)
- Ajout du support de typage pour une meilleure maintenabilité et détection d'erreurs. [#a4a120f](https://github.com/suitenumerique/menshen/commit/a4a120f)
- Automatisation de la génération des variables d'environnement pour les environnements de développement et CI. [#449a218](https://github.com/suitenumerique/menshen/commit/449a218)
