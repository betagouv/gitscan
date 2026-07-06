## Changelog : document-ia (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de nouvelles fonctionnalités pour le traitement des taxes foncières, notamment la gestion d'identités multiples et d'informations sur le destinataire. Une nouvelle version des workflows a également été implémentée, ainsi qu'une page de console pour l'exécution de ces workflows. Des corrections de sécurité et des améliorations de la documentation ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de spécifier le destinataire et son identité pour les documents de taxe foncière. [#75](https://github.com/betagouv/document-ia/issues/75)
- Ajout de la gestion d'identités multiples pour les documents de taxe foncière. [#74](https://github.com/betagouv/document-ia/issues/74)
- Nouvelle page dans la console pour exécuter la version 2 des workflows. [#71](https://github.com/betagouv/document-ia/issues/71)
- Implémentation des workflows V2. [#69](https://github.com/betagouv/document-ia/issues/69)
- Ajout d'un indicateur dans l'API pour afficher le nombre de messages en attente de traitement dans la queue. [#73](https://github.com/betagouv/document-ia/issues/73)
- Création d'une nouvelle version des données de vérité (ground truth) et d'autres pages associées. [#72](https://github.com/betagouv/document-ia/issues/72)

### Évolutions techniques
- Correction d'une vulnérabilité (CVE) dans la librairie Starlette. [#74](https://github.com/betagouv/document-ia/issues/74)
- Nettoyage des prompts utilisés par le système. [#68](https://github.com/betagouv/document-ia/issues/68)

### Autres changements
- Mise à jour de la documentation pour les contributeurs. [#78](https://github.com/betagouv/document-ia/issues/78)
- Mise à jour de la documentation pour les instructions de snapshot des tests. [#79](https://github.com/betagouv/document-ia/issues/79)
- Publication des versions 1.0.5 et 1.0.6.
