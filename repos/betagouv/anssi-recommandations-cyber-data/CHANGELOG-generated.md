## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'implémentation de l'authentification WebAuthn (YubiKey), l'amélioration de l'interface utilisateur pour la gestion des documents et des collections, et des corrections de sécurité. Des améliorations de l'expérience utilisateur sont également apportées, notamment avec l'ajout d'un tableau de bord.

### Évolutions fonctionnelles
- Ajout d'une documentation pour l'authentification avec une YubiKey.
- Implémentation de l'authentification WebAuthn (YubiKey) :
    - Possibilité d'enrôler et d'utiliser une YubiKey pour l'authentification.
    - Ajout de routes pour l'initialisation, la finalisation et la vérification de l'authentification.
- Amélioration de l'interface utilisateur :
    - Affichage des collections d'indexation et de "jeopardy" dans un tableau de bord (TDB).
    - Affichage des documents associés à chaque collection.
    - Ajout d'un champ de recherche pour filtrer les documents.
    - Amélioration du design de la page d'authentification.
    - Ajout d'un bouton d'identification de test.
- Ajout d'un tableau de bord protégé accessible après authentification.
- Possibilité de récupérer la liste des documents pour chaque collection via l'API `/api/documents`.
- Expose une route GET `/api/collections` pour obtenir des informations sur les collections d'indexation et de jeopardy.

### Évolutions techniques
- Sécurisation de la clef de session et du challenge dans la session côté serveur.
- Correction de l'exécution de l'enrôlement et de l'authentification WebAuthn.
- Correction du typage du payload pour finaliser l'authentification.
- Utilisation de la bonne clef pour récupérer la clé publique de l'utilisateur.
- Ajustement de la version de la GitHub Action pour le clonage du dépôt.
- Mise à jour de la dépendance `starlette` pour corriger une vulnérabilité de sécurité.
- Correction d'un problème lié au dépôt temporaire des fichiers d'évaluation et de mapping.

### Autres changements
- Renommage de la classe `ReponseCollection` en `ReponseCreationCollection` pour plus de clarté.
- Explicitation des variables d'environnement pour l'authentification.
- Ajout de style avec Tailwind CSS.
- Suppression des espaces potentiels lors de la construction des listes de fichiers.
- Épinglage des versions des dépendances des GitHub Actions pour assurer la stabilité.
