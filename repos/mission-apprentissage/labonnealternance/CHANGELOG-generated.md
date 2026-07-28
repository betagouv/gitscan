## Changelog : labonnealternance (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment en matière de recherche d'alternances et de suivi des entreprises. Des optimisations SEO ont également été apportées pour améliorer la visibilité de la plateforme. Plusieurs corrections de bugs et améliorations techniques ont été réalisées pour stabiliser et optimiser le fonctionnement de la plateforme.

### Évolutions fonctionnelles
- **Recherche d'alternances :** Nouveau moteur de recherche v2 en phase de test ([#4785](https://github.com/mission-apprentissage/labonnealternance/issues/4785)).
- **Incitation aux candidatures :** Relance automatique des candidats inactifs 7 jours après leur inscription ([#4976](https://github.com/mission-apprentissage/labonnealternance/issues/4976)).
- **SEO :** Optimisation SEO de la page salaire (guide rémunération + FAQPage + maillage interne) ([#5050](https://github.com/mission-apprentissage/labonnealternance/issues/5050)). Ajout de metas SEO dynamiques sur les pages de recherche ([#5040](https://github.com/mission-apprentissage/labonnealternance/issues/5040)).
- **Entreprises :** Nurturing des entreprises dormantes à l'anniversaire du dépôt d'offre ([#4980](https://github.com/mission-apprentissage/labonnealternance/issues/4980)).
- **Administration :** Possibilité de mentionner des membres de l'équipe dans les notifications Slack ([#4967](https://github.com/mission-apprentissage/labonnealternance/issues/4967)).
- **CFA :** Ajout d'un écran d'administration pour les entreprises de type CFA ([#4974](https://github.com/mission-apprentissage/labonnealternance/issues/4974)). Nouvel article pour le guide CFA ([#5026](https://github.com/mission-apprentissage/labonnealternance/issues/5026)).
- **Notifications :** Expose la date de dernière action et de dernière offre dans l'export Brevo ([#4978](https://github.com/mission-apprentissage/labonnealternance/issues/4978)). Relance email J+7 des candidats inactifs vers Brevo ([#4952](https://github.com/mission-apprentissage/labonnealternance/issues/4952)).
- **Pages d'erreur :** Refonte de la page d'erreur globale et affichage d'une erreur spécifique pour la page RDVA ([#4916](https://github.com/mission-apprentissage/labonnealternance/issues/4916)).
- **Contenu éditorial :** Mise à jour du contenu de 2 pages du guide alternant ([#4988](https://github.com/mission-apprentissage/labonnealternance/issues/4988)).

### Évolutions techniques
- **API :** Pilotage des robots d'indexation via l'API metadata de Next.js ([#5044](https://github.com/mission-apprentissage/labonnealternance/issues/5044)).
- **Infrastructure :** Rotation du secret principal SOPS ([#4939](https://github.com/mission-apprentissage/labonnealternance/issues/4939)). Correction du point de montage du volume Metabase pour la preview ([#4981](https://github.com/mission-apprentissage/labonnealternance/issues/4981)).
- **Sécurité :** Bloque la réactivation d'un compte ayant déjà un accès actif sur une autre organisation ([#4890](https://github.com/mission-apprentissage/labonnealternance/issues/4890)).
- **Tests :** Alignement des tests Hellowork sur le caller hellowork-api et régénération des tests ([#4927](https://github.com/mission-apprentissage/labonnealternance/issues/4927)).
- **Divers :** Suppression de champs `origin` dans les collections `rolemanagements` et `usersWithAccounts` ([#4983](https://github.com/mission-apprentissage/labonnealternance/issues/4983), [#4899](https://github.com/mission-apprentissage/labonnealternance/issues/4899)).

### Autres changements
- Mise à jour de la liste des CFA en blacklist ([#5030](https://github.com/mission-apprentissage/labonnealternance/issues/5030)).
- Mise à jour de Metabase ([#5031](https://github.com/mission-apprentissage/labonnealternance/issues/5031)).
- Création d'un template Epic pour le projet Roadmap GitHub ([#4878](https://github.com/mission-apprentissage/labonnealternance/issues/4878)).
- Correction de l'utilisation de Sentry (type options et format extra) ([#4937](https://github.com/mission-apprentissage/labonnealternance/issues/4937)).
- Correction de l'erreur d'hydratation React sur les pages ville ([#4884](https://github.com/mission-apprentissage/labonnealternance/issues/4884)).
- Correction de la déduplication Hellowork avec l'opérateur substrCP ([#4925](https://github.com/mission-apprentissage/labonnealternance/issues/4925)).
