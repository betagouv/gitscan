# Synthèse d'activité : codegouvfr (du 30 mai au 12 juin 2026)

## Résumé de l'activité
L'activité de codegouvfr sur les deux dernières semaines a été marquée par des améliorations significatives sur plusieurs de ses projets clés.  [sill-deploy](/repos/codegouvfr/sill-deploy) a reçu des mises à jour importantes pour la gestion des organisations et des sources de données, ainsi que pour l'interface utilisateur, facilitant la sélection et le déploiement de logiciels. [catalogi](/repos/codegouvfr/catalogi) a également bénéficié d'optimisations de performance et d'améliorations de l'interface, notamment pour la recherche et l'affichage des protections logicielles. Enfin, les premiers pas vers la structuration des critères d'évaluation pour les logiciels libres ont été posés avec [floss-criteria](/repos/codegouvfr/floss-criteria), tandis que [cartonum](/repos/codegouvfr/cartonum) a enrichi sa cartographie des informations avec de nouvelles fonctionnalités de gestion documentaire et de sécurité.

## Sécurité
- Correction d'un bug dans [keycloak-theme-dsfr](/repos/codegouvfr/keycloak-theme-dsfr) qui pouvait entraîner des erreurs de redirection si le client Keycloak spécifié n'existait pas.

## Autres changements notables
- Refactoring dans [sill-deploy](/repos/codegouvfr/sill-deploy) pour effectuer le filtrage au niveau SQL, améliorant ainsi les performances.
- Optimisation de la requête SQL pour l'importation de données dans [catalogi](/repos/codegouvfr/catalogi).
- Mise en cache des navigateurs Playwright en CI dans [catalogi](/repos/codegouvfr/catalogi) pour accélérer les tests.

## Dépôts les plus actifs
- [sill-deploy](/repos/codegouvfr/sill-deploy) : Ajout de fonctionnalités pour la gestion des organisations, des sources de données et amélioration de l'interface utilisateur.
- [catalogi](/repos/codegouvfr/catalogi) : Optimisations de performance, améliorations de l'interface et intégration de nouvelles sources de données.
- [floss-criteria](/repos/codegouvfr/floss-criteria) : Début de la structuration des critères d'évaluation pour les logiciels libres.
- [cartonum](/repos/codegouvfr/cartonum) : Enrichissement de la cartographie des informations avec de nouvelles fonctionnalités de gestion documentaire et de sécurité.
- [react-dsfr](/repos/codegouvfr/react-dsfr) : Correction d'un bug concernant l'attribut `role` du composant `Alert` pour une meilleure flexibilité en matière d'accessibilité.
