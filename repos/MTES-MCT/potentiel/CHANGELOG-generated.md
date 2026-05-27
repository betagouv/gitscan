## Changelog : potentiel (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur et la correction de bugs, notamment autour de la gestion des abandons de projets, des notifications, et de l'importation de données. Des améliorations techniques ont également été apportées pour la maintenance et la performance du service.

### Évolutions fonctionnelles
- Possibilité de demander une mainlevée suite à un abandon de projet. [#4209](https://github.com/MTES-MCT/potentiel/issues/4209)
- Amélioration de la gestion des états PPA lors d'un abandon de projet, avec annulation de l'état PPA en cas d'annulation de la demande d'abandon. [#4244](https://github.com/MTES-MCT/potentiel/issues/4244)
- L'administration peut désormais annuler un signalement PPA. [#4204](https://github.com/MTES-MCT/potentiel/issues/4204)
- Ajout de la possibilité de signaler un PPA (DREAL/DGEC). [#4192](https://github.com/MTES-MCT/potentiel/issues/4192)
- Autocomplétion du nom du producteur à partir du SIRET. [#4266](https://github.com/MTES-MCT/potentiel/issues/4266)
- Ajout des coordonnées géodésiques. [#4191](https://github.com/MTES-MCT/potentiel/issues/4191)
- Amélioration de l'affichage du SIREN/SIRET (formatage). [#4254](https://github.com/MTES-MCT/potentiel/issues/4254)
- Ajout d'une raison lors de la modification de l'achèvement par l'administration. [#4247](https://github.com/MTES-MCT/potentiel/issues/4247)
- Ajout du rapport associé optionnel lors de la modification post achèvement (par l'administration). [#4263](https://github.com/MTES-MCT/potentiel/issues/4263)
- Importation des données fournisseur lors de la candidature via DN et mise à jour des exports. [#4200](https://github.com/MTES-MCT/potentiel/issues/4200)
- Possibilité de dissocier l'attestation de conformité du rapport associé pour la transmission (PP). [#4257](https://github.com/MTES-MCT/potentiel/issues/4257)

### Évolutions techniques
- Réécriture du mécanisme anti-CSRF pour plus de sécurité. [#4246](https://github.com/MTES-MCT/potentiel/issues/4246)
- Remplacement de ESLint et Prettier par Biome pour améliorer la performance et la qualité du code. [#4245](https://github.com/MTES-MCT/potentiel/issues/4245)
- Mise à jour des dépendances Next.js, React et React-DSFR pour corriger des failles de sécurité. [#4195](https://github.com/MTES-MCT/potentiel/issues/4195)
- Correction de problèmes de fuites de mémoire EventEmitter. [#4256](https://github.com/MTES-MCT/potentiel/issues/4256)
- Amélioration de la gestion des erreurs de `pg_notify` et des événements avec des payloads trop conséquents. [#4237](https://github.com/MTES-MCT/potentiel/issues/4237)
- Suppression des utilisations de `getContext` du package `@potentiel-applications/request-context` dans le SSR. [#4224](https://github.com/MTES-MCT/potentiel/issues/4224)
- Ajout de variables d'environnement nécessaires pour le s3Schema de la partie CLI. [#4188](https://github.com/MTES-MCT/potentiel/issues/4188)
- Mise à jour de Next.js. [#4242](https://github.com/MTES-MCT/potentiel/issues/4242)

### Autres changements
- Correction du script `build:dev`. [#4273](https://github.com/MTES-MCT/potentiel/issues/4273)
- Suppression de références inutiles à `package-lock` dans `packages/applications/feature-flag`. [#4267](https://github.com/MTES-MCT/potentiel/issues/4267)
- Correction de typos et améliorations de la documentation. [#4270](https://github.com/MTES-MCT/potentiel/issues/4270)
- Correction de problèmes de tests flaky. [#4259](https://github.com/MTES-MCT/potentiel/issues/4259), [#4240](https://github.com/MTES-MCT/potentiel/issues/4240), [#4213](https://github.com/MTES-MCT/potentiel/issues/4213)
- Suppression de fichiers `.vscode` du dépôt. [#4253](https://github.com/MTES-MCT/potentiel/issues/4253)
- Intégration des modifications des releases 3.77, 3.78 et 3.79. [#4271](https://github.com/MTES-MCT/potentiel/issues/4271), [#4233](https://github.com/MTES-MCT/potentiel/issues/4233), [#4223](https://github.com/MTES-MCT/potentiel/issues/4223)
- Correction de problèmes de redirection d'emails. [#4239](https://github.com/MTES-MCT/potentiel/issues/4239)
- Amélioration des CSP pour Crisp. [#4212](https://github.com/MTES-MCT/potentiel/issues/4212)
