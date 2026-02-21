## Changelog : meet (30 derniers jours)

### Résumé
Les dernières mises à jour de Meet se concentrent sur la sécurité, l'amélioration de l'accessibilité et l'optimisation des performances. Des correctifs de sécurité importants ont été implémentés, notamment des mises à jour de bibliothèques vulnérables et des améliorations de la validation des API. L'accessibilité a été renforcée grâce à des améliorations pour les lecteurs d'écran et des ajustements pour les utilisateurs ayant des besoins spécifiques. Enfin, des optimisations ont été apportées à l'interface d'administration et à la gestion des enregistrements pour améliorer la réactivité et l'efficacité.

### Évolutions fonctionnelles
- Ajout d'un lien configurable pour rediriger les utilisateurs non authentifiés vers une page externe (#976).
- Amélioration de l'accessibilité avec l'ajout d'annonces pour les lecteurs d'écran lors de l'épinglage/désépinglage de participants (#922, #908).
- Ajout d'un lien cliquable vers les paramètres généraux dans le modal d'inactivité (#974).
- Amélioration des annonces pour les effets d'arrière-plan pour les lecteurs d'écran.
- Ajout de raccourcis clavier supplémentaires pour améliorer l'accessibilité.
- Correction d'une vulnérabilité XSS sur la page d'enregistrement (#911).

### Évolutions techniques
- Mise à jour de Django pour corriger plusieurs vulnérabilités de sécurité critiques (#954).
- Mise à jour d'OpenSSL dans les agents pour corriger une vulnérabilité (CVE-2025-15467).
- Épingle de la version de Protobuf à 6.33.5 pour corriger une vulnérabilité (CVE-2026-0994).
- Refactorisation de la classe ApplicationViewSet pour utiliser un ViewSet de base.
- Optimisation des requêtes dans la vue d'administration des enregistrements en sélectionnant la salle au niveau SQL.
- Amélioration des performances de l'administration Django en préchargeant l'accès utilisateur.
- Utilisation d'une image de base Alpine pour améliorer la sécurité et réduire la taille des images.
- Suppression de `pip` des images de production pour réduire les risques de sécurité.
- Ajout de scripts de déploiement PaaS, testés sur Scalingo (#957).
- Standardisation de la récupération de la variable d'environnement `DATABASE_URL` (#957).
- Ajout de la possibilité de remplacer le logo personnalisé sur Scalingo (#957).
- Activation temporaire de la suppression de l'étape de scan Trivy pour l'image backend.
- Amélioration de la gestion des autorisations au niveau des objets dans l'endpoint des salles.
- Amélioration de la logique de suppression des préfixes de portée.
- Ajout de tests pour exposer un défaut de permission dans l'API externe.
- Renforcement de la couverture des tests pour le ViewSet de l'API externe.
- Ajout de la surveillance des échecs de limitation du débit via Sentry.
- Extraction des classes de limitation du débit dans un module.
- Mise à jour des dépendances JavaScript (#976).
- Mise à jour de Prettier (#976).
- Mise à jour des étapes du workflow GitHub Actions.

### Autres changements
- Correction d'une faute de frappe dans le nom d'une variable d'environnement buildpack.
- Mise à jour de la documentation pour inclure un exemple de génération de clé API.
- Correction de la documentation pour les variables d'environnement Docker Compose.
- Ajout d'une mention du déploiement à grande échelle par l'État français dans le README.
- Mise à jour du lien vers les variables d'environnement dans la documentation.
- Mise à jour du changelog avec les changements récents.
- Correction d'un problème d'indentation dans le fichier Tilt.
- Ajout de tests pour les notifications.
- Ajout de la configuration des webhooks LiveKit dans la pile Docker Compose locale.
- Mise à jour des termes juridiques.
- Centralisation des raccourcis dans un catalogue.
- Support des touches Shift et Alt lors de la création de raccourcis.
- Documentation du déploiement Scalingo.
- Ajout de l'annonceur générique de lecteur d'écran.
- Amélioration des styles du spinner.
- Correction des étiquettes de formulaire et du câblage de l'autocomplétion pour l'accessibilité.
- Amélioration du contraste pour les options sélectionnées.
- Annonce de l'état de copie dans la boîte de dialogue d'invitation.
- Alignement de l'étiquette de fermeture de la boîte de dialogue dans la locale des salles.
- Correction de la documentation pour l'utilisation de `mkdir`.
- Correction de la variable d'environnement incorrecte dans Docker.
