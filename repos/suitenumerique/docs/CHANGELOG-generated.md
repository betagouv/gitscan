## Changelog : docs (30 derniers jours, au 2026-07-03)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec une nouvelle barre flottante, un menu utilisateur, des améliorations de l'accessibilité et de la recherche. Des corrections de bugs et des optimisations de performance ont également été apportées, notamment pour la gestion des documents et des commentaires. Enfin, des fonctionnalités d'administration et de gestion des utilisateurs ont été ajoutées.

### Évolutions fonctionnelles
- Ajout d'un menu utilisateur pour une meilleure gestion du profil et des préférences [#2463](https://github.com/suitenumerique/docs/issues/2463).
- Nouvelle barre flottante en haut de l'écran pour un accès rapide aux fonctions principales [#2471](https://github.com/suitenumerique/docs/issues/2471).
- Possibilité de quitter un document.
- Les utilisateurs non authentifiés peuvent désormais effectuer des recherches.
- Ajout d'un bouton pour créer des sous-documents.
- Ajout d'un support pour les liens `mailto:` dans le menu d'aide.
- Ajout d'une limite au nombre de réactions par commentaire, avec une interface utilisateur correspondante [#1978](https://github.com/suitenumerique/docs/issues/1978).
- Possibilité de réinitialiser un document via une commande de gestion.

### Évolutions techniques
- Refactorisation de la suppression d'un utilisateur pour gérer correctement les relations.
- Amélioration de la performance lors de la récupération de l'arborescence des documents.
- Optimisation des requêtes pour la récupération des commentaires d'un fil de discussion afin de corriger un problème N+1.
- Mise à jour de la gestion des erreurs de connexion à la base de données lors des tests.
- Monture d'un certificat CA personnalisé dans le déploiement yprovider (helm).
- Suppression d'un backend d'authentification inutilisé.
- Correction d'un problème de rechargement de la page lors du focus sur un onglet.
- Correction d'un problème de positionnement du composant Waffle.
- Correction d'un problème de regression dans les tests d'export.
- Ajout de tests pour la conversion HTML/markdown.
- Mise à jour des dépendances de sécurité (PyJWT).

### Autres changements
- Améliorations de l'accessibilité :
    - Suppression d'attributs `aria-label` redondants.
    - Amélioration de la navigation au clavier et des annonces pour le mode présentateur.
    - Utilisation d'éléments de titre appropriés pour la section des documents épinglés.
    - Amélioration de l'accessibilité des composants de recherche.
- Ajout d'un badge DPG au README.
- Mise à jour des chaînes de traduction.
- Correction de fautes de frappe dans le guide de contribution.
- Suppression de Crisp du projet.
- Ajout d'un sous-menu légal configurable dans le menu d'aide.
- Suppression d'une tâche CI inutile.
- Ajout de la configuration `CONVERSION_UPLOAD_ENABLED` manquante dans la documentation.
- Epinglage des dépendances Prosemirror pour éviter des regressions.
- Correction d'une alerte de sécurité JavaScript.
