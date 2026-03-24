# Synthèse d'activité : cloud-gouv (derniers 7 jours)

## Résumé de l'activité
L'organisation cloud-gouv a connu une semaine productive, marquée par le lancement d'un nouveau dépôt pour les charts Helm ([common-helm-charts](/repos/cloud-gouv/common-helm-charts)) et des améliorations significatives dans plusieurs projets existants. Les efforts se sont concentrés sur la sécurité, avec des corrections de vulnérabilités dans [openbao](/repos/cloud-gouv/openbao) et l'ajout de fonctionnalités de sécurité avancées comme le mTLS dans [portail](/repos/cloud-gouv/portail).  Des améliorations fonctionnelles ont également été apportées à la gestion des clusters Kubernetes via [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) et à l'outil de gestion de secrets [openbao](/repos/cloud-gouv/openbao).

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité des outils cloud-gouv :

- Correction de vulnérabilités dans `go.opentelemetry.io/otel/sdk` et Go lui-même dans [openbao](/repos/cloud-gouv/openbao).
- Ajout du support mTLS côté serveur dans [portail](/repos/cloud-gouv/portail) pour une communication plus sécurisée.
- Suppression du mode développeur dans [securix](/repos/cloud-gouv/securix), renforçant ainsi la posture de sécurité par défaut.

## Autres changements notables
- [portail](/repos/cloud-gouv/portail) a ajouté le support de la redirection HTTP CONNECT, augmentant sa flexibilité et son intégration avec différents environnements.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) a amélioré la gestion des clusters Kubernetes sur Openstack et Outscale, notamment en corrigeant des problèmes de configuration CoreDNS et en ajoutant le support du multi-tenant sur Outscale.
- [openbao](/repos/cloud-gouv/openbao) a corrigé des bugs liés à l'auto-déverrouillage et à la révocation de baux, améliorant ainsi sa fiabilité.
- [securix](/repos/cloud-gouv/securix) a ajouté le support de qrencode pour faciliter l'authentification et le partage de clés.

## Dépôts les plus actifs
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et améliorations de sécurité liées à la gestion des secrets.
- [portail](/repos/cloud-gouv/portail) : Ajout de nouvelles fonctionnalités de sécurité et de proxy.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Améliorations de la gestion des clusters Kubernetes sur différentes plateformes cloud.
- [securix](/repos/cloud-gouv/securix) : Corrections de bugs, ajout de nouvelles fonctionnalités et améliorations de la configuration.
