## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 09 juillet 2026)

### Résumé
Ce mois-ci, les principales évolutions concernent l'implémentation de l'authentification WebAuthn, avec la gestion de l'enrôlement, de la vérification et de la finalisation du processus. Des améliorations ont également été apportées à l'interface utilisateur, notamment l'ajout d'un tableau de bord et la gestion des collections de documents. Enfin, des corrections et optimisations diverses ont été effectuées pour améliorer la stabilité et la sécurité de l'application.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord (TDB) avec affichage des collections d'indexation et de jeopardy sous forme d'onglets.
- Implémentation de l'authentification WebAuthn :
    - Ajout de formulaires d'enrôlement et d'authentification.
    - Gestion de l'initiation, de la vérification et de la finalisation de l'authentification.
    - Possibilité de s'authentifier avec une YubiKey (documentation ajoutée).
- Ajout d'un bouton pour lancer une identification de test.
- Possibilité de supprimer des documents.
- Ajout d'un formulaire pour "jeopardiser" une collection entière.
- Ajout d'un champ de recherche pour filtrer les documents.
- Affichage des informations de collections dans le TDB.
- Expose une API pour récupérer les documents des collections.
- Corrige l'enrôlement en fournissant le bon nom d'utilisateur.
- Corrige l'exécution de l’enrôlement et de l’authentification.

### Évolutions techniques
- Mise à jour de nombreuses dépendances (tailwindcss, vite, eslint, svelte, etc.) pour corriger des failles de sécurité et bénéficier des dernières améliorations.
- Sécurisation de la clef de session et du challenge dans la session côté serveur.
- Amélioration de la gestion des variables d'environnement pour l'authentification.
- Ajustement de la version de la GitHub Action pour le clonage du dépôt.
- Correction du typage du payload pour finaliser l’authentification.
- Encode en base 64 le challenge généré lors de l’initialisation de l’authentification.
- Utilisation de la bonne clef pour récupérer la clé publique de l’utilisateur.
- Ajout de l'action Renovate pour la gestion automatisée des dépendances.

### Autres changements
- Correction de l'encodage des noms de documents en UTF-8.
- Modification du prompt pour éviter les hallucinations.
- Retouche du design de la page d'authentification.
- Ajout de styles avec Tailwind CSS.
- Suppression des espaces potentiels lors de la construction des listes de fichiers.
- Ajout de documentation pour l'authentification avec YubiKey.
- Élargis la disposition du TDB.
- Filtre les documents sans chunks et les documents manquants.
- Récupère les collections d’indexation et de jeopardy.
- Renommage de la classe `ReponseCollection` en `ReponseCreationCollection`.
- Correction de la configuration du docker-compose pour inclure l'UI.
- Épingle les versions des dépendances des GitHub Actions.
