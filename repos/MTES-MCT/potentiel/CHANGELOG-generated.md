## Changelog : potentiel (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment concernant la gestion des numéros SIRET/SIREN, les abandons de projets et les notifications. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Possibilité pour les porteurs de projet (PP) de corriger leur numéro SIRET/SIREN via un formulaire dédié. [#4322](https://github.com/MTES-MCT/potentiel/issues/4322)
- Ajout de la technologie aux exports des listes de lauréats et d'éliminés. [#4323](https://github.com/MTES-MCT/potentiel/issues/4323)
- Affichage du motif de GF (Gestion Favorable) en attente sur la page projet. [#4320](https://github.com/MTES-MCT/potentiel/issues/4320)
- Affichage d'une alerte sur la page projet si l'AR (Autorisation de Raccordement) de la DCR (Demande de Connexion Réseau) est manquante. [#4315](https://github.com/MTES-MCT/potentiel/issues/4315)
- Amélioration de la gestion des abandons de projets, notamment avec la possibilité de déclarer un état PPA (Plan de Protection des Activités) lors de la demande d'abandon. [#4206](https://github.com/MTES-MCT/potentiel/issues/4206) et [#4252](https://github.com/MTES-MCT/potentiel/issues/4252)
- Possibilité pour les GRD (Gestionnaires de Réseau de Distribution) de modifier le SIRET d'un projet. [#4225](https://github.com/MTES-MCT/potentiel/issues/4225)
- Ajout de la description de l'AO (Appel d'Offres) / famille dans la section CDC (Cahier des Charges). [#4282](https://github.com/MTES-MCT/potentiel/issues/4282)
- Amélioration de l'affichage des badges dans les listes de projets. [#4277](https://github.com/MTES-MCT/potentiel/issues/4277)
- Possibilité pour les administrateurs d'indiquer une raison lors de la modification de l'achèvement d'un projet. [#4247](https://github.com/MTES-MCT/potentiel/issues/4247)
- Possibilité pour les PP de déclarer un état PPA lors de la demande d'abandon. [#4258](https://github.com/MTES-MCT/potentiel/issues/4258)

### Évolutions techniques
- Mise à jour de la sécurité de la librairie `shell-quote`. [#4324](https://github.com/MTES-MCT/potentiel/issues/4324)
- Simplification des readable streams. [#4321](https://github.com/MTES-MCT/potentiel/issues/4321)
- Refactorisation du mécanisme anti-CSRF. [#4246](https://github.com/MTES-MCT/potentiel/issues/4246)
- Migration vers Biome en remplacement de ESLint et Prettier. [#4245](https://github.com/MTES-MCT/potentiel/issues/4245)
- Suppression de schémas et extensions PostGIS inutiles. [#4294](https://github.com/MTES-MCT/potentiel/issues/4294)
- Amélioration de la gestion des erreurs de `pg_notify` et gestion des événements avec des payloads trop conséquents. [#4237](https://github.com/MTES-MCT/potentiel/issues/4237)
- Suppression des utilisations de `getContext` du package `@potentiel-applications/request-context` dans le SSR (Server Side Rendering). [#4224](https://github.com/MTES-MCT/potentiel/issues/4224)
- Mise à jour de Next.js. [#4242](https://github.com/MTES-MCT/potentiel/issues/4242)
- Mise à jour de better-auth. [#4284](https://github.com/MTES-MCT/potentiel/issues/4284)

### Autres changements
- Correction de bugs mineurs et améliorations de la stabilité générale.
- Amélioration des scripts de base de données et ajout du paramètre `sslrootcert`. [#4306](https://github.com/MTES-MCT/potentiel/issues/4306)
- Amélioration des statistiques projets avec l'ajout de booléens pour `enService` et `PPA`. [#4305](https://github.com/MTES-MCT/potentiel/issues/4305)
- Correction d'un flaky test dans `corrigerCandidature`. [#4319](https://github.com/MTES-MCT/potentiel/issues/4319)
- Correction d'un flaky test pour modifier le site de production. [#4240](https://github.com/MTES-MCT/potentiel/issues/4240)
- Suppression de la référence au `package-lock` dans les packages d'applications. [#4267](https://github.com/MTES-MCT/potentiel/issues/4267)
- Ajout des types fournisseur PV pour l'import DN. [#4290](https://github.com/MTES-MCT/potentiel/issues/4290)
- Correction de l'affichage des erreurs lors du remplissage des coordonnées. [#4268](https://github.com/MTES-MCT/potentiel/issues/4268)
- Amélioration de la gestion des redirections des emails. [#4239](https://github.com/MTES-MCT/potentiel/issues/4239)
- Correction de l'affichage des items d'historique. [#4238](https://github.com/MTES-MCT/potentiel/issues/4238)
- Correction d'un bug empêchant la modification des GRD sans email de contact. [#4229](https://github.com/MTES-MCT/potentiel/issues/4229)
- Suppression des projets avec PPA des projets avec achèvement en attente. [#4255](https://github.com/MTES-MCT/potentiel/issues/4255)
- Correction d'une erreur d'affichage de la demande représentant légal. [#4309](https://github.com/MTES-MCT/potentiel/issues/4309)
- Correction des retours de Mathieu concernant le formulaire représentant légal. [#4326](https://github.com/MTES-MCT/potentiel/issues/4326)
