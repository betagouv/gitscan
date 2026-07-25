# Synthèse d'activité : cloud-gouv (du 23/06 au 23/07)

## Résumé de l'activité
L'organisation cloud-gouv a connu une période d'activité soutenue, avec des améliorations significatives apportées à plusieurs projets clés. SécurixOS a progressé avec l'ajout de support matériel et l'intégration d'un portail de gestion. OpenBao a bénéficié de corrections de sécurité et d'améliorations de la CLI. Les charts Helm pour Cluster API ont été mis à jour pour assurer la compatibilité avec les dernières versions de l'opérateur, et les charts communs ont vu l'ajout de nouvelles fonctionnalités et de corrections. L'initialisation du dépôt [playground-public](/repos/cloud-gouv/playground-public) marque le début d'un espace d'expérimentation prometteur.

## Sécurité
Plusieurs dépôts ont reçu des mises à jour de sécurité :
- [openbao](/repos/cloud-gouv/openbao) a été mis à jour vers Go 1.25.7 et des crates Rust ont été mises à jour pour corriger des vulnérabilités.
- [securix](/repos/cloud-gouv/securix) a supprimé l'utilisation de `sudo` avec un utilisateur vide et l'IFD pour les clés hôtes SSH, améliorant ainsi la sécurité.

## Autres changements notables
- Intégration du Portail dans [securix](/repos/cloud-gouv/securix) pour une gestion centralisée des configurations.
- Refactorisation de l'API de réaction de NetworkManager dans [securix](/repos/cloud-gouv/securix).
- Ajout de tests de complexité cyclomatique dans [openbao](/repos/cloud-gouv/openbao).
- Mise à jour de `clusterctl` dans [dockerfiles](/repos/cloud-gouv/dockerfiles) vers la version 1.13.1.

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Ajout de support matériel, intégration du Portail et améliorations de la gestion des configurations réseau.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs, mises à jour de sécurité et améliorations de la CLI.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Ajout de nouvelles fonctionnalités aux charts Helm, notamment pour Matrix, Coturn et pgbench.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Mises à jour pour la compatibilité avec les dernières versions de l'opérateur Cluster API.
