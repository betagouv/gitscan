## Changelog : service-national-universel (30 derniers jours)

### Résumé
Les dernières mises à jour du Service National Universel se concentrent sur l'amélioration de la gestion des emails, notamment en réponse à des problèmes de délivrabilité avec Microsoft, et sur le renforcement des contrôles d'accès pour la suppression des utilisateurs. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Ajout de dates de réception du passeport dans le schéma "Young" via l'API. (#5255)
- Les super-modérateurs sont désormais les seuls autorisés à supprimer des utilisateurs. (#5241)
- Une alerte est maintenant affichée sur les pages de connexion et d'accueil de l'administration en cas de problèmes d'envoi d'emails. (#5247)
- Amélioration des vérifications du statut des référents pour prendre en compte les référents inactifs. (#5250)

### Évolutions techniques
- Mise à jour des versions de certaines librairies spécifiques. (#5245)
- Réintroduction du filtrage des domaines email Microsoft dans la tâche cron `noticePushMission` pour gérer les problèmes de délivrabilité. (#5254)
- Ajout de fonctions pour détecter les domaines email publics Microsoft afin de filtrer les envois. (#5251, #5252)
- Suppression temporaire du filtrage des domaines email Microsoft suite à des problèmes. (#5253)

### Autres changements
- Fin de la mitigation concernant les problèmes de délivrabilité des emails Microsoft. (#5255)
