# Synthèse d'activité : codegouvfr (du 07/05 au 16/05)

## Résumé de l'activité
L'activité récente de l'organisation codegouvfr s'est concentrée sur l'amélioration de la qualité des données, l'accessibilité et la robustesse des outils existants. Plusieurs dépôts ont bénéficié d'améliorations de l'interface utilisateur, notamment pour l'affichage de la provenance des données et la prise en charge des appareils mobiles. Des efforts ont également été déployés pour structurer les critères d'évaluation des logiciels libres et pour renforcer la sécurité, notamment au niveau de l'authentification via Keycloak. L'enrichissement des données via Wikidata reste une priorité.

## Sécurité
Le thème Keycloak [keycloak-theme-dsfr](/repos/codegouvfr/keycloak-theme-dsfr) a été mis à jour pour corriger un bug potentiel de redirection lors de l'authentification, améliorant ainsi la sécurité et la robustesse du processus.

## Autres changements notables
- Refactoring du type `SoftwareData` dans [catalogi](/repos/codegouvfr/catalogi) pour simplifier la structure des données.
- Ajout de workflows CI/CD pour le déploiement sur le SILL dans [sill-deploy](/repos/codegouvfr/sill-deploy).
- Début de la structuration des critères d'évaluation pour les logiciels libres dans [floss-criteria](/repos/codegouvfr/floss-criteria).
- Optimisations de performance de l'API dans [catalogi](/repos/codegouvfr/catalogi) pour réduire les erreurs liées aux limitations de débit de Wikidata.

## Dépôts les plus actifs
- [catalogi](/repos/codegouvfr/catalogi) : Amélioration de l'affichage de la provenance des données et optimisation de l'API.
- [sill-deploy](/repos/codegouvfr/sill-deploy) : Amélioration de l'affichage de la provenance des données, ajout de la configuration via fichiers et prise en charge des systèmes mobiles.
- [cartonum](/repos/codegouvfr/cartonum) : Enrichissement de la cartographie des informations avec de nouvelles fonctionnalités de gestion documentaire et de sécurité.
- [react-dsfr](/repos/codegouvfr/react-dsfr) : Amélioration de l'accessibilité et de la flexibilité des composants.
