# Synthèse d'activité : codegouvfr (du 16/04 au 27/08)

## Résumé de l'activité
L'activité récente de l'organisation se concentre sur le renforcement de la fiabilité des données et la simplification de l'administration des catalogues de logiciels. Les outils [catalogi](/repos/codegouvfr/catalogi) et [sill-deploy](/repos/codegouvfr/sill-deploy) ont bénéficié de capacités accrues d'importation automatique et de recherche d'organisations (via Wikidata, ROR ou HAL), facilitant ainsi la gestion et la visibilité des actifs numériques.

L'expérience utilisateur est également optimisée grâce à des améliorations d'accessibilité et de performance dans [react-dsfr](/repos/codegouvfr/react-dsfr), tandis que [cartonum](/repos/codegouvfr/cartonum) étend ses capacités de gestion documentaire et d'infrastructure. Enfin, le lancement de [floss-criteria](/repos/codegouvfr/floss-criteria) marque une étape clé dans la structuration de l'évaluation des logiciels libres pour l'administration.

## Sécurité
- Ajout de fonctionnalités de gestion des mots de passe et de coffres-forts partagés dans [cartonum](/repos/codegouvfr/cartonum).
- Amélioration de la robustesse du thème [keycloak-theme-dsfr](/repos/codegouvfr/keycloak-theme-dsfr) pour éviter des erreurs de redirection lors de l'absence de clients spécifiés.

## Autres changements notables
- **Optimisation et refactoring** : Introduction d'un chargement sélectif du CSS pour améliorer les performances de [react-dsfr](/repos/codegouvfr/react-dsfr) et passage d'un filtrage applicatif à un filtrage SQL dans [sill-deploy](/repos/codegouvfr/sill-deploy).
- **Évolutions d'infrastructure** : Migration de la configuration de l'interface vers PostgreSQL dans [catalogi](/repos/codegouvfr/catalogi) pour permettre une gestion dynamique via API, et extension du périmètre technique de [cartonum](/repos/codegouvfr/cartonum) (conteneurisation, stockage objet).

## Dépôts les plus actifs
- [catalogi](/repos/codegouvfr/catalogi) : Renforcement majeur des outils d'administration et fiabilisation des processus d'importation de données.
- [sill-deploy](/repos/codegouvfr/sill-deploy) : Évolutions fonctionnelles sur la gestion des organisations et nouveaux workflows de déploiement.
- [react-dsfr](/repos/codegouvfr/react-dsfr) : Améliorations de l'accessibilité et optimisation des performances de rendu.
- [cartonum](/repos/codegouvfr/cartonum) : Enrichissement des fonctionnalités de cartographie, de gestion documentaire et d'infrastructure.
