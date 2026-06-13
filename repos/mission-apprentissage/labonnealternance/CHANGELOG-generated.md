## Changelog : labonnealternance (30 derniers jours, au 2026-06-12)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau du formulaire de candidature et de la recherche d'offres. Des corrections ont également été apportées pour assurer la stabilité et la fiabilité de la plateforme, ainsi que des optimisations techniques pour améliorer les performances et la maintenance.

### Évolutions fonctionnelles
- Amélioration de l'UX du formulaire de prise de rendez-vous avec les CFA, incluant le défilement automatique vers le premier champ d'erreur et un focus sur celui-ci [#4771](https://github.com/mission-apprentissage/labonnealternance/issues/4771).
- Renommage du libellé du filtre "candidatures spontanées" en "entreprise à contacter" pour une meilleure clarté [#4797](https://github.com/mission-apprentissage/labonnealternance/issues/4797).
- Application d'un seuil de 80 candidatures aux offres partenaires utilisant la fonctionnalité "smart apply" [#4799](https://github.com/mission-apprentissage/labonnealternance/issues/4799).
- Correction de l'affichage du titre sur la page recruteur [#4744](https://github.com/mission-apprentissage/labonnealternance/issues/4744).
- Ajout d'un garde-fou pour éviter un double envoi de données [#4728](https://github.com/mission-apprentissage/labonnealternance/issues/4728).
- Amélioration des blocs salaires pour le SEO [#3213](https://github.com/mission-apprentissage/labonnealternance/issues/3213).
- Ajout de 10 nouvelles pages métier pour le SEO, améliorant la visibilité de la plateforme [#2893](https://github.com/mission-apprentissage/labonnealternance/issues/2893).
- Ajout de questions au candidat lors de la création d'une offre [#3172](https://github.com/mission-apprentissage/labonnealternance/issues/3172).
- Mise à jour de la liste des CFA blacklistées [#4689](https://github.com/mission-apprentissage/labonnealternance/issues/4689).
- Modification des CTA (boutons d'appel à l'action) de dépôt d'offre [#3136](https://github.com/mission-apprentissage/labonnealternance/issues/3136).
- Adaptation des boutons "je postule" en fonction des partenaires [#3175](https://github.com/mission-apprentissage/labonnealternance/issues/3175).
- Correction de l'affichage des marges sur la page Handimatch [#3176](https://github.com/mission-apprentissage/labonnealternance/issues/3176).

### Évolutions techniques
- Mise à jour de Next.js [#4691](https://github.com/mission-apprentissage/labonnealternance/issues/4691).
- Unification du logging sur Pino avec corrélation `reqId` et enrichissement des logs HTTP [#4800](https://github.com/mission-apprentissage/labonnealternance/issues/4800).
- Suppression de Swagger et de ses dépendances de l'API v1 [#4717](https://github.com/mission-apprentissage/labonnealternance/issues/4717).
- Suppression du champ `establishment_id` de la table `jobs_partners` [#4767](https://github.com/mission-apprentissage/labonnealternance/issues/4767).
- Suppression de la fonte Marianne Medium inutilisée [#4762](https://github.com/mission-apprentissage/labonnealternance/issues/4762).
- Suppression de la collection `eligible_trainings_for_appointments_histories` et refactoring de la tâche de nettoyage [#4725](https://github.com/mission-apprentissage/labonnealternance/issues/4725).
- Modernisation des templates d'issues et migration des références Jira vers GitHub Issues [#4698](https://github.com/mission-apprentissage/labonnealternance/issues/4698).
- Ajout d'un fichier `llms.txt` à la racine du site pour la gestion des modèles de langage [#4765](https://github.com/mission-apprentissage/labonnealternance/issues/4765).

### Autres changements
- Correction de la cartographie du niveau de diplôme visé vers la qualification d'emploi France Travail [#4819](https://github.com/mission-apprentissage/labonnealternance/issues/4819).
- Sécurisation de l'annulation des offres absentes du flux via des sous-jobs dédiés [#4814](https://github.com/mission-apprentissage/labonnealternance/issues/4814).
- Mise à jour de l'accès BAL [#4817](https://github.com/mission-apprentissage/labonnealternance/issues/4817).
- Correction d'un bug de mise à jour de la description d'une offre [#4804](https://github.com/mission-apprentissage/labonnealternance/issues/4804).
- Suppression du rate-limit par IP sur les routes consommées via `api-apprentissage` [#4810](https://github.com/mission-apprentissage/labonnealternance/issues/4810).
- Restauration des offres `offres_emploi_lba` désactivées par erreur [#4813](https://github.com/mission-apprentissage/labonnealternance/issues/4813).
- Ajout d'OPCO EP à la whitelist pour éviter la classification erronée en offre CFA [#4784](https://github.com/mission-apprentissage/labonnealternance/issues/4784).
- Correction de la classification CFA: suppression du passage de l'ID [#4779](https://github.com/mission-apprentissage/labonnealternance/issues/4779).
- Correction d'un problème de graisse de la police Marianne [#4720](https://github.com/mission-apprentissage/labonnealternance/issues/4720).
- Envoi du changelog sur Slack après un déploiement en production [#4723](https://github.com/mission-apprentissage/labonnealternance/issues/4723).
- Correction de l'encodage des entités HTML dans `offer_title` et `workplace_name` [#3174](https://github.com/mission-apprentissage/labonnealternance/issues/3174).
- Correction du scrolling après fermeture de la modale de désinscription [#3179](https://github.com/mission-apprentissage/labonnealternance/issues/3179).
- Correction du fallback de géolocalisation France Travail sur le chef-lieu du département [#4709](https://github.com/mission-apprentissage/labonnealternance/issues/4709).
- Configuration du merge driver sops pour les fichiers d'environnement chiffrés [#4736](https://github.com/mission-apprentissage/labonnealternance/issues/4736).
- Correction du hardbounce Brevo qui ne retirait pas l'email des recruteurs LBA [#4734](https://github.com/mission-apprentissage/labonnealternance/issues/4734).
- Correction de la validation des numéros d'issues pour éviter les cascades d'erreurs GraphQL [#4732](https://github.com/mission-apprentissage/labonnealternance/issues/4732).
- Correction du conflit `_id` lors de l'upsert des recruteurs LBA [#4708](https://github.com/mission-apprentissage/labonnealternance/issues/4708).
- Correction de la signature de `onSuccessFunction` [#4764](https://github.com/mission-apprentissage/labonnealternance/issues/4764).
- Suppression des scripts Biome redondants et mise à jour de la documentation [#4761](https://github.com/mission-apprentissage/labonnealternance/issues/4761).
- Amélioration des notifications Slack MEP et release (Block Kit) [#4751](https://github.com/mission-apprentissage/labonnealternance/issues/4751).
- Ajout d'un business error `expired` pour tous les mappers [#4740](https://github.com/mission-apprentissage/labonnealternance/issues/4740).
