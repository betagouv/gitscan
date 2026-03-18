## Changelog : infomedicament (30 derniers jours, au 4 mars 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent principalement sur la recherche de médicaments. L'expérience utilisateur a été significativement améliorée avec un tri des résultats plus pertinent, une autocomplétion plus intelligente et l'ajout d'informations supplémentaires sur les médicaments. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Recherche :** Les résultats de recherche sont désormais triés en fonction du type de correspondance (nom exact, spécialité, etc.) [#197](https://github.com/betagouv/infomedicament/pull/197).
- **Recherche :** L'autocomplétion propose désormais des noms de spécialités en plus des noms de médicaments [#191](https://github.com/betagouv/infomedicament/pull/191).
- **Recherche :** La recherche est limitée à 100 résultats pour améliorer la performance.
- **Recherche :** Ajout de badges d'explication pour les codes ATC et les substances.
- **Recherche :** Cliquer sur une spécialité dans les résultats de recherche ouvre maintenant la page correspondante.
- **Page médicament :** Intégration de toutes les données disponibles pour une page médicament spécifique [#157](https://github.com/betagouv/infomedicament/pull/157).
- **Liste des médicaments :** Correction de l'ordre des lettres dans la liste des médicaments.

### Évolutions techniques
- **CI/CD :** Ajout de Lighthouse pour évaluer la performance des applications de revue (review apps).
- **CI/CD :** Amélioration de l'attente pour la vérification de l'application Scalingo dans le workflow CI.
- **CI/CD :** Ajout de tests lint et unitaires au CI GitHub.
- **Base de données :** Migration de la base de données pour optimiser la recherche et l'utilisation des données.
- **Refactoring :** Simplification du code et de l'interface utilisateur de la recherche.
- **Refactoring :** Suppression de code inutilisé après la refactorisation de la recherche.
- **Sentry :** Réduction du taux d'échantillonnage de Sentry à 10% et suppression de l'intégration coûteuse de la relecture.
- **Sentry :** Correction de problèmes liés à Sentry et ajout de la permission nécessaire dans le CSP.
- **Scripts :** Correction d'un problème de blocage du script PDBM en fermant la connexion MySQL.
- **Tests :** Ajout de tests unitaires pour la recherche et correction d'un test manquant.

### Autres changements
- **Documentation :** Ajout d'une commande `db:update-resume` pour mettre à jour les données de résumé.
- **Configuration :** Suppression d'une ancienne migration de base de données.
- **Correction :** Correction d'un problème d'importation dans le script `updateResumeData`.
- **Correction :** Correction d'un problème d'ordre d'exécution des migrations.
- **Correction :** Correction d'un problème lié à un gestionnaire d'événements.
- **Correction :** Correction de l'ordre des lettres dans la liste des médicaments.
- **Outils :** Ajout de `@next/bundle-analyzer` aux dépendances de développement pour l'analyse de la taille des bundles.
- **Linting :** Application du linting pour améliorer la qualité du code.
