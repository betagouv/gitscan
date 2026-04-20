# Synthèse d'activité : cloud-gouv (derniers 7 jours)

## Résumé de l'activité
L'organisation cloud-gouv a connu une activité soutenue cette semaine, principalement axée sur l'amélioration de la stabilité et de la configuration de ses outils. Les mises à jour apportées à [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) renforcent la sécurité des nœuds worker et offrent une plus grande flexibilité dans la gestion des clusters Kubernetes. Le projet [portail](/repos/cloud-gouv/portail) s'est concentré sur la correction de bugs et l'ajout de tests pour améliorer la robustesse du proxy upstream. Enfin, [securix](/repos/cloud-gouv/securix) a simplifié sa configuration et supprimé le support d'Openstack.

## Sécurité
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) permet désormais d'injecter des règles de sécurité supplémentaires (Security Groups) aux nœuds worker.

## Autres changements notables
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Amélioration de la gestion des CIDR et des volumes snapshot, avec des options de configuration plus fines.
- [portail](/repos/cloud-gouv/portail) : Correction d'une erreur de configuration TLS et amélioration de la gestion des erreurs pour une meilleure robustesse.
- [securix](/repos/cloud-gouv/securix) : Suppression du module Openstack, simplifiant ainsi le projet.

## Dépôts les plus actifs
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Améliorations significatives de la gestion des clusters Kubernetes, notamment en termes de sécurité et de configuration.
- [portail](/repos/cloud-gouv/portail) : Stabilisation et ajout de tests pour le proxy upstream Tinyproxy.
- [securix](/repos/cloud-gouv/securix) : Simplification de la configuration et suppression du support d'Openstack.
