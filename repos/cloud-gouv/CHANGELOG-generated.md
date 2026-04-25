# Synthèse d'activité : cloud-gouv (du 17/04 au 17/05)

## Résumé de l'activité
L'activité récente de l'organisation cloud-gouv s'est concentrée sur l'amélioration de la stabilité et de la flexibilité de ses outils. Les charts Helm ([common-helm-charts](/repos/cloud-gouv/common-helm-charts)) ont été enrichis de nouvelles fonctionnalités, notamment la gestion de secrets externes et la personnalisation des chemins d'accès.  Des améliorations significatives ont également été apportées à Securix ([securix](/repos/cloud-gouv/securix)) pour le support matériel et la simplification des mises à jour. Le portail ([portail](/repos/cloud-gouv/portail)) a bénéficié de corrections de bugs et de l'ajout de tests pour améliorer sa robustesse.

## Sécurité
Aucun changement lié à la sécurité n'a été signalé durant cette période.

## Autres changements notables
- Refactorisation de la configuration dans [securix](/repos/cloud-gouv/securix) pour une meilleure lisibilité et cohérence, utilisant `mkDefault` et `mkForce`.
- Suppression du module Openstack de [securix](/repos/cloud-gouv/securix).
- Initialisation de la version 1 des règles d'accès (ACL) dans [portail](/repos/cloud-gouv/portail).

## Dépôts les plus actifs
- [common-helm-charts](/repos/cloud-gouv/common-helm-charts) : Amélioration des charts Helm avec de nouvelles fonctionnalités et corrections de bugs.
- [securix](/repos/cloud-gouv/securix) : Ajout de support matériel et amélioration de l'outil de mise à jour.
- [portail](/repos/cloud-gouv/portail) : Stabilisation et ajout de tests pour le proxy upstream Tinyproxy.
