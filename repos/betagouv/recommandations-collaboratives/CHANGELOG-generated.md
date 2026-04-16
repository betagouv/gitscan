## Changelog : recommandations-collaboratives (30 derniers jours, au 15 avril 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur, notamment dans les conversations et la gestion des documents, ainsi que par des corrections de bugs et des optimisations de performance. Des fonctionnalités ont été ajoutées pour faciliter la gestion des ressources et des tâches, et l'expérience utilisateur a été améliorée pour les conseillers.

### Évolutions fonctionnelles
- **Gestion des conversations :**
    - Ajout de la gestion des brouillons de recommandations pour les conseillers, incluant la possibilité de les créer, modifier et supprimer.
    - Amélioration de l'affichage des brouillons de recommandations dans le panneau de partage de contenu.
    - Intégration des brouillons de recommandations dans le flux de travail des conversations.
- **Gestion des documents :**
    - Distinction claire entre les documents privés et publics, avec des permissions d'accès appropriées.
    - Possibilité pour les conseillers de télécharger des documents privés.
    - Amélioration de l'affichage des documents dans le panneau de partage de contenu.
    - Ajout de notifications lors du téléchargement de documents.
- **Gestion des tâches :**
    - Amélioration de l'affichage et du filtrage des tâches.
    - Correction de bugs liés à la gestion des tâches et des actions associées.
- **CRM :**
    - Affichage des actions des utilisateurs et des objets associés dans le CRM.
    - Amélioration de l'affichage des informations sur les conseillers acceptés ou rejetés.
    - Correction de bugs liés à l'affichage des informations dans le CRM.
- **Statistiques :**
    - Correction d'un bug empêchant l'inclusion des tâches "NON_INTERESTED" dans les exports CSV.
    - Amélioration de la cohérence du filtrage des projets dans les statistiques et l'export CSV.
- **Interface utilisateur :**
    - Amélioration de l'accessibilité des panneaux de ressources et de partage de contenu.
    - Refonte du sélecteur de catégories pour une meilleure expérience utilisateur.
    - Suppression des alertes redondantes concernant les ressources.
    - Correction de liens et d'URL obsolètes.

### Évolutions techniques
- **Refactoring :**
    - Suppression de code mort et simplification de la logique dans plusieurs composants.
    - Amélioration de la gestion des états et des données dans les composants Alpine.js.
    - Standardisation de l'utilisation de `formatDate` pour la gestion des dates.
- **Dépendances :**
    - Mise à jour de plusieurs dépendances, notamment `Django`, `pytest`, `pillow`, `cryptography`, `vite`, `lodash`, `axios`, `picomatch`, `flatted`, `requests`, `uv` et les dépendances frontend.
- **CI/CD :**
    - Utilisation de `uv` pour la gestion des dépendances Python et la génération du fichier `requirements.txt`.
- **Infrastructure :**
    - Mise à jour de la configuration de Vite.
    - Ajout de fichiers `.gitignore` pour exclure les fichiers sensibles et temporaires.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les modifications apportées.
- Amélioration des tests unitaires et d'intégration.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout de commentaires pour clarifier la logique du code.
- Mise à jour des liens vers la documentation.
- Nettoyage du code et suppression de code redondant.
- Ajout d'un script de gestion des communes pour l'outil géomatique.
- Amélioration de la gestion des erreurs et des exceptions.
