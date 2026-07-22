## Changelog : anssi-recommandations-cyber-data (30 derniers jours, au 21 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'interface utilisateur et la gestion des documents, notamment avec l'ajout d'un tableau de bord (TDB) plus complet pour la gestion des collections et des documents. Des corrections ont également été apportées pour améliorer la robustesse et la sécurité de l'application. L'automatisation des mises à jour de dépendances a été renforcée.

### Évolutions fonctionnelles
- Ajout d'un formulaire permettant de "jeopardiser" (supprimer ?) une collection de documents.
- Implémentation d'un filtre de recherche pour les documents.
- Affichage des collections d'indexation et de jeopardy dans un tableau de bord unifié.
- Possibilité de supprimer des documents.
- Affichage des informations sur les collections (nom, contenu) dans le tableau de bord.
- Redirection vers le TDB après authentification.
- Correction de l'enrôlement des utilisateurs (correction du nom d'utilisateur fourni).
- Correction de l'encodage des noms de documents en UTF-8 pour éviter les problèmes d'affichage.
- Amélioration du prompt pour réduire les "hallucinations" du modèle.
- Ajout d'une documentation spécifique pour l'authentification avec YubiKey.

### Évolutions techniques
- Mise en place d'un outil de validation de la configuration (`zizmor`) pour renforcer la sécurité.
- Désactivation des identifiants `git` dans les dépôts clonés pour des raisons de sécurité.
- Ajout de l'action Renovate pour l'automatisation des mises à jour de dépendances.
- Mises à jour de nombreuses dépendances (voir section "Autres changements").

### Autres changements
- Mises à jour régulières des dépendances (eslint-plugin-svelte, tailwindcss, @lab-anssi/ui-kit, postcss, @tailwindcss/vite, prettier, vitest, @eslint/compat, @sveltejs/vite-plugin-svelte, lint-staged, etc.) via Renovate. Ces mises à jour incluent des correctifs de sécurité pour plusieurs dépendances (aiohttp, pyjwt, starlette, vitest, python-multipart).
- Amélioration de la disposition du TDB et de la page d'authentification.
- Renommage d'une classe pour plus de clarté.
- Ajout de routes API pour récupérer les informations sur les collections et les documents associés.
- Récupération et affichage de la liste des documents pour chaque collection.
