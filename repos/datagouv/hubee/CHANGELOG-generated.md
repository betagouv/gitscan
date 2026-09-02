## Changelog : hubee (30 derniers jours, au 01/09/2026)

### Résumé
Ce mois a été marqué par une refonte majeure du système d'authentification et le lancement de la version 2 de l'API. La sécurité a été considérablement renforcée, notamment par l'intégration de la double authentification (MFA) et une meilleure traçabilité des accès. L'expérience utilisateur sur le portail a également été améliorée pour offrir des messages d'erreur plus clairs et une navigation plus intuitive.

### Évolutions fonctionnelles
- **Sécurité et Authentification** :
    - Support de la double authentification (MFA) imposée par le fournisseur d'identité.
    - Exigence systématique d'un second facteur pour les comptes à privilèges.
    - Gestion des sessions par durée d'inactivité et durée absolue.
- **Expérience Utilisateur (Portail)** :
    - Refonte de l'interface : l'identité et la déconnexion sont désormais regroupées dans l'en-tête.
    - Amélioration des messages d'erreur : les motifs de refus de rattachement et les erreurs de connexion sont désormais explicites.
    - Ajout d'options de recours sur les pages d'échec de connexion.
- **Gestion des Agents** :
    - Enrichissement des profils agents : ajout de la civilité, du rôle, de la fonction et des habilitations aux processus.
    - Normalisation des numéros de téléphone au format international.

### Évolutions techniques
- **API V2** :
    - Mise en place du socle OAuth2 (flux `client_credentials`).
    - Protection des points d'accès par jetons (tokens) avec attribution des appels.
    - Automatisation de la purge quotidienne des jetons expirés.
- **Authentification & OIDC** :
    - Migration de la gestion de ProConnect vers une implémentation native OIDC (sortie d'OmniAuth).
    - Renforcement de la sécurité des échanges : vérification des signatures, nonces et claims des jetons, et chiffrement des jetons au repos.
    - Amélioration de la résilience face aux indisponibilités du fournisseur d'identité.
- **Audit et Traçabilité** :
    - Mise en place d'un système de consignation des décisions d'accès en base de données (avec politique de rétention).
    - Suivi systématique du fournisseur d'identité pour chaque décision d'accès.
    - Sécurisation des logs par le filtrage des données sensibles (codes d'autorisation).
- **Architecture et Maintenance** :
    - Nouveau modèle de données pour le rattachement des agents aux organisations (via le couple SIRET/INSEE).
    - Mise à jour de l'outil de scan de sécurité Brakeman [#131](https://github.com/datagouv/hubee/issues/131).

### Autres changements
- **Documentation** :
    - Publication d'un guide d'utilisation (runbook) pour les clients de l'API.
    - Documentation de la transition vers l'API V2.
- **Internationalisation** : Traduction des messages du framework en français.
