## Changelog : mirai-mesreunions (30 derniers jours, au 2026-06-14)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives en termes de sécurité, de stabilité et d'expérience utilisateur. L'intégration de l'importation de vidéos YouTube et l'amélioration de la gestion des fichiers MCR sont des points forts. Des efforts importants ont également été consacrés à la correction de bugs et à l'optimisation des performances, notamment au niveau de la gestion des transcriptions et de l'interface utilisateur.

### Évolutions fonctionnelles
- **Importation YouTube:** Ajout de la fonctionnalité d'importation de vidéos YouTube avec prise en charge du karaoké synchronisé et de l'extraction de transcriptions.
- **Importation MCR:** Amélioration de l'importation depuis MCR, avec gestion des erreurs, affichage de l'état d'avancement et possibilité de supprimer en masse les importations.
- **Gestion des transcriptions:** Amélioration de l'éditeur de transcription avec possibilité de barrer/supprimer des blocs, de renommer les intervenants et de corriger les erreurs.
- **Recherche:** Ajout d'une fonctionnalité de recherche sémantique dans les réunions (RAG) permettant d'interroger le contenu des réunions.
- **Glossaire:** Ajout d'un glossaire éditable avec possibilité de nettoyer automatiquement les termes.
- **Téléchargement en masse:** Possibilité de télécharger en masse les réunions au format ZIP.
- **Interface utilisateur:** Refonte de l'interface utilisateur de la liste des réunions et de la fiche détail, avec des améliorations de l'ergonomie et de l'accessibilité.
- **Authentification:** Renforcement de la sécurité de l'authentification avec une vérification plus stricte des identités OIDC et une gestion améliorée des sessions.

### Évolutions techniques
- **Sécurité:** Durcissement de la sécurité avec des corrections de vulnérabilités potentielles et une meilleure gestion des autorisations.
- **Architecture:** Refactorisation de l'architecture pour améliorer la modularité et la maintenabilité du code.
- **Performance:** Optimisation des performances de l'application, notamment au niveau de la gestion des requêtes et de l'accès aux données.
- **Infrastructure:** Amélioration de l'infrastructure de déploiement avec des mises à jour de Docker et de Kubernetes.
- **Tests:** Ajout de tests unitaires et d'intégration pour améliorer la qualité du code.
- **Diarisation:** Bascule vers le backend de diarisation Kevent.
- **Nettoyage du code:** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Gestion des erreurs:** Amélioration de la gestion des erreurs et ajout de logs plus détaillés pour faciliter le débogage.

### Autres changements
- **Documentation:** Mise à jour de la documentation avec des informations sur les nouvelles fonctionnalités et les changements apportés à l'application.
- **Configuration:** Mise à jour de la configuration de l'application pour améliorer la sécurité et les performances.
- **Changement de nom:** Renommage du dépôt de `mcr-secure-audio-upload` à `mirai-mesreunions`.
- **Correction de bugs:** Correction de nombreux bugs mineurs et amélioration de la stabilité de l'application.
- **Amélioration de l'observabilité:** Ajout de métriques et de logs pour faciliter la surveillance et le débogage de l'application.
