## Changelog : labonnealternance (30 derniers jours, au 20 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'expérience utilisateur, notamment sur les pages d'erreur, la gestion des comptes utilisateurs et le partage d'offres. Des corrections ont également été apportées pour améliorer la stabilité et la fiabilité de la plateforme, ainsi que des optimisations techniques pour la gestion des secrets et l'export des données.

### Évolutions fonctionnelles
- Amélioration de l'affichage des erreurs, avec une refonte de la page d'erreur globale et de la page RDVA ([#4916](https://github.com/mission-apprentissage/labonnealternance/issues/4916)).
- Clarification des libellés des actions de partage d'offre pour une meilleure compréhension des utilisateurs ([#4943](https://github.com/mission-apprentissage/labonnealternance/issues/4943)).
- Blocage de la réactivation d'un compte utilisateur s'il est déjà actif sur une autre organisation ([#4890](https://github.com/mission-apprentissage/labonnealternance/issues/4890)).
- Exclusion des offres GEIQ du rendu détaillé des offres partenaires ([#4930](https://github.com/mission-apprentissage/labonnealternance/issues/4930)).
- Amélioration de l'affichage des informations relatives aux offres de GEIQ (emploi et formation) ([#4801](https://github.com/mission-apprentissage/labonnealternance/issues/4801)).
- Mise à jour des visuels et des contenus de la page d'accueil candidat, de la landing page recruteurs, de la landing page CFA et de la page À propos ([#4824](https://github.com/mission-apprentissage/labonnealternance/issues/4824)).
- Standardisation des modales pour une expérience utilisateur plus cohérente ([#4851](https://github.com/mission-apprentissage/labonnealternance/issues/4851)).
- Activation de l'export des offres d'emploi ([#4920](https://github.com/mission-apprentissage/labonnealternance/issues/4920)).
- Correction de l'écran de récapitulatif des intentions envoyées ([#4935](https://github.com/mission-apprentissage/labonnealternance/issues/4935)).
- Amélioration du wording des niveaux d'étude ([#4869](https://github.com/mission-apprentissage/labonnealternance/issues/4869)).

### Évolutions techniques
- Suppression de l'origine du rôle "rolemanagements" et normalisation dans les comptes utilisateurs ([#4983](https://github.com/mission-apprentissage/labonnealternance/issues/4983)).
- Correction du point de montage du volume Metabase pour l'environnement de prévisualisation ([#4981](https://github.com/mission-apprentissage/labonnealternance/issues/4981)).
- Rotation du secret principal SOPS pour renforcer la sécurité ([#4939](https://github.com/mission-apprentissage/labonnealternance/issues/4939)).
- Correction de l'utilisation de Sentry (type d'options et format extra) ([#4937](https://github.com/mission-apprentissage/labonnealternance/issues/4937)).
- Correction de l'hydratation React sur les pages ville ([#4884](https://github.com/mission-apprentissage/labonnealternance/issues/4884)).
- Masquage de la navigation LBA en mode widget et fluidification de l'animation du header au scroll ([#4891](https://github.com/mission-apprentissage/labonnealternance/issues/4891)).
- Mise en place d'un flux dédié pour les offres confiées à France Travail ([#4831](https://github.com/mission-apprentissage/labonnealternance/issues/4831)).
- Correction des tests Hellowork pour les aligner sur le caller hellowork-api ([#4927](https://github.com/mission-apprentissage/labonnealternance/issues/4927)).
- Ajout de Maazi à la liste blanche ([#4863](https://github.com/mission-apprentissage/labonnealternance/issues/4863)).

### Autres changements
- Renommage du fichier epic en epic.yml ([#4886](https://github.com/mission-apprentissage/labonnealternance/issues/4886)).
- Création d'un template Epic pour le roadmap du projet GitHub ([#4878](https://github.com/mission-apprentissage/labonnealternance/issues/4878)).
- Correction du texte de la page Espace développeur ([#4873](https://github.com/mission-apprentissage/labonnealternance/issues/4873)).
- Désactivation temporaire de Sentry côté serveur pendant la migration ([#4871](https://github.com/mission-apprentissage/labonnealternance/issues/4871)).
- Correction de l'envoi des emails RDV bloqués ([#580](https://github.com/mission-apprentissage/labonnealternance/issues/580)).
