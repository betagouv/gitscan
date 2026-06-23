## Changelog : labonnealternance (30 derniers jours, au 2026-06-19)

### Résumé
Les dernières mises à jour de La Bonne Alternance se concentrent sur la correction de bugs, l'amélioration de la gestion des offres d'alternance et l'optimisation de l'expérience utilisateur, notamment sur le formulaire de prise de rendez-vous CFA et la recherche d'offres. Des améliorations techniques ont également été apportées à l'infrastructure et aux outils de développement.

### Évolutions fonctionnelles
- Ajout de la date de début de contrat lors du dépôt d'une offre ([#4768](https://github.com/mission-apprentissage/labonnealternance/issues/4768)).
- Amélioration de la page de prise de rendez-vous CFA avec une meilleure UX ([#4773](https://github.com/mission-apprentissage/labonnealternance/issues/4773)).
- Renommage du libellé du filtre "candidatures spontanées" en "entreprise à contacter" ([#4797](https://github.com/mission-apprentissage/labonnealternance/issues/4797)).
- Application d'un seuil de 80 candidatures aux offres partenaires en "smart apply" ([#4799](https://github.com/mission-apprentissage/labonnealternance/issues/4799)).
- Ajout d'un garde-fou pour éviter un double envoi de données ([#4728](https://github.com/mission-apprentissage/labonnealternance/issues/4728)).
- Correction de l'affichage du titre 1j1s sur la page recruteur ([#4744](https://github.com/mission-apprentissage/labonnealternance/issues/4744)).
- Mise à jour de la liste des CFA blacklistés ([#4689](https://github.com/mission-apprentissage/labonnealternance/issues/4689)).
- Ajout d'un bloc "Mes Aides" ([#589](https://github.com/mission-apprentissage/labonnealternance/issues/589)).
- Amélioration des liens Google sur les pages ville + code postal ([#586](https://github.com/mission-apprentissage/labonnealternance/issues/586)).
- Ajout de la fonctionnalité SEO pour le baromètre T1 2026 de l'alternance ([#4718](https://github.com/mission-apprentissage/labonnealternance/issues/4718)).
- Ajout de hubs SEO/GEO pour l'alternance par métiers, villes et diplômes ([#3222](https://github.com/mission-apprentissage/labonnealternance/issues/3222)).

### Évolutions techniques
- Migration des serveurs lba-production, lba-preview et lba-recette.
- Suppression des sous-modules `.infra/authorizations` et `.infra/inventories`.
- Suppression de Swagger et de ses dépendances de l'API v1.
- Mise à jour de Next.js.
- Amélioration du logging avec Pino et corrélation reqId.
- Standardisation du champ `offer_origin` ([#4789](https://github.com/mission-apprentissage/labonnealternance/issues/4789)).
- Suppression du champ `establishment_id` de `jobs_partners` ([#4767](https://github.com/mission-apprentissage/labonnealternance/issues/4767)).
- Généralisation de la règle binary des PNG dans `.gitattributes` ([#4805](https://github.com/mission-apprentissage/labonnealternance/issues/4805)).
- Correction de l'import Décathlon défaillant ([#4836](https://github.com/mission-apprentissage/labonnealternance/issues/4836)).
- Correction du mapper Kelio pour gérer les `cover_url` nullable et valider le code postal ([#4803](https://github.com/mission-apprentissage/labonnealternance/issues/4803)).
- Correction de la détection des doublons pour éviter les dépassements BSON ([#4839](https://github.com/mission-apprentissage/labonnealternance/issues/4839)).
- Ajout d'un job manuel pour traiter les offres manquantes dans le flux ([#4827](https://github.com/mission-apprentissage/labonnealternance/issues/4827)).
- Correction de la détection des doublons en erreur ([#4833](https://github.com/mission-apprentissage/labonnealternance/issues/4833)).
- Ajout d'une migration pour nettoyer les données ([#4834](https://github.com/mission-apprentissage/labonnealternance/issues/4834)).
- Sécurisation de l'annulation des offres absentes du flux via des sous-jobs dédiés ([#4814](https://github.com/mission-apprentissage/labonnealternance/issues/4814)).
- Suppression de la fonte Marianne Medium inutilisée ([#4762](https://github.com/mission-apprentissage/labonnealternance/issues/4762)).

### Autres changements
- Correction de bugs mineurs et améliorations de la stabilité.
- Mise à jour de la documentation.
- Modernisation des templates d'issues et migration des références Jira vers GitHub Issues ([#4698](https://github.com/mission-apprentissage/labonnealternance/issues/4698)).
- Configuration du merge driver sops pour les fichiers d'environnement chiffrés ([#4736](https://github.com/mission-apprentissage/labonnealternance/issues/4736)).
- Envoi du changelog sur Slack après un déploiement en production ([#4723](https://github.com/mission-apprentissage/labonnealternance/issues/4723)).
- Correction de typos ([#4826](https://github.com/mission-apprentissage/labonnealternance/issues/4826)).
- Suppression de l'entrée générique `BTP CFA` de la liste des CFA bloqués ([#4798](https://github.com/mission-apprentissage/labonnealternance/issues/4798)).
- Correction de la classification des offres CFA ([#4779](https://github.com/mission-apprentissage/labonnealternance/issues/4779)).
- Correction d'un bug de maj de la description de l'offre ([#4804](https://github.com/mission-apprentissage/labonnealternance/issues/4804)).
- Suppression du rate-limit par IP sur les routes consommées via api-apprentissage ([#4810](https://github.com/mission-apprentissage/labonnealternance/issues/4810)).
- Restauration des offres `offres_emploi_lba` désactivées par erreur ([#4813](https://github.com/mission-apprentissage/labonnealternance/issues/4813)).
- Correction de la signature de `onSuccessFunction` ([#4764](https://github.com/mission-apprentissage/labonnealternance/issues/4764)).
- Suppression des scripts Biome redondants et mise à jour de la documentation ([#4761](https://github.com/mission-apprentissage/labonnealternance/issues/4761)).
- Amélioration des notifications Slack MEP et release (Block Kit) ([#4751](https://github.com/mission-apprentissage/labonnealternance/issues/4751)).
- Ajout de `business error expired` pour tous les mappers ([#4740](https://github.com/mission-apprentissage/labonnealternance/issues/4740)).
- Correction du fallback de géolocalisation France Travail sur le chef-lieu du département ([#4709](https://github.com/mission-apprentissage/labonnealternance/issues/4709)).
- Correction du conflit `_id` lors de l'upsert des recruteurs lba ([#4708](https://github.com/mission-apprentissage/labonnealternance/issues/4708)).
- Correction du hardbounce Brevo qui ne retirait pas l'email des recruteurs lba ([#4734](https://github.com/mission-apprentissage/labonnealternance/issues/4734)).
- Correction de la validation des numéros d'issues pour éviter les cascades d'erreurs GraphQL ([#4732](https://github.com/mission-apprentissage/labonnealternance/issues/4732)).
- Mise à jour BAL access ([#4817](https://github.com/mission-apprentissage/labonnealternance/issues/4817)).
- Mappe le niveau de diplôme visé vers la qualification d'emploi France Travail ([#4819](https://github.com/mission-apprentissage/labonnealternance/issues/4819)).
