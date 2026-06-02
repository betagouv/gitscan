## Changelog : potentiel (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment autour de la gestion des abandons de projets, des signalements PPA et de l'importation de données. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme. L'ajout de nouvelles fonctionnalités comme l'autocomplétion du producteur et l'affichage des coordonnées géodésiques enrichissent les capacités de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité pour l'administration d'annuler un signalement PPA. [#4204](https://github.com/MTES-MCT/potentiel/issues/4204)
- Implémentation de la demande de mainlevée suite à un abandon de projet. [#4209](https://github.com/MTES-MCT/potentiel/issues/4209)
- Ajout de l'autocomplétion du nom du producteur à partir du SIRET. [#4266](https://github.com/MTES-MCT/potentiel/issues/4266)
- Affichage des coordonnées géodésiques. [#4191](https://github.com/MTES-MCT/potentiel/issues/4191)
- Possibilité pour l'administration de modifier l'attestation de conformité avec son rapport associé. [#4272](https://github.com/MTES-MCT/potentiel/issues/4272)
- Ajout de la description de l'appel à projets/famille dans la section Cahier des Charges. [#4282](https://github.com/MTES-MCT/potentiel/issues/4282)
- Affichage de l'identifiant projet. [#4269](https://github.com/MTES-MCT/potentiel/issues/4269)
- Amélioration de l'affichage des badges dans les listes d'items. [#4277](https://github.com/MTES-MCT/potentiel/issues/4277)
- Ajout d'une instruction pour l'abandon avec le choix PPA. [#4260](https://github.com/MTES-MCT/potentiel/issues/4260)
- Gestion des tâches porteur dans un contexte d'abandon. [#4262](https://github.com/MTES-MCT/potentiel/issues/4262)
- Importation des données fournisseur lors de la candidature via DN et mise à jour des exports. [#4200](https://github.com/MTES-MCT/potentiel/issues/4200)
- Possibilité de signaler un PPA (DREAL/DGEC). [#4192](https://github.com/MTES-MCT/potentiel/issues/4192)
- Amélioration de l'affichage et de la gestion des erreurs lors du remplissage des coordonnées. [#4268](https://github.com/MTES-MCT/potentiel/issues/4268)

### Évolutions techniques
- Mise à jour des dépendances Next.js, React et React-DSFR pour corriger des failles de sécurité. [#4195](https://github.com/MTES-MCT/potentiel/issues/4195)
- Remplacement de ESLint et Prettier par Biome pour l'analyse et le formatage du code. [#4245](https://github.com/MTES-MCT/potentiel/issues/4245)
- Réécriture du mécanisme anti-CSRF. [#4246](https://github.com/MTES-MCT/potentiel/issues/4246)
- Suppression des schémas et extensions PostGIS inutiles. [#4294](https://github.com/MTES-MCT/potentiel/issues/4294)
- Utilisation d'un helper server-only pour gérer les feature flags côté SSR. [#4218](https://github.com/MTES-MCT/potentiel/issues/4218)
- Correction d'un problème de fuite mémoire potentielle dans les notifications. [#4237](https://github.com/MTES-MCT/potentiel/issues/4237)
- Amélioration de la gestion des erreurs de droits sur les redirections. [#4265](https://github.com/MTES-MCT/potentiel/issues/4265)

### Autres changements
- Amélioration des tests GRD (requêtes et ajout d'un test). [#4201](https://github.com/MTES-MCT/potentiel/issues/4201)
- Correction de divers bugs et améliorations mineures suite aux tests et retours utilisateurs. [#4273](https://github.com/MTES-MCT/potentiel/issues/4273), [#4283](https://github.com/MTES-MCT/potentiel/issues/4283), [#4290](https://github.com/MTES-MCT/potentiel/issues/4290)
- Correction du script `build:dev`. [#4273](https://github.com/MTES-MCT/potentiel/issues/4273)
- Ajout de titres aux pages pour améliorer l'accessibilité. [#4205](https://github.com/MTES-MCT/potentiel/issues/4205)
- Suppression de la référence au fichier `package-lock.json` dans le package `feature-flag`. [#4267](https://github.com/MTES-MCT/potentiel/issues/4267)
- Suppression du dossier `.vscode` du dépôt. [#4253](https://github.com/MTES-MCT/potentiel/issues/4253)
- Correction de typos et améliorations de la formulation. [#4270](https://github.com/MTES-MCT/potentiel/issues/4270)
- Mise à jour de Better Auth à la version 1.6.11. [#4284](https://github.com/MTES-MCT/potentiel/issues/4284)
- Intégration des modifications de la release 3.80. [#4287](https://github.com/MTES-MCT/potentiel/issues/4287), [#4292](https://github.com/MTES-MCT/potentiel/issues/4292), [#4301](https://github.com/MTES-MCT/potentiel/issues/4301)
- Intégration des modifications de la release 3.79. [#4278](https://github.com/MTES-MCT/potentiel/issues/4278), [#4271](https://github.com/MTES-MCT/potentiel/issues/4271)
- Intégration des modifications de la release 3.78. [#4233](https://github.com/MTES-MCT/potentiel/issues/4233), [#4227](https://github.com/MTES-MCT/potentiel/issues/4227)
