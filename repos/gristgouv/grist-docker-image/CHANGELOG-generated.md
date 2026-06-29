## Changelog : grist-docker-image (30 derniers jours, au 26 juin 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives en matière de sécurité grâce à l'intégration d'un scanner de vulnérabilités (Trivy) et une meilleure gestion de l'environnement de construction avec GVISOR. L'image Grist a également été mise à jour vers la version 1.7.15.

### Évolutions fonctionnelles
- Mise à jour de l'image Grist vers la version 1.7.15 [#66](https://github.com/gristgouv/grist-docker-image/pull/66).

### Évolutions techniques
- Intégration de Trivy pour l'analyse des vulnérabilités de l'image Docker [#67](https://github.com/gristgouv/grist-docker-image/pull/67).
  - Ajout d'un rapport JSON des vulnérabilités détectées dans les artefacts de la CI.
  - Déclenchement de l'analyse Trivy manuellement ou lors de la création d'une nouvelle image.
- Amélioration de l'intégration du workflow GVISOR pour une meilleure abstraction et une construction plus robuste [#69](https://github.com/gristgouv/grist-docker-image/pull/69).
- Ajout d'une construction avec une version plus récente de GVISOR [#78a357f](https://github.com/gristgouv/grist-docker-image/commit/78a357f).
- Refactorisation de l'intégration du workflow GVISOR [#4f666cb](https://github.com/gristgouv/grist-docker-image/commit/4f666cb).

### Autres changements
- Suppression d'une dépendance inutilisée [#e3bc3ee](https://github.com/gristgouv/grist-docker-image/commit/e3bc3ee).
- Amélioration des noms et titres des jobs CI [#3472f68](https://github.com/gristgouv/grist-docker-image/commit/3472f68) et [#5261fb1](https://github.com/gristgouv/grist-docker-image/commit/5261fb1).
- Suppression de la dernière image Docker en cache [#50f7e8e](https://github.com/gristgouv/grist-docker-image/commit/50f7e8e).
