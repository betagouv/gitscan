## Changelog : rdvsp-bridging (30 derniers jours, au 28 octobre 2026)

### Résumé
Ce mois-ci, le projet est passé d'une phase de conception à une version fonctionnelle et sécurisée. Les principales avancées incluent la capacité de synchroniser les calendriers avec Google et Pipedrive, ainsi que la mise en place d'un système de déploiement automatique. Un effort majeur a été consacré à la sécurisation de l'application pour protéger les données des utilisateurs et des agents.

### Évolutions fonctionnelles
- **Intégration de Google Calendar** : Ajout du support pour connecter des calendriers Google via le protocole OAuth2.
- **Synchronisation Pipedrive** : Mise en place de la synchronisation bidirectionnelle entre les activités Pipedrive et les créneaux de disponibilité/rendez-vous.
- **Interface d'administration** : Ajout de pages d'administration et de tâches permettant de gérer les comptes et les connexions.
- **Service CalDAV** : Capacité de servir un calendrier CalDAV par connexion, calqué sur le comportement du client RDV-SP.

### Évolutions techniques
- **Sécurisation de l'application (Audit de sécurité)** : Suite à un audit [#2](https://github.com/gip-inclusion/rdvsp-bridging/pull/2), plusieurs mesures ont été implémentées :
    - Limitation du débit (rate limiting) pour les tentatives d'authentification échouées sur l'administration et le CalDAV.
    - Passage au hachage SHA-256 pour les mots de passe CalDAV.
    - Sécurisation des webhooks Pipedrive via une authentification Basic Auth et limitation de la taille des requêtes (1 Mo).
    - Filtrage des données sensibles (activités Pipedrive) dans les journaux de requêtes (logs).
    - Restriction de l'hôte autorisé pour les URLs en production.
- **Infrastructure et CI/CD** :
    - Automatisation du déploiement vers Scaleway via GitHub Actions.
    - Intégration de l'exécution des tests et du linting dans le pipeline CI.
    - Mise en place de Dependabot avec auto-merge pour les mises à jour mineures [#1](https://github.com/gip-inclusion/rdvsp-bridging/pull/1).
- **Mises à jour critiques** :
    - Passage à Ruby 4.0.9 pour corriger des vulnérabilités (CVE) sur Onigmo [#3](https://github.com/gip-inclusion/rdvsp-bridging/pull/3).
    - Mise à jour de la bibliothèque `crass` pour corriger une faille de contournement de l'assainisseur CSS.
- **Refactoring** : Extraction de la logique de contenu des rendez-vous dans une classe dédiée (`RdvContent`) pour une meilleure gestion des données partagées avec les fournisseurs.

### Autres changements
- **Documentation** : Mise à jour de la documentation concernant l'architecture, le journal de décisions (decision log), le déploiement Scaleway et l'utilisation du fournisseur Google.
- **Tests** : Ajout de scripts de tests de bout en bout (E2E) contre un client RDV-SP réel.
- **Identité** : Renommage officiel du projet en `rdvsp-bridging`.
