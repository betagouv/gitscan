## Changelog : labonnealternance (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité, de la gestion des offres d'apprentissage (notamment celles de France Travail et GEIQ), et de l'expérience utilisateur, avec une refonte de certaines pages et l'ajout de nouvelles fonctionnalités pour les recruteurs et les candidats. Des corrections de bugs ont également été apportées pour améliorer la stabilité de la plateforme.

### Évolutions fonctionnelles
- **Blocage de la réactivation de comptes:** Il n'est plus possible de réactiver un compte si l'utilisateur a déjà un accès actif sur une autre organisation. [#4890](https://github.com/mission-apprentissage/labonnealternance/issues/4890)
- **Exclusion des offres GEIQ:** Les offres d'apprentissage proposées par GEIQ ne sont plus affichées dans le détail des offres partenaires. [#4930](https://github.com/mission-apprentissage/labonnealternance/issues/4930)
- **Refonte des pages d'erreur:** La page d'erreur globale et la page d'erreur RDVA ont été refonçues pour une meilleure expérience utilisateur. [#4916](https://github.com/mission-apprentissage/labonnealternance/issues/4916)
- **Export des offres XP FT:** Activation de l'export des offres d'expérience professionnelle France Travail. [#4920](https://github.com/mission-apprentissage/labonnealternance/issues/4920)
- **Masquage des liens externes et des comptes CFA:** Les liens externes sont maintenant masqués et les délimitations pour les comptes CFA ont été corrigées. [#4926](https://github.com/mission-apprentissage/labonnealternance/issues/4926)
- **Empêchement de la réinscription des recruteurs DENIED:** Les tentatives de réinscription des recruteurs ayant un statut DENIED sont maintenant bloquées. [#4885](https://github.com/mission-apprentissage/labonnealternance/issues/4885)
- **Recherche ciblée des entreprises:** Possibilité de rechercher des entreprises de l'algorithme directement dans l'administration. [#4875](https://github.com/mission-apprentissage/labonnealternance/issues/4875)
- **Standardisation des modales:** Uniformisation du style et du comportement des modales. [#4851](https://github.com/mission-apprentissage/labonnealternance/issues/4851)
- **Refonte des intentions recruteurs:** Refonte de l'interface utilisateur pour la gestion des intentions des recruteurs, incluant les jobs et les emails associés. [#4866](https://github.com/mission-apprentissage/labonnealternance/issues/4866)
- **Mise à jour des visuels et contenus:** Mise à jour des visuels et des contenus des pages d'accueil candidat, landing page recruteurs, landing page CFA et page À propos. [#4824](https://github.com/mission-apprentissage/labonnealternance/issues/4824)
- **Ajout de Maazi à la whitelist:** Ajout de Maazi à la liste blanche des sources d'offres. [#4863](https://github.com/mission-apprentissage/labonnealternance/issues/4863)
- **Affichage des informations emploi et formation GEIQ:** Affichage des informations relatives à l'emploi et à la formation pour les offres GEIQ. [#4801](https://github.com/mission-apprentissage/labonnealternance/issues/4801)
- **Date de début de contrat:** Ajout de la possibilité de spécifier la date de début de contrat lors du dépôt d'une offre. [#4768](https://github.com/mission-apprentissage/labonnealternance/issues/4768)
- **Baromètre T1 2026 de l'alternance:** Ajout du baromètre T1 2026 de l'alternance pour le SEO. [#4718](https://github.com/mission-apprentissage/labonnealternance/issues/4718)
- **SEO pour les hubs:** Amélioration du SEO pour les hubs de métiers, villes et diplômes. [#3222](https://github.com/mission-apprentissage/labonnealternance/issues/3222)

### Évolutions techniques
- **Rotation du secret SOPS:** Rotation du secret principal SOPS pour renforcer la sécurité. [#4939](https://github.com/mission-apprentissage/labonnealternance/issues/4939)
- **Correction de l'utilisation de Sentry:** Correction de l'utilisation de Sentry pour une meilleure gestion des erreurs. [#4937](https://github.com/mission-apprentissage/labonnealternance/issues/4937)
- **Migration du serveur:** Migration du serveur LBA (preview, recette et production). [#4829](https://github.com/mission-apprentissage/labonnealternance/issues/4829), [#4828](https://github.com/mission-apprentissage/labonnealternance/issues/4828), [#4837](https://github.com/mission-apprentissage/labonnealternance/issues/4837)
- **Logging avec Pino:** Unification du logging avec Pino, incluant la corrélation des requêtes et l'enrichissement des logs HTTP. [#4800](https://github.com/mission-apprentissage/labonnealternance/issues/4800)
- **Suppression des sous-modules .infra:** Suppression des sous-modules .infra/authorizations et .infra/inventories. [#4825](https://github.com/mission-apprentissage/labonnealternance/issues/4825)
- **Généralisation de la règle binary pour les PNG:** Généralisation de la règle binary pour les fichiers PNG dans le fichier .gitattributes. [#4805](https://github.com/mission-apprentissage/labonnealternance/issues/4805)

### Autres changements
- **Renommage de l'epic:** Renommage du fichier epic en epic.yml. [#4886](https://github.com/mission-apprentissage/labonnealternance/issues/4886)
- **Création de template Epic:** Création d'un template Epic pour le projet Roadmap GitHub. [#4878](https://github.com/mission-apprentissage/labonnealternance/issues/4878)
- **Correction de la déduplication hellowork:** Correction de la déduplication des offres Hellowork avec l'opérateur substrCP. [#4925](https://github.com/mission-apprentissage/labonnealternance/issues/4925)
- **Alignement des tests hellowork:** Alignement des tests Hellowork sur le caller hellowork-api et régénération des données de test. [#4927](https://github.com/mission-apprentissage/labonnealternance/issues/4927)
