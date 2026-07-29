## Changelog : domifa (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette version apporte des corrections de sécurité, des améliorations de la gestion des erreurs et des ajustements sur l'interface utilisateur, notamment au niveau des formulaires et des pages d'information. Des optimisations ont également été apportées à l'infrastructure pour améliorer la sécurité et la performance.

### Évolutions fonctionnelles
- Correction du formulaire de mot de passe sur le frontend pour une meilleure expérience utilisateur.
- Ajout de domaines et d'adresses email à une liste blanche pour améliorer la sécurité et la gestion des accès.
- Mise à jour des pages CGU et FAQ avec du nouveau contenu.
- Amélioration de la gestion des erreurs et des alertes sur le frontend.
- Correction de l'affichage de la liste des utilisateurs dans l'administration.

### Évolutions techniques
- Amélioration de la sécurité en servant les headers de sécurité depuis le serveur Nginx de l'application plutôt que depuis l'ingress.
- Refactorisation de la configuration Nginx pour partager un seul fichier de configuration entre les différentes images SPA.
- Migration des builds d'images vers buildkit-operator pour une meilleure gestion des builds Docker.
- Correction de problèmes liés à l'enregistrement des adresses IP.
- Mise à jour de la dépendance `typeorm` vers la version 0.3.31.

### Autres changements
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour de la documentation.
- Nettoyage du code et amélioration de la lisibilité.
