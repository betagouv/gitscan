## Changelog : labonnealternance (30 derniers jours, au 2026-08-01)

### Résumé
Les dernières mises à jour de la plateforme La Bonne Alternance se concentrent sur l'amélioration de la recherche d'alternances, notamment avec l'introduction d'un nouveau moteur de recherche basé sur MongoDB. Des corrections de sécurité importantes ont également été apportées, ainsi que des améliorations de l'expérience utilisateur et du SEO.

### Évolutions fonctionnelles
- Amélioration du moteur de recherche avec une nouvelle version basée sur MongoDB ([#4785](https://github.com/mission-apprentissage/labonnealternance/issues/4785)).
- Incitation aux candidatures spontanées avec une relance des candidats inactifs 7 jours après leur inscription ([#4976](https://github.com/mission-apprentissage/labonnealternance/issues/4976)).
- Amélioration du SEO avec des métas dynamiques pour les pages de recherche et optimisation de la page salaire ([#5040](https://github.com/mission-apprentissage/labonnealternance/issues/5040), [#5050](https://github.com/mission-apprentissage/labonnealternance/issues/5050)).
- Ajout d'un écran d'administration pour les entreprises de type CFA ([#4974](https://github.com/mission-apprentissage/labonnealternance/issues/4974)).
- Ajout d'un nouvel article au guide CFA ([#5026](https://github.com/mission-apprentissage/labonnealternance/issues/5026)).
- Refonte de la page d'erreur globale et affichage d'erreur spécifique pour la page RDVA ([#4781](https://github.com/mission-apprentissage/labonnealternance/issues/4781)).
- Possibilité de mentionner des membres de l'équipe dans les notifications Slack ([#4967](https://github.com/mission-apprentissage/labonnealternance/issues/4967)).
- Correction de l'envoi des emails de confirmation de création d'offre ([#4815](https://github.com/mission-apprentissage/labonnealternance/issues/4815)).
- Amélioration du nurturing des entreprises dormantes à l'anniversaire du dépôt d'offre ([#4980](https://github.com/mission-apprentissage/labonnealternance/issues/4980)).
- Blocage des tentatives de réinscription des recruteurs DENIED ([#4885](https://github.com/mission-apprentissage/labonnealternance/issues/4885)).
- Ajout d'un bloc "Mes Aides" ([#590](https://github.com/mission-apprentissage/labonnealternance/issues/590)).

### Évolutions techniques
- Correction de 2 CVE critiques dans les dépendances (vitest, tar) ([#5055](https://github.com/mission-apprentissage/labonnealternance/issues/5055)).
- Mise à jour de Metabase ([#5031](https://github.com/mission-apprentissage/labonnealternance/issues/5031)).
- Amélioration de la gestion des secrets avec une rotation du secret principal SOPS ([#4939](https://github.com/mission-apprentissage/labonnealternance/issues/4939)).
- Amélioration de l'utilisation de Sentry pour le suivi des erreurs ([#4937](https://github.com/mission-apprentissage/labonnealternance/issues/4937)).
- Ajout de la dimension `search_engine=production` aux événements Matomo du moteur de recherche legacy ([#5065](https://github.com/mission-apprentissage/labonnealternance/issues/5065)).
- Pilotage des robots d'indexation et ajout de balises canonical via l'API metadata de Next.js ([#5044](https://github.com/mission-apprentissage/labonnealternance/issues/5044)).
- Amélioration de la performance et de la fiabilité du moteur de recherche (correction de bugs et optimisation des requêtes).

### Autres changements
- Mise à jour du contenu de 2 pages du guide alternant ([#4988](https://github.com/mission-apprentissage/labonnealternance/issues/4988)).
- Mise à jour de la liste des CFA blacklistés ([#5030](https://github.com/mission-apprentissage/labonnealternance/issues/5030)).
- Correction de la déduplication Hellowork avec l'opérateur `substrCP` ([#4925](https://github.com/mission-apprentissage/labonnealternance/issues/4925)).
- Diverses corrections de bugs et améliorations de l'interface utilisateur.
- Correction de l'ouverture en nouvel onglet sur le lien de sortie du moteur beta ([#5064](https://github.com/mission-apprentissage/labonnealternance/issues/5064)).
- Emission de l'événement `new_search_optout` avant la navigation depuis le nouveau moteur de recherche ([#5063](https://github.com/mission-apprentissage/labonnealternance/issues/5063)).
- Force la lecture des agrégations `$search` sur le primaire ([#5062](https://github.com/mission-apprentissage/labonnealternance/issues/5062)).
- Relègue les candidatures spontanées en fin du tri par date de début de contrat ([#5060](https://github.com/mission-apprentissage/labonnealternance/issues/5060)).
- Correction des correctifs moteur de recherche ([#5059](https://github.com/mission-apprentissage/labonnealternance/issues/5059)).
- Restreint la validation des noms aux schémas de saisie ([#5058](https://github.com/mission-apprentissage/labonnealternance/issues/5058)).
- Active le bouton de recherche mobile à la modification des filtres ([#5057](https://github.com/mission-apprentissage/labonnealternance/issues/5057)).
- Bulkwrite de la passe cache keywords et export brevo limité à la production ([#5054](https://github.com/mission-apprentissage/labonnealternance/issues/5054)).
- Expose la date de dernière action et de dernière offre dans l'export Brevo ([#4978](https://github.com/mission-apprentissage/labonnealternance/issues/4978)).
- Correction des libellés des actions de partage d'offre ([#4943](https://github.com/mission-apprentissage/labonnealternance/issues/4943)).
- Masque les liens externes et corrige les délimitations pour les comptes cfa ([#4926](https://github.com/mission-apprentissage/labonnealternance/issues/4926)).
- Masque la nav LBA en mode widget et fluidifie l'animation du header au scroll ([#4891](https://github.com/mission-apprentissage/labonnealternance/issues/4891)).
- Correction du point de montage du volume metabase pour preview ([#4981](https://github.com/mission-apprentissage/labonnealternance/issues/4981)).
- Correction de l'écran récap intention envoyée ([#4935](https://github.com/mission-apprentissage/labonnealternance/issues/4935)).
- Correction de l'utilisation de Sentry (type options et format extra) ([#4937](https://github.com/mission-apprentissage/labonnealternance/issues/4937)).
- Correction de l'exclusion des offres GEIQ du rendu PartnerJobDetail ([#4930](https://github.com/mission-apprentissage/labonnealternance/issues/4930)).
- Correction de l'alignement des tests hellowork sur le caller hellowork-api ([#4927](https://github.com/mission-apprentissage/labonnealternance/issues/4927)).
- Correction du caller name hellowork api ([#4918](https://github.com/mission-apprentissage/labonnealternance/issues/4918)).
- Ajout de la possibilité de bloquer la réactivation d'un compte ayant déjà un accès actif sur une autre organisation ([#4890](https://github.com/mission-apprentissage/labonnealternance/issues/4890)).
