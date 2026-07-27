## Changelog : securix (30 derniers jours, au 24 juillet 2026)

### Résumé
Les dernières mises à jour de SécurixOS améliorent la sécurité et la flexibilité du système. L'intégration du Portail offre une nouvelle interface d'administration, tandis que l'ajout du support pour les puces de sécurité P14SG6 renforce les options d'authentification. Des corrections et améliorations diverses ont également été apportées pour une meilleure stabilité et une expérience utilisateur optimisée.

### Évolutions fonctionnelles
- **Intégration du Portail :** Ajout de l'intégration du Portail pour une gestion centralisée et simplifiée du système. [#181](https://github.com/cloud-gouv/securix/issues/181)
- **Support P14SG6 :** Ajout du support pour les puces de sécurité P14SG6, offrant une option d'authentification matérielle supplémentaire. [#219](https://github.com/cloud-gouv/securix/issues/219)
- **Support préliminaire x390 :** Ajout d'un support préliminaire pour les systèmes x390. [#190](https://github.com/cloud-gouv/securix/issues/190)
- **Amélioration de la gestion des proxies :** Généralisation de l'API de réaction de NetworkManager pour une gestion plus flexible des proxies. [#198](https://github.com/cloud-gouv/securix/issues/198)

### Évolutions techniques
- **Suppression de l'IFD pour les clés SSH :** Suppression de l'IFD (Interface de Définition d'Interface) pour les clés SSH, simplifiant ainsi la configuration. [#220](https://github.com/cloud-gouv/securix/issues/220)
- **Correction de la dépendance dynamic-updates :** Correction d'un problème de dépendance avec `dynamic-updates` dans le module Portail. [#215](https://github.com/cloud-gouv/securix/issues/215)
- **Refactoring général :** Reformattage du code pour une meilleure lisibilité et maintenabilité. [#211](https://github.com/cloud-gouv/securix/issues/211)

### Autres changements
- **Mise à jour des CODEOWNERS :** Mise à jour du fichier `CODEOWNERS` pour inclure de nouveaux responsables de code. [#224](https://github.com/cloud-gouv/securix/issues/224)
- **Ajout d'informations de licence SPDX :** Ajout d'informations de licence SPDX au fichier `CODEOWNERS`. [#222](https://github.com/cloud-gouv/securix/issues/222)
- **Renommage du projet :** Renommage du projet en "SécurixOS" dans le fichier `README`. [#213](https://github.com/cloud-gouv/securix/issues/213)
- **Ajout d'un modèle de demande de fonctionnalité :** Ajout d'un modèle de demande de fonctionnalité (ISSUE TEMPLATE) pour faciliter la soumission de nouvelles idées. [#203](https://github.com/cloud-gouv/securix/issues/203)
- **Corrections de configuration :** Corrections des chemins `infraRepositoryPath` et `infraRepositorySubdir`. [#183](https://github.com/cloud-gouv/securix/issues/183)
- **Améliorations des tests :** Corrections et améliorations des tests unitaires et d'intégration. [#178](https://github.com/cloud-gouv/securix/issues/178), [#177](https://github.com/cloud-gouv/securix/issues/177), [#176](https://github.com/cloud-gouv/securix/issues/176)
