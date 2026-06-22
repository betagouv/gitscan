## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation et la sécurisation de l'authentification WebAuthn.  De nouvelles fonctionnalités permettent l'enrôlement et l'authentification des utilisateurs via cette méthode, avec une attention particulière portée à la sécurité des clés et des sessions. L'interface utilisateur a également été améliorée avec l'ajout d'un tableau de bord protégé et de boutons d'enrôlement et d'identification.

### Évolutions fonctionnelles
- Ajout d'une page protégée "Tableau de bord" accessible après authentification.
- Implémentation de l'enrôlement et de l'authentification WebAuthn :
    - Ajout de boutons d'enrôlement et d'identification.
    - Possibilité de saisir les identifiants pour l'enrôlement et l'authentification.
    - Initialisation de l'enrôlement d'une clé.
    - Ajout d'un bouton d'identification de test.
- Amélioration de la gestion des erreurs : retour d'une erreur si l'utilisateur est inconnu.
- Correction de l'exécution de l'enrôlement et de l'authentification.
- Correction du typage du payload pour finaliser l’authentification.
- Ajout des routes `/auth/finalise` pour finaliser l’authentification.

### Évolutions techniques
- Sécurisation de la clé de session et du challenge dans la session côté serveur.
- Utilisation de la bonne clé pour récupérer la clé publique de l’utilisateur.
- Mise à jour de la librairie `starlette` pour des raisons de sécurité.
- Ajustement de la version de la GitHub Action pour le clonage du dépôt.
- Implémentation de la recherche d'utilisateurs pour l'authentification.
- Passage de la clé publique de l’utilisateur au service de vérification.
- Génération d'un token JWT et ajout de ce token à la session.
- Correction de l'intégration de l'UI dans le Docker Compose.
- Modification de la collection.
- Ajout de style avec Tailwind.
- Suppression des espaces potentiels lors de la construction des listes de fichiers.
- Dépose du fichier d’évaluation ainsi que du mapping dans un répertoire temporaire.

### Autres changements
- Explicitation des variables d’environnement pour l’authentification.
- Épinglage des versions des dépendances des GitHub Actions pour une meilleure reproductibilité.
- Revert d'une version de la GHA.
