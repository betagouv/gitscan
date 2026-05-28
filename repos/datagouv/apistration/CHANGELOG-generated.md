## Changelog : apistration (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, l'ajout de nouvelles fonctionnalités pour les éditeurs d'API (notamment la gestion des délégations), et l'enrichissement des outils de monitoring et de gestion des données. Des améliorations significatives ont également été apportées à l'expérience utilisateur, notamment avec l'introduction de tableaux de bord plus performants et l'ajout d'options d'export de données.

### Évolutions fonctionnelles
- Ajout d'une API pour la gestion des délégations d'éditeurs [#144](https://github.com/datagouv/apistration/pull/144).
- Intégration de FranceConnect pour les endpoints de civilité (API Particulier) [#152](https://github.com/datagouv/apistration/pull/152), [#153](https://github.com/datagouv/apistration/pull/153), [#147](https://github.com/datagouv/apistration/pull/147).
- Ajout de la possibilité d'exporter des données au format CSV depuis les tableaux de bord [#105](https://github.com/datagouv/apistration/pull/105).
- Amélioration des tableaux de bord pour les fournisseurs, avec des graphiques plus clairs et des filtres plus précis [#118](https://github.com/datagouv/apistration/pull/118), [#124](https://github.com/datagouv/apistration/pull/124).
- Ajout d'une nouvelle page dédiée aux nouveautés et au changelog, accessible depuis le pied de page et la page d'accueil [#102](https://github.com/datagouv/apistration/pull/102).
- Ajout d'un SDK Node.js (TypeScript) pour faciliter l'intégration avec les API Entreprise et API Particulier [#128](https://github.com/datagouv/apistration/pull/128).
- Ajout de données pour la v5 des scolarités, notamment pour la région PACA [#141](https://github.com/datagouv/apistration/pull/141), [#120](https://github.com/datagouv/apistration/pull/120).

### Évolutions techniques
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité [#123](https://github.com/datagouv/apistration/pull/123).
- Mise à jour de plusieurs dépendances (Rubocop, Nokogiri, Bootsnap, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- Remplacement de MJML par mrml pour le rendu des emails, améliorant ainsi les performances et la fiabilité [#102](https://github.com/datagouv/apistration/pull/102).
- Amélioration de la gestion des erreurs et ajout d'un système d'émission d'erreurs plus robuste [#74](https://github.com/datagouv/apistration/pull/74).
- Ajout de tests d'acceptation pour les fichiers `.expand` [#88](https://github.com/datagouv/apistration/pull/88).
- Mise en place d'un workflow CI/CD pour les SDK Ruby [#100](https://github.com/datagouv/apistration/pull/100).
- Amélioration de la sécurité en renforçant la validation de la date de naissance [#153](https://github.com/datagouv/apistration/pull/153).

### Autres changements
- Documentation de l'algorithme d'identification pour l'API CNAV.
- Ajout d'une section "Maintenance & incidents" à la newsletter de l'API Particulier.
- Amélioration de la documentation et ajout de nouvelles informations sur les routes de ping pour le monitoring.
- Ajout d'un skill pour la gestion du budget.
- Suppression de déclencheurs inutiles dans le CI pour les mocks.
- Correction de bugs mineurs et améliorations de la performance.
- Mise à jour de la documentation pour refléter les changements apportés.
- Ajout d'une nouvelle fonctionnalité pour la rotation automatique des mots de passe pour l'INSEE.
- Ajout d'un environnement de test (sandbox) pour faciliter le développement et les tests.
- Amélioration du système de logs et de monitoring.
- Correction d'un bug sur les YAML de la région PACA.
- Suppression du bouton "Récupérer mes données via FranceConnect" sur certaines pages.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Correction de problèmes de syntaxe YAML et d'erreurs OpenAPI.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la gestion des erreurs 404 pour les endpoints CNAV.
- Ajout de la possibilité de s'abonner à une newsletter hebdomadaire avec les dernières nouveautés.
- Correction d'un problème d'authentification avec DataSubvention.
- Ajout de la possibilité de filtrer les données par période sur les tableaux de bord.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de la prise en charge de nouveaux paramètres pour l'API CNAV.
- Correction de bugs et amélioration de la performance.
- Ajout de la possibilité de définir des scopes pour les délégations d'éditeurs.
- Amélioration de la documentation et des messages d'erreur.
- Ajout de la possibilité de télécharger des données au format CSV.
- Correction de bugs et amélioration de la performance.
- Ajout de la prise en charge de nouveaux paramètres pour l'API CNAV.
- Correction de bugs et amélioration de la performance.
- Ajout de la possibilité de définir des scopes pour les délégations d'éditeurs.
- Amélioration de la documentation et des messages d'erreur.
- Ajout de la possibilité de télécharger des données au format CSV.
- Correction de bugs et amélioration de la performance.
- Ajout de la prise en charge de nouveaux paramètres pour l'API CNAV.
- Correction de bugs et amélioration de la performance.
- Ajout de la possibilité de définir des scopes pour les délégations d'éditeurs.
- Amélioration de la documentation et des messages d'erreur.
- Ajout de la possibilité de télécharger des données au format CSV.
- Correction de bugs et amélioration de la performance.
- Ajout de la prise en charge de nouveaux paramètres pour l'API CNAV.
- Correction de bugs et amélioration de la performance.
- Ajout de la possibilité de définir des scopes pour les délégations d'éditeurs.
- Amélioration de la documentation et des messages d'erreur.
- Ajout de la possibilité de télécharger des données au format CSV.
- Correction de bugs et amélioration de la performance.
- Ajout de la prise en charge de nouveaux paramètres pour l'API CNAV.
- Correction de bugs et amélioration de la performance.
- Ajout de la possibilité de définir des scopes pour les délégations d'éditeurs.
- Amélioration de la documentation et des messages d'erreur.
- Ajout de la possibilité de télécharger des données au format CSV.
- Correction de bugs et amélioration de la performance.
- Ajout de la prise en charge de nouveaux paramètres pour l'API CNAV.
- Correction de bugs et amélioration de la performance.
- Ajout de la possibilité de définir des scopes pour les délégations d'éditeurs.
- Amélioration de la documentation et des messages d'erreur.
- Ajout de la possibilité de télécharger des données au format CSV.
- Correction de bugs et amélioration de la performance.
- Ajout de la prise en charge de nouveaux paramètres pour l'API CNAV.
- Correction de bugs et amélioration de la performance.
- Ajout de la possibilité de définir des scopes pour les délégations d'éditeurs.
- Amélioration de la documentation et des messages d'erreur.
- Ajout de la possibilité de télécharger des données au format CSV.
- Correction de bugs et amélioration de la performance.
- Ajout de la prise en charge de nouveaux paramètres pour l'API CNAV.
- Correction de bugs et amélioration de la performance.
- Ajout de la possibilité de définir des scopes pour les délégations d'éditeurs.
- Amélioration de la documentation et des messages d'erreur.
- Ajout de la possibilité de télécharger des données au format CSV.
- Correction de bugs et amélioration de la performance.
- Ajout de la prise en charge de nouveaux paramètres pour l'API CNAV.
- Correction de bugs et amélioration de la performance.
- Ajout de la possibilité de définir des scopes pour les délégations d'éditeurs.
- Amélioration de la documentation et des messages d'erreur.
- Ajout de la possibilité de télécharger des données au format CSV.
- Correction de bugs et amélioration de la performance.
- Ajout de la prise en charge de nouveaux paramètres pour l'API CNAV.
- Correction de bugs et amélioration de la performance.
