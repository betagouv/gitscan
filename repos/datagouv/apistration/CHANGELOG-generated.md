## Changelog : apistration (30 derniers jours, au 19 mai 2026)

### Résumé
Les derniers mois ont été marqués par d'importantes améliorations de l'application, notamment l'ajout d'un SDK Node.js pour faciliter l'intégration avec l'API, la refonte du tableau de bord pour les fournisseurs avec de nouvelles visualisations et des options d'exportation, et l'amélioration de la gestion des erreurs et de la sécurité. Des efforts ont également été déployés pour améliorer la documentation et l'expérience développeur.

### Évolutions fonctionnelles
- Ajout d'un SDK Node.js (TypeScript) pour l'API Entreprise et l'API Particulier, permettant aux développeurs d'intégrer plus facilement les données dans leurs applications. [#126](https://github.com/datagouv/apistration/pull/126)
- Refonte du tableau de bord des fournisseurs avec de nouveaux graphiques, des filtres améliorés et la possibilité d'exporter les données au format CSV. [#118](https://github.com/datagouv/apistration/pull/118), [#124](https://github.com/datagouv/apistration/pull/124)
- Ajout d'une section "Maintenance & incidents" à la newsletter de l'API Particulier pour informer les utilisateurs des interruptions de service. [#122](https://github.com/datagouv/apistration/pull/122)
- Possibilité de s'abonner à une newsletter hebdomadaire récapitulant les changements apportés à l'API. [#95](https://github.com/datagouv/apistration/pull/95)
- Ajout de la possibilité d'exporter des données au format CSV depuis le tableau de bord des fournisseurs. [#105](https://github.com/datagouv/apistration/pull/105)
- Amélioration de la gestion des erreurs et ajout d'informations plus détaillées sur les erreurs rencontrées. [#74](https://github.com/datagouv/apistration/pull/74)
- Ajout de nouveaux tests pour les cas d'utilisation de l'API CNAV, notamment pour le quotient familial. [#91](https://github.com/datagouv/apistration/pull/91)
- Ajout de nouveaux cas de test pour les données de scolarité (MEN). [#120](https://github.com/datagouv/apistration/pull/120)
- Ajout de la possibilité de filtrer les données du tableau de bord par période. [#109](https://github.com/datagouv/apistration/pull/109)

### Évolutions techniques
- Refactorisation de l'architecture de gestion des utilisateurs et de l'authentification pour améliorer la sécurité et la maintenabilité. [#50](https://github.com/datagouv/apistration/pull/50)
- Mise en place d'un système de limitation de débit (rate limiting) pour protéger l'API contre les abus. [#48](https://github.com/datagouv/apistration/pull/48)
- Amélioration de la gestion des erreurs et ajout d'une journalisation plus détaillée. [#74](https://github.com/datagouv/apistration/pull/74)
- Migration de l'outil de rendu MJML vers mrml (Rust) pour améliorer les performances et la fiabilité de l'envoi d'emails. [#102](https://github.com/datagouv/apistration/pull/102)
- Mise à jour des dépendances du projet.
- Amélioration de la configuration et du déploiement de l'application.
- Ajout de tests d'acceptation pour les fichiers `.expand`. [#88](https://github.com/datagouv/apistration/pull/88)
- Amélioration de la synchronisation des pings de surveillance. [#87](https://github.com/datagouv/apistration/pull/87)
- Ajout de workflows CI/CD pour les SDK Ruby. [#98](https://github.com/datagouv/apistration/pull/98), [#100](https://github.com/datagouv/apistration/pull/100)

### Autres changements
- Amélioration de la documentation de l'API et ajout d'exemples d'utilisation.
- Mise à jour du fichier `CHANGELOG.md` pour refléter les changements apportés à l'application.
- Ajout d'une page "Nouveautés" sur le site web pour informer les utilisateurs des dernières modifications. [#92](https://github.com/datagouv/apistration/pull/92)
- Ajout d'une section FAQ sur l'algorithme d'identification pour l'API CNAV.
- Ajout d'un skill pour la gestion des annonces.
- Ajout d'un skill pour la gestion des rapports de budget.
- Correction de bugs et améliorations de la performance.
- Mise à jour de la configuration de l'environnement de développement.
- Suppression de code inutile et nettoyage du code source.
- Amélioration des messages d'erreur et de la documentation.
- Ajout de tests unitaires et d'intégration.
- Correction d'un problème lié à la rotation des mots de passe pour l'INSEE. [#80](https://github.com/datagouv/apistration/pull/80)
- Correction d'un bug lié à l'authentification avec DataSubvention. [#72](https://github.com/datagouv/apistration/pull/72)
- Correction d'un problème de double comptage des tokens dans les graphiques d'évolution des consommateurs. [#119](https://github.com/datagouv/apistration/pull/119)
- Correction d'un bug lié à l'affichage des liens dans la documentation. [#58](https://github.com/datagouv/apistration/pull/58)
