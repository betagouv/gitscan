## Changelog : portail (30 derniers jours, au 17 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilisation et l'ajout de tests pour le proxy upstream Tinyproxy, ainsi que sur la correction de bugs liés à la configuration TLS et à la gestion des erreurs. Une initialisation de la version 1 des règles d'accès (ACL) a également été effectuée.

### Évolutions fonctionnelles
- Ajout d'un test E2E pour le proxy upstream Tinyproxy, permettant de valider son fonctionnement. [#70](https://github.com/cloud-gouv/portail/issues/70)

### Évolutions techniques
- Correction d'une erreur où le nom du serveur TLS n'était pas correctement configuré. [#75](https://github.com/cloud-gouv/portail/issues/75)
- Suppression d'un `unwrap` potentiellement problématique, améliorant la robustesse du code. [#76](https://github.com/cloud-gouv/portail/issues/76)
- Ajout de commandes CI Cargo pour faciliter l'intégration continue. [#68](https://github.com/cloud-gouv/portail/issues/68)
- Initialisation de la version 1 des règles d'accès (ACL).

### Autres changements
- Mise à jour de la dépendance `zlink` vers la version 0.4.1. (mise à jour automatique)
