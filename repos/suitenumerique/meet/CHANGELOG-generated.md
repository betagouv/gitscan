## Changelog : meet (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe de développement s'est concentrée sur l'amélioration de l'accessibilité, la sécurité et la performance de la plateforme Meet. Des correctifs de sécurité importants ont été implémentés, notamment pour prévenir les vulnérabilités XSS et renforcer la protection des API externes. L'expérience utilisateur a également été améliorée grâce à des ajustements d'accessibilité pour les utilisateurs ayant des besoins spécifiques, ainsi que des optimisations de performance au niveau de l'administration et des requêtes. De plus, des améliorations ont été apportées au déploiement sur des plateformes PaaS comme Scalingo.

### Évolutions fonctionnelles
- Ajout d'un lien vers l'application Windows via le web (#976)
- Ajout de raccourcis clavier supplémentaires pour améliorer l'accessibilité.
- Ajout d'un lien cliquable vers les paramètres généraux dans la fenêtre d'inactivité (#974)
- Possibilité de rediriger les utilisateurs non authentifiés vers une URL externe configurable (#904)
- Documentation du déploiement sur Scalingo (#957)
- Ajout de la prise en charge des annonces pour les actions d'épinglage/désépinglage de participants pour les lecteurs d'écran.
- Amélioration des annonces pour le minuteur de déconnexion d'inactivité.

### Évolutions techniques
- Mise à jour de Django pour corriger plusieurs vulnérabilités de sécurité critiques (#954)
- Refactorisation de la vue d'ensemble de l'application pour utiliser un ViewSet de base.
- Amélioration de la performance des requêtes dans l'interface d'administration pour les enregistrements.
- Optimisation de la sélection des salles dans la vue d'administration des enregistrements.
- Ajout de tests pour exposer un défaut de permission dans l'API externe.
- Renforcement des contrôles de permission au niveau des objets pour l'endpoint des salles.
- Activation temporaire de la vérification de vulnérabilités Trivy pour l'image backend.
- Ajout de scripts de déploiement pour les plateformes PaaS, testés sur Scalingo.
- Amélioration de la gestion des scopes pour l'API externe.
- Ajout de la surveillance des échecs de limitation de débit via Sentry (#964)
- Extraction des classes de limitation de débit dans un module dédié.

### Autres changements
- Correction de la documentation pour les variables d'environnement Docker Compose.
- Correction d'une erreur dans le rendu GitHub de la documentation Docker Compose.
- Mise à jour des termes juridiques.
- Ajout d'un exemple de génération de clé API en utilisant OpenSSL.
- Correction d'une erreur de casse dans une variable d'environnement Docker.
- Ajout d'une mention du déploiement à l'échelle de l'État français dans le README.
- Correction d'un bug dans les tests de notification suite à un changement de variable d'environnement.
- Ajout de traductions allemandes manquantes pour les paramètres d'accessibilité.
- Correction d'un bug d'ordre des segments de transcription.
- Amélioration de la gestion des exceptions liées aux fichiers lors de la manipulation des enregistrements.
- Mise à jour de la documentation pour corriger un lien vers les variables d'environnement.
