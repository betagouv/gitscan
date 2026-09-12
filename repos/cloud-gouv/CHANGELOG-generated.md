# Synthèse d'activité : cloud-gouv (du 20/05 au 27/05)

## Résumé de l'activité
L'activité de cette période est marquée par une montée en maturité significative des outils de gestion et de sécurité de l'organisation. L'intégration de [securix](/repos/cloud-gouv/securix) avec le [portail](/repos/cloud-gouv/portail) permet désormais une gestion centralisée du système, offrant une expérience utilisateur plus fluide et unifiée. 

Parallèlement, l'organisation renforce ses bases d'infrastructure avec l'optimisation de la légèreté des images dans [dockerfiles](/repos/cloud-gouv/dockerfiles) et l'amélioration de la compatibilité des déploiements Kubernetes via [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts). Ces évolutions visent à offrir des environnements plus stables, sécurisés et faciles à administrer pour les utilisateurs finaux.

## Sécurité
- Renforcement de l'authentification matérielle avec le support des puces de sécurité P14SG6 dans [securix](/repos/cloud-gouv/securix).
- Correction de vulnérabilités via la mise à jour de Go et d'OpenTelemetry dans [openbao](/repos/cloud-gouv/openbao).
- Amélioration de la détection d'anomalies avec l'émission de notifications automatiques en cas d'échec de négociation TLS dans [portail](/repos/cloud-gouv/portail).
- Correction de la gestion de la liste noire des ressources au niveau des projets dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts).

## Autres changements notables
- **Refonte majeure de [portail](/repos/cloud-gouv/portail)** : Implémentation d'un système d'événements (bus d'événements, interfaces RPC), amélioration de la gestion des logs et mise en place d'une documentation complète et multilingue.
- **Optimisation de l'infrastructure de conteneurs** : Introduction d'une image "autofix" pour l'automatisation des corrections et réduction de la taille des images existantes dans [dockerfiles](/repos/cloud-gouv/dockerfiles).
- **Évolutions de compatibilité** : Mise à jour des versions d'API pour l'opérateur Cluster API et les ressources OpenStack dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts), et travaux de compatibilité pour le compilateur GCC 15 dans [nixpkgs](/repos/cloud-gouv/nixpkgs).
- **Initialisation de nouveaux projets** : Lancement de [playground-public](/repos/cloud-gouv/playground-public) pour les expérimentations d'infrastructure et de [openproject](/repos/cloud-gouv/openproject) pour le déploiement Kubernetes.

## Dépôts les plus actifs
- [portail](/repos/cloud-gouv/portail) : Évolutions majeures sur la surveillance, la documentation et l'architecture réseau.
- [securix](/repos/cloud-gouv/securix) : Intégration système et nouveaux supports matériels et architecture.
- [openbao](/repos/cloud-gouv/openbao) : Résolution de bugs critiques et mises à jour de sécurité.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Amélioration de l'observabilité et de la gestion des accès utilisateurs.
- [nixpkgs](/repos/cloud-gouv/nixpkgs) : Mises à jour de paquets et travaux de compatibilité technique.
