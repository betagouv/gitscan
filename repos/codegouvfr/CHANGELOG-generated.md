# Synthèse d'activité : codegouvfr (du 01/05 au 16/05)

## Résumé de l'activité
L'organisation codegouvfr a connu une activité soutenue ces dernières semaines, avec des améliorations significatives sur plusieurs de ses projets phares. Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur et de la robustesse des outils, notamment avec des ajouts de fonctionnalités d'administration et d'optimisation des performances sur [sill-deploy](/repos/codegouvfr/sill-deploy) et [catalogi](/repos/codegouvfr/catalogi).  Des premiers pas sont également réalisés pour structurer les critères d'évaluation des logiciels libres avec [floss-criteria](/repos/codegouvfr/floss-criteria). Enfin, des correctifs de bugs et des améliorations d'accessibilité ont été apportés à [react-dsfr](/repos/codegouvfr/react-dsfr) et [keycloak-theme-dsfr](/repos/codegouvfr/keycloak-theme-dsfr).

## Sécurité
Un correctif a été appliqué sur [keycloak-theme-dsfr](/repos/codegouvfr/keycloak-theme-dsfr) pour corriger un bug potentiel lors de la redirection vers la page d'autorisation, améliorant ainsi la robustesse du thème.

## Autres changements notables
- Refactorisation du type `SoftwareData` et suppression des colonnes `content` de la table `softwares` sur [sill-deploy](/repos/codegouvfr/sill-deploy) et [catalogi](/repos/codegouvfr/catalogi).
- Ajout de workflows CI/CD pour le déploiement SILL sur [sill-deploy](/repos/codegouvfr/sill-deploy).
- Amélioration de la gestion des erreurs et des limites de débit de l'API Wikidata sur [sill-deploy](/repos/codegouvfr/sill-deploy) et [catalogi](/repos/codegouvfr/catalogi).
- Premières étapes de structuration des critères d'évaluation pour les logiciels libres sur [floss-criteria](/repos/codegouvfr/floss-criteria).

## Dépôts les plus actifs
- [sill-deploy](/repos/codegouvfr/sill-deploy) : Amélioration de l'administration, de l'affichage des données et des performances de l'API.
- [catalogi](/repos/codegouvfr/catalogi) : Optimisation des performances, correction de bugs liés à Wikidata et ajout de fonctionnalités d'administration.
- [cartonum](/repos/codegouvfr/cartonum) : Enrichissement de la cartographie des informations avec de nouvelles fonctionnalités de gestion documentaire et de sécurité.
- [react-dsfr](/repos/codegouvfr/react-dsfr) : Amélioration de l'accessibilité et ajout d'un exemple d'utilisation.
