# Synthèse d'activité : cloud-gouv (du 25/09 au 02/10)

## Résumé de l'activité
L'activité de l'organisation est marquée par un renforcement de la maturité des produits existants et une expansion significative de l'écosystème de déploiement. Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur et de la documentation pour [securix](/repos/cloud-gouv/securix) et [portail](/repos/cloud-gouv/portail), tout en enrichissant les capacités de déploiement Kubernetes via [common-helm-charts](/repos/cloud-gouv/common-helm-charts) et [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).

Parallèlement, l'organisation amorce la mise en place de nouveaux services avec l'initialisation de projets dédiés au déploiement de [openproject](/repos/cloud-gouv/openproject) et [k8s-glpi](/repos/cloud-gouv/k8s-glpi), consolidant ainsi l'offre de solutions prêtes pour le cloud.

## Sécurité
- [securix](/repos/cloud-gouv/securix) : Renforcement de la confidentialité en masquant les comptes administrateurs sur l'écran de connexion.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de vulnérabilités via la mise à jour de Go et OpenTelemetry, ainsi que la résolution de problèmes critiques sur le déverrouillage KMS et la gestion des baux.
- [portail](/repos/cloud-gouv/portail) : Amélioration de la visibilité sur les erreurs de connexion sécurisée grâce à la notification des échecs de handshake TLS.

## Autres changements notables
- **Déploiement et Infrastructure** : Extension du catalogue de déploiement avec l'ajout de nouveaux composants dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts) et mise à jour de la compatibilité avec l'opérateur Cluster API dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts). Initialisation de la structure de déploiement pour [ openproject](/repos/cloud-gouv/openproject) et [k8s-glpi](/repos/cloud-gouv/k8s-glpi).
- **Documentation et Observabilité** : Refonte majeure de la documentation et ajout du support bilingue pour [securix](/repos/cloud-gouv/securix) et [portail](/repos/cloud-gouv/portail). Mise en place d'un suivi d'événements en temps réel pour le [portail](/repos/cloud-gouv/portail) afin de faciliter le diagnostic.
- **Maintenance Système** : Optimisation des processus de mise à jour automatique dans [securix](/repos/cloud-gouv/securix) et migration technique importante vers `finalAttrs` dans [nixpkgs](/repos/cloud-gouv/nixpkgs).

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Améliorations de l'interface, de la fiabilité des mises à jour et de la documentation.
- [portail](/repos/cloud-gouv/portail) : Travaux intensifs sur l'observabilité, l'internationalisation et la documentation.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Élargissement du catalogue de déploiement et optimisation du monitoring.
- [openbao](/repos/cloud-gouv/openbao) : Maintenance corrective et mises à jour de sécurité.
