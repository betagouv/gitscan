# Synthèse d'activité : cloud-gouv (du 21/08 au 28/08/2026)

## Résumé de l'activité
L'activité de cette période est marquée par un renforcement de la fiabilité opérationnelle et une extension des capacités de gestion et de sécurité. L'intégration de [securix](/repos/cloud-gouv/securix) au [portail](/repos/cloud-gouv/portail) permet désormais une gestion centralisée du système, tandis que l'introduction du support pour les puces de sécurité matérielles améliore l'expérience d'authentification des utilisateurs.

Parallèlement, l'organisation consolide ses bases d'infrastructure avec l'initialisation de nouveaux projets comme [openproject](/repos/cloud-gouv/openproject) pour le déploiement Kubernetes et [playground-public](/repos/cloud-gouv/playground-public) pour l'expérimentation. Les efforts sur [portail](/repos/cloud-gouv/portail) et [common-helm-charts](/repos/cloud-gouv/common-helm-charts) visent à offrir une meilleure observabilité et une gestion plus fine des accès et des ressources pour les utilisateurs finaux.

## Sécurité
- Mise à jour de sécurité critique pour Go et OpenTelemetry dans [openbao](/repos/cloud-gouv/openbao).
- Durcissement de l'évaluateur d'ACL et de la gestion des connexions (timeouts, limites de connexions simultanées) dans [portail](/repos/cloud-gouv/portail).
- Correction de la gestion de la liste noire des ressources au niveau des projets dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts).
- Support de l'authentification matérielle via les puces de sécurité P14SG6 dans [securix](/repos/cloud-gouv/securix).

## Autres changements notables
- Refactorisation majeure de la logique de routage (HTTP/SOCKS5) et de la détection des protocoles dans [portail](/repos/cloud-gouv/portail).
- Mise à jour des charts Helm pour assurer la compatibilité avec l'opérateur Cluster API et la correction des ressources OpenStack dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).
- Migrations techniques vers `finalAttrs` et amélioration de la compatibilité avec GCC 15 dans [nixpkgs](/repos/cloud-gouv/nixpkgs).
- Optimisation des pipelines CI/CD et amélioration des tableaux de bord de monitoring (Grafana) dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts).
- Mise en place de la structure de déploiement Kubernetes et Helm pour [openproject](/repos/cloud-gouv/openproject).

## Dépôts les plus actifs
- [portail](/repos/cloud-gouv/portail) : Améliorations majeures de la connectivité, de la gestion des logs et de la résilience du routage.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs critiques, mises à jour de sécurité et enrichissement des bibliothèques clientes.
- [securix](/repos/cloud-gouv/securix) : Évolutions vers la gestion centralisée et support de nouveaux matériels et systèmes.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Améliorations de l'observabilité, de la gestion des accès et de la CI/CD.
