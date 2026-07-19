## Changelog : datagouv-mcp (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations de stabilité et de performance, notamment en remplaçant la librairie HTTPX par niquests. Des corrections ont été apportées au suivi des statistiques Matomo et à la configuration de l'outil Autohand Code MCP. La documentation a également été enrichie.

### Évolutions fonctionnelles
- Ajout de la configuration pour Autohand Code MCP. [#124](https://github.com/datagouv/datagouv-mcp/pull/124)
- Correction du suivi des statistiques Matomo pour le healthcheck. [#122](https://github.com/datagouv/datagouv-mcp/pull/122)
- Correction d'un lien dans le template de création d'issues GitHub.
- Suppression des requêtes Matomo inutiles sur `/mcp`, ne conservant que les événements des outils. [#120](https://github.com/datagouv/datagouv-mcp/pull/120)

### Évolutions techniques
- Remplacement de la librairie HTTPX par niquests pour améliorer les performances et la stabilité. [#119](https://github.com/datagouv/datagouv-mcp/pull/119)
- Amélioration de la gestion des probes de santé pour éviter les fuites de descripteurs de fichiers. [#121](https://github.com/datagouv/datagouv-mcp/pull/121)
- Mise à jour des dépendances.

### Autres changements
- Publication des versions 0.2.30, 0.2.29, 0.2.28, 0.2.27.
