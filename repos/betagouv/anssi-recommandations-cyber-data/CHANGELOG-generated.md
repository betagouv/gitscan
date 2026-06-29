## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation de l'authentification WebAuthn (yubikey), l'amélioration de l'interface utilisateur pour la gestion des collections de documents et l'ajout de fonctionnalités pour faciliter la recherche et l'affichage des documents indexés. Des corrections de sécurité ont également été apportées pour maintenir l'intégrité du système.

### Évolutions fonctionnelles
- Ajout d'une documentation pour l'authentification avec une yubikey.
- Implémentation de l'authentification WebAuthn (yubikey) :
    - Possibilité d'enrôler et d'authentifier une clef WebAuthn.
    - Ajout de routes pour l'initialisation, la finalisation et la vérification de l'authentification.
- Amélioration de l'interface utilisateur :
    - Affichage des collections d'indexation et de "jeopardy" dans un tableau.
    - Ajout d'un champ de recherche pour filtrer les documents.
    - Affichage des documents pour chaque collection.
    - Affichage des informations des collections sous forme d'onglets.
    - Modification du design de la page d'authentification.
- Ajout d'une page "Tableau de bord" protégée par authentification.

### Évolutions techniques
- Sécurisation de la clef de session et du challenge dans la session côté serveur.
- Correction de l'exécution de l'enrôlement et de l'authentification WebAuthn.
- Ajustement de la version de la GitHub Action pour le clonage du dépôt.
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité : `aiohttp`, `pyjwt`, `starlette`, `python-multipart`, `vite`, `vitest`.
- Correction du typage du payload pour finaliser l’authentification.
- Utilisation de la bonne clef pour récupérer la clé publique de l’utilisateur.
- Encapsulation du challenge généré lors de l’initialisation de l’authentification en base64.

### Autres changements
- Renommage de la classe `ReponseCollection` en `ReponseCreationCollection` pour plus de clarté.
- Suppression des espaces potentiels lors de la construction des listes de fichiers.
- Ajout de variables d'environnement explicites pour l'authentification.
- Correction de la configuration du `docker-compose` pour inclure l'interface utilisateur.
- Épinglage des versions des dépendances des GitHub Actions pour assurer la reproductibilité des builds.
- Dépose du fichier d’évaluation ainsi que du mapping dans un répertoire temporaire.
