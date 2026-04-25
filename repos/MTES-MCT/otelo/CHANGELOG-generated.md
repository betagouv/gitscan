## Changelog : otelo (30 derniers jours, au 23 avril 2026)

### Résumé
Le projet Otelo a connu un mois d'avril riche en améliorations, notamment une refonte significative du tableau de bord, l'ajout de nouvelles fonctionnalités pour la gestion des utilisateurs et des données, ainsi que des corrections de bugs et des optimisations diverses. Ces évolutions visent à améliorer l'expérience utilisateur et à renforcer les capacités d'analyse et de pilotage de l'application.

### Évolutions fonctionnelles
- **Tableau de bord refondu** : Amélioration de la présentation et des fonctionnalités du tableau de bord, incluant la comparaison de scénarios via un tableau de bord dédié [#40](https://github.com/MTES-MCT/otelo/pull/40).
- **Prévisualisation des résultats** : Possibilité de prévisualiser les résultats directement dans les formulaires de création et de mise à jour [#39](https://github.com/MTES-MCT/otelo/pull/39).
- **Gestion des utilisateurs** :
    - Ajout d'un nouveau type d'utilisateur et d'une fonctionnalité associée dans l'interface CLI [#38](https://github.com/MTES-MCT/otelo/pull/38).
    - Possibilité d'impersonner un administrateur.
    - Importation d'utilisateurs à partir d'un fichier CSV.
- **Gestion des données** :
    - Import de données via la CLI.
    - Dataversioning implémenté.
    - Ajout de la gestion des besoins en renouvellement urbain.
    - Ajout de la gestion des besoins annuels de Sitadel.
- **Améliorations diverses** :
    - Ajout d'une page changelog.
    - Ajout de liens vers le centre d'aide et nouvelles illustrations.
    - Amélioration des descriptions des logements.
    - Ajout de la gestion des clés API et de leurs consommateurs.

### Évolutions techniques
- **Architecture & Infrastructure** :
    - Amélioration de la gestion des injections de modules CLI.
    - Correction de problèmes de build web.
    - Mise en place de tests E2E.
    - Correction de problèmes liés aux locks pnpm et amélioration du linting.
    - Amélioration de la gestion des erreurs et des tests.
- **API** :
    - Ajout d'énums Swagger pour une meilleure documentation.
    - Correction de problèmes liés aux mises à jour asynchrones.
- **Divers** :
    - Refactoring de la gestion des taux de disparition.
    - Amélioration de la gestion des données démographiques.

### Autres changements
- Mise à jour des wordings et des libellés dans l'interface utilisateur.
- Correction de bugs mineurs et améliorations de la stabilité.
- Amélioration de la gestion des templates d'emails (Brevo).
- Suppression de l'envoi d'emails en environnement local pour faciliter le développement.
- Correction du calcul de l'année de base dans les graphiques de comparaison.
- Amélioration de l'exportation des données Excel.
- Correction de la somme des besoins de renouvellement.
- Amélioration de la gestion des années de millésime.
