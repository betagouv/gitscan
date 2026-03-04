## Changelog : kontinuous (30 derniers jours)

### Résumé
Les dernières mises à jour de Kontinuous se concentrent sur la correction de bugs et l'amélioration de la gestion des configurations, notamment pour les environnements alpha, bêta et de production. Des corrections spécifiques ont été apportées aux templates de politiques réseau (netpol) pour PostgreSQL et à la gestion des images dans les branches alpha et bêta.

### Évolutions fonctionnelles
- Correction d'un bug d'indentation dans le template de politique réseau (netpol) pour PostgreSQL, améliorant ainsi la lisibilité et la validité de la configuration. [#ad0422d](https://github.com/socialgouv/kontinuous/commit/ad0422d9119cf6bbc54deeaf2981d604ef1d461e)
- Correction du tag d'image pour les branches alpha et bêta, assurant le déploiement des bonnes versions. [#7d495c1](https://github.com/socialgouv/kontinuous/commit/7d495c1f3b99bd9126a74f733b43231191189bd9)

### Évolutions techniques
- Correction d'un bug concernant les politiques réseau (netpol) pour CNPG. [#867d5d3](https://github.com/socialgouv/kontinuous/commit/867d5d3399c3e881236ada3e4ae64098d5f0b738)
- Ajout de la gestion des environnements alpha, bêta et next pour la persistance des données. [#247e205](https://github.com/socialgouv/kontinuous/commit/247e205f3588d263286f8cc5e25f9e86736df3b7)

### Autres changements
- Mise à jour des snapshots. [#15dfde86](https://github.com/socialgouv/kontinuous/commit/15dfde86)
- Publication des versions 1.185.3, 1.185.4, 1.185.5 et 1.185.6.
