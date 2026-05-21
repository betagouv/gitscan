## Changelog : potentiel (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur pour l'administration, notamment en ajoutant des fonctionnalités de gestion des signalements PPA, d'annulation d'abandons et de modification des informations d'entreprises. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme. Une mise à jour des dépendances a été effectuée pour renforcer la sécurité.

### Évolutions fonctionnelles
- L'administration peut désormais annuler un signalement PPA. [#4204](https://github.com/MTES-MCT/potentiel/issues/4204)
- Possibilité pour l'administration de modifier l'achèvement d'un dossier avec indication d'une raison. [#4247](https://github.com/MTES-MCT/potentiel/issues/4247)
- En cas d'annulation d'une déclaration d'abandon avec PPA, l'état PPA est automatiquement annulé. [#4244](https://github.com/MTES-MCT/potentiel/issues/4244)
- Ajout de la possibilité de déclarer un état PPA lors d'une demande d'abandon. [#4206](https://github.com/MTES-MCT/potentiel/issues/4206)
- Modification du SIRET est désormais possible. [#4225](https://github.com/MTES-MCT/potentiel/issues/4225)
- Ajout des coordonnées géodésiques. [#4191](https://github.com/MTES-MCT/potentiel/issues/4191)
- Intégration de l'import des données fournisseur via DN lors de la candidature. [#4207](https://github.com/MTES-MCT/potentiel/issues/4207)
- Possibilité de demander une mainlevée suite à un abandon. [#4209](https://github.com/MTES-MCT/potentiel/issues/4209)
- Ajout du SIREN / SIRET. [#4193](https://github.com/MTES-MCT/potentiel/issues/4193)
- Amélioration de l'affichage du SIREN/SIRET. [#4254](https://github.com/MTES-MCT/potentiel/issues/4254)
- Notification lors de la modification de l'achèvement d'un dossier. [#4252](https://github.com/MTES-MCT/potentiel/issues/4252)

### Évolutions techniques
- Remplacement de ESLint et Prettier par Biome pour le linting et le formattage du code. [#4245](https://github.com/MTES-MCT/potentiel/issues/4245)
- Refonte du mécanisme anti-CSRF pour une meilleure sécurité. [#4246](https://github.com/MTES-MCT/potentiel/issues/4246)
- Mise à jour de Next.js. [#4242](https://github.com/MTES-MCT/potentiel/issues/4242)
- Mise à jour des actions CI/CD. [#4241](https://github.com/MTES-MCT/potentiel/issues/4241)
- Correction de problèmes liés à la gestion des événements PostgreSQL (payload trop conséquent). [#4237](https://github.com/MTES-MCT/potentiel/issues/4237)
- Suppression des utilisations de `getContext` dans le SSR. [#4224](https://github.com/MTES-MCT/potentiel/issues/4224)
- Ajout d'un helper server only pour gérer les feature flags côté SSR. [#4218](https://github.com/MTES-MCT/potentiel/issues/4218)
- Mise à jour des dépendances Next, React et React-DSFR (corrections de sécurité). [#4195](https://github.com/MTES-MCT/potentiel/issues/4195)
- Ajout de la variable d'environnement `AWS_REGION` pour le s3Schema de la partie CLI. [#4188](https://github.com/MTES-MCT/potentiel/issues/4188)

### Autres changements
- Correction de redirections d'emails. [#4239](https://github.com/MTES-MCT/potentiel/issues/4239)
- Redirection simplifiée après modification d'une évaluation carbone. [#4248](https://github.com/MTES-MCT/potentiel/issues/4248)
- Suppression du dossier `.vscode` du dépôt. [#4253](https://github.com/MTES-MCT/potentiel/issues/4253)
- Correction d'un test flaky. [#4240](https://github.com/MTES-MCT/potentiel/issues/4240)
- Ajout de la raison dans les items d'historique. [#4238](https://github.com/MTES-MCT/potentiel/issues/4238)
- Intégration des modifications de la release 3.78 et 3.77. [#4233](https://github.com/MTES-MCT/potentiel/issues/4233), [#4210](https://github.com/MTES-MCT/potentiel/issues/4210)
- Amélioration des titres des pages pour l'accessibilité. [#4205](https://github.com/MTES-MCT/potentiel/issues/4205)
- Mise à jour des CSP pour Crisp. [#4212](https://github.com/MTES-MCT/potentiel/issues/4212)
- Vérifications des variables d'environnement sur les scripts @potentiel/cli. [#4211](https://github.com/MTES-MCT/potentiel/issues/4211)
- Correction de bugs et améliorations diverses.
