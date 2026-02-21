## Changelog : service-national-universel (30 derniers jours)

### Résumé
Les dernières mises à jour du Service National Universel se concentrent sur l'amélioration de la gestion des emails, notamment en réponse à des problèmes de délivrabilité avec Microsoft, et sur le renforcement des permissions d'administration. Des corrections ont également été apportées pour améliorer la robustesse de l'API et de l'interface d'administration.

### Évolutions fonctionnelles
- Ajout des dates de réception du passeport dans les informations du jeune via l'API (#5255).
- Les super-modérateurs sont désormais les seuls autorisés à supprimer des utilisateurs (#5241).
- Une alerte est affichée sur les pages de connexion et d'accueil de l'administration en cas de problèmes d'envoi d'emails (#5247).
- Amélioration de la gestion des statuts des référents dans l'API pour prendre en compte les référents inactifs (#5250).

### Évolutions techniques
- Montée de version de librairies spécifiques (lib' spécifiques) (#5245).
- Mise en place d'un filtrage temporaire des domaines email Microsoft pour atténuer les problèmes de délivrabilité, puis suppression de ce filtrage après investigation (#5251, #5252, #5253, #5254, #5255).
- Ajout de fonctions pour détecter les domaines email publics Microsoft (#5251).
