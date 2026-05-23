# Synthèse d'activité : codegouvfr (du 16/04 au 16/05)

## Résumé de l'activité
L'activité récente de l'organisation codegouvfr s'est concentrée sur l'amélioration de la fiabilité et de la performance de ses outils, notamment [catalogi](/repos/codegouvfr/catalogi) et [sill-deploy](/repos/codegouvfr/sill-deploy). Des efforts importants ont été déployés pour optimiser l'intégration avec Wikidata, améliorer la gestion des données et l'expérience utilisateur.  Parallèlement, les fondations d'un nouveau projet, [floss-criteria](/repos/codegouvfr/floss-criteria), ont été posées pour structurer l'évaluation des logiciels libres. Enfin, des améliorations de sécurité et de gestion documentaire ont été apportées à [cartonum](/repos/codegouvfr/cartonum), et des corrections ont été implémentées dans [keycloak-theme-dsfr](/repos/codegouvfr/keycloak-theme-dsfr) et [react-dsfr](/repos/codegouvfr/react-dsfr) pour améliorer la robustesse et l'accessibilité.

## Sécurité
- Correction d'un bug dans [keycloak-theme-dsfr](/repos/codegouvfr/keycloak-theme-dsfr) empêchant la redirection vers la page d'autorisation si le client Keycloak spécifié n'existait pas.

## Autres changements notables
- Mise en place de workflows CI/CD pour le déploiement sur le SILL dans [sill-deploy](/repos/codegouvfr/sill-deploy).
- Refactoring du type `SoftwareData` et suppression de colonnes inutilisées dans la table `softwares` dans [catalogi](/repos/codegouvfr/catalogi).
- Début de la structuration des critères d'évaluation pour les logiciels libres dans [floss-criteria](/repos/codegouvfr/floss-criteria).
- Ajout de nouvelles fonctionnalités de sauvegarde, gestion documentaire et accès aux actifs dans [cartonum](/repos/codegouvfr/cartonum).

## Dépôts les plus actifs
- [catalogi](/repos/codegouvfr/catalogi) : Amélioration de la fiabilité et de la performance de l'intégration avec Wikidata, et de la traçabilité des données.
- [sill-deploy](/repos/codegouvfr/sill-deploy) : Amélioration de l'affichage de la provenance des données et mise en place de workflows CI/CD.
- [cartonum](/repos/codegouvfr/cartonum) : Enrichissement de la cartographie des informations avec de nouvelles fonctionnalités de gestion documentaire et de sécurité.
- [floss-criteria](/repos/codegouvfr/floss-criteria) : Initialisation et structuration du projet pour l'évaluation des logiciels libres.
