## Changelog : mon-service-securise (30 derniers jours, au 7 octobre 2026)

### Résumé
Ce mois-ci, le service a franchi une étape majeure avec l'introduction de la gestion par groupes de services et le lancement d'une API publique sécurisée. Les outils de notification et de suivi de la complétude des dossiers ont également été considérablement enrichis pour faciliter le travail des agents et la gestion de leurs services.

### Évolutions fonctionnelles
- **Gestion des groupes de services** : possibilité de créer, renommer et supprimer des groupes pour organiser les services. L'interface permet désormais d'associer ou de dissocier des services à un groupe, avec un affichage optimisé via des accordéons et un tri alphabétique.
- **API Publique** : mise à disposition d'une API documentée permettant d'accéder aux données (risques, mesures, homologation, indice cyber). L'accès est sécurisé par un système de clés d'API avec gestion de l'expiration et des quotas.
- **Système de notifications** : enrichissement du centre de notifications avec des alertes d'échéance (homologation, mesures), des notifications d'invitation pour les contributeurs, et une fonction pour marquer toutes les notifications comme lues.
- **Suivi de complétude** : calcul automatique du taux de complétude des services et intégration du numéro de téléphone comme champ obligatoire dans le profil utilisateur.

### Évolutions techniques
- **Sécurité et API** : implémentation d'un middleware de limitation de débit (rate limiting) pour l'API, protection via Helmet, et mise en place d'une traçabilité (audit log) des appels à l'API publique.
- **Optimisation CI/CD** : accélération des pipelines de tests grâce à la parallélisation des contrôles, à la mise en cache de Chromium et à une meilleure gestion des environnements Docker.
- **Architecture et Code** : migration de plusieurs modèles métier vers TypeScript, réorganisation structurelle du code (middlewares, routes, mappers) et optimisation des performances (requêtes statistiques en parallèle et lecture optimisée des SIRET).
- **Observabilité** : ajout d'un adaptateur de logs permettant de centraliser les erreurs vers Sentry et de notifier les équipes via un webhook Mattermost.

### Autres changements
- **Documentation** : mise à jour de la documentation technique (OpenAPI) et des Conditions Générales d'Utilisation (CGU).
- **Interface utilisateur** : ajustements cosmétiques (marges, polices, thèmes) et amélioration du wording pour une meilleure clarté.
