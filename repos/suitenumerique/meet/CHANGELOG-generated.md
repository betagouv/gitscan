## Changelog : meet (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe de développement s'est concentrée sur l'amélioration de la sécurité, de l'accessibilité et des performances de Meet. Des correctifs de sécurité importants ont été appliqués, notamment des mises à jour de bibliothèques vulnérables et des améliorations de la validation des API. L'accessibilité a également été renforcée avec des améliorations pour les utilisateurs de lecteurs d'écran et des ajustements pour une meilleure expérience utilisateur. Enfin, des optimisations ont été apportées à l'interface d'administration et à la gestion des enregistrements pour améliorer la réactivité et l'efficacité.

### Évolutions fonctionnelles
- Ajout d'un lien vers l'application Windows via l'interface web (#976).
- Possibilité de configurer une redirection externe pour les utilisateurs non authentifiés (#904).
- Ajout d'un lien cliquable vers les paramètres généraux dans le modal d'inactivité (#974).
- Amélioration des annonces pour les lecteurs d'écran concernant l'épinglage/désépinglage des participants (#898).
- Amélioration des annonces pour les lecteurs d'écran concernant le minuteur de déconnexion en cas d'inactivité (#908).
- Ajout d'un annonceur global pour les lecteurs d'écran (#922).
- Correction d'un bug empêchant la configuration des raccourcis pour les participants (#985).

### Évolutions techniques
- Mise à jour de Django pour corriger plusieurs vulnérabilités de sécurité critiques (#954).
- Mise à jour d'OpenSSL dans les agents pour corriger une vulnérabilité (CVE-2025-15467).
- Épinglage de la version de Protobuf à 6.33.5 pour corriger une vulnérabilité (CVE-2026-0994).
- Passage à une image de base Alpine pour réduire la taille des images et améliorer la sécurité.
- Refactorisation de la vue d'ensemble de l'application pour utiliser un ViewSet de base.
- Optimisation des requêtes dans la vue d'administration des enregistrements pour améliorer les performances.
- Suppression de `pip` des images de production pour réduire les risques de sécurité.
- Activation temporaire de la vérification Trivy pour l'image backend.
- Amélioration de la validation des applications lors de la consommation de JWT externes.
- Renforcement des contrôles de permission au niveau des objets dans l'endpoint des salles.
- Amélioration de la logique de suppression des préfixes de portée.
- Ajout de tests pour exposer un défaut de permission dans l'API externe.
- Amélioration de la couverture des tests pour la vue d'ensemble de l'API externe.
- Refactorisation des permissions pour mieux s'aligner sur les responsabilités de DRF.
- Mise à jour des dépendances JavaScript (#973).
- Mise à jour de Prettier (#972).
- Mise à jour des étapes des workflows GitHub Actions.

### Autres changements
- Correction d'une faute de frappe dans le nom d'une variable d'environnement du buildpack.
- Correction d'un problème d'indentation dans le fichier Tilt.
- Documentation du déploiement sur Scalingo.
- Standardisation de la récupération de la variable d'environnement `DATABASE_URL`.
- Ajout d'un override de logo personnalisé pour Scalingo.
- Ajout d'un exemple de génération de clé API en utilisant OpenSSL.
- Correction de la documentation concernant les variables d'environnement.
- Mise à jour du lien vers Mosacloud dans la liste des instances SaaS.
- Mise à jour des termes légaux.
- Ajout de commentaires dans le code.
