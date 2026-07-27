## Changelog : labonnealternance (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment sur les interfaces d'administration des CFA et la gestion des intentions des recruteurs. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de la plateforme, ainsi que des optimisations techniques pour la gestion des données et la surveillance des performances.

### Évolutions fonctionnelles
- Amélioration de l'administration des entreprises de type CFA avec un nouvel écran dédié. [#4974](https://github.com/mission-apprentissage/labonnealternance/issues/4974)
- Publication d'un nouvel article guide pour les CFA. [#5026](https://github.com/mission-apprentissage/labonnealternance/issues/5026)
- Adaptation du canevas des articles aux nouvelles recommandations du DSFR (Design System de la République Française). [#4995](https://github.com/mission-apprentissage/labonnealternance/issues/4995)
- Suppression du champ "origin" des informations des CFA. [#4899](https://github.com/mission-apprentissage/labonnealternance/issues/4899)
- Suppression du champ "origin" des rôles et normalisation des informations des utilisateurs. [#4983](https://github.com/mission-apprentissage/labonnealternance/issues/4983)
- Refonte de la page d'erreur globale et affichage d'une erreur spécifique pour la page RDVA. [#4916](https://github.com/mission-apprentissage/labonnealternance/issues/4916)
- Refonte de l'interface et des emails liés aux intentions des recruteurs. [#4866](https://github.com/mission-apprentissage/labonnealternance/issues/4866)
- Clarification des libellés des actions de partage d'offre. [#4943](https://github.com/mission-apprentissage/labonnealternance/issues/4943)
- Correction de l'écran de récapitulatif des intentions envoyées. [#4935](https://github.com/mission-apprentissage/labonnealternance/issues/4935)
- Possibilité de mentionner des membres de l'équipe dans les notifications Slack. [#4967](https://github.com/mission-apprentissage/labonnealternance/issues/4967)
- Correction de l'envoi des emails de rendez-vous bloqués.
- Ajout de la possibilité d'exporter les offres GEIQ.
- Blocage de la réactivation d'un compte ayant déjà un accès actif sur une autre organisation. [#4890](https://github.com/mission-apprentissage/labonnealternance/issues/4890)
- Mise à jour de la liste des CFA en "blacklist". [#5030](https://github.com/mission-apprentissage/labonnealternance/issues/5030)
- Correction de l'utilisation de Sentry (type options et format extra). [#4937](https://github.com/mission-apprentissage/labonnealternance/issues/4937)
- Activation de l'export des offres d'emploi avec le format XP FT. [#4920](https://github.com/mission-apprentissage/labonnealternance/issues/4920)
- Amélioration de la recherche ciblée des entreprises dans l'interface d'administration. [#4875](https://github.com/mission-apprentissage/labonnealternance/issues/4875)
- Standardisation des modales. [#4851](https://github.com/mission-apprentissage/labonnealternance/issues/4851)
- Suivi des actions des recruteurs avec Matomo. [#4987](https://github.com/mission-apprentissage/labonnealternance/issues/4987)

### Évolutions techniques
- Mise à jour de Metabase. [#5031](https://github.com/mission-apprentissage/labonnealternance/issues/5031)
- Rotation du secret principal SOPS. [#4939](https://github.com/mission-apprentissage/labonnealternance/issues/4939)
- Correction du point de montage du volume Metabase pour la preview. [#4981](https://github.com/mission-apprentissage/labonnealternance/issues/4981)
- Suppression du champ `opco_short_name` de la collection Opcos. [#4989](https://github.com/mission-apprentissage/labonnealternance/issues/4989)
- Blocage des CFA AURLOM BTS+ Paris dans le filtre des employeurs. [#5028](https://github.com/mission-apprentissage/labonnealternance/issues/5028)
- Correction de l'hydratation React sur les pages ville. [#4884](https://github.com/mission-apprentissage/labonnealternance/issues/4884)
- Correction de l'erreur d'hydratation React sur les pages ville. [#4884](https://github.com/mission-apprentissage/labonnealternance/issues/4884)
- Correction de la déduplication Hellowork avec l'opérateur `substrCP`. [#4925](https://github.com/mission-apprentissage/labonnealternance/issues/4925)
- Alignement des tests Hellowork sur le caller Hellowork-API et régénération des tests. [#4927](https://github.com/mission-apprentissage/labonnealternance/issues/4927)
- Masquage de la navigation LBA en mode widget et fluidification de l'animation du header au scroll. [#4891](https://github.com/mission-apprentissage/labonnealternance/issues/4891)
- Réactivation de Sentry après migration du serveur. [#4892](https://github.com/mission-apprentissage/labonnealternance/issues/4892)

### Autres changements
- Renommage de l'épique en `epic.yml`. [#4886](https://github.com/mission-apprentissage/labonnealternance/issues/4886)
- Création d'un template Epic pour le projet Roadmap GitHub. [#4878](https://github.com/mission-apprentissage/labonnealternance/issues/4878)
- Mise à jour du texte de la page Espace développeur. [#4873](https://github.com/mission-apprentissage/labonnealternance/issues/4873)
- Correction du nom du caller Hellowork API. [#4918](https://github.com/mission-apprentissage/labonnealternance/issues/4918)
- Suppression des liens externes et correction des délimitations pour les comptes CFA. [#4926](https://github.com/mission-apprentissage/labonnealternance/issues/4926)
- Correction du calibrage du passage des headers en sticky. [#4855](https://github.com/mission-apprentissage/labonnealternance/issues/4855)
- Jobs déclenchables par un administrateur. [#4868](https://github.com/mission-apprentissage/labonnealternance/issues/4868)
- Correction du CTA de recherche désactivé. [#4872](https://github.com/mission-apprentissage/labonnealternance/issues/4872)
- Correction du flux confié export France Travail (filtre expiration, plafond J+30, correspondant). [#4882](https://github.com/mission-apprentissage/labonnealternance/issues/4882)
- Wording des niveaux d'étude. [#4869](https://github.com/mission-apprentissage/labonnealternance/issues/4869)
