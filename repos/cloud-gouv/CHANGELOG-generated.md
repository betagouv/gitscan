# Synthèse d'activité : cloud-gouv (derniers 7 jours)

## Résumé de l'activité
L'organisation cloud-gouv a connu une activité soutenue ces dernières semaines, avec des améliorations notables en matière de sécurité, de flexibilité et de correction de bugs dans plusieurs de ses dépôts. Les charts Helm pour Cluster API ([k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts)) ont été enrichis de nouvelles fonctionnalités de sécurité et de gestion des secrets. Le portail ([portail](/repos/cloud-gouv/portail)) a bénéficié de l'ajout du support mTLS et de la redirection HTTP CONNECT, renforçant ainsi la sécurité et la flexibilité du proxy. OpenBao ([openbao](/repos/cloud-gouv/openbao)) a également reçu des mises à jour de sécurité importantes et des corrections de bugs.

## Sécurité
Plusieurs changements liés à la sécurité ont été apportés :

- Correction de vulnérabilités dans OpenBao ([openbao](/repos/cloud-gouv/openbao)) avec la mise à jour vers Go 1.25.7 et des dépendances OpenTelemetry.
- Possibilité d'injecter des règles de sécurité supplémentaires pour les nœuds worker dans les charts Helm pour Cluster API ([k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts)).
- Activation du support mTLS côté serveur dans le portail ([portail](/repos/cloud-gouv/portail)) pour une communication plus sécurisée.
- Suppression du module Openstack dans Securix ([securix](/repos/cloud-gouv/securix)) simplifiant la configuration et réduisant la surface d'attaque.

## Autres changements notables
- Les charts Helm communs ([common-helm-charts](/repos/cloud-gouv/common-helm-charts)) ont été améliorés avec la possibilité de personnaliser les chemins d'applications et l'intégration du terminal web ArgoCD.
- L'image `k8s-tools` ([dockerfiles](/repos/cloud-gouv/dockerfiles)) a été mise à jour avec l'ajout de `kustomize` et des versions récentes des outils Kubernetes.
- Securix ([securix](/repos/cloud-gouv/securix)) a vu l'ajout d'une commande de mise à niveau documentée et l'activation forcée de `boot.initrd.systemd.enable`.

## Dépôts les plus actifs
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Amélioration de la sécurité, de la gestion des secrets et correction de bugs liés à la configuration des nœuds et de CoreDNS.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs, mises à jour de sécurité et ajout de support pour de nouvelles bibliothèques clientes.
- [portail](/repos/cloud-gouv/portail) : Ajout du support mTLS et de la redirection HTTP CONNECT pour une sécurité et une flexibilité accrues.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Amélioration de la personnalisation des charts Helm et intégration de nouvelles fonctionnalités.
