## Changelog : dsfr-mcp (30 derniers jours, au 15 juin 2026)

### Résumé
Cette version apporte une nouvelle fonctionnalité permettant d'extraire des informations structurées sur l'accessibilité RGAA des composants du DSFR, facilitant ainsi la création d'assistants IA capables de générer des composants plus inclusifs. Une correction a également été apportée pour améliorer la publication du package npm.

### Évolutions fonctionnelles
- Ajout d'un outil `get_component_accessibility` pour extraire des informations structurées sur l'accessibilité RGAA des composants DSFR. [#1](https://github.com/SocialGouv/dsfr-mcp/pull/1)
- Intégration de l'extraction structurée RGAA pour une meilleure accessibilité des composants générés par les assistants IA. [#1](https://github.com/SocialGouv/dsfr-mcp/pull/1)

### Évolutions techniques
- Ajout du champ `repository` pour la provenance npm, améliorant la sécurité et la traçabilité des publications. [f8e98d9](https://github.com/SocialGouv/dsfr-mcp/commit/f8e98d9)
