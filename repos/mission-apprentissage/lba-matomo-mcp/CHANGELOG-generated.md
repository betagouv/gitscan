## Changelog : lba-matomo-mcp (30 derniers jours, au 17 novembre 2026)

### Résumé
Lancement des fonctionnalités principales du projet. Le serveur est désormais capable de piloter le gestionnaire de balises Matomo et de fournir des analyses de données détaillées, permettant ainsi une interaction directe avec les outils de suivi de La Bonne Alternance.

### Évolutions fonctionnelles
- **Pilotage du Tag Manager** : Capacité de piloter le conteneur Matomo Tag Manager dédié à LBA.
- **Reporting et statistiques** : 
    - Extraction de statistiques agrégées via l'API de reporting Matomo.
    - Accès à des indicateurs analytiques avancés : entonnoirs de conversion, cartes de chaleur (heatmaps), suivi des formulaires et annotations.

### Évolutions techniques
- **Architecture MCP** : Implémentation de la structure serveur basée sur le protocole MCP (Model Context Protocol) pour permettre l'intégration avec des modèles de langage.
