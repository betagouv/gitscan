# Synthèse d'activité : codegouvfr (du 16 avril 2026 au 16 mai 2026)

## Résumé de l'activité
L'activité de codegouvfr au cours des dernières semaines s'est concentrée sur l'amélioration de la provenance des données, la robustesse des API et l'expérience utilisateur de ses différents outils. Plusieurs dépôts ont bénéficié d'optimisations de performance, notamment en lien avec l'utilisation de Wikidata. Des efforts ont également été déployés pour structurer les critères d'évaluation des logiciels libres et enrichir la cartographie des informations. L'accent est mis sur la flexibilité des composants ([react-dsfr](/repos/codegouvfr/react-dsfr)), la configuration des applications ([sill-deploy](/repos/codegouvfr/sill-deploy), [catalogi](/repos/codegouvfr/catalogi)) et la sécurité des thèmes Keycloak ([keycloak-theme-dsfr](/repos/codegouvfr/keycloak-theme-dsfr)).

## Sécurité
- Correction d'un bug dans [keycloak-theme-dsfr](/repos/codegouvfr/keycloak-theme-dsfr) qui pouvait entraîner une erreur lors de la redirection vers la page d'autorisation si le client Keycloak spécifié n'existait pas.
- Mise à jour de la politique de sécurité du contenu (CSP) dans [sill-deploy](/repos/codegouvfr/sill-deploy) et [catalogi](/repos/codegouvfr/catalogi) pour autoriser les sources d'images HTTPS arbitraires et les workers Sentry.

## Autres changements notables
- Refactorisation du type `SoftwareData` et suppression des colonnes de contenu de la table `softwares` dans [sill-deploy](/repos/codegouvfr/sill-deploy) et [catalogi](/repos/codegouvfr/catalogi) pour simplifier la structure de la base de données.
- Début de la structuration des critères d'évaluation pour les logiciels libres dans [floss-criteria](/repos/codegouvfr/floss-criteria).
- Ajout de fonctionnalités de sauvegarde de documents et de gestion des mots de passe dans [cartonum](/repos/codegouvfr/cartonum).

## Dépôts les plus actifs
- [catalogi](/repos/codegouvfr/catalogi) : Amélioration de la provenance des données, de la performance de l'API et de l'expérience utilisateur.
- [sill-deploy](/repos/codegouvfr/sill-deploy) : Amélioration de la provenance des données, optimisation des performances de l'API et ajout de fonctionnalités de configuration.
- [cartonum](/repos/codegouvfr/cartonum) : Enrichissement de la cartographie des informations avec de nouvelles fonctionnalités de gestion documentaire et de sécurité.
- [floss-criteria](/repos/codegouvfr/floss-criteria) : Initialisation et structuration des critères d'évaluation pour les logiciels libres.
