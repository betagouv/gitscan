## Changelog : docs (30 derniers jours, au 09/10/2026)

### Résumé
Ce mois a été marqué par le passage à la version majeure 6.0.0, introduisant une refonte profonde de l'architecture de collaboration via l'intégration de YHub. Pour les utilisateurs, cela se traduit par une plateforme plus stable, de nouvelles fonctionnalités comme le téléchargement en Markdown et une gestion améliorée des mentions et des liens internes. L'interface utilisateur a également été modernisée, notamment via la refonte des pages d'erreur et l'ajout de raccourcis clavier.

### Évolutions fonctionnelles
- **Collaboration et Documents**
  - Introduction d'un système de mentions avec notifications par email (envoyées de manière asynchrone).
  - Possibilité de dupliquer des documents en incluant leurs sous-documents.
  - Support du mode hors-ligne pour l'arborescence des documents.
  - Conversion automatique des liens de documents collés en liens internes (interlinks).
  - Ajout d'une option de téléchargement des documents au format Markdown.
- **Interface Utilisateur (UI/UX)**
  - Refonte visuelle des pages d'erreur (401, 403 et 404) pour une meilleure expérience.
  - Ajout d'un raccourci clavier pour activer le mode présentation.
  - Amélioration de la recherche : possibilité d'ouvrir les résultats dans un nouvel onglet avec Ctrl/Cmd+clic.
  - Amélioration de la gestion des images : conservation de la légende et de l'alignement lors du remplacement d'une image.
  - Affichage des indications de raccourcis clavier dans les options de documents.
- **Corrections**
  - Résolution de bugs sur le glisser-déposer, la recherche/remplacement, et l'affichage des commentaires.
  - Correction de problèmes de rendu lors de l'impression en PDF.

### Évolutions techniques
- **Architecture de Collaboration**
  - Migration majeure du serveur de collaboration de HocusPocus vers YHub.
  - Implémentation de la suppression logique (soft-delete) synchronisée avec le serveur YHub.
  - Optimisation de la gestion des connexions de collaboration (réinitialisation automatique lors de la suppression d'un document ou d'un changement d'accès).
  - Migration des documents hérités (S3) vers le nouveau système YHub.
- **Sécurité et Authentification**
  - Renforcement de la sécurité des mentions (validation UUID, contrôle d'accès explicite, limitation du débit).
  - Amélioration de la gestion des jetons JWT (ajout de l'audience, exposition d'un endpoint JWKS, support des jetons RS256 mis en cache).
  - Utilisation de jetons JWT pour sécuriser les services de conversion.
- **Infrastructure et DevOps**
  - Mise en place d'une suite complète de tests de charge (scénarios k6, dashboards Grafana, et canaris de navigateur pour mesurer la perception utilisateur).
  - Amélioration de la CI/CD avec l'ajout de tests de linting, typechecking et build pour le serveur de collaboration.
  - Optimisation des images Docker (passage à des images "slim" pour YHub et suppression de pip dans l'image backend).
  - Mise à jour des déploiements Helm (support des métriques Prometheus via ServiceMonitor/PodMonitor et gestion de l'indexation des moteurs de recherche).
  - Remplacement de Minio par Silo dans la configuration Docker.
- **Observabilité**
  - Ajout de métriques Prometheus personnalisées pour le backend et YHub.
  - Intégration de la remontée d'erreurs YHub vers Sentry.

### Autres changements
- **Documentation**
  - Mise à jour de la documentation d'architecture.
  - Finalisation du guide de mise à niveau vers YHub et des instructions d'installation.
  - Correction de la documentation Kubernetes (guides Keycloak et Minio).
- **Internationalisation**
  - Mise à jour et nettoyage des chaînes de caractères traduites (i18n).
