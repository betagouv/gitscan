## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation de l'authentification WebAuthn (yubikey) et l'amélioration de l'interface utilisateur, notamment avec l'ajout d'un tableau de bord et la gestion des collections de documents. Des corrections de sécurité et des ajustements techniques ont également été apportés pour stabiliser et sécuriser l'application.

### Évolutions fonctionnelles
- **Authentification WebAuthn :** Implémentation complète de l'authentification avec yubikey, incluant l'enrôlement, la vérification et la finalisation du processus. Une documentation spécifique à l'utilisation de la yubikey a été ajoutée. [#1234 (exemple)]
- **Tableau de bord :** Ajout d'un tableau de bord protégé, accessible après authentification.
- **Gestion des collections :**
    - Affichage des collections d'indexation et de jeopardy dans un tableau.
    - Possibilité de filtrer les documents par collection.
    - Affichage des informations de chaque collection sous forme d'onglets.
    - Récupération et exposition via une API des informations sur les collections.
- **Recherche de documents :** Ajout d'un champ de recherche pour filtrer les documents.
- **Amélioration de l'interface utilisateur :**
    - Retouche du design de la page d'authentification.
    - Amélioration de la disposition du tableau de bord.

### Évolutions techniques
- **Sécurité :**
    - Sécurisation de la clé de session et du challenge côté serveur.
    - Mise à jour de la librairie `starlette` pour corriger des failles de sécurité.
- **Docker :** Correction de la configuration Docker Compose pour inclure l'interface utilisateur.
- **GitHub Actions :** Épinglage des versions des dépendances des GitHub Actions pour une meilleure stabilité.
- **Typage :** Correction du typage du payload pour l'authentification.
- **Gestion des fichiers :** Suppression des espaces potentiels lors de la construction des listes de fichiers.

### Autres changements
- Ajout d'une documentation pour l'authentification avec la yubikey uniquement.
- Renommage d'une classe pour plus de clarté.
- Ajout de variables d'environnement explicites pour l'authentification.
- Correction de l'exécution de l'enrôlement et de l'authentification.
- Utilisation de la bonne clé pour récupérer la clé publique de l'utilisateur.
- Ajustement de la version de la GHA pour le clonage du dépôt.
- Retour à une version précédente de la GHA.
- Ajout d'une route `/auth/finalise` pour finaliser l'authentification.
- Correction d'une erreur lors de la création de fichiers temporaires.
