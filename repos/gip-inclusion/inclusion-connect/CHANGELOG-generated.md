## Changelog : inclusion-connect (30 derniers jours, au 16 septembre 2026)

### Résumé
Les récentes interventions se sont concentrées sur le renforcement de la sécurité du système d'authentification et la mise à jour des composants critiques du service pour garantir la robustesse de la plateforme.

### Évolutions techniques
- **Sécurité & Authentification** : Renforcement du protocole OIDC via l'implémentation du hachage des secrets clients (`hash_client_secret`).
- **Qualité logicielle** : Amélioration de la fiabilité des tests en supprimant l'utilisation de secrets clients par défaut.
- **Maintenance des dépendances** : Mise à jour de la bibliothèque de gestion de l'authentification `django-oauth-toolkit`.
