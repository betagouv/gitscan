## Changelog : rdvsp-bridging (30 derniers jours, au 28 octobre 2026)

### Résumé
Ce mois a marqué le passage du projet d'une phase de conception à une version fonctionnelle et sécurisée. Les principales avancées incluent l'intégration de Google Calendar, la synchronisation bidirectionnelle avec Pipedrive et la mise en place d'une infrastructure de déploiement automatisée sur Scaleway. Un effort majeur a également été porté sur le renforcement de la sécurité du système.

### Évolutions fonctionnelles
- **Intégration Google Calendar** : Ajout de la possibilité de connecter des calendriers Google via OAuth.
- **Synchronisation Pipedrive** : Mise en place de la synchronisation des activités Pipedrive vers les blocs d'indisponibilité et des rendez-vous vers les activités Pipedrive.
- **Serveur CalDAV** : Implémentation d'un serveur CalDAV fournissant un calendrier par connexion, calqué sur le comportement du client RDV-SP.
- **Administration** : Ajout de pages d'administration et de tâches de gestion pour faciliter l'onboarding des comptes et des connexions.
- **Extraction de données** : Amélioration de la détection et de l'extraction des liens RDV-SP contenus dans les descriptions de rendez-vous.

### Évolutions techniques
- **Sécurité et durcissement** :
    - Renforcement de l'authentification : limitation du débit (rate limiting) pour l'administration et les tentatives CalDAV, et passage au hachage SHA-256 pour les mots de passe CalDAV.
    - Sécurisation des webhooks : authentification des webhooks Pipedrive via Basic Auth et vérification des jetons avant analyse du corps de la requête.
    - Protection de l'infrastructure : limitation de la taille des corps de requête (1 MB) et restriction des hôtes autorisés en production.
    - Confidentialité : filtrage des données sensibles de Pipedrive dans les journaux (logs) de la plateforme.
    - Correction de vulnérabilités : mise à jour de Ruby ([#3](https://github.com/gip-inclusion/rdvsp-bridging/pull/3)) et de la bibliothèque Crass pour corriger des failles de sécurité.
    - Application d'un audit de sécurité complet ([#2](https://github.com/gip-inclusion/rdvsp-bridging/pull/2)).
- **Infrastructure et CI/CD** :
    - Automatisation du déploiement sur Scaleway via GitHub Actions.
    - Mise en place de workflows pour l'exécution automatique des tests et du linting.
    - Possibilité de déployer la branche `main` à la demande depuis la CI.
- **Architecture** :
    - Implémentation du cœur du système : gestion des comptes, des connexions, des jetons de synchronisation et des rendez-vous.

### Autres changements
- **Renommage** : Le projet a été officiellement renommé `rdvsp-bridging`.
- **Documentation** : Rédaction de la documentation technique (architecture, journal de décisions, déploiement) et de la documentation utilisateur pour le fournisseur Google.
- **Initialisation** : Configuration initiale de l'environnement avec Rails 8.1, Docker et PostgreSQL.
