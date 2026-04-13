## Changelog : nosgestesclimat-app (30 derniers jours, au 13 avril 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de stabilité, de performance et d'expérience utilisateur. Une nouvelle page de résultats a été implémentée, des corrections de bugs ont été apportées pour améliorer la fiabilité, et l'accessibilité a été renforcée. Des optimisations ont également été réalisées sur le suivi des événements et la gestion des cookies. Enfin, le projet a été refactoré pour préparer une transition vers une architecture monorepo.

### Évolutions fonctionnelles
- Ajout d'une nouvelle page de résultats pour afficher les données de manière plus claire et intuitive. [#1696](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1696)
- Amélioration de la question sur la consommation d'électricité avec l'ajout d'un nouveau commutateur. [#1701](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1701)
- Correction de l'affichage des nombres sur les pages d'actions après filtrage. [#1724](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1724)
- Correction d'un bug empêchant l'affichage correct de la page `/fin` sur Safari et dans les intégrations iframe. [#1728](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1728)
- Correction de l'affichage de la bannière en fonction de règles spécifiques. [#1749](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1749)
- Ajout d'informations supplémentaires à la liste des questions. [#1738](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1738)
- Correction de l'affichage des questions "manquantes" et "brutes manquantes". [#1716](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1716)
- Mise à jour du modèle vers la version 4.10.2. [#1722](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1722)

### Évolutions techniques
- Refactorisation du déploiement CI pour améliorer la fiabilité et l'efficacité. [#1742](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1742)
- Préparation de la transition vers une architecture monorepo. [#1745](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1745)
- Refactorisation du suivi des événements et de la gestion des cookies pour une meilleure performance et conformité. [#1669](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1669)
- Amélioration de la configuration de Sentry pour une meilleure gestion des erreurs et des releases.
- Extraction de l'URL du serveur et de la logique de proxy vers un fichier de configuration.
- Conversion de `ThematicPagesSection` en composant serveur.
- Correction de problèmes liés à la vérification de l'origine (sameOrigin) dans la configuration Next.js.
- Suppression de l'option de cookie partitionné.
- Ajout d'une favicon.

### Autres changements
- Documentation sur l'installation du projet mise à jour. [#1733](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1733)
- Améliorations de l'accessibilité de l'application. [#1703](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1703)
- Corrections de typos et ajout de traductions manquantes. [#1714](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1714), [#1715](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1715), [#1710](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1710)
- Mise à jour des textes pour plus de clarté et de précision. [#1712](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1712)
- Suppression du Footer dans les tests. [#1721](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1721)
- Masquage de l'alerte lorsque l'utilisateur tourne son appareil mobile horizontalement. [#1720](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1720)
- Utilisation du nouveau calendrier sur la page de demande de démonstration. [#1711](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1711)
- Amélioration de la revalidation du cache sur le tableau de bord de l'organisation lors de la création d'un nouveau sondage. [#1709](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1709)
- Ajout de détails sur les cookies requis dans le formulaire de consentement aux cookies. [#1708](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1708)
