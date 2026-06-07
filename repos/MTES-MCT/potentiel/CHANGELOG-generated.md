## Changelog : potentiel (30 derniers jours, au 04 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment pour les agents de l'administration, avec des fonctionnalités liées à la gestion des abandons de projets, des attestations de conformité et des rapports associés. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Gestion des abandons et PPA :**
    - Possibilité pour l'administration d'annuler un signalement PPA [#4204](https://github.com/MTES-MCT/potentiel/issues/4204).
    - Gestion des projets avec PPA lors d'un abandon, incluant l'annulation de l'état PPA [#4255](https://github.com/MTES-MCT/potentiel/issues/4255).
    - Déclaration d'un état PPA lors d'une demande d'abandon [#4218](https://github.com/MTES-MCT/potentiel/issues/4218).
- **Attestations de conformité et rapports :**
    - Dissociation de l'attestation de conformité du rapport associé pour la transmission [#4257](https://github.com/MTES-MCT/potentiel/issues/4257).
    - Possibilité pour le porteur de modifier l'attestation de conformité avec son rapport associé [#4272](https://github.com/MTES-MCT/potentiel/issues/4272).
    - Ajout de la raison de la modification dans l'historique des attestations [#4238](https://github.com/MTES-MCT/potentiel/issues/4238).
- **Interface utilisateur :**
    - Amélioration de l'affichage des identifiants de projet [#4269](https://github.com/MTES-MCT/potentiel/issues/4269).
    - Autocomplétion du nom du producteur à partir du SIRET [#4266](https://github.com/MTES-MCT/potentiel/issues/4266).
    - Affichage de la description de l'AO/famille dans la section CDC [#4282](https://github.com/MTES-MCT/potentiel/issues/4282).
    - Amélioration de l'affichage des badges dans les listes [#4277](https://github.com/MTES-MCT/potentiel/issues/4277).
    - Correction de l'affichage des demandes représentant légal [#4309](https://github.com/MTES-MCT/potentiel/issues/4309).
- **Accès :**
    - Accès des GRD aux pages de raccordement [#4311](https://github.com/MTES-MCT/potentiel/issues/4311).
- **Ouverture de documents :**
    - Possibilité d'ouvrir un document sans le télécharger [#4068](https://github.com/MTES-MCT/potentiel/issues/4068).

### Évolutions techniques
- **Refactoring et Optimisations :**
    - Réécriture du mécanisme anti CSRF [#4246](https://github.com/MTES-MCT/potentiel/issues/4246).
    - Suppression des schémas et extensions PostGIS inutiles [#4294](https://github.com/MTES-MCT/potentiel/issues/4294).
    - Utilisation de Biome en remplacement de ESLint et Prettier [#4245](https://github.com/MTES-MCT/potentiel/issues/4245).
    - Suppression des utilisations de `getContext` du package `@potentiel-applications/request-context` en SSR [#4224](https://github.com/MTES-MCT/potentiel/issues/4224).
- **Infrastructure et CI/CD :**
    - Mise à jour de Next.js [#4242](https://github.com/MTES-MCT/potentiel/issues/4242).
    - Mise à jour des actions GitHub [#4241](https://github.com/MTES-MCT/potentiel/issues/4241).
    - Utilisation des SHA1 des GitHub Actions plutôt que des tags pour les builds [#4310](https://github.com/MTES-MCT/potentiel/issues/4310).
    - Correction du script `build:dev` [#4273](https://github.com/MTES-MCT/potentiel/issues/4273).
- **Base de données :**
    - Correction des scripts de base de données et ajout du paramètre `sslrootcert` [#4306](https://github.com/MTES-MCT/potentiel/issues/4306).

### Autres changements
- Ajout des types fournisseur PV pour l'import DN [#4290](https://github.com/MTES-MCT/potentiel/issues/4290).
- Ajout de booléens pour `enService` et `PPA` dans les statistiques projet [#4305](https://github.com/MTES-MCT/potentiel/issues/4305).
- Mise à jour des statistiques projet et du dump [#4304](https://github.com/MTES-MCT/potentiel/issues/4304).
- Suppression du feature flag PPA [#4303](https://github.com/MTES-MCT/potentiel/issues/4303).
- Export des données fournisseur à la candidature importées via DN [#4207](https://github.com/MTES-MCT/potentiel/issues/4207).
- Correction de l'affichage des champs supplémentaires optionnels avant le passage sur DN (eolien) [#4295](https://github.com/MTES-MCT/potentiel/issues/4295).
- Correction des SIRET-producteur [#4300](https://github.com/MTES-MCT/potentiel/issues/4300).
- Amélioration du wording concernant la modification de l'attestation [#4302](https://github.com/MTES-MCT/potentiel/issues/4302).
- Correction d'un input invalide [#4291](https://github.com/MTES-MCT/potentiel/issues/4291).
- Correction d'un bug lié au proxy withAuth [#4283](https://github.com/MTES-MCT/potentiel/issues/4283).
- Suppression des schémas auth, tiger, tiger_date, topology et des extensions inutiles postgis_tiger_geocoder, postgis_topology et postgis [#4294](https://github.com/MTES-MCT/potentiel/issues/4294).
- Correction d'un problème de flaky test [#4213](https://github.com/MTES-MCT/potentiel/issues/4213) et [#4240](https://github.com/MTES-MCT/potentiel/issues/4240).
- Ajout de title manquant et uniformisation [#4228](https://github.com/MTES-MCT/potentiel/issues/4228).
- Suppression de la référence au package lock dans packages/applications/feature-flag [#4250](https://github.com/MTES-MCT/potentiel/issues/4250).
- Mise à jour des CSP pour Crisp [#4212](https://github.com/MTES-MCT/potentiel/issues/4212).
- Correction d'une erreur d'affichage lors de la modification d'un site de production [#4265](https://github.com/MTES-MCT/potentiel/issues/4265).
- Ajout d'un helper server only pour gérer les feature flag côté SSR [#4218](https://github.com/MTES-MCT/potentiel/issues/4218).
- Correction d'un bug lié au remplissage de coordonnées invalides [#4268](https://github.com/MTES-MCT/potentiel/issues/4268).
- Intégration des modifications de la release 3.80 [#4312](https://github.com/MTES-MCT/potentiel/issues/4312), [#4299](https://github.com/MTES-MCT/potentiel/issues/4299), [#4301](https://github.com/MTES-MCT/potentiel/issues/4301), [#4292](https://github.com/MTES-MCT/potentiel/issues/4292), [#4287](https://github.com/MTES-MCT/potentiel/issues/4287).
- Intégration des modifications de la release 3.79 [#4278](https://github.com/MTES-MCT/potentiel/issues/4278), [#4271](https://github.com/MTES-MCT/potentiel/issues/4271), [#4233](https://github.com/MTES-MCT/potentiel/issues/4233).
- Intégration des modifications de la release 3.78 [#4227](https://github.com/MTES-MCT/potentiel/issues/4227), [#4223](https://github.com/MTES-MCT/potentiel/issues/4223).
