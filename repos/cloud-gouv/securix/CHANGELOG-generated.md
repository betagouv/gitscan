## Changelog : securix (30 derniers jours, au 16 juillet 2026)

### Résumé
Les dernières mises à jour de Securix se concentrent sur l'intégration du Portail, l'amélioration de la gestion des réseaux et la préparation du support pour de nouvelles architectures matérielles. Des corrections et des ajustements ont également été apportés pour améliorer la stabilité et la configuration du système.

### Évolutions fonctionnelles
- Intégration du Portail pour une gestion centralisée des configurations et des mises à jour. [#181](https://github.com/cloud-gouv/securix/issues/181)
- Ajout d'une prise en charge préliminaire de l'architecture x390. [#190](https://github.com/cloud-gouv/securix/issues/190)
- Initialisation de la localisation en français pour l'interface utilisateur. [#182](https://github.com/cloud-gouv/securix/issues/182)

### Évolutions techniques
- Généralisation de l'API de réaction de NetworkManager pour une meilleure flexibilité et maintenabilité. [#198](https://github.com/cloud-gouv/securix/issues/198)
- Correction d'un problème de dépendance dynamique dans le portail. [#215](https://github.com/cloud-gouv/securix/issues/215)
- Correction de l'emplacement des répertoires d'infrastructure. [#183](https://github.com/cloud-gouv/securix/issues/183)
- Amélioration de la gestion des erreurs et des redémarrages automatiques dans certains scripts. [#177](https://github.com/cloud-gouv/securix/issues/177)
- Suppression de l'utilisation de `sudo` avec un utilisateur vide. [#176](https://github.com/cloud-gouv/securix/issues/176)
- Correction de tests liés à la présence de la clé `ruleId`. [#178](https://github.com/cloud-gouv/securix/issues/178)
- Correction de l'importation de la localisation i18n. [#199](https://github.com/cloud-gouv/securix/issues/199)

### Autres changements
- Initialisation du fichier `CODEOWNERS` pour une meilleure gestion des contributions. [#216](https://github.com/cloud-gouv/securix/issues/216)
- Ajout d'un modèle de demande de fonctionnalité (feature request) dans les issues. [#203](https://github.com/cloud-gouv/securix/issues/203)
- Reformatage du code source pour une meilleure lisibilité. [#211](https://github.com/cloud-gouv/securix/issues/211)
- Rétractation de l'intégration initiale de Qemu/KVM. [#193](https://github.com/cloud-gouv/securix/issues/193)
