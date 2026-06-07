## Changelog : labonnealternance (30 derniers jours, au 2026-06-05)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment en corrigeant des bugs et en ajoutant des fonctionnalités pour faciliter la gestion des offres et des candidatures. Des optimisations techniques ont également été apportées, notamment concernant la configuration, la gestion des erreurs et la modernisation des outils de développement.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'affichage correct du titre sur la page recruteur [#4744](https://github.com/mission-apprentissage/labonnealternance/issues/4744).
- Amélioration de la gestion des erreurs lors de la création d'offres, avec un affichage plus clair des erreurs de mutation pour faciliter le diagnostic [#4727](https://github.com/mission-apprentissage/labonnealternance/issues/4727).
- Correction d'un problème de graisse de police sur la page Marianne [#4720](https://github.com/mission-apprentissage/labonnealternance/issues/4720).
- Ajout de questions au candidat lors de la création d'une offre [#3172](https://github.com/mission-apprentissage/labonnealternance/issues/3172).
- Mise à jour de la liste des CFA en "blacklist" [#4689](https://github.com/mission-apprentissage/labonnealternance/issues/4689).
- Mise à jour du bloc salaire [#3213](https://github.com/mission-apprentissage/labonnealternance/issues/3213).
- Ajout de 10 nouvelles pages métier SEO pour améliorer le référencement [#2893](https://github.com/mission-apprentissage/labonnealternance/issues/2893).
- Modification des CTA (Call To Action) sur la page de dépôt d'offre [#3136](https://github.com/mission-apprentissage/labonnealternance/issues/3136).
- Adaptation des CTA "je postule" en fonction des partenaires [#3175](https://github.com/mission-apprentissage/labonnealternance/issues/3175).
- Correction de l'encodage des caractères spéciaux dans les titres d'offres et les noms des lieux de travail [#3174](https://github.com/mission-apprentissage/labonnealternance/issues/3174).
- Correction d'un problème de scrolling après la fermeture de la modale de désinscription [#3179](https://github.com/mission-apprentissage/labonnealternance/issues/3179).
- Ajout d'un garde-fou pour éviter un double envoi de données [#4728](https://github.com/mission-apprentissage/labonnealternance/issues/4728).

### Évolutions techniques
- Mise à jour de Next.js [#4691](https://github.com/mission-apprentissage/labonnealternance/issues/4691).
- Suppression de Swagger et de ses dépendances de l'API v1 [#4717](https://github.com/mission-apprentissage/labonnealternance/issues/4717).
- Configuration du merge driver SOPS pour les fichiers d'environnement chiffrés [#4736](https://github.com/mission-apprentissage/labonnealternance/issues/4736).
- Amélioration des notifications Slack pour les MEP (Mise en Production) et les releases (Block Kit) [#4751](https://github.com/mission-apprentissage/labonnealternance/issues/4751).
- Suppression de la collection `eligible_trainings_for_appointments_histories` et refactorisation de la tâche de nettoyage associée [#4725](https://github.com/mission-apprentissage/labonnealternance/issues/4725).
- Ajout d'un fichier `llms.txt` à la racine du site [#4765](https://github.com/mission-apprentissage/labonnealternance/issues/4765).
- Suppression d'une fonte Marianne Medium inutilisée [#4762](https://github.com/mission-apprentissage/labonnealternance/issues/4762).
- Suppression de scripts Biome redondants et mise à jour de la documentation [#4761](https://github.com/mission-apprentissage/labonnealternance/issues/4761).
- Correction de la signature de `onSuccessFunction` [#4764](https://github.com/mission-apprentissage/labonnealternance/issues/4764).
- Correction pour s'assurer que `onSuccessFunction` est bien une fonction [#4763](https://github.com/mission-apprentissage/labonnealternance/issues/4763).
- Ajout d'un "business error expired" pour tous les mappers [#4740](https://github.com/mission-apprentissage/labonnealternance/issues/4740).
- Modernisation des templates d'issues et migration des références Jira vers GitHub Issues [#4698](https://github.com/mission-apprentissage/labonnealternance/issues/4698).
- Correction d'un conflit `_id` lors de l'upsert des recruteurs LBA [#4708](https://github.com/mission-apprentissage/labonnealternance/issues/4708).
- Fallback de la géolocalisation France Travail sur le chef-lieu du département [#4709](https://github.com/mission-apprentissage/labonnealternance/issues/4709).
- Suppression de la route `/v1/application` et des schémas orphelins [#4025](https://github.com/mission-apprentissage/labonnealternance/issues/4025).
- Activation du heartbeat timer et des heatmaps Matomo [#4011](https://github.com/mission-apprentissage/labonnealternance/issues/4011).
- Correction de l'utilisation du rôle utilisateur dans l'admin [#3961](https://github.com/mission-apprentissage/labonnealternance/issues/3961).
- Ajout d'un export CSV zippé double flux vers France Travail [#3977](https://github.com/mission-apprentissage/labonnealternance/issues/3977).
- Réduction du bruit Sentry sur les erreurs externes [#2947](https://github.com/mission-apprentissage/labonnealternance/issues/2947).
- Correction d'un oubli de report de données CFA [#2887](https://github.com/mission-apprentissage/labonnealternance/issues/2887).

### Autres changements
- Ajout d'assets pour la migration des issues (plusieurs commits).
- Mise à jour du SMIC au 1er juin 2026 dans le simulateur alternant [#4724](https://github.com/mission-apprentissage/labonnealternance/issues/4724).
- Ajout de changelog sur Slack après un déploiement en production [#4723](https://github.com/mission-apprentissage/labonnealternance/issues/4723).
- Correction d'un problème de hardbounce Brevo qui empêchait la suppression des emails des recruteurs LBA [#4734](https://github.com/mission-apprentissage/labonnealternance/issues/4734).
- Validation des numéros d'issues pour éviter les cascades d'erreurs GraphQL [#4732](https://github.com/mission-apprentissage/labonnealternance/issues/4732).
