## Changelog : portail-rse (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation de l'export des données VSME au format PowerPoint (.pptx).  Cette nouvelle fonctionnalité permettra aux utilisateurs de générer des rapports plus visuels et adaptés à leurs besoins de présentation. Des améliorations et corrections ont également été apportées à l'interface utilisateur et à la gestion des données.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les données VSME au format PowerPoint (.pptx).  L'export comprend désormais des indicateurs, des tableaux et des informations d'entreprise sur la couverture.
- Amélioration des boutons de téléchargement pour les rapports VSME.
- Affichage de toutes les diapos dans l'export PPTX.
- Notification à l'utilisateur lors de l'enregistrement d'un indicateur.
- Redirection vers l'exigence de publication si la requête de l'indicateur n'est pas Htmx.
- Correction : La page de connexion s'affiche correctement même si la session a expiré pendant le remplissage d'un indicateur.
- Correction : Empêche la suppression involontaire de lignes dans les tableaux lors de l'utilisation de la touche Entrée.

### Évolutions techniques
- Refactorisation importante du code d'export PPTX pour simplifier la logique et améliorer la maintenabilité.
- Utilisation d'un nouveau modèle PPTX plus complet pour l'export VSME.
- Optimisation du remplissage des tableaux dans l'export PPTX, notamment pour les tableaux à lignes variables et fixes.
- Déplacement des fichiers modèles (XLSX et PPTX) pour une meilleure organisation.
- Mise à jour des dépendances : `cryptography` (46.0.7 -> 48.0.1), `aiohttp` (3.13.4 -> 3.14.1), `pyjwt` (2.12.1 -> 2.13.0).
- Ajout de l'attribut `EXT_ID` de Brevo.

### Autres changements
- Correction de typos dans les labels VSME.
- Complétion du diagramme d'overview de la documentation.
- Suppression de lignes vides en fin de fichier.
- Suppression de diapos inutilisées dans le template PPTX.
- Ajout d'une URL protégée pour la fourniture d'un fichier PPTX vide.
- Alignement de l'image de fond sur la diapo 51 du template PPTX.
