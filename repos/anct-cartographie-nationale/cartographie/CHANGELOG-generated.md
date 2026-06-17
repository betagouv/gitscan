## Changelog : cartographie (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'observabilité et de la robustesse de la plateforme. Des outils de surveillance et de journalisation ont été ajoutés pour faciliter le diagnostic et la résolution des problèmes. De plus, un formulaire de contact a été implémenté pour permettre aux utilisateurs de communiquer plus facilement avec l'équipe.

### Évolutions fonctionnelles
- Ajout d'un formulaire de contact avec envoi d'emails via SMTP. Le formulaire inclut des champs de base et un envoi d'email avec un template HTML.
- Amélioration de l'affichage de l'état de santé de l'application avec l'exposition du timestamp de dernière actualisation du cache.

### Évolutions techniques
- Mise en place d'une journalisation structurée des requêtes serveur pour faciliter l'analyse et le débogage.
- Intégration de Sentry pour la remontée des erreurs et le suivi des performances.
- Utilisation de `@arckit/telemetry` pour centraliser la gestion des événements et des erreurs.
- Amélioration de la gestion du cache :
    - Tentative de relance en cas d'échec de chargement du cache.
    - Attente de la fin du rafraîchissement de la mémoire avant d'invalider le cache Next.js.
    - Réduction du TTL du cache Nginx à 5 minutes pour une propagation plus rapide des mises à jour.
- Refactorings importants :
    - Adoption de `@arckit/nextjs` pour simplifier et standardiser la gestion des routes et des paramètres.
    - Remplacement de la bibliothèque de formulaires locale par `@arckit/form`.
    - Adoption de `@arckit/daisyui` pour les composants d'interface utilisateur standard.
    - Migration de Matomo vers `@arckit/telemetry` pour l'analyse.
- Amélioration de la configuration et du déploiement :
    - Utilisation de Secret Manager pour la gestion des informations sensibles (SMTP).
    - Mise à jour des dépendances et configuration de Dependabot pour les mises à jour automatiques.
    - Ajout de la détection de secrets via Gitleaks.

### Autres changements
- Documentation de la capture de l'état de démarrage pour le warm-up du cache.
- Documentation de la journalisation structurée et de la capture d'erreurs.
- Ajout de tests pour le point de terminaison de santé.
- Mise à jour des dépendances et configuration de Dependabot.
- Amélioration de la configuration CI/CD.
- Nettoyage du code et suppression de dépendances inutilisées.
