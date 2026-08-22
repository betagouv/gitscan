# Synthèse d'activité : cloud-gouv (du 14/08 au 22/08/2026)

## Résumé de l'activité
L'activité récente de l'organisation est centrée sur le renforcement de la sécurité et la consolidation des infrastructures de gestion. L'intégration de [securix](/repos/cloud-gouv/securix) avec le [portail](/repos/cloud-gouv/portail) marque une étape clé vers une gestion centralisée, tandis que les optimisations de performance et de robustesse apportées à [portail](/repos/cloud-gouv/portail) et [openbao](/repos/cloud-gouv/openbao) garantissent une meilleure stabilité des services critiques.

Parallèlement, l'organisation améliore ses capacités de déploiement et d'audit, notamment via la mise à jour des charts Helm ([common-helm-charts](/repos/cloud-gouv/common-helm-charts) et [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts)) et l'intégration de nouveaux outils de détection de vulnérabilités dans [dockerfiles](/repos/cloud-gouv/dockerfiles).

## Sécurité
- Renforcement de la sécurité applicative et détection de vulnérabilités : durcissement des ACL et des permissions de fichiers dans [portail](/repos/cloud-gouv/portail), suppression de blocs de code non sécurisés dans [portail](/repos/cloud-gouv/portail), mise à jour de composants critiques (Go, OpenTelemetry) dans [openbao](/repos/cloud-gouv/openbao) et intégration de l'outil `debsecan` pour le scan de paquets Debian dans [dockerfiles](/repos/cloud-gouv/dockerfiles).
- Authentification matérielle : ajout du support pour les puces de sécurité P14SG6 dans [securix](/repos/cloud-gouv/securix).

## Autres changements notables
- Optimisation des infrastructures et du routage : refonte majeure du moteur de routage et amélioration des performances de connexion (DNS, Happy Eyeballs v2) dans [portail](/repos/cloud-gouv/portail), et intégration de [securix](/repos/cloud-gouv/securix) au Portail pour une gestion centralisée.
- Évolutions des outils de déploiement et de compatibilité : mise à jour des versions d'API pour la compatibilité avec l'opérateur Cluster API dans [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) et implémentation d'une gestion de versions individuelle pour les charts dans [common-helm-charts](/repos/cloud-gouv/common-helm-charts), ainsi que l'élargissement du support matériel et logiciel dans [nixpkgs](/repos/cloud-gouv/nixpkgs).

## Dépôts les plus actifs
- [portail](/repos/cloud-gouv/portail) : Travaux intensifs sur la refonte du routage, la performance et la sécurisation.
- [securix](/repos/cloud-gouv/securix) : Évolutions majeures incluant l'intégration au Portail et le support de l'authentification matérielle.
- [openbao](/repos/cloud-gouv/openbao) : Corrections de bugs et mises à jour de sécurité importantes.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Améliorations fonctionnelles et gestion de versions pour les différents charts.
