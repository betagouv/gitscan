## Changelog : meet (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment concernant la gestion des participants en grand groupe, l'accessibilité et l'intégration de nouveaux outils d'analyse. Des corrections de bugs et des optimisations techniques ont également été implémentées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Possibilité de forcer l'affichage du nom d'utilisateur SSO pour les utilisateurs authentifiés.
- Amélioration de l'affichage des vignettes en mode Picture-in-Picture (PiP) avec pagination et priorisation du partage d'écran.
- Ajout d'un indicateur visuel pour les participants avec la caméra désactivée.
- Possibilité de masquer par défaut les participants lors de l'entrée dans une réunion de grande taille.
- Amélioration de l'accessibilité des effets vidéo et des contrôles d'arrière-plan personnalisés.
- Ajout d'une option pour inclure une enquête de satisfaction à la fin des enregistrements.
- Amélioration de la recherche des enregistrements par adresse email du propriétaire.

### Évolutions techniques
- Mise à jour de plusieurs dépendances frontend (React, PostHog, LiveKit, etc.) pour bénéficier des dernières corrections et améliorations.
- Refactorisation du code frontend pour optimiser la gestion des assets (modèles, WASM) et améliorer la performance.
- Intégration d'un système d'analyse configurable basé sur PostHog.
- Amélioration de la gestion des variables d'environnement.
- Mise à jour de l'image Docker frontend avec Node 22.
- Correction d'un bug empêchant l'affichage correct de l'info panel pour les salles non enregistrées.
- Correction d'un bug lié à la récupération de l'ID client depuis la requête.
- Normalisation des clés d'objets S3 pour une meilleure compatibilité.
- Suppression du support de la version 1 du service de résumé.
- Amélioration de la gestion des erreurs et de l'instrumentation avec Sentry pour les agents LiveKit.

### Autres changements
- Ajout de documentation pour la personnalisation du favicon via un volume mount.
- Ajout de Clever Cloud à la liste des fournisseurs SaaS supportés.
- Clarification des directives de contribution.
- Mise à jour de la documentation pour refléter la suppression de la version 1 du service de résumé.
- Ajout de badges DPG au README.
- Mise à jour des images de base Alpine et FFMPEG.
- Correction de problèmes de build sur Scalingo.
- Suppression de l'appel au flag de fonctionnalité "summary enabled".
- Mise à jour des images Helm et correction du rendu des hôtes multiples.
- Amélioration de l'accessibilité du contrôle de pagination.
- Correction de l'initialisation du nom complet dans le champ de saisie de connexion.
- Organisation des paquets JavaScript dans `package.json`.
- Ajout de la prise en charge d'un domaine dédié pour l'API des flags de fonctionnalité.
- Rejet des tokens d'accès utilisateur sur l'API.
- Ajout de tests pour la normalisation des clés S3 encodées.
- Mise à jour des dépendances Python.
- Correction d'un bug dans le collecteur de métadonnées de l'agent.
- Ajout d'un modèle d'environnement manquant pour le collecteur de métadonnées.
- Amélioration de la précision des événements d'analyse.
- Correction d'un bug empêchant l'activation du bouton "Mute Everyone" dans certains cas.
- Mise à jour de la documentation pour refléter les changements de nommage ("Premium" -> "Advanced").
