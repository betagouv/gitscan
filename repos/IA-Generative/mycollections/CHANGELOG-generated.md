## Changelog : mycollections (30 derniers jours, au 25 octobre 2026)

### Résumé
Ce mois a été marqué par une évolution majeure du projet avec l'introduction des "Assistants de recherche", permettant de transformer des collections de documents en agents conversationnels spécialisés. Parallèlement, l'interface utilisateur a bénéficié d'une refonte complète pour offrir une navigation plus fluide, une meilleure visibilité sur la qualité des données et une gestion simplifiée des flux Resana.

### Évolutions fonctionnelles
- **Assistants de recherche** : Création d'un parcours guidé pour concevoir des assistants, incluant un "bac à sable" pour tester les réponses, la définition de consignes spécifiques et la gestion de la publication ([#83](https://github.com/IA-Generative/mycollections/pull/83), [#91](https://github.com/IA-Generative/mycollections/pull/91)).
- **Gestion documentaire et indexation** : 
    - Conversion automatique des formats bureautiques en PDF via un service dédié ([#161](https://github.com/IA-Generative/mycollections/pull/161)).
    - Amélioration de la fidélité de lecture (Markdown) et détection des scans pour une meilleure précision de l'IA ([#162](https://github.com/IA-Generative/mycollections/pull/162), [#160](https://github.com/IA-Generative/mycollections/pull/160)).
    - Introduction de métriques de qualité par document pour identifier les contenus incomplets ([#159](https://github.com/IA-Generative/mycollections/pull/159)).
- **Intégration Resana** : Amélioration du partage de collections par groupe, gestion de la sensibilité des documents et optimisation du parcours d'importation ([#140](https://github.com/IA-Generative/mycollections/pull/140), [#136](https://github.com/IA-Generative/mycollections/pull/136)).
- **Interface Utilisateur (UI/UX)** : 
    - Refonte de l'accueil (version compacte) et du catalogue de collections avec affichage des avis utilisateurs ([#88](https://github.com/IA-Generative/mycollections/pull/88), [#81](https://github.com/IA-Generative/mycollections/pull/81)).
    - Création de fiches détaillées pour les collections et assistants (historique, consignes, qualité) ([#82](https://github.com/IA-Generative/mycollections/pull/82)).
    - Renommage de l'assistant en "Chat MirAI" pour une meilleure identité ([#141](https://github.com/IA-Generative/mycollections/pull/141)).
- **Réseau d'entraide** : Mise en place d'un système d'appels et de réponses entre utilisateurs pour partager des connaissances ([#4cdb8cf](https://github.com/IA-Generative/mycollections/commits/4cdb8cf)).

### Évolutions techniques
- **Architecture et Protocoles** : 
    - Implémentation d'un serveur MCP (Model Context Protocol) pour étendre les capacités des assistants ([#107](https://github.com/IA-Generative/mycollections/pull/107)).
    - Refactorisation du moteur d'indexation pour utiliser une interface générique, facilitant l'intégration de nouveaux moteurs ([#125](https://github.com/IA-Generative/mycollections/pull/125)).
- **Sécurité et Authentification** : 
    - Optimisation de la gestion des sessions pour éviter les déconnexions intempestives lors du renouvellement des jetons ([#131](https://github.com/IA-Generative/mycollections/pull/131), [#127](https://github.com/IA-Generative/mycollections/pull/127)).
    - Correction de vulnérabilités critiques sur les dépendances `certifi` et `pillow` ([#114](https://github.com/IA-Generative/mycollections/pull/114)).
- **Performance et Fiabilité** : 
    - Optimisation du débit d'indexation et gestion intelligente des reprises après interruption ([#137](https://github.com/IA-Generative/mycollections/pull/137), [#4f70f77](https://github.com/IA-Generative/mycollections/commits/4f70f77)).
    - Amélioration de la gestion des doublons lors des imports ([#133](https://github.com/IA-Generative/mycollections/pull/133)).
- **DevOps et Qualité** : 
    - Mise en place de la CI/CD avec ArgoCD et Helm ([#62](https://github.com/IA-Generative/mycollections/pull/62)).
    - Renforcement de la couverture de tests (E2E et unitaires) sur l'ensemble du parcours utilisateur ([#47](https://github.com/IA-Generative/mycollections/pull/47), [#48](https://github.com/IA-Generative/mycollections/pull/48)).

### Autres changements
- **Documentation** : Mise à jour des documents de référence (ADR) et de la documentation technique des composants ([#69](https://github.com/IA-Generative/mycollections/pull/69)).
- **Refactorisation** : Migration vers des modèles de données Pydantic pour une meilleure validation des entrées/sorties API ([#297f4bb](https://github.com/IA-Generative/mycollections/commits/297f4bb)).
