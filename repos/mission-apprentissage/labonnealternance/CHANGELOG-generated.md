## Changelog : labonnealternance (30 derniers jours, au 03 juillet 2026)

### Résumé
Les dernières mises à jour de La Bonne Alternance se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur la recherche d'entreprises et d'offres, ainsi que sur l'optimisation des flux de données et de la gestion des offres d'apprentissage. Des corrections de bugs et des améliorations techniques ont également été apportées pour garantir la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Recherche d'entreprises:** Possibilité de rechercher spécifiquement des entreprises dans l'interface d'administration. [#4875](https://github.com/mission-apprentissage/labonnealternance/issues/4875)
- **Flux France Travail:** Amélioration de l'export des offres vers France Travail, avec gestion des expirations, des plafonds et des correspondants. [#4882](https://github.com/mission-apprentissage/labonnealternance/issues/4882)
- **Intégration GEIQ:** Affichage des informations emploi et formation pour les offres proposées par les GEIQ. [#4801](https://github.com/mission-apprentissage/labonnealternance/issues/4801)
- **Candidatures Spontanées:** Renommage du filtre "candidatures spontanées" en "entreprise à contacter" pour plus de clarté. [#4797](https://github.com/mission-apprentissage/labonnealternance/issues/4797)
- **Formulaire RDV CFA:** Amélioration de l'expérience utilisateur du formulaire de prise de rendez-vous avec les CFA. [#4773](https://github.com/mission-apprentissage/labonnealternance/issues/4773)
- **Intégration Maazi:** Ajout de Maazi à la liste blanche pour éviter une classification erronée des offres. [#4863](https://github.com/mission-apprentissage/labonnealternance/issues/4863)
- **Refonte Intention Recruteurs:** Mise à jour des visuels et des contenus de la page d'intention des recruteurs. [#4824](https://github.com/mission-apprentissage/labonnealternance/issues/4824)
- **Wording Niveaux d'étude:** Mise à jour du wording des niveaux d'étude. [#4869](https://github.com/mission-apprentissage/labonnealternance/issues/4869)
- **Dépôt d'offre:** Ajout de la date de début de contrat lors du dépôt d'une offre. [#4768](https://github.com/mission-apprentissage/labonnealternance/issues/4768)
- **Standardisation Modales:** Standardisation des modales. [#4851](https://github.com/mission-apprentissage/labonnealternance/issues/4851)

### Évolutions techniques
- **Migration Serveur:** Migration du serveur de production, de recette et de preview. [#4837](https://github.com/mission-apprentissage/labonnealternance/issues/4837), [#4829](https://github.com/mission-apprentissage/labonnealternance/issues/4829), [#4828](https://github.com/mission-apprentissage/labonnealternance/issues/4828)
- **Logging:** Unification du logging sur Pino avec corrélation reqId et enrichissement des logs HTTP. [#4800](https://github.com/mission-apprentissage/labonnealternance/issues/4800)
- **Suppression Sous-modules:** Suppression des sous-modules .infra/authorizations et .infra/inventories. [#4825](https://github.com/mission-apprentissage/labonnealternance/issues/4825)
- **Correction Hydratation React:** Correction d'une erreur d'hydratation React sur les pages ville. [#4884](https://github.com/mission-apprentissage/labonnealternance/issues/4884)
- **Sentry:** Réactivation de Sentry après la migration du serveur. [#4892](https://github.com/mission-apprentissage/labonnealternance/issues/4892) et désactivation temporaire pendant la migration. [#4871](https://github.com/mission-apprentissage/labonnealternance/issues/4871)
- **CLI:** Amélioration de l'utilisation de la CLI pour le remplissage des données. [#4854](https://github.com/mission-apprentissage/labonnealternance/issues/4854)

### Autres changements
- **Documentation:** Mise à jour du texte de la page Espace développeur. [#4873](https://github.com/mission-apprentissage/labonnealternance/issues/4873)
- **Configuration:** Renommage du fichier epic en epic.yml. [#4886](https://github.com/mission-apprentissage/labonnealternance/issues/4886)
- **Git Attributes:** Généralisation de la règle binary des PNG dans .gitattributes. [#4805](https://github.com/mission-apprentissage/labonnealternance/issues/4805)
- **SEO:** Améliorations SEO pour les pages hubs et géolocalisées. [#3222](https://github.com/mission-apprentissage/labonnealternance/issues/3222) et [#4718](https://github.com/mission-apprentissage/labonnealternance/issues/4718)
- **UI:** Masquage de la navigation LBA en mode widget et fluidification de l'animation du header au scroll. [#4891](https://github.com/mission-apprentissage/labonnealternance/issues/4891)
- **Correction Import Décathlon:** Correction d'un problème d'import des données Décathlon. [#4836](https://github.com/mission-apprentissage/labonnealternance/issues/4836)
- **Correction Duplicats:** Amélioration de la détection des offres en doublon. [#4832](https://github.com/mission-apprentissage/labonnealternance/issues/4832) et [#4839](https://github.com/mission-apprentissage/labonnealternance/issues/4839)
