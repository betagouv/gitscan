## Changelog : grist-docker-image (30 derniers jours, au 22 juin 2026)

### Résumé
Cette mise à jour apporte des améliorations de sécurité grâce à l'intégration d'un scanner de vulnérabilités (Trivy) et met à jour Grist vers la version 1.7.15.  Une nouvelle option de build utilisant une version plus récente de gvisor a également été ajoutée.

### Évolutions fonctionnelles
- Mise à jour de Grist vers la version 1.7.15 [#66](https://github.com/gristgouv/grist-docker-image/pull/66).

### Évolutions techniques
- Intégration de Trivy pour l'analyse des vulnérabilités de l'image Docker.
    - Ajout d'un job Trivy pour scanner les vulnérabilités [#67](https://github.com/gristgouv/grist-docker-image/pull/67).
    - Génération d'un rapport JSON des vulnérabilités détectées.
    - Déclenchement de l'analyse Trivy manuellement ou lors de la création d'une nouvelle image.
- Ajout d'une nouvelle build utilisant une version plus récente de gvisor [#68](https://github.com/gristgouv/grist-docker-image/pull/68).
- Amélioration de la configuration du workflow CI/CD pour une meilleure gestion des builds et des analyses de sécurité.

### Autres changements
- Nettoyage de la configuration du workflow (suppression d'une dépendance inutilisée).
- Amélioration des noms et titres des jobs CI/CD pour une meilleure lisibilité.
