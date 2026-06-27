## Changelog : mirai-api (30 derniers jours, au 26 juin 2026)

### Résumé
Cette mise à jour se concentre sur l'amélioration de la documentation de l'API MirAI, notamment en clarifiant les informations sur la passerelle, les niveaux d'accès (quotas) et la gestion des données sensibles (PII). Les modifications apportées visent à faciliter l'intégration et l'utilisation de l'API par les partenaires et les utilisateurs internes.

### Évolutions fonctionnelles
- Modification de la durée de rétention des données à 72 heures (au lieu de 24h).
- Clarification des niveaux d'accès (Découverte, Intégration, Production, Critique) et de leurs quotas respectifs [#f540a17](https://github.com/IA-Generative/mirai-api/commit/f540a17).

### Évolutions techniques
- Suppression des références à Kafka dans la documentation, indiquant potentiellement une simplification de l'architecture ou un changement d'infrastructure. [#4c18e02](https://github.com/IA-Generative/mirai-api/commit/4c18e02)
- Complétion de la liste des données personnellement identifiables (PII) dans la documentation, renforçant la conformité et la transparence en matière de protection des données. [#4c18e02](https://github.com/IA-Generative/mirai-api/commit/4c18e02)

### Autres changements
- Ajout d'une section dédiée à la passerelle dans la documentation, améliorant la compréhension de l'architecture de l'API. [#f540a17](https://github.com/IA-Generative/mirai-api/commit/f540a17)
