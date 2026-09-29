## Changelog : inclusion-connect (30 derniers jours, au 28 septembre 2026)

### Résumé
Les récentes interventions se sont concentrées sur le renforcement de la sécurité du protocole d'authentification (OIDC) et le nettoyage de la base de code.

### Évolutions techniques
- **Sécurité & Authentification** : Amélioration de la gestion des secrets clients via l'implémentation du hachage (`hash_client_secret`) dans les configurations OIDC.
- **Tests** : Sécurisation de la suite de tests en supprimant l'utilisation d'un secret client par défaut.
- **Dépendances** : Mise à jour de la bibliothèque de gestion OAuth2 (`django-oauth-toolkit` vers la version 3.4.1).

### Autres changements
- **Nettoyage** : Suppression d'un ancien template devenu obsolète.
