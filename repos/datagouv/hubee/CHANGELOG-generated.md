## Changelog : hubee (30 derniers jours, au 27 août 2026)

### Résumé
Ce mois a été marqué par une refonte majeure du système d'authentification et le lancement de la version 2 de l'API. Les évolutions se concentrent sur la sécurisation des accès via ProConnect (support de l'authentification multi-facteurs et du standard OIDC), l'amélioration de l'expérience utilisateur sur le portail et le renforcement de la traçabilité des décisions d'accès.

### Évolutions fonctionnelles
- **Amélioration de la connexion :** Intégration native du protocole OIDC avec ProConnect et prise en compte de l'authentification multi-facteurs (MFA) imposée par le fournisseur d'identité.
- **Gestion des sessions :** Renforcement de la sécurité des sessions par l'imposition de limites d'inactivité et de durées de connexion maximales.
- **Expérience utilisateur (Portail) :** 
    - Déplacement des éléments d'identité et de déconnexion dans l'en-tête pour une meilleure ergonomie.
    - Amélioration de la clarté des messages d'erreur et ajout d'options de recours en cas d'échec de connexion.
- **Gestion des agents :** 
    - Enrichissement des profils (ajout de la civilité, du rôle, de la fonction et normalisation internationale des numéros de téléphone).
    - Amélioration du système de rattachement des agents à leurs organisations via le SIRET.

### Évolutions techniques
- **Lancement de l'API V2 :** 
    - Mise en place du socle OAuth2 (flux `client_credentials`).
    - Protection des points d'accès par jetons avec attribution des appels.
    - Automatisation de la purge quotidienne des jetons expirés.
    - Uniformisation des réponses d'erreur (standardisation du code 401).
- **Sécurité et Authentification :**
    - Migration de la gestion ProConnect vers une implémentation OIDC native (sortie d'OmniAuth).
    - Chiffrement des jetons ProConnect au repos en base de données.
    - Renforcement de la sécurité pour les comptes à privilèges (exigence systématique d'un second facteur).
    - Amélioration de la résilience face aux indisponibilités du fournisseur d'identité.
- **Traçabilité et Modélisation :**
    - Mise en place d'un système d'enregistrement et de rétention des décisions d'accès en base de données.
    - Création des nouveaux modèles de données `Agent` et `ProviderSession`.

### Autres changements
- **Documentation :** Publication d'un guide d'utilisation (runbook) pour les clients de l'API et mise à jour de la documentation concernant la reprise de l'API V2.
- **Internationalisation :** Traduction des messages du framework en français.
- **Sécurité des logs :** Filtrage des données sensibles (codes d'autorisation) dans les journaux système.
