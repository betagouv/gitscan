## Changelog : accounts (30 derniers jours, au 07/09/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration du parcours utilisateur lors des phases de connexion et de déconnexion, tout en renforçant la fiabilité technique du protocole d'authentification OIDC.

### Évolutions fonctionnelles
- Amélioration de l'interface de connexion avec l'ajout d'une page intermédiaire.
- Optimisation du processus de déconnexion : la confirmation de déconnexion (RP-Initiated logout) est désormais transmise au frontend pour une meilleure expérience utilisateur.

### Évolutions techniques
- Amélioration de la gestion du protocole OIDC : réécriture de la réponse d'introspection lors du recours aux backends PSA et correction du nommage des paramètres d'indice d'introspection.

### Autres changements
- Stabilisation de l'environnement de développement par le verrouillage de la version Node.js (v22) pour l'outil de parsing des traductions (`i18next-parser`).
