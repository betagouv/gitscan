## Changelog : apistration (30 derniers jours, au 2026-05-25)

### Résumé
Les 30 derniers jours ont été marqués par d'importantes améliorations de l'application, notamment l'ajout de nouveaux SDK pour faciliter l'intégration avec l'API, l'amélioration des tableaux de bord pour les fournisseurs avec de nouvelles visualisations et des options d'export, et des corrections de bugs pour améliorer la stabilité et la fiabilité du système. Des efforts ont également été déployés pour améliorer la documentation et les processus de déploiement.

### Évolutions fonctionnelles
- Ajout de SDK Node.js (TypeScript) pour l'API Entreprise et l'API Particulier, facilitant l'intégration pour les développeurs JavaScript. [#126](https://github.com/datagouv/apistration/pull/126)
- Amélioration de la page d'édition des délégations avec affichage de l'UUID, des scopes et de la date de création. [#142](https://github.com/datagouv/apistration/pull/142)
- Ajout de données pour la v5 de scolarité, pour la région PACA. [#141](https://github.com/datagouv/apistration/pull/141)
- Ajout de la possibilité de télécharger des données au format CSV depuis les tableaux de bord des fournisseurs. [#105](https://github.com/datagouv/apistration/pull/105)
- Ajout d'un tableau de bord global pour les fournisseurs, permettant une vue d'ensemble de leur utilisation de l'API. [#123](https://github.com/datagouv/apistration/pull/123)
- Ajout d'une section "Nouveautés" et d'un changelog sur les pages de newsletter. [#95](https://github.com/datagouv/apistration/pull/95)
- Possibilité de s'abonner à une newsletter hebdomadaire présentant les changements récents. [#102](https://github.com/datagouv/apistration/pull/102)
- Amélioration des graphiques et des filtres sur les tableaux de bord des fournisseurs. [#80](https://github.com/datagouv/apistration/pull/80)
- Ajout de la possibilité de définir des plages de dates prédéfinies sur les tableaux de bord des fournisseurs.
- Ajout de la possibilité de filtrer les données des tableaux de bord des fournisseurs par portée (scopes). [#109](https://github.com/datagouv/apistration/pull/109)

### Évolutions techniques
- Refactorisation du code pour extraire la logique de transcogage dans un module dédié. [#117](https://github.com/datagouv/apistration/pull/117)
- Mise à jour des dépendances (Ruby, Rails, Node.js, etc.).
- Amélioration des tests et de la couverture de code.
- Utilisation de mrml (Rust) au lieu de MJML pour le rendu des emails, améliorant ainsi les performances et la fiabilité. [#102](https://github.com/datagouv/apistration/pull/102)
- Amélioration de la gestion des erreurs et ajout d'un système de gestion des erreurs centralisé. [#74](https://github.com/datagouv/apistration/pull/74)
- Amélioration de la gestion des logs et de la surveillance.
- Mise en place de workflows CI/CD pour les SDK Ruby. [#100](https://github.com/datagouv/apistration/pull/100)
- Amélioration de la configuration et du déploiement de l'application.
- Correction de problèmes de synchronisation des pings de surveillance. [#87](https://github.com/datagouv/apistration/pull/87)

### Autres changements
- Documentation améliorée pour les nouvelles fonctionnalités et les SDK.
- Correction de liens incorrects dans la documentation de l'API SIREN. [#72](https://github.com/datagouv/apistration/pull/72)
- Ajout d'une documentation sur l'utilisation des tokens d'éditeur.
- Ajout de tests d'acceptation pour la couverture des fichiers `.expand`. [#88](https://github.com/datagouv/apistration/pull/88)
- Amélioration de la gestion des erreurs 404 pour l'API CNAV. [#89](https://github.com/datagouv/apistration/pull/89)
- Ajout d'un skill pour le reporting budgétaire. [#73](https://github.com/datagouv/apistration/pull/73)
- Mise à jour de la documentation sur la rotation des mots de passe pour l'INSEE.
- Suppression de déclencheurs inutiles dans les workflows CI. [#96](https://github.com/datagouv/apistration/pull/96)
- Correction d'un bug empêchant la rotation des mots de passe dans certains cas. [#93](https://github.com/datagouv/apistration/pull/93)
