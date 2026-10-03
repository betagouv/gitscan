# Synthèse d'activité : cloud-gouv (du 25/09 au 02/10)

## Résumé de l'activité
L'activité de l'organisation a été marquée par une phase d'expansion de l'écosystème et une consolidation des outils de déploiement. Plusieurs nouveaux projets ont été initiés pour faciliter l'adoption de services clés sur Kubernetes, notamment pour la gestion de parc avec [k8s-glpi](/repos/cloud-gouv/k8s-glpi) et [openproject](/repos/cloud-gouv/openproject). Parallèlement, un effort majeur a été consenti sur l'expérience utilisateur et l'observabilité, avec une refonte de la documentation et l'ajout de capacités de suivi en temps réel dans [portail](/repos/cloud-gouv/portail) et [securix](/repos/cloud-gouv/securix).

L'efficacité opérationnelle est également renforcée par l'enrichissement du catalogue de déploiements dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts) et l'optimisation des images de conteneurs dans [dockerfiles](/repos/cloud-gouv/dockerfiles), permettant des infrastructures plus légères et plus faciles à maintenir.

## Sécurité
- Renforcement de la confidentialité dans [securix](/repos/cloud-gouv/securix) par le masquage des comptes administrateurs sur l'écran de connexion.
- Corrections critiques dans [openbao](/repos/cloud-gouv/openbao) concernant l'auto-déverrouillage KMS, la gestion des baux irrévocables et l'invalidation du cache PKI.
- Mise à jour des dépendances de sécurité (Go et OpenTelemetry) et suppression de montages de groupes d'identité corrompus dans [openbao](/repos/cloud-gouv/openbao).

## Autres changements notables
- Optimisation du processus de mise à jour automatique de [securix](/repos/cloud-gouv/securix) via une stratégie de tentatives exponentielles.
- Refonte technique importante de l'architecture de communication dans [portail](/repos/cloud-gouv/portail), incluant l'implémentation d'interfaces RPC via Varlink.
- Migration vers `finalAttrs` et préparation du support pour le compilateur GCC 15 dans [nixpkgs](/repos/cloud-gouv/nixpkgs).
- Mise à jour des versions d'API pour assurer la compatibilité avec l'opérateur Cluster API et les ressources OpenStack dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts).
- Optimisation de la taille des images pour réduire l'empreinte stockage dans [dockerfiles](/repos/cloud-gouv/dockerfiles).

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Améliorations de l'interface, de la sécurité et de la fiabilité des mises à jour système.
- [portail](/repos/cloud-gouv/portail) : Travaux massifs sur l'internationalisation, la documentation et l'observabilité système.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Extension du catalogue de composants et amélioration des outils de monitoring.
- [openbao](/repos/cloud-gouv/openbao) : Correctifs de stabilité et de sécurité sur la gestion des secrets.
