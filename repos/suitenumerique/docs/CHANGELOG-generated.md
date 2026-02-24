## Changelog : docs (30 derniers jours)

### Résumé
Les 30 derniers jours ont été marqués par des améliorations significatives de l'expérience utilisateur, notamment l'ajout de nouvelles fonctionnalités comme la duplication de sous-pages, l'impression de documents et la gestion des demandes de réconciliation de comptes utilisateurs. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme. Enfin, des améliorations d'accessibilité ont été implémentées pour rendre l'outil plus inclusif.

### Évolutions fonctionnelles
- Ajout de la possibilité de dupliquer des sous-pages (#1893).
- Implémentation de la gestion des requêtes de réconciliation de comptes utilisateurs (#1878).
- Ajout d'une barre flottante avec un bouton pour masquer le panneau latéral (#1876).
- Possibilité d'imprimer un document directement depuis le navigateur (#1832).
- Ajout de paramètres UTM aux liens de documents partagés pour un meilleur suivi.
- Intégration de statistiques Crisp pour le suivi de l'utilisation.
- Ajout de la fonctionnalité de connexion silencieuse (#1690).

### Évolutions techniques
- Ajout du support de la plateforme ARM64 pour les images Docker.
- Amélioration de la configuration du cache backend.
- Correction de l'utilisation des ressources Celery dans le déploiement Helm.
- Inversion de l'ordre des sondes liveness et readiness dans le déploiement Helm.
- Ajout d'un workflow GHCR pour les tests sur les forks de dépôt.
- Activation de l'analyse de vulnérabilités Trivy sur l'image backend.
- Modification de l'URL de mime.types dans le Dockerfile.
- Mise à jour des dépendances JavaScript (axios).

### Autres changements
- Mise à jour de la documentation pour l'intégration de nouveaux utilisateurs.
- Correction de l'affichage du timestamp des documents.
- Mise à jour des chaînes de traduction.
- Amélioration de l'alignement des couleurs et du logo avec la nouvelle identité visuelle.
- Correction de bugs mineurs liés à l'accessibilité (focus, navigation).
- Correction de bugs liés à la synchronisation du store broadcast.
- Correction d'un bug empêchant la préservation du texte tapé après le symbole "@" avec la touche Echap.
- Suppression du code lié à l'ancien système de templates.
- Ajout d'un flag de fonctionnalité pour activer la connexion silencieuse.
- Amélioration de la gestion des erreurs et des types dans le code.
