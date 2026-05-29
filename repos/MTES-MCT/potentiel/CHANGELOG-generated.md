## Changelog : potentiel (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment concernant la gestion des abandons de projets, l'affichage des informations clés et l'intégration de nouvelles fonctionnalités pour les agents de l'administration. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité pour l'administration d'annuler un signalement PPA [#4204](https://github.com/MTES-MCT/potentiel/issues/4204).
- Implémentation de la demande de mainlevée suite à un abandon de projet [#4209](https://github.com/MTES-MCT/potentiel/issues/4209).
- Affichage de l'identifiant du projet [#4269](https://github.com/MTES-MCT/potentiel/issues/4269).
- Ajout de la description de l'appel d'offres/famille dans la section Cahier des Charges [#4282](https://github.com/MTES-MCT/potentiel/issues/4282).
- Ajout du SIREN/SIRET [#4193](https://github.com/MTES-MCT/potentiel/issues/4193).
- Possibilité de modifier l'attestation de conformité avec son rapport associé [#4272](https://github.com/MTES-MCT/potentiel/issues/4272) et d'enregistrer une nouvelle attestation avec son rapport [#4264](https://github.com/MTES-MCT/potentiel/issues/4264).
- Affichage des badges dans les listes d'éléments [#4277](https://github.com/MTES-MCT/potentiel/issues/4277).
- Ajout de l'instruction de l'abandon avec le choix PPA [#4260](https://github.com/MTES-MCT/potentiel/issues/4260).
- Amélioration de l'affichage de la pagination [#4280](https://github.com/MTES-MCT/potentiel/issues/4280) et [#4279](https://github.com/MTES-MCT/potentiel/issues/4279).
- Ajout du producteur actuel dans la vue statistiques projets [#4274](https://github.com/MTES-MCT/potentiel/issues/4274).
- Ajout de la possibilité d'importer le renouvellement et la puissance initiale avec DN et mise à jour des exports [#4200](https://github.com/MTES-MCT/potentiel/issues/4200).
- Ajout des coordonnées géodésiques [#4191](https://github.com/MTES-MCT/potentiel/issues/4191).
- Amélioration de l'autocomplétion du nom du producteur à partir du SIRET [#4266](https://github.com/MTES-MCT/potentiel/issues/4266).
- Ajout de l'affichage de l'état PPA lors de la demande d'abandon [#4206](https://github.com/MTES-MCT/potentiel/issues/4206).

### Évolutions techniques
- Réécriture du mécanisme anti CSRF [#4246](https://github.com/MTES-MCT/potentiel/issues/4246).
- Migration vers Biome en remplacement de ESLint et Prettier [#4245](https://github.com/MTES-MCT/potentiel/issues/4245).
- Mise à jour des dépendances Next.js, React et React-DSFR (corrections de sécurité) [#4195](https://github.com/MTES-MCT/potentiel/issues/4195).
- Utilisation du type helper `IdentifiantParameter` aux endroits oubliés [#4214](https://github.com/MTES-MCT/potentiel/issues/4214).
- Suppression des utilisations de la méthode `getContext` du package `@potentiel-applications/request-context` dans le SSR [#4224](https://github.com/MTES-MCT/potentiel/issues/4224).
- Correction du proxy withAuth [#4283](https://github.com/MTES-MCT/potentiel/issues/4283).
- Correction du script `build:dev` [#4273](https://github.com/MTES-MCT/potentiel/issues/4273).
- Correction des oublis liés à la séparation des rôles admin/DGE [#4208](https://github.com/MTES-MCT/potentiel/issues/4208).

### Autres changements
- Amélioration de la documentation et des tests.
- Corrections de typos et d'erreurs d'affichage.
- Suppression de références inutiles dans le code.
- Mise à jour de better-auth 1.6.11 [#4284](https://github.com/MTES-MCT/potentiel/issues/4284).
- Intégration des modifications des releases 3.77, 3.78, 3.79 et 3.80 [#4210](https://github.com/MTES-MCT/potentiel/issues/4210), [#4233](https://github.com/MTES-MCT/potentiel/issues/4233), [#4271](https://github.com/MTES-MCT/potentiel/issues/4271), [#4287](https://github.com/MTES-MCT/potentiel/issues/4287).
- Ne pas mettre les inputs en erreur si ils sont vides [#4286](https://github.com/MTES-MCT/potentiel/issues/4286).
- Ajout PPA aux stats projet [#4285](https://github.com/MTES-MCT/potentiel/issues/4285).
- Correction du problème d'abandon et recours list item keys [#4281](https://github.com/MTES-MCT/potentiel/issues/4281).
- Correction d'un bug lié au producteur projector [#4275](https://github.com/MTES-MCT/potentiel/issues/4275).
- Correction d'un bug lié au remplissage de coordonnées invalides [#4268](https://github.com/MTES-MCT/potentiel/issues/4268).
- Correction d'un bug lié à l'affichage de la bonne page d'erreur [#4265](https://github.com/MTES-MCT/potentiel/issues/4265).
- Correction d'un test flaky [#4259](https://github.com/MTES-MCT/potentiel/issues/4259) et [#4260](https://github.com/MTES-MCT/potentiel/issues/4260).
- Ajout de title manquant et uniformisation [#4228](https://github.com/MTES-MCT/potentiel/issues/4228).
- Fix export lauréat et Ajout des coordonnées à NomEtLocalitéLauréatImportés-V1 [#4232](https://github.com/MTES-MCT/potentiel/issues/4232).
- Correction d'un bug lié à la suppression de la projection raccordement lors d'un abandon [#4187](https://github.com/MTES-MCT/potentiel/issues/4187).
- Suppression du raccordement d'un projet abandonné en cas d'annulation d'un état PPA [#4258](https://github.com/MTES-MCT/potentiel/issues/4258).
- Raccordement modifiable si abandon en cours/accordé pour un projet PPA [#4235](https://github.com/MTES-MCT/potentiel/issues/4235).
- Dissocier l'attestation de conformité du rapport associé pour la transmission (PP) [#4257](https://github.com/MTES-MCT/potentiel/issues/4257).
- Increment max listeners due to message "Possible EventEmitter memory leak detected" [#4256](https://github.com/MTES-MCT/potentiel/issues/4256).
- Retirer les projets avec PPA des projets avec achèvement en attente [#4255](https://github.com/MTES-MCT/potentiel/issues/4255).
- Formatted siren ou siret pour l'affichage [#4254](https://github.com/MTES-MCT/potentiel/issues/4254).
- Fix linter warnings [#4250](https://github.com/MTES-MCT/potentiel/issues/4250).
- Notification modification achèvement [#4252](https://github.com/MTES-MCT/potentiel/issues/4252).
- Redirection post modification évaluation carbone simplifiée par l'administration [#4248](https://github.com/MTES-MCT/potentiel/issues/4248).
- Ignore .vscode folder [#4253](https://github.com/MTES-MCT/potentiel/issues/4253).
- ETQ admin, j'indique une raison lors de la modification de l'achèvement [#4247](https://github.com/MTES-MCT/potentiel/issues/4247).
- ETP PP, si j'ai fait une décla d'abandon avec PPA, l'état PPA est annulé en cas d'annulation [#4244](https://github.com/MTES-MCT/potentiel/issues/4244).
- Ajout du rapport associé optionnel dans le cas de la modification post achèvement (par l'administration) [#4263](https://github.com/MTES-MCT/potentiel/issues/4263).
- Typo producteur [#4270](https://github.com/MTES-MCT/potentiel/issues/4270).
- Remove package lock reference to packages/applications/feature-flag [#4267](https://github.com/MTES-MCT/potentiel/issues/4267).
- Renommer steps attestation conformité -> achèvement réel [#4261](https://github.com/MTES-MCT/potentiel/issues/4261).
- Mise à jour des CSP pour Crisp [#4212](https://github.com/MTES-MCT/potentiel/issues/4212).
- Utilisation de variable d'env sur les différents scripts @potentiel/cli [#4211](https://github.com/MTES-MCT/potentiel/issues/4211).
