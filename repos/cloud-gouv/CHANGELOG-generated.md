# Synthèse d'activité : cloud-gouv (du 01/04 au 14/10/2026)

## Résumé de l'activité
L'activité de l'organisation est marquée par une montée en maturité de ses outils de gestion et une expansion de son catalogue de déploiement. Les améliorations apportées à [portail](/repos/cloud-gouv/portail) et [securix](/repos/cloud-gouv/securix) renforcent l'expérience utilisateur et la visibilité sur le système, tandis que l'initialisation de nouveaux projets comme [openproject](/repos/cloud-gouv/openproject) et [k8s-glpi](/repos/cloud-gouv/k8s-glpi) étend les capacités de déploiement Kubernetes de l'organisation.

Ces évolutions permettent aux utilisateurs finaux de bénéficier de systèmes plus robustes, d'une meilleure observabilité des erreurs de connexion et d'une plus grande facilité de déploiement des services essentiels.

## Sécurité
- Mise à jour de sécurité critiques via Go et la bibliothèque OpenTelemetry dans [openbao](/repos/cloud-gouv/openbao).
- Résolution de problèmes liés au déverrouillage automatique (KMS), à l'invalidation du cache PKI et à la gestion des groupes d'identité dans [openbao](/repos/cloud-gouv/openbao).

## Autres changements notables
- **Infrastructure et Déploiement** : Mise à jour de la compatibilité avec Cluster API et OpenStack dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) et enrichissement du catalogue de composants (itsm-ng, envoy) dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts).
- **Robustesse Système** : Optimisation de la fiabilité des mises à jour automatiques et de la gestion CPU dans [securix](/repos/cloud-gouv/securix), ainsi que des migrations techniques importantes dans [nixpkgs](/repos/cloud-gouv/nixpkgs).
- **Observabilité et Documentation** : Structuration d'une documentation complète et ajout du support de la langue française pour [portail](/repos/cloud-gouv/portail), accompagnés de nouveaux outils de suivi des événements système.

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Améliorations de l'interface utilisateur, de la fiabilité des mises à jour et des outils de sécurité.
- [portail](/repos/cloud-gouv/portail) : Travaux majeurs sur la documentation, l'internationalisation et l'observabilité.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de sécurité critiques et amélioration de la robustesse globale.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Extension du catalogue de déploiement et optimisation du monitoring.
