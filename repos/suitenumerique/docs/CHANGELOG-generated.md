## Changelog : docs (30 derniers jours, au 5 novembre 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de la collaboration grâce à l'introduction des mentions d'utilisateurs et d'une meilleure gestion des sous-documents. L'interface de l'éditeur a été affinée (emojis, listes de tâches) et les outils d'administration ont été considérablement enrichis pour faciliter la gestion des utilisateurs et des contenus.

### Évolutions fonctionnelles
- **Collaboration & Mentions** : 
    - Ajout de la possibilité de mentionner des utilisateurs via un menu déroulant (`@`) avec affichage du contenu en ligne et notifications.
    - Amélioration de la gestion des sous-documents avec un nouveau bloc `/children` pour lister les documents enfants.
- **Éditeur & Interface** :
    - Intégration du sélecteur d'emojis "Frimousse" pour une meilleure expérience de saisie.
    - Amélioration du rendu visuel : style natif pour les listes de tâches, gestion des niveaux de titres (1 à 3) et correction de l'italique dans l'éditeur.
    - Optimisation de l'affichage mobile (placeholders de paragraphes) et de l'accessibilité (bouton d'accueil, chargeur d'upload, arbre de documents).
- **Export & Impression** :
    - Corrections sur l'export PDF pour assurer le bon fonctionnement des liens internes, des diagrammes et de l'habillage du texte long.

### Évolutions techniques
- **Administration & Gestion** :
    - Nouveaux outils d'administration pour fusionner des utilisateurs, transférer des documents/invitations et gérer les doublons.
    - Amélioration du suivi avec l'affichage de la dernière connexion des utilisateurs et des informations de version dans l'admin.
- **Sécurité & Permissions** :
    - Renforcement des droits de suppression pour les sous-documents (nécessite des droits d'édition).
    - Sécurisation de l'accès aux fils de discussion et aux commentaires.
- **Performance & Infrastructure** :
    - Optimisation de la recherche utilisateur via des index trigrammes.
    - Amélioration des performances de `yhub` via la mise en cache des décisions d'autorisation et l'optimisation des appels backend.
    - Mise à jour de l'infrastructure (images Nginx non-privilégiées, configuration Helm pour les sondes de santé).
- **Intelligence Artificielle** :
    - Ajout de nouvelles compétences (skills) pour les agents et amélioration de leur résilience et efficacité.

### Autres changements
- **Internationalisation** : Mises à jour régulières des chaînes de traduction et ajout de contexte pour Crowdin.
- **Documentation** : Mise à jour des guides de démarrage, de la documentation des agents et de la liste des variables d'environnement.
- **Nettoyage** : Suppression de dépendances inutilisées (Pillow, easy-thumbnails) et nettoyage de certains assets de police.
