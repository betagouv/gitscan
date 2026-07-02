## Changelog : labonnealternance (30 derniers jours, au 2026-07-01)

### Résumé
Ce mois-ci, les évolutions de la plateforme se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur les pages d'accueil et les formulaires, ainsi que sur l'intégration et le traitement des offres d'alternance provenant de France Travail et d'autres partenaires. Des corrections de bugs et des optimisations techniques ont également été apportées pour assurer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Page d'accueil et Landing Pages :** Mise à jour des visuels et des contenus pour les candidats, les recruteurs et les CFA [#4824](https://github.com/mission-apprentissage/labonnealternance/issues/4824).
- **Intégration France Travail :** Amélioration de l'export des offres d'alternance confiées par France Travail, avec gestion des filtres d'expiration, de plafond et des correspondants [#4882](https://github.com/mission-apprentissage/labonnealternance/issues/4882).
- **GEIQ :** Affichage des informations emploi et formation pour les offres proposées par les GEIQ [#4801](https://github.com/mission-apprentissage/labonnealternance/issues/4801).
- **CFA :** Amélioration de l'UX du formulaire de prise de rendez-vous avec les CFA [#4773](https://github.com/mission-apprentissage/labonnealternance/issues/4773).
- **Candidatures :** Ajout d'un focus sur le premier champ en erreur lors de la soumission du formulaire de candidature [#4771](https://github.com/mission-apprentissage/labonnealternance/issues/4771).
- **Dépôt d'offre :** Ajout de la possibilité de spécifier la date de début de contrat lors du dépôt d'une offre [#4768](https://github.com/mission-apprentissage/labonnealternance/issues/4768).
- **Filtres :** Renommage du filtre "candidatures spontanées" en "entreprise à contacter" [#4797](https://github.com/mission-apprentissage/labonnealternance/issues/4797).
- **Intention Recruteurs :** Refonte de l'interface utilisateur pour la gestion des intentions des recruteurs [#4866](https://github.com/mission-apprentissage/labonnealternance/issues/4866).
- **Niveaux d'étude :** Mise à jour du wording des niveaux d'étude [#4869](https://github.com/mission-apprentissage/labonnealternance/issues/4869).

### Évolutions techniques
- **Migration Serveurs :** Migration des serveurs lba-production, lba-preview et lba-recette [#4837](https://github.com/mission-apprentissage/labonnealternance/issues/4837), [#4829](https://github.com/mission-apprentissage/labonnealternance/issues/4829), [#4828](https://github.com/mission-apprentissage/labonnealternance/issues/4828).
- **Logging :** Unification du logging avec Pino, incluant la corrélation reqId et l'enrichissement des logs HTTP [#4800](https://github.com/mission-apprentissage/labonnealternance/issues/4800).
- **Sentry :** Désactivation temporaire de Sentry côté serveur pendant la migration [#4871](https://github.com/mission-apprentissage/labonnealternance/issues/4871).
- **Jobs :** Déplacement de `processMissingRomeAndImportToJobPartners` vers un job manuel [#4827](https://github.com/mission-apprentissage/labonnealternance/issues/4827).
- **Architecture :** Suppression des sous-modules `.infra/authorizations` et `.infra/inventories` [#4825](https://github.com/mission-apprentissage/labonnealternance/issues/4825).
- **Configuration :** Ajout de Maazi à la white list [#4863](https://github.com/mission-apprentissage/labonnealternance/issues/4863).
- **Standardisation :** Standardisation du champ `offer_origin` [#4789](https://github.com/mission-apprentissage/labonnealternance/issues/4789).

### Autres changements
- **Documentation :** Mise à jour du texte de la page Espace développeur [#4873](https://github.com/mission-apprentissage/labonnealternance/issues/4873).
- **Git Attributes :** Généralisation de la règle binary des PNG dans `.gitattributes` [#4805](https://github.com/mission-apprentissage/labonnealternance/issues/4805).
- **Epic :** Renommage de l'epic en epic.yml et création d'un template pour les epics GitHub [#4886](https://github.com/mission-apprentissage/labonnealternance/issues/4886), [#4878](https://github.com/mission-apprentissage/labonnealternance/issues/4878).
- **SEO :** Ajout de la génération d'un fichier `llms.txt` à la racine du site [#4765](https://github.com/mission-apprentissage/labonnealternance/issues/4765) et implémentation de hubs SEO/GEO pour l'alternance [#3222](https://github.com/mission-apprentissage/labonnealternance/issues/3222).
- **Correction :** Correction d'un problème de calibration du passage des headers en sticky [#4855](https://github.com/mission-apprentissage/labonnealternance/issues/4855).
- **Correction :** Correction d'une erreur d'hydratation React sur les pages ville [#4884](https://github.com/mission-apprentissage/labonnealternance/issues/4884).
- **Correction :** Correction de l'import Décathlon défaillant [#4836](https://github.com/mission-apprentissage/labonnealternance/issues/4836).
- **Correction :** Correction d'une erreur de détection de doublons [#4833](https://github.com/mission-apprentissage/labonnealternance/issues/4833).
- **Correction :** Correction du mapper Kelio pour gérer les URLs de couverture nullables et valider le code postal [#4803](https://github.com/mission-apprentissage/labonnealternance/issues/4803).
- **Correction :** Correction d'un bug de mise à jour de la description de l'offre [#4804](https://github.com/mission-apprentissage/labonnealternance/issues/4804).
- **Correction :** Correction de la classification erronée des offres CFA [#4784](https://github.com/mission-apprentissage/labonnealternance/issues/4784).
- **Correction :** Correction d'un bug d'affichage du titre 1j1s sur la page recruteur [#4744](https://github.com/mission-apprentissage/labonnealternance/issues/4744).
- **Correction :** Correction d'un problème lié à l'annulation des offres absentes du flux [#4814](https://github.com/mission-apprentissage/labonnealternance/issues/4814).
- **Correction :** Correction d'un problème lié à l'envoi des emails de rendez-vous [#4826](https://github.com/mission-apprentissage/labonnealternance/issues/4826).
