## Changelog : labonnealternance (30 derniers jours, au 2026-07-17)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'expérience utilisateur, notamment sur la gestion des offres d'apprentissage et des comptes utilisateurs. Des corrections ont été apportées pour améliorer la fiabilité et la performance de la plateforme, ainsi que des optimisations de sécurité. Des mises à jour de l'interface utilisateur ont également été déployées pour une meilleure expérience globale.

### Évolutions fonctionnelles
- Amélioration de l'affichage des erreurs sur la page RDVA et refonte de la page d'erreur globale. [#4916](https://github.com/mission-apprentissage/labonnealternance/issues/4916)
- Activation de l'export des offres d'emploi avec expérience. [#4920](https://github.com/mission-apprentissage/labonnealternance/issues/4920)
- Blocage de la réactivation d'un compte utilisateur ayant déjà un accès actif sur une autre organisation. [#4890](https://github.com/mission-apprentissage/labonnealternance/issues/4890)
- Standardisation des modales pour une expérience utilisateur plus cohérente. [#4851](https://github.com/mission-apprentissage/labonnealternance/issues/4851)
- Ajout de la possibilité de spécifier la date de début de contrat lors du dépôt d'une offre. [#4768](https://github.com/mission-apprentissage/labonnealternance/issues/4768)
- Mise à jour des visuels et contenus de la page d'accueil candidat, de la landing page recruteurs, de la landing page CFA et de la page À propos. [#4824](https://github.com/mission-apprentissage/labonnealternance/issues/4824)
- Amélioration de l'affichage des informations emploi et formation pour les offres de GEIQ. [#4801](https://github.com/mission-apprentissage/labonnealternance/issues/4801)
- Ajout de Maazi à la liste blanche. [#4863](https://github.com/mission-apprentissage/labonnealternance/issues/4863)
- Ajout d'une entrée générique `BTP CFA` à la liste des CFA bloqués. [#4798](https://github.com/mission-apprentissage/labonnealternance/issues/4798)

### Évolutions techniques
- Rotation du secret principal SOPS pour renforcer la sécurité. [#4939](https://github.com/mission-apprentissage/labonnealternance/issues/4939)
- Correction de l'utilisation de Sentry (type options et format extra) pour une meilleure surveillance des erreurs. [#4937](https://github.com/mission-apprentissage/labonnealternance/issues/4937)
- Migration du serveur de production LBA. [#4837](https://github.com/mission-apprentissage/labonnealternance/issues/4837)
- Correction de l'hydratation React sur les pages ville. [#4884](https://github.com/mission-apprentissage/labonnealternance/issues/4884)
- Correction de la déduplication Hellowork avec l'opérateur `substrCP`. [#4925](https://github.com/mission-apprentissage/labonnealternance/issues/4925)
- Alignement des tests Hellowork sur le caller hellowork-api et régénération des tests. [#4927](https://github.com/mission-apprentissage/labonnealternance/issues/4927)

### Autres changements
- Correction du point de montage du volume Metabase pour la preview. [#4981](https://github.com/mission-apprentissage/labonnealternance/issues/4981)
- Clarification des libellés des actions de partage d'offre. [#4943](https://github.com/mission-apprentissage/labonnealternance/issues/4943)
- Correction de l'écran récapitulatif de l'intention envoyée. [#4935](https://github.com/mission-apprentissage/labonnealternance/issues/4935)
- Masquage des liens externes et correction des délimitations pour les comptes CFA. [#4926](https://github.com/mission-apprentissage/labonnealternance/issues/4926)
- Exclusion des offres GEIQ du rendu PartnerJobDetail. [#4930](https://github.com/mission-apprentissage/labonnealternance/issues/4930)
- Masquage de la navigation LBA en mode widget et fluidification de l'animation du header au scroll. [#4891](https://github.com/mission-apprentissage/labonnealternance/issues/4891)
- Recherche ciblée des entreprises de l'algorithme dans l'admin. [#4875](https://github.com/mission-apprentissage/labonnealternance/issues/4875)
- Réactivation de Sentry après migration du serveur. [#4892](https://github.com/mission-apprentissage/labonnealternance/issues/4892)
- Renommage de `epic` en `epic.yml`. [#4886](https://github.com/mission-apprentissage/labonnealternance/issues/4886)
- Correction du mapper Kelio pour gérer les `cover_url` nullables et valider le code postal. [#4803](https://github.com/mission-apprentissage/labonnealternance/issues/4803)
- Correction de l'import Décathlon défaillant. [#4836](https://github.com/mission-apprentissage/labonnealternance/issues/4836)
- Ajout d'une migration de nettoyage. [#4834](https://github.com/mission-apprentissage/labonnealternance/issues/4834)
- Généralisation de la règle binary des PNG dans `.gitattributes`. [#4805](https://github.com/mission-apprentissage/labonnealternance/issues/4805)
- Correction de la détection des doublons. [#4832](https://github.com/mission-apprentissage/labonnealternance/issues/4832)
- Correction du texte de la page Espace développeur. [#4873](https://github.com/mission-apprentissage/labonnealternance/issues/4873)
- Correction pour garder le CTA de recherche désactivé tant que métier ou lieu n'est pas modifié. [#4872](https://github.com/mission-apprentissage/labonnealternance/issues/4872)
- Correction d'un mauvais calibrage du passage des headers en sticky. [#4855](https://github.com/mission-apprentissage/labonnealternance/issues/4855)
- Création d'un template Epic pour le projet Roadmap GitHub. [#4878](https://github.com/mission-apprentissage/labonnealternance/issues/4878)
- Correction d'une erreur d'hydratation React sur les pages ville. [#4884](https://github.com/mission-apprentissage/labonnealternance/issues/4884)
- Correction d'un problème d'envoi des emails RDV bloqués.
- Correction d'un problème de flux confié export France Travail. [#4882](https://github.com/mission-apprentissage/labonnealternance/issues/4882)
- Correction d'un problème avec l'appel à l'API Hellowork. [#4918](https://github.com/mission-apprentissage/labonnealternance/issues/4918)
- Désactivation temporaire de Sentry côté serveur pendant la migration. [#4871](https://github.com/mission-apprentissage/labonnealternance/issues/4871)
- Correction d'un problème de détection des doublons. [#4839](https://github.com/mission-apprentissage/labonnealternance/issues/4839)
