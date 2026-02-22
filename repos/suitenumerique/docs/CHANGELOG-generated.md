## Changelog : docs (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à la documentation et au code source de Docs au cours des 30 derniers jours. Les mises à jour incluent des corrections de bugs, des améliorations de l'interface utilisateur, des optimisations de sécurité et l'ajout de nouvelles fonctionnalités comme la gestion des requêtes de réconciliation de comptes utilisateurs et l'ajout de liens UTM pour le partage de documents.

### Évolutions fonctionnelles
- Ajout de paramètres UTM aux liens de partage de documents pour un meilleur suivi (#1876).
- Ajout d'une barre flottante avec un bouton de réduction pour le panneau latéral gauche.
- Possibilité d'imprimer un document directement depuis le navigateur (#1832).
- Ajout de la gestion des requêtes de réconciliation de comptes utilisateurs (#1878).
- Ajout de la connexion silencieuse (silent login) (#1690).
- Amélioration de la recherche d'utilisateurs : les résultats sont maintenant triés par proximité avec l'utilisateur actif (#1802).

### Évolutions techniques
- Ajout du support de la plateforme ARM64 pour les builds d'images Docker.
- Ajout d'un workflow GHCR pour les tests de forks.
- Correction de l'utilisation des ressources dans le déploiement Helm (Celery au lieu de Backend).
- Inversion de l'ordre des checks liveness et readiness dans le déploiement Helm.
- Activation de l'analyse de vulnérabilités Trivy sur l'image backend.
- Modification de l'URL des types MIME dans le Dockerfile.
- Ajout de la variable d'environnement `DJANGO_EMAIL_URL_APP`.
- Refactorisation du code frontend pour utiliser des hooks au lieu de hooks uniques.
- Mise à jour des dépendances JavaScript.

### Autres changements
- Correction d'une erreur dans la configuration de l'utilisateur Docker.
- Correction de l'affichage de l'horodatage des documents.
- Mise à jour des chaînes de traduction.
- Remplacement du lien de démonstration dans le README (#1875).
- Amélioration de la sécurité : renforcement de la vérification des URL.
- Changement du format d'intégration des blocs PDF en iframe pour une meilleure sécurité.
- Ajout d'un seuil dans les tests de régression.
- Limitation de l'exécution des checks d'impression au backend.
- Amélioration de l'accessibilité : empêchement de la focalisation des dates et amélioration de la navigation au clavier.
- Correction de la synchronisation du store broadcast.
- Ajout du support de la variable d'environnement `AWS_S3_SIGNATURE_VERSION`.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour de la documentation.
- Suppression du code lié à l'ancien système de templates.
- Correction de l'affichage des enfants dans les favoris.
- Correction de la fermeture du sélecteur d'emoji dans l'arborescence.
- Correction d'un type error dans TRASHBIN_CUTOFF_DAYS.
- Amélioration de la position de l'icône dans les blocs callout.
- Correction de l'exportation PDF.
- Ajout de statistiques Crisp.
- Amélioration de l'accessibilité pour l'exportation HTML.
- Ajout de labels manquants pour améliorer l'accessibilité.
