# Synthèse d'activité : cloud-gouv (du 17/09 au 24/09)

## Résumé de l'activité
L'activité de l'organisation a été marquée par une montée en maturité significative, notamment à travers une refonte majeure de la documentation pour la rendre bilingue (français/anglais) sur des projets clés comme [securix](/repos/cloud-gouv/securix) et [portail](/repos/cloud-gouv/portail). Ces efforts visent à améliorer l'accessibilité et l'adoption des outils par la communauté.

Parallèlement, l'écosystème d'infrastructure s'est enrichi avec l'initialisation de nouveaux dépôts pour le déploiement Kubernetes ([openproject](/repos/cloud-gouv/openproject)) et l'extension du catalogue de déploiements automatisés ([common-helm-charts](/repos/cloud-gouv/common-helm-charts)). Ces évolutions renforcent la capacité de l'organisation à fournir des solutions prêtes à l'emploi, plus robustes et plus faciles à maintenir.

## Sécurité
- [securix](/repos/cloud-gouv/securix) : Renforcement de la sécurité SSH via la désactivation de l'authentification par mot de passe et sécurisation de l'installateur (gestion des clés SSH).
- [openbao](/repos/cloud-gouv/openbao) : Correction de vulnérabilités de sécurité par la mise à jour de Go et d'OpenTelemetry, et résolution de problèmes liés à l'auto-déverrouillage KMS.
- [portail](/repos/cloud-gouv/portail) : Mise en place de notifications automatiques en cas d'échec de la négociation TLS.

## Autres changements notables
- [portail](/repos/cloud-gouv/portail) : Implémentation d'un bus d'événements pour la surveillance et refonte de la logique de routage réseau (HTTP/SOCKS5) et de détection de protocole.
- [nixpkgs](/repos/cloud-gouv/nixpkgs) : Travaux de maintenance technique pour assurer la compatibilité avec le compilateur GCC 15 et optimisation de la gestion des attributs.
- [k8s-cluster-api-helm-charts](/repos/cloud-gouv/k8s-cluster-api-helm-charts) : Mise à jour des versions d'API pour garantir la compatibilité avec le dernier opérateur Cluster API, notamment pour les environnements OpenStack.
- [dockerfiles](/repos/cloud-gouv/dockerfiles) : Optimisation de l'image "autofix" pour réduire sa taille et améliorer la rapidité des déploiements.

## Dépôts les plus actifs
- [securix](/repos/cloud-gouv/securix) : Améliorations de l'expérience utilisateur (VPN, interface), de la documentation et de la sécurité système.
- [portail](/repos/cloud-gouv/portail) : Évolutions majeures sur la surveillance, la gestion des logs et l'internationalisation.
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Enrichissement du catalogue de composants et optimisation des pipelines CI/CD.
- [openbao](/repos/cloud-gouv/openbao) : Maintenance corrective importante sur la gestion des secrets et la robustesse des services.
