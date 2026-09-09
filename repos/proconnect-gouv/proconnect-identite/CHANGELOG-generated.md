## Changelog : proconnect-identite (30 derniers jours, au 08/09/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec une refonte majeure de son architecture interne pour gagner en modularité et en maintenabilité. Côté utilisateurs, l'expérience est enrichie par de nouvelles options de gestion d'identité (possibilité de déconnecter FranceConnect), une automatisation de la connexion par Passkey et un meilleur suivi des demandes de modération via des notifications par email.

### Évolutions fonctionnelles
- **Gestion de l'identité** : Possibilité de déconnecter son identité FranceConnect ([#2062](https://github.com/proconnect-gouv/proconnect-identite/issues/2062)).
- **Amélioration de l'expérience Passkey** : Déclenchement automatique de la demande de Passkey si celui-ci est déjà configuré ([#2080](https://github.com/proconnect-gouv/proconnect-identite/issues/2080)).
- **Notifications et communication** :
    - Envoi d'un email de notification lorsqu'une demande de modération est annulée ([#2079](https://github.com/proconnect-gouv/proconnect-identite/issues/2079)).
    - Amélioration de la clarté des emails de réinitialisation 2FA ([#2128](https://github.com/proconnect-gouv/proconnect-identite/issues/2128)).
    - Ajout du SIRET et du libellé dans les emails en cas d'échec de jonction d'une organisation ([#2073](https://github.com/proconnect-gouv/proconnect-identite/issues/2073)).
    - Amélioration du contenu des emails de suppression de clés d'accès (sujet et corps pré-remplis).
- **Corrections et interface** :
    - Correction d'une faille permettant de contourner le code de contact officiel.
    - Harmonisation du formatage de la date de dernière mise à jour FranceConnect ([#2121](https://github.com/proconnect-gouv/proconnect-identite/issues/2121)).
    - Nettoyage de l'interface (suppression de liens d'aide en double et corrections de fautes de frappe).
    - Gestion améliorée des liens en attente.

### Évolutions techniques
- **Migration vers une architecture de "connecteurs"** : Refonte majeure visant à centraliser et modulariser la logique métier. Cette migration concerne les dépôts et services d'authentification, d'utilisateur, d'organisation, de modération et le client OIDC ([#2089](https://github.com/proconnect-gouv/proconnect-identite/issues/2089), [#2090](https://github.com/proconnect-gouv/proconnect-identite/issues/2090), [#2094](https://github.com/proconnect-gouv/proconnect-identite/issues/2094), [#2095](https://github.com/proconnect-gouv/proconnect-identite/issues/2095), [#2096](https://github.com/proconnect-gouv/proconnect-identite/issues/2096), [#2097](https://github.com/proconnect-gouv/proconnect-identite/issues/2097)).
- **Optimisation des données** : 
    - Récupération directe des listes SIREN depuis Grist pour plus de fiabilité.
    - Automatisation et optimisation de la synchronisation quotidienne des données administratives via Grist.
- **Refactoring et performance** :
    - Simplification des vues de configuration MFA pour éliminer les doublons.
    - Optimisation du temps de réinitialisation de la base de données de test dans la CI.
    - Sécurisation du serveur Hono en restreignant son accès à son chemin de montage.
- **Nettoyage du code** : Suppression des anciennes implémentations de `is_service_public`.

### Autres changements
- Suppression de la variable d'environnement inutilisée `ZAMMAD_TOKEN` ([#2085](https://github.com/proconnect-gouv/proconnect-identite/issues/2085)).
