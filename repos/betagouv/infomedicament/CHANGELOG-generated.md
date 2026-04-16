## Changelog : infomedicament (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration des performances du site, en particulier sur la page d'accueil et les pages de médicaments. Des optimisations ont été apportées pour réduire le temps de chargement et améliorer l'expérience utilisateur.  De plus, l'infrastructure a été renforcée avec la mise en place de bases de données PostgreSQL isolées pour les environnements de revue d'applications, et l'ajout de données HAS (ASMR et SMR). Enfin, des informations supplémentaires sur les présentations des médicaments ont été ajoutées.

### Évolutions fonctionnelles
- Ajout d'informations issues de la table CNAM_Retro sur les présentations des médicaments. [#1234](https://github.com/betagouv/infomedicament/issues/1234)
- Affichage d'informations sur le statut de commercialisation des médicaments.
- Ajout de badges d'informations sur les présentations des médicaments.
- Calcul dynamique du nombre de médicaments commercialisés.
- Ajout d'un indicateur de fraîcheur des données dans le modal d'accueil.
- Ajout de surlignages dans la page médicament pour le glossaire.
- Correction : Autorisation d'un plus grand nombre de caractères dans les titres de page.
- Correction : Prévention d'une vulnérabilité IDOR sur la soumission avancée de notes.

### Évolutions techniques
- Optimisation des performances de la page d'accueil :
    - Optimisation de l'SVG de la page d'accueil avec svgo.
    - Suppression du chargement précoce (prefetching) des articles sur la page d'accueil.
    - Déplacement de la fonction de sanitisation HTML vers la couche de données côté serveur.
    - Chargement paresseux (lazy-loading) des composants de la vue détaillée des médicaments.
    - Rendu synchrone des enfants dans `ContentContainer` pour améliorer le LCP (Largest Contentful Paint).
- Refactorisation :
    - Suppression de la dépendance MUI pour les étoiles de notation.
    - Remplacement de l'Autocomplete MUI par une combobox personnalisée.
    - Suppression de l'utilisation de `setState` dans `useCallback`.
- Infrastructure :
    - Provisionnement de bases de données PostgreSQL isolées par environnement de revue d'application.
    - Ajout de scripts pour initialiser les bases de données des environnements de revue d'application à partir de la base de staging.
    - Mise à jour vers Next.js 16.1.6.
    - Ajout d'une interface OpenSearch pour le développement local.
- Amélioration de la sécurité :
    - Limitation du nombre de requêtes à l'endpoint `/rating` (2 requêtes par IP par minute).
    - Ajout de règles de validation plus strictes pour les notes.
- Ajout de tests unitaires et d'intégration.
- Mise à jour du linter vers ESLint.

### Autres changements
- Ajout de la vérification de la console de recherche Google.
- Ajout de données HAS (ASMR et SMR) à la base de données PostgreSQL.
- Suppression des tests d'interface utilisateur.
- Corrections de linting et de style.
- Ajout de configurations pour les environnements de revue d'application.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de code pour gérer les codes CIS dans les scripts de revue d'application.
- Correction de problèmes liés au chargement des images Leaflet dans les environnements de revue d'application.
- Correction de problèmes liés aux migrations de base de données.
- Ajout de commentaires et de documentation.
