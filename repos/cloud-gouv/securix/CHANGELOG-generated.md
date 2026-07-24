## Changelog : securix (30 derniers jours, au 23 juillet 2026)

### Résumé
Ce mois-ci, les évolutions de SécurixOS se concentrent sur l'ajout de support pour de nouveaux matériels (p14sg6, x390), l'intégration du Portail, et l'amélioration de la gestion des configurations réseau. Des corrections et des améliorations de la documentation ont également été apportées.

### Évolutions fonctionnelles
- Ajout du support pour les jetons de sécurité p14sg6 [#219](https://github.com/cloud-gouv/securix/pull/219).
- Intégration du Portail, permettant une gestion centralisée des configurations et des mises à jour [#181](https://github.com/cloud-gouv/securix/pull/181).
- Ajout d'un support préliminaire pour le matériel x390 [#190](https://github.com/cloud-gouv/securix/pull/190).
- Mise en place de modèles de traductions en français pour l'interface utilisateur [#182](https://github.com/cloud-gouv/securix/pull/182).

### Évolutions techniques
- Refactorisation de l'API de réaction de NetworkManager pour une plus grande généralisation [#198](https://github.com/cloud-gouv/securix/pull/198).
- Suppression de l'IFD (Interface de Définition d'Interface) pour les clés hôtes SSH, améliorant la sécurité [#220](https://github.com/cloud-gouv/securix/pull/220).
- Correction d'un problème de dépendance dynamique dans le module "portail" [#215](https://github.com/cloud-gouv/securix/pull/215).
- Correction de la configuration des chemins `infraRepositoryPath` et `infraRepositorySubdir` [#183](https://github.com/cloud-gouv/securix/pull/183).
- Amélioration des tests de présence de la clé `ruleId` [#178](https://github.com/cloud-gouv/securix/pull/178).
- Correction de l'auto-pull pour éviter les redémarrages inutiles en cas de code de sortie 103 [#177](https://github.com/cloud-gouv/securix/pull/177).
- Suppression de l'utilisation de `sudo` avec un utilisateur vide [#176](https://github.com/cloud-gouv/securix/pull/176).

### Autres changements
- Ajout d'informations de licence SPDX au fichier CODEOWNERS [#222](https://github.com/cloud-gouv/securix/pull/222).
- Renommage du projet en "SécurixOS" dans le fichier README [#213](https://github.com/cloud-gouv/securix/pull/213).
- Initialisation du fichier CODEOWNERS [#216](https://github.com/cloud-gouv/securix/pull/216).
- Reformatage du code source [#211](https://github.com/cloud-gouv/securix/pull/211).
- Ajout d'un modèle de demande de fonctionnalité (feature request) dans les templates d'issues [#203](https://github.com/cloud-gouv/securix/pull/203).
- Correction de l'importation de la localisation i18n [#199](https://github.com/cloud-gouv/securix/pull/199).
