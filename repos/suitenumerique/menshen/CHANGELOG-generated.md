## Changelog : menshen (30 derniers jours, au 29 juillet 2026)

### Résumé
Ce mois a été marqué par une transition vers une architecture plus robuste et moderne, notamment avec le passage au framework `django-ninja`. Le code a été largement restructuré pour améliorer la maintenabilité et la lisibilité, tout en renforçant la sécurité et en facilitant l'intégration grâce à l'ajout d'un client API de base.

### Évolutions fonctionnelles
- Ajout d'un client API de base pour faciliter l'intégration du service par les développeurs.
- Renforcement de la sécurité en restreignant le périmètre (*scope*) de l'échange de jetons à `openid`.

### Évolutions techniques
- Migration du framework d'API vers `django-ninja` pour gagner en performance et en modernité.
- Refactorisation majeure de l'architecture interne : extraction de la logique métier (révocation de jetons, introspection, gestion des requêtes) vers des services dédiés et l'utilisation de *mixins* pour améliorer la structure du code.
- Amélioration de la qualité des réponses API via une simplification des messages d'erreur liés à la validation des jetons.
- Optimisation de la structure des énumérations (*Enums*) pour une meilleure clarté.
- Amélioration de l'observabilité avec l'ajout du support Django pour le SDK Sentry.
- Correction d'un bug lié à l'importation de modules.

### Autres changements
- Mise à jour de la commande d'exécution pour l'environnement de production.
- Optimisation de la CI/CD avec la correction de la version de l'action GitHub pour le login Docker.
- Nettoyage de la configuration en supprimant les paramètres OIDC inutilisés.
