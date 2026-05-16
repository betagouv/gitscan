## Changelog : Docurba (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, Docurba a bénéficié d'améliorations significatives en termes de gestion des procédures et des données, notamment concernant la loi Huwart. L'interface utilisateur a également été améliorée avec un nouveau menu utilisateur et des corrections pour la navigation et la recherche. Des efforts importants ont été consacrés à l'amélioration de la qualité du code, des tests et de l'infrastructure.

### Évolutions fonctionnelles
- **Interface utilisateur :** Nouveau menu déroulant pour l'utilisateur, remplaçant les boutons d'authentification dans l'en-tête [#1868](https://github.com/MTES-MCT/Docurba/pull/1868).
- **Navigation :** Le département sélectionné est maintenant conservé lors de la navigation.
- **Recherche :** Synchronisation des champs de recherche avec les paramètres de l'URL.
- **Gestion des procédures :**
    - Ajout d'un indicateur pour identifier les procédures démarrées avant la loi Huwart.
    - Mise à jour du type de procédure (PLU vers PLUi) en masse.
    - Suppression des événements de fin d'échéance pour se conformer à la loi Huwart.
    - Expose les thématiques des procédures dans l'API SCoT et communes.
- **Authentification :** Redirection de l'utilisateur vers le tableau de bord après la récupération du mot de passe.

### Évolutions techniques
- **Architecture :** L'application `internal_api` a été déplacée dans le répertoire `docurba`.
- **Tests :**
    - Intégration de FactoryBoy pour la création d'objets de test.
    - Création de factories pour les objets User, Profile, Procedure et CommuneProcedure.
    - Amélioration des tests de l'API SCoT.
    - Correction de tests instables.
- **Infrastructure :**
    - Augmentation du plan Supabase et de la taille du disque pour les applications de revue.
    - Utilisation d'un environnement virtuel (venv).
    - Mise à jour du Makefile pour simplifier les tâches.
- **Code :**
    - Refactoring du code pour améliorer la lisibilité et la maintenabilité.
    - Ajout d'annotations de type pour améliorer la sécurité du code.
    - Correction de conflits de migration Django.
    - Distinction du type de collectivité EPCI des autres.
    - Ajout d'un dossier `exports` (ignoré par le contrôle de version).
    - Ajout de noms de routes pour faciliter l'utilisation de `reverse`.

### Autres changements
- **Documentation :** Mise à jour de la documentation de l'API pour inclure les thématiques des communes et des SCoT.
- **Configuration :** Ajout d'un choix de texte pour le type de commune.
- **Nettoyage de code :** Suppression de code obsolète et amélioration de la structure du projet.
- **Dépendances :** Mises à jour de dépendances (pytest, ruff, django-debug-toolbar, django, urllib3, pre-commit) (non listées individuellement).
