## Changelog : mon-service-securise (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des administrateurs, la refonte du parcours d'homologation avec une nouvelle interface en SPA (Single Page Application), et des corrections d'accessibilité et d'ergonomie. Des améliorations techniques ont également été apportées, notamment la migration de composants vers TypeScript et la mise à jour de dépendances.

### Évolutions fonctionnelles
- **Gestion des administrateurs :**
    - Ajout de la possibilité d'inviter et de gérer les administrateurs d'une entité. [#1234](https://github.com/betagouv/mon-service-securise/issues/1234)
    - Implémentation de la récupération de la liste des administrateurs associés à une entité.
    - Possibilité de nommer des administrateurs en tant que superviseurs.
    - Affichage du nombre d'utilisateurs et de services associés à chaque entité supervisée.
- **Parcours d'homologation :**
    - Refonte complète du parcours d'homologation avec une nouvelle interface en SPA.
    - Ajout des étapes "Récapitulatif", "Avis", "Téléchargement du dossier" et "Décision".
    - Navigation entre les étapes du parcours.
    - Affichage d'un étapier pour suivre la progression.
    - Possibilité de sauvegarder la décision d'homologation.
- **Améliorations diverses :**
    - Ajout de landings pour "Sécurisez votre service numérique" et "Industrialisez vos homologations".
    - Amélioration de l'affichage des informations sur la page d'accueil (bloc "Notre équipe", "Communauté").
    - Correction de l'affichage de l'indice cyber personnalisé.
    - Ajout d'une modale pour la démarche d'homologation indicative.

### Évolutions techniques
- **Migration vers TypeScript :** Conversion de plusieurs composants et services vers TypeScript pour améliorer la maintenabilité et la robustesse du code.
- **Refactoring :**
    - Extraction de composants et fonctions pour améliorer la modularité et la réutilisabilité du code.
    - Suppression de code obsolète.
- **Infrastructure :**
    - Mise à jour de plusieurs dépendances (eslint, axios, uuid, etc.).
    - Chiffrement des données sensibles dans les tables `superviseur` et `admin_organisations`.
    - Utilisation d'un nouveau dépôt de données pour les superviseurs.
- **Tests :** Ajout de tests d'accessibilité et correction des problèmes identifiés.

### Autres changements
- Amélioration de l'accessibilité de plusieurs pages (Statistiques, CGU, Activation, Connexion, Création de service, Mentions Légales, Accessibilité, Politique de Confidentialité, Inscription).
- Correction de problèmes de style et d'affichage sur différentes pages.
- Ajout de commentaires et documentation pour améliorer la compréhension du code.
- Correction de fuites CSS.
- Mise à jour de la documentation.
