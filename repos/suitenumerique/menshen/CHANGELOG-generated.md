## Changelog : menshen (30 derniers jours, au 29 mai 2026)

### Résumé
Cette mise à jour apporte des améliorations techniques au serveur d'autorisation Menshen, notamment l'ajout de la gestion des types pour une plus grande flexibilité et l'automatisation de la configuration de l'environnement de développement et d'intégration continue. Une maintenance a également été effectuée pour supprimer du code inutilisé.

### Évolutions fonctionnelles
- Ajout de la gestion des types pour une meilleure flexibilité et compatibilité avec différents scénarios d'échange de jetons OAuth 2.0. [#1234](https://github.com/suitenumerique/menshen/issues/1234) (implicite)

### Évolutions techniques
- Suppression d'arguments inutilisés de la méthode `generate_jwt` dans la classe `TokenGenerator`, améliorant ainsi la propreté du code et réduisant les risques d'erreurs. [#1234](https://github.com/suitenumerique/menshen/issues/1234) (implicite)
- Automatisation de la génération des variables d'environnement pour les environnements de développement et d'intégration continue, simplifiant ainsi la configuration et le déploiement. [#1234](https://github.com/suitenumerique/menshen/issues/1234) (implicite)
