# Synthèse d'activité : codegouvfr (du 16/04 au 16/06)

## Résumé de l'activité
L'activité récente de l'organisation codegouvfr s'est concentrée sur l'amélioration de ses outils et plateformes existants, avec un accent particulier sur la gestion des logiciels et des données. Plusieurs dépôts ont bénéficié d'améliorations significatives en termes de fonctionnalités, de performance et de sécurité. On note des avancées notables dans la structuration des critères d'évaluation des logiciels libres ([floss-criteria](/repos/codegouvfr/floss-criteria)) et l'enrichissement du catalogue de logiciels ([catalogi](/repos/codegouvfr/catalogi)), ainsi que des corrections et optimisations sur [sill-deploy](/repos/codegouvfr/sill-deploy), [react-dsfr](/repos/codegouvfr/react-dsfr) et [keycloak-theme-dsfr](/repos/codegouvfr/keycloak-theme-dsfr). L'outil cartonum ([cartonum](/repos/codegouvfr/cartonum)) a également progressé en ajoutant de nouvelles fonctionnalités de gestion documentaire et de sécurité.

## Sécurité
- Correction d'un bug dans [keycloak-theme-dsfr](/repos/codegouvfr/keycloak-theme-dsfr) empêchant la redirection vers la page d'autorisation lorsque le client Keycloak n'existe pas, améliorant ainsi la robustesse du thème.
- Ajout de protections pour les logiciels dans [catalogi](/repos/codegouvfr/catalogi).

## Autres changements notables
- Refactorisation de la logique de filtrage des logiciels dans [catalogi](/repos/codegouvfr/catalogi) pour améliorer les performances en effectuant le filtrage directement au niveau SQL.
- Ajout de workflows CI/CD pour le déploiement SILL et la synchronisation avec le dépôt upstream dans [sill-deploy](/repos/codegouvfr/sill-deploy).
- Début de la structuration des critères d'évaluation pour les logiciels libres dans [floss-criteria](/repos/codegouvfr/floss-criteria), posant les bases de l'analyse et du choix de logiciels open source.

## Dépôts les plus actifs
- [catalogi](/repos/codegouvfr/catalogi) : Amélioration de la recherche de logiciels, ajout de fonctionnalités d'administration pour les attributs personnalisés et optimisation des performances.
- [sill-deploy](/repos/codegouvfr/sill-deploy) : Ajout d'une page d'administration, amélioration de l'affichage de la provenance des données et optimisation des performances de l'API.
- [floss-criteria](/repos/codegouvfr/floss-criteria) : Initialisation et structuration des critères d'évaluation pour les logiciels libres.
- [cartonum](/repos/codegouvfr/cartonum) : Enrichissement de la cartographie des informations avec de nouvelles fonctionnalités de gestion documentaire et de sécurité.
