## Changelog : proconnect-identite (30 derniers jours, au 11/09/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec une refonte structurelle visant à accroître son autonomie et sa robustesse, notamment par la migration de plusieurs composants vers une nouvelle architecture de "connecteurs". Côté utilisateurs, l'expérience est enrichie par une meilleure gestion des identités (déconnexion FranceConnect, automatisation des Passkeys) et des renforcements de sécurité importants.

### Évolutions fonctionnelles
- **Gestion de l'identité** : Possibilité de déconnecter une identité FranceConnect liée au compte [#2062].
- **Expérience Passkey** : Déclenchement automatique de l'authentification Passkey sans clic supplémentaire lors de la configuration [#2080].
- **Notifications** : Envoi d'un email automatique à l'utilisateur lorsqu'une demande de modération est annulée [#2079].
- **Sécurité** : Correction d'une faille permettant le contournement du code de vérification des contacts officiels.
- **Améliorations UX/UI** : 
    - Clarification des messages d'email pour la réinitialisation du 2FA.
    - Amélioration du formatage des dates FranceConnect et de l'encodage des liens "mailto" pour la suppression de clés d'accès.
    - Correction de typos et suppression de liens d'aide en doublon.

### Évolutions techniques
- **Migration architecturale** : Migration massive de la logique métier (utilisateurs, organisations, authentificateurs, modération, etc.) vers un nouveau système de "connectors" pour une meilleure modularité [#2089, #2090, #2093, #2094, #2095, #2096, #2097, #2098].
- **Autonomie des données** : Réduction des dépendances externes par l'intégration locale de certaines données et types (notamment les tranches d'effectifs et les types d'authentificateurs).
- **Nouveaux composants** : Création d'un dépôt dédié pour la gestion des informations utilisateur FranceConnect [#2159].
- **Refactorisation** : 
    - Optimisation du processus de vérification des contacts officiels [#2131].
    - Homogénéisation des méthodes de recherche (`get` vs `find`) au sein des repositories.
- **Performance et Sécurité** : 
    - Amélioration de la gestion de la limitation de débit (rate limiting) [#2138].
    - Restriction du serveur Hono à son chemin de montage pour plus de sécurité.
- **CI/CD** : 
    - Optimisation du temps de reset de la base de données lors des tests.
    - Mise à jour du workflow de release avec Changesets [#2146].

### Autres changements
- **Maintenance** : Synchronisation régulière de la liste des administrations via Grist.
- **Nettoyage** : Suppression de variables d'environnement inutilisées.
