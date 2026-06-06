# Synthèse d'activité : cloud-gouv (du 24 avril 2026 au 4 juin 2026)

## Résumé de l'activité
L'activité récente de l'organisation cloud-gouv s'est concentrée sur l'amélioration de la sécurité, la correction de bugs et l'ajout de nouvelles fonctionnalités à ses différents projets.  Des efforts importants ont été déployés pour renforcer la sécurité d'OpenBao et de Securix, avec des corrections de vulnérabilités et des améliorations de la configuration. Les charts Helm de common-helm-charts ont été enrichis avec de nouveaux outils de monitoring et de benchmark, tandis que les charts k8s-cluster-api-helm-charts ont bénéficié d'améliorations en matière de gestion des CIDR et de la sécurité des nœuds worker. L'ajout de Go à l'image Docker de GitLab Runner via [dockerfiles](/repos/cloud-gouv/dockerfiles) permet une plus grande flexibilité pour les pipelines CI/CD.

## Sécurité
Plusieurs changements liés à la sécurité ont été apportés :
- Correction d'une vulnérabilité de sécurité dans OpenBao avec une mise à jour vers Go 1.25.7 et des dépendances OpenTelemetry ([openbao](/repos/cloud-gouv/openbao)).
- Amélioration de la sécurité de Securix avec la désactivation optionnelle de KWallet et une configuration affinée pour une meilleure conformité aux recommandations ANSSI ([securix](/repos/cloud-gouv/securix)).
- Amélioration de la sécurité des nœuds worker via l'injection de règles de sécurité supplémentaires dans k8s-cluster-api-helm-charts ([k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts)).

## Autres changements notables
- Correction d'un problème de non-déterminisme dans les tests du proxy [portail](/repos/cloud-gouv/portail).
- Amélioration de la robustesse d'OpenBao avec la correction d'erreurs non gérées et de problèmes d'initialisation de PostgreSQL ([openbao](/repos/cloud-gouv/openbao)).
- Ajout d'un fichier README initial pour l'implémentation de référence Securix ([securix-infra-reference-implementation](/repos/cloud-gouv/securix-infra-reference-implementation)).
- Amélioration de la gestion des CIDR et des volumes snapshot dans k8s-cluster-api-helm-charts ([k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts)).

## Dépôts les plus actifs
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs, améliorations de la sécurité et de la robustesse du gestionnaire de secrets.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Améliorations de la gestion des CIDR, de la sécurité des nœuds worker et correction de bugs.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Ajout de nouveaux charts (pgbench, dashboard HAProxy) et amélioration des charts existants.
- [securix](/repos/cloud-gouv/securix) : Améliorations de la sécurité et de la robustesse de l'installateur et de la configuration.
