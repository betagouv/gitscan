## Changelog : cartographie (30 derniers jours, au 31 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout d'un formulaire de contact complet permettant d'envoyer des emails directement depuis l'application. De nombreuses refactorisations techniques ont également été effectuées pour moderniser le code et améliorer sa maintenabilité, en adoptant des bibliothèques et des pratiques plus récentes. La sécurité a également été renforcée avec l'ajout d'une détection de secrets.

### Évolutions fonctionnelles
- Ajout d'un formulaire de contact avec envoi d'emails via SMTP. Le formulaire inclut un template HTML personnalisé et des champs de saisie améliorés.
- Amélioration de l'expérience utilisateur du formulaire de contact.
- Ajout de documentation et de liens vidéo pour aider les utilisateurs à utiliser le formulaire de contact.

### Évolutions techniques
- Migration du système de suivi d'événements (analytics) de Matomo vers `@arckit/telemetry`.
- Refactorisation importante de l'utilisation de Next.js, adoptant `@arckit/nextjs` et des utilitaires associés pour une meilleure gestion des routes et des paramètres.
- Adoption de `@arckit/form` pour la gestion des formulaires, remplaçant la bibliothèque locale existante.
- Adoption de `@arckit/daisyui` pour les composants d'interface utilisateur standardisés.
- Refactorisation de la gestion de la configuration Next.js.
- Mise à jour de la gestion des dépendances et des versions de paquets.
- Amélioration de la configuration CI/CD avec l'ajout de la détection de secrets via Gitleaks.
- Passage de l'action Pulumi à l'utilisation du `GITHUB_TOKEN` pour éviter les limitations de débit.
- Migration du service SMTP de Scaleway TEM vers Brevo via Secret Manager.

### Autres changements
- Ajout d'une configuration Dependabot pour la gestion des dépendances npm et des actions GitHub.
- Mise à jour de la configuration de l'action pnpm.
- Ajout d'un fichier docker-compose pour faciliter le développement local avec Mailpit (serveur SMTP local).
- Nettoyage et suppression de dépendances inutilisées.
