## Changelog : potentiel (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des projets, notamment en ce qui concerne les abandons, les raccordements et les signalements PPA. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme. Une mise à jour des dépendances a été effectuée pour renforcer la sécurité.

### Évolutions fonctionnelles
- Possibilité pour l'administration d'annuler un signalement PPA [#4204](https://github.com/MTES-MCT/potentiel/issues/4204).
- Ajout de la possibilité de déclarer un état PPA lors d'une demande d'abandon pour les projets PP [#4206](https://github.com/MTES-MCT/potentiel/issues/4206).
- Amélioration de la gestion des raccordements : suppression automatique en cas d'annulation d'un état PPA [#4258](https://github.com/MTES-MCT/potentiel/issues/4258) et modification possible si abandon en cours/accordé [#4235](https://github.com/MTES-MCT/potentiel/issues/4235).
- Import des données fournisseur et de la puissance initiale via DN [#4207](https://github.com/MTES-MCT/potentiel/issues/4207) et [#4199](https://github.com/MTES-MCT/potentiel/issues/4199).
- Ajout des coordonnées géodésiques [#4191](https://github.com/MTES-MCT/potentiel/issues/4191).
- Possibilité de demander une mainlevée suite à un abandon [#4209](https://github.com/MTES-MCT/potentiel/issues/4209).
- Ajout du SIREN/SIRET [#4193](https://github.com/MTES-MCT/potentiel/issues/4193).
- Notification lors de la modification de l'achèvement [#4252](https://github.com/MTES-MCT/potentiel/issues/4252).
- Amélioration de l'affichage du SIRET et du SIREN (formatage) [#4254](https://github.com/MTES-MCT/potentiel/issues/4254).

### Évolutions techniques
- Remplacement de ESLint et Prettier par Biome pour le linting et le formattage du code [#4245](https://github.com/MTES-MCT/potentiel/issues/4245).
- Mise à jour de Next.js [#4242](https://github.com/MTES-MCT/potentiel/issues/4242).
- Réécriture du mécanisme anti-CSRF [#4246](https://github.com/MTES-MCT/potentiel/issues/4246).
- Mise à jour des dépendances Next, React et React-DSFR pour corriger des failles de sécurité [#4195](https://github.com/MTES-MCT/potentiel/issues/4195).
- Utilisation d'un helper server only pour gérer les feature flags côté SSR [#4218](https://github.com/MTES-MCT/potentiel/issues/4218).
- Suppression des utilisations de `getContext` du package `@potentiel-applications/request-context` dans le SSR [#4224](https://github.com/MTES-MCT/potentiel/issues/4224).
- Correction des erreurs de `pg_notify` et gestion des événements avec un payload trop conséquent [#4237](https://github.com/MTES-MCT/potentiel/issues/4237).
- Ajout de la variable d'environnement `AWS_REGION` pour le s3Schema de la partie CLI [#4188](https://github.com/MTES-MCT/potentiel/issues/4188).
- Correction d'un test flaky concernant la modification d'un site de production [#4240](https://github.com/MTES-MCT/potentiel/issues/4240) et un autre test général [#4213](https://github.com/MTES-MCT/potentiel/issues/4213).

### Autres changements
- Renommage des étapes d'attestation de conformité en achèvement réel [#4261](https://github.com/MTES-MCT/potentiel/issues/4261).
- Suppression du dossier `.vscode` du dépôt git [#4253](https://github.com/MTES-MCT/potentiel/issues/4253).
- Ajout d'une raison lors de la modification de l'achèvement par l'administration [#4247](https://github.com/MTES-MCT/potentiel/issues/4247).
- Correction de la redirection post modification évaluation carbone simplifiée [#4248](https://github.com/MTES-MCT/potentiel/issues/4248).
- Correction de bugs mineurs et améliorations diverses de l'interface utilisateur et des tests.
- Intégration des modifications de la release 3.77 et 3.78 [#4210](https://github.com/MTES-MCT/potentiel/issues/4210), [#4222](https://github.com/MTES-MCT/potentiel/issues/4222), [#4223](https://github.com/MTES-MCT/potentiel/issues/4223), [#4227](https://github.com/MTES-MCT/potentiel/issues/4227), [#4232](https://github.com/MTES-MCT/potentiel/issues/4232), [#4233](https://github.com/MTES-MCT/potentiel/issues/4233).
- Correction de l'export lauréat et ajout des coordonnées à NomEtLocalitéLauréatImportés-V1 [#4232](https://github.com/MTES-MCT/potentiel/issues/4232).
- Correction d'une erreur lors de la suppression de raccordements [#4259](https://github.com/MTES-MCT/potentiel/issues/4259).
- Correction d'une erreur lors de l'import DN concernant la date d'échéance GF [#4197](https://github.com/MTES-MCT/potentiel/issues/4197) et [#426a32f9](https://github.com/MTES-MCT/potentiel/issues/426a32f9).
