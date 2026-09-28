## Changelog : proconnect-identite (30 derniers jours, au 24/09/2026)

### Résumé
Ce mois a été marqué par une amélioration de l'autonomie des utilisateurs, notamment avec la possibilité de déconnecter une identité FranceConnect. Le projet a également renforcé la fiabilité des données d'organisation via l'intégration de l'API RNE et a consolidé sa sécurité par une meilleure gestion des limites de requêtes et la protection des données personnelles lors des exports.

### Évolutions fonctionnelles
- **Gestion des identités** : Possibilité de déconnecter une identité FranceConnect depuis les informations personnelles [#2062](https://github.com/proconnect-gouv/proconnect-identite/issues/2062).
- **Données d'organisation** : Utilisation de l'API RNE pour récupérer les informations des organisations, garantissant une meilleure précision.
- **Expérience utilisateur (UX)** :
    - Amélioration de la clarté des e-mails (réinitialisation 2FA, suppression de clé d'accès).
    - Correction de la validation des adresses e-mail (gestion des formats invalides).
    - Normalisation des noms pour la certification (gestion des accents et diacritiques).
    - Retour au déclenchement manuel des passkeys (revert de l'auto-trigger [#2080](https://github.com/proconnect-gouv/proconnect-identite/issues/2080)).
- **Sécurité et Confidentialité** :
    - Correction d'une faille permettant de contourner le code de contact officiel.
    - Anonymisation de la fonction occupée dans les données exportées pour protéger la vie privée.
    - Enrichissement des alertes de sécurité avec le nom de la clé d'accès concernée.
- **Nouvelle fonctionnalité** : Mise en place de la gestion des liens en attente.

### Évolutions techniques
- **Architecture** :
    - Création d'un dépôt dédié pour les informations utilisateur FranceConnect.
    - Localisation de certaines données et types (TrancheEffectifs, types d'authentificateurs) pour réduire la dépendance aux API externes.
    - Refactorisation de l'usage des dépôts (homogénéisation des méthodes `get` et `find`).
- **Sécurité** :
    - Optimisation et ajustement du "rate limiting" pour mieux protéger l'API [#2166](https://github.com/proconnect-gouv/proconnect-identite/issues/2166) [#2138](https://github.com/proconnect-gouv/proconnect-identite/issues/2138).
    - Blocage de l'indexation par les moteurs de recherche via `robots.txt`.
    - Restriction du serveur Hono à son chemin de montage pour limiter la surface d'exposition.
- **Optimisations** :
    - Utilisation d'endpoints gratuits pour les services de "debounce" et les tests de santé (health checks).
    - Refactorisation du processus de vérification des contacts officiels.
    - Amélioration de la gestion des variables d'environnement (utilisation de `.dotenv`).

### Autres changements
- **Automatisation** : Amélioration de la synchronisation quotidienne des listes d'administrations via Grist.
- **Développement** : Ajout d'une commande "watch" pour faciliter l'exécution des tests [#2137](https://github.com/proconnect-gouv/proconnect-identite/issues/2137).
