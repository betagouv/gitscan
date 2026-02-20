## Changelog : docs (30 derniers jours)

### Résumé
Les 30 derniers jours ont été marqués par des améliorations significatives de l'expérience utilisateur, notamment l'ajout de la possibilité d'imprimer des documents directement depuis le navigateur, l'importation de documents, et des ajustements d'accessibilité. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout de la possibilité d'imprimer un document en utilisant la fonctionnalité native du navigateur. (#1832)
- Implémentation de l'importation de documents. (#1609)
- Ajout d'une barre flottante avec un bouton pour réduire le panneau latéral. (#1876)
- Ajout de paramètres UTM aux liens de documents partagés pour un meilleur suivi.
- Ajout d'une fonctionnalité de connexion silencieuse. (#1690)
- Gestion des requêtes de réconciliation pour les comptes utilisateurs. (#1878)
- Possibilité de définir des libellés personnalisés pour les boutons dans les modèles d'email. (#1817)

### Évolutions techniques
- Amélioration de la validation des fichiers importés.
- Augmentation de la valeur `client_max_body_size` dans la configuration Helm.
- Ajout de tests pour la fonctionnalité d'importation de documents.
- Mise à jour de l'API docspec vers la version 2.4.4.
- Suppression du code lié aux templates.
- Ajout d'un workflow GHCR pour les tests sur les forks.
- Correction de l'ordre de priorité des sondes liveness et readiness dans le déploiement backend.
- Utilisation des ressources Celery au lieu de celles du backend dans la configuration Helm.
- Ajout d'un scan Trivy sur l'image backend.
- Modification de l'URL des types MIME dans le Dockerfile.
- Ajout de support pour la variable d'environnement `AWS_S3_SIGNATURE_VERSION`.
- Amélioration de la synchronisation du store broadcast.
- Corrections et améliorations de l'accessibilité (focus, navigation).
- Suppression de la dépendance à des templates.

### Autres changements
- Mise à jour de la documentation pour la configuration des langues.
- Remplacement du lien de démonstration dans le README.
- Ajustement des typages pour correspondre aux composants stylisés.
- Amélioration de la hauteur de ligne des titres dans l'exportation PDF.
- Mise à jour des dépendances axios à la version 1.13.5 (correction de sécurité).
- Mise à jour des dépendances lodash à la version 4.17.23 (correction de sécurité).
- Mise à jour des chaînes de caractères traduites.
- Suppression de la surveillance des mises à jour de la dépendance `react-resizable-panels`.
- Ajout d'un flag de fonctionnalité `FRONTEND_SILENT_LOGIN_ENABLED`.
- Correction de l'affichage des timestamps des documents.
- Suppression du guard Trivy sur le backend.
- Ajout de tests de régression pour l'exportation PDF.
- Ajout d'un avertissement si le thème n'est pas mis à jour.
- Amélioration de la configuration du cache.
- Ajustement des couleurs et du logo pour correspondre à l'UI Kit v2.
- Tri des résultats de recherche d'utilisateurs par proximité avec l'utilisateur actif. (#1802)
- Ignorer la casse lors de la recherche de fallback par email. (#1880)
